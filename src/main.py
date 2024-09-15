import os
import json

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from s3 import *
from prompts import (
    PROMPT_COMPANY_COMPERHENSIVE_ANALYSIS,
    PROMPT_EXTRACT_COMPANY_DETAILS,
    COMPANY_PARSER,
)


def companies_list():
    return fetch_s3_object("companies.txt").decode("utf-8").splitlines()


def generate_companies_data(companies: list):
    generated_companies_data = {}

    # llm = ChatGroq(
    #     temperature=0,
    #     groq_api_key=os.getenv("GROQ_API_KEY", ""),
    #     model_name="llama-3.1-70b-versatile",
    # )
    llm = ChatOpenAI(
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY", ""),
        model_name="gpt-4o-mini",
    )

    llm_history = {}

    def _get_session_history(session_id: str) -> InMemoryChatMessageHistory:
        if session_id not in llm_history:
            llm_history[session_id] = InMemoryChatMessageHistory()
        return llm_history[session_id]

    for i, company in enumerate(companies):
        try:
            chain = RunnableWithMessageHistory(
                PROMPT_COMPANY_COMPERHENSIVE_ANALYSIS | llm,
                _get_session_history,
                input_messages_key="company",
                history_messages_key="history",
            )
            chain.invoke(
                {"company": company},
                config={"configurable": {"session_id": "1"}},
            )

            chain = RunnableWithMessageHistory(
                PROMPT_EXTRACT_COMPANY_DETAILS | llm,
                _get_session_history,
                input_messages_key="company",
                history_messages_key="history",
            )
            output = chain.invoke(
                {"company": company},
                config={"configurable": {"session_id": "1"}},
            )
            result = COMPANY_PARSER.parse(output.content)
            generated_companies_data[company] = json.loads(result.model_dump_json())
            print(i, generated_companies_data[company])
            with open("/tmp/companies_details.json", "w") as f:
                json.dump(generated_companies_data, f)
        except Exception as e:
            print(i, e)

    return generated_companies_data


if __name__ == "__main__":
    companies = companies_list()
    companies_data = generate_companies_data(companies)
