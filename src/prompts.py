from enum import Enum
from langchain_core.prompts import (
    PromptTemplate,
    FewShotPromptTemplate,
)
from langchain.output_parsers import PydanticOutputParser

from pydantic import BaseModel, Field

from pydantic import BaseModel, Field
from typing import List, Dict



class Sector(Enum):
    ENERGY = "Energy"
    MATERIALS = "Materials"
    INDUSTRIALS = "Industrials"
    CONSUMER_DISCRETIONARY = "Consumer Discretionary"
    CONSUMER_STAPLES = "Consumer Staples"
    HEALTH_CARE = "Health Care"
    FINANCIALS = "Financials"
    INFORMATION_TECHNOLOGY = "Information Technology"
    COMMUNICATION_SERVICES = "Communication Services"
    UTILITIES = "Utilities"
    REAL_ESTATE = "Real Estate"


class IndustryGroup(Enum):
    ENERGY = "Energy"
    MATERIALS = "Materials"
    CAPITAL_GOODS = "Capital Goods"
    COMMERCIAL_PROFESSIONAL_SERVICES = "Commercial & Professional Services"
    TRANSPORTATION = "Transportation"
    AUTOMOBILES_COMPONENTS = "Automobiles & Components"
    CONSUMER_DURABLES_APPAREL = "Consumer Durables & Apparel"
    CONSUMER_SERVICES = "Consumer Services"
    RETAILING = "Retailing"
    FOOD_STAPLES_RETAILING = "Food & Staples Retailing"
    FOOD_BEVERAGE_TOBACCO = "Food, Beverage & Tobacco"
    HOUSEHOLD_PERSONAL_PRODUCTS = "Household & Personal Products"
    HEALTH_CARE_EQUIPMENT_SERVICES = "Health Care Equipment & Services"
    PHARMACEUTICALS_BIOTECH_LIFE_SCIENCES = (
        "Pharmaceuticals, Biotechnology & Life Sciences"
    )
    BANKS = "Banks"
    DIVERSIFIED_FINANCIALS = "Diversified Financials"
    INSURANCE = "Insurance"
    SOFTWARE_SERVICES = "Software & Services"
    TECHNOLOGY_HARDWARE_EQUIPMENT = "Technology Hardware & Equipment"
    SEMICONDUCTORS_EQUIPMENT = "Semiconductors & Semiconductor Equipment"
    TELECOMMUNICATION_SERVICES = "Telecommunication Services"
    MEDIA_ENTERTAINMENT = "Media & Entertainment"
    UTILITIES = "Utilities"
    REAL_ESTATE = "Real Estate"


class TradeStatus(Enum):
    PUBLIC = "Public"
    PRIVATE = "Private"


class ProductService(Enum):
    PHYSICAL = "Physical"
    VIRTUAL = "Virtual"
    BOTH = "Both"


class Segment(Enum):
    B2C = "B2C"
    B2B = "B2B"
    B2G = "B2G"
    C2C = "C2C"


class Company(BaseModel):
    Sectors: List[Sector] = Field(
        description="All GICS Sectors that the company is active at. A company may operate in one or more of these sectors."
    )
    IndustryGroups: List[IndustryGroup] = Field(
        description="The GICS Industry Groups that the company is active at. A company may operate in one or more of these industry groups."
    )
    Location: str = Field(
        description="The city where the company's headquarters is located. This should be the official registered location."
    )
    GeographicScope: str = Field(
        description="Refers to the regions, countries, or areas where a company operates, offers its products or services, or has a market presence. Include only one of the provided categories."
    )
    YearFounded: int = Field(
        description="The year a company was established. It should be a valid year between 1800 and the current year."
    )
    Size: int = Field(
        description="Number of company's employees. This should be a positive integer."
    )
    PublicPrivate: TradeStatus = Field(
        description="Whether the company is publicly traded or privately held."
    )
    ProductServiceType: ProductService = Field(
        description="The type of product or service the company offers. This field specifies whether the company offers physical products, virtual services, or both."
    )
    CustomerSegment: List[Segment] = Field(
        description="List of customer bases that the company serves. A company can serve one or more of the following customer types: B2C (Business to Consumer), B2B (Business to Business), B2G (Business to Government), and C2C (Consumer to Consumer). In cases where a company serves multiple segments, include all applicable segments."
    )
    Revenue: float = Field(
        description="Company's annual revenue in US dollars. The value must be positive and should not include currency symbols."
    )
    Competitors: Dict[str, float] = Field(
        description="A list of at least five competitor companies within the same industry or market. Each entry includes the competitor's name and revenue in US dollars. The list can have fewer than ten competitors if the company operates in a niche industry."
    )
    MarketShares: Dict[str, str] = Field(
        description="Top five product/service markets that the company is targeting (not geographic regions or countries) and its estimated market share in each market as a percentage range (e.g., '20-25%'). These are estimates and do not need to be exact values."
    )


COMPANY_PARSER = PydanticOutputParser(pydantic_object=Company)


_company_detail_json_schema = """{{"Company":{{"Sectors":{{"description":"Same as GICS Sectors. A company may operate in one or more of these sectors.","constraints":["Energy","Materials","Industrials","Consumer Discretionary","Consumer Staples","Health Care","Financials","Information Technology","Communication Services","Utilities","Real Estate"],"type":"list","example":["Information Technology","Health Care"]}},"IndustryGroups":{{"description":"Same as GICS Industry Groups. A company may operate in one or more of these industry groups.","constraints":["Energy","Materials","Capital Goods","Commercial & Professional Services","Transportation","Automobiles & Components","Consumer Durables & Apparel","Consumer Services","Retailing","Food & Staples Retailing","Food, Beverage & Tobacco","Household & Personal Products","Health Care Equipment & Services","Pharmaceuticals, Biotechnology & Life Sciences","Banks","Diversified Financials","Insurance","Software & Services","Technology Hardware & Equipment","Semiconductors & Semiconductor Equipment","Telecommunication Services","Media & Entertainment","Utilities","Real Estate"],"type":"list","example":["Software & Services","Pharmaceuticals, Biotechnology & Life Sciences"]}},"Location":{{"description":"The city where the company's headquarters is located. This should be the official registered location.","type":"string","example":"San Francisco"}},"GeographicScope":{{"description":"Refers to the regions, countries, or areas where a company operates, offers its products or services, or has a market presence. Include only one of the provided categories.","constraints":["Local","National","International","Global"],"type":"string","example":"International"}},"YearFounded":{{"description":"The year a company was established. It should be a valid year between 1800 and the current year.","type":"integer","example":1998,"constraints":{{"min":1800,"max":2024}}}},"Size":{{"description":"Number of company's employees. This should be a positive integer.","type":"integer","example":5000,"constraints":{{"min":1}}}},"PublicPrivate":{{"description":"Whether the company is publicly traded or privately held.","constraints":["Public","Private"],"type":"string","example":"Public"}},"ProductServicetype":{{"description":"The type of product or service the company offers. This field specifies whether the company offers physical products, virtual services, or both.","constraints":["Physical","Virtual","Both"],"type":"string","example":"Both"}},"CustomerSegment":{{"description":"List of customer bases that the company serves. A company can serve one or more of the following customer types: B2C (Business to Consumer), B2B (Business to Business), B2G (Business to Government), and C2C (Consumer to Consumer). In cases where a company serves multiple segments, include all applicable segments.","constraints":["B2C","B2B","B2G","C2C"],"type":"list","example":["B2B","B2G"]}},"Revenue":{{"description":"Company's annual revenue in US dollars. The value must be positive and should not include currency symbols.","type":"float","example":50000000.0,"constraints":{{"min":0.0}}}},"Competitors":{{"description":"A list of at least five competitor companies within the same industry or market. Each entry includes the competitor's name and revenue in US dollars. The list can have fewer than ten competitors if the company operates in a niche industry.","type":"dict","example":{{"Competitor1":20000000.0,"Competitor2":15000000.0}},"constraints":{{"min_items":5}}}},"MarketShares":{{"description":"Top five product/service markets that the company is targeting (not geographic regions or countries) and its estimated market share in each market as a percentage range (e.g., '20-25%'). These are estimates and do not need to be exact values.","type":"dict","example":{{"Market1":"20-25%","Market2":"15-20%"}},"constraints":{{"min_items":1}}}}}}}}"""
_company_detail_example = {
    "company": "Autodesk, Inc.",
    "output": """{{"Autodesk, Inc.":{{"Sectors":["Information Technology"],"IndustryGroups":["Software & Services"],"Location":"San Rafael, California, USA","GeographicScope":"Global","YearFounded":1982,"Size":12600,"Revenue":4386000000,"PublicPrivate":"Public","ProductServiceType":"Both","CustomerSegment":["B2B","B2C"],"Competitors":["PTC","Siemens Digital Industries Software","Adobe","Trimble","Ansys","Bentley Systems","Hexagon AB","Nemetschek","Altair Engineering"],"MarketShares":{{"CAD software":"30-35%","BIM software":"25-30%","Engineering software":"15-20%","3D modeling and animation software":"10-15%"}}}}}}""",
}
_prompt_example_extract_company_info = PromptTemplate(
    input_variables=["company", "output"],
    template="Company: {company}\nOutput: {output}",
)

PROMPT_COMPANY_COMPERHENSIVE_ANALYSIS = PromptTemplate(
    input_variables=["company"],
    template="There are some definitions within this JSON schema:\n"
    + _company_detail_json_schema
    + "Make a comprehensive analysis of '{company}' based on provided definitions. Create a chain-of-thought to acheive the answer. Breakdown each steps to smaller steps (like explaining an LLM agent to gather a specific data). Then follow the steps and generate the answer.",
)
PROMPT_EXTRACT_COMPANY_DETAILS = FewShotPromptTemplate(
    examples=[
        # _company_detail_example,
    ],
    example_prompt=_prompt_example_extract_company_info,
    prefix="Based on the analysis you've done, fit the results into an JSON, regarding the provided JSON schema and the examples.\n{format_instructions}\n",
    suffix="Company: {company}\nOutput: ",
    input_variables=["company"],
    example_separator="\n",
    partial_variables={"format_instructions": COMPANY_PARSER.get_format_instructions()},
)
