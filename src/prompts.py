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
    Competitors: List[str] = Field(
        description="A list of at least five competitor companies within the same industry or market. The list can have fewer than ten competitors if the company operates in a niche industry."
    )
    MarketShares: Dict[str, str] = Field(
        description="Top five product/service markets that the company is targeting (not geographic regions or countries) and the company's estimated market share in each market as a percentage range (e.g., '20-25%'). These are estimates and do not need to be exact values."
    )


COMPANY_PARSER = PydanticOutputParser(pydantic_object=Company)


# _company_detail_json_schema = """{{"Company":{{"Sectors":{{"description":"Same as GICS Sectors. A company may operate in one or more of these sectors.","constraints":["Energy","Materials","Industrials","Consumer Discretionary","Consumer Staples","Health Care","Financials","Information Technology","Communication Services","Utilities","Real Estate"],"type":"list","example":["Information Technology","Health Care"]}},"IndustryGroups":{{"description":"Same as GICS Industry Groups. A company may operate in one or more of these industry groups.","constraints":["Energy","Materials","Capital Goods","Commercial & Professional Services","Transportation","Automobiles & Components","Consumer Durables & Apparel","Consumer Services","Retailing","Food & Staples Retailing","Food, Beverage & Tobacco","Household & Personal Products","Health Care Equipment & Services","Pharmaceuticals, Biotechnology & Life Sciences","Banks","Diversified Financials","Insurance","Software & Services","Technology Hardware & Equipment","Semiconductors & Semiconductor Equipment","Telecommunication Services","Media & Entertainment","Utilities","Real Estate"],"type":"list","example":["Software & Services","Pharmaceuticals, Biotechnology & Life Sciences"]}},"Location":{{"description":"The city where the company's headquarters is located. This should be the official registered location.","type":"string","example":"San Francisco"}},"GeographicScope":{{"description":"Refers to the regions, countries, or areas where a company operates, offers its products or services, or has a market presence. Include only one of the provided categories.","constraints":["Local","National","International","Global"],"type":"string","example":"International"}},"YearFounded":{{"description":"The year a company was established. It should be a valid year between 1800 and the current year.","type":"integer","example":1998,"constraints":{{"min":1800,"max":2024}}}},"Size":{{"description":"Number of company's employees. This should be a positive integer.","type":"integer","example":5000,"constraints":{{"min":1}}}},"PublicPrivate":{{"description":"Whether the company is publicly traded or privately held.","constraints":["Public","Private"],"type":"string","example":"Public"}},"ProductServicetype":{{"description":"The type of product or service the company offers. This field specifies whether the company offers physical products, virtual services, or both.","constraints":["Physical","Virtual","Both"],"type":"string","example":"Both"}},"CustomerSegment":{{"description":"List of customer bases that the company serves. A company can serve one or more of the following customer types: B2C (Business to Consumer), B2B (Business to Business), B2G (Business to Government), and C2C (Consumer to Consumer). In cases where a company serves multiple segments, include all applicable segments.","constraints":["B2C","B2B","B2G","C2C"],"type":"list","example":["B2B","B2G"]}},"Revenue":{{"description":"Company's annual revenue in US dollars. The value must be positive and should not include currency symbols.","type":"float","example":50000000.0,"constraints":{{"min":0.0}}}},"Competitors":{{"description":"A list of at least five competitor companies within the same industry or market. The list can have fewer than ten competitors if the company operates in a niche industry.","type":"list","example":["Competitor1","Competitor2"],"constraints":{{"min_items":5}}}},"MarketShares":{{"description":"Top five product/service markets that the company is targeting (not geographic regions or countries) and its estimated market share in each market as a percentage range (e.g., '20-25%'). These are estimates and do not need to be exact values.","type":"dict","example":{{"Market1":"X-Y%","Market2":"Z-W%"}},"constraints":{{"min_items":1}}}}}}}}"""
_company_detail = """A company operates in one or more sectors similar to the GICS Sectors, such as Energy, Materials, Industrials, Consumer Discretionary, Consumer Staples, Health Care, Financials, Information Technology, Communication Services, Utilities, and Real Estate. For instance, a company might operate in sectors like 'Information Technology' or 'Health Care'.\nIndustry Groups are categories a company might belong to, similar to GICS Industry Groups. Examples include Capital Goods, Transportation, Consumer Services, Retailing, Health Care Equipment & Services, Software & Services, and many others. A company could, for example, be part of 'Software & Services' or 'Pharmaceuticals, Biotechnology & Life Sciences'.\nThe company's headquarters location refers to the city where it is officially registered, such as 'San Francisco'. The geographic scope defines where the company has a market presence, which could be 'Local', 'National', 'International', or 'Global'. For example, a company might operate on an 'International' scale.\nThe year a company was established should be a valid year between 1500 and the 2024. For example, it might have been founded in 1998. The company size is determined by the number of employees, which should be a positive number, such as 5000.\nThe company can be publicly traded or privately held, referred to as 'Public' or 'Private'. For example, it could be a 'Public' company. The type of product or service the company offers can be physical products, virtual services, or both. For instance, a company might offer 'Both'.\nCustomer segments include the types of customers the company serves, which could be B2C (Business to Consumer), B2B (Business to Business), B2G (Business to Government), or C2C (Consumer to Consumer). A company could, for instance, serve both 'B2B' and 'B2G' segments.\nAnnual revenue is expressed in US dollars and should be a positive number, like 50000000.0, without currency symbols. The company also has a list of competitors, typically at least five, but fewer if operating in a niche market. For example, competitors might include 'Competitor1' and 'Competitor2'.\nLastly, the company targets specific product or service markets, not geographic regions, with estimated market shares as percentage ranges. For example, it might have a market share of '20-25%' in 'Market1' and '15-20%' in 'Market2'."""
_company_detail_example = [
    {
        "company": "Nvidia",
        "output": """{{"Sectors":["Information Technology"],"IndustryGroups":["Semiconductors & Semiconductor Equipment"],"Location":"Santa Clara, California","GeographicScope":"Global","YearFounded":1993,"Size":26196,"PublicPrivate":"Public","ProductServicetype":"Hardware and Software","CustomerSegment":["B2B","B2C"],"Revenue":26974000000.0,"Competitors":["AMD","Intel","Qualcomm","Apple","Google"],"MarketShares":{{"GPU Market":"80-85%","AI Chips":"80-90%","Data Center GPUs":"90-95%","Professional Visualization":"70-75%","Automotive Chips":"15-20%"}}}}""",
    },
    {
        "company": "Microsoft",
        "output": """{{"Sectors":["Information Technology"],"IndustryGroups":["Software & Services","Technology Hardware & Equipment"],"Location":"Redmond, Washington","GeographicScope":"Global","YearFounded":1975,"Size":221000,"PublicPrivate":"Public","ProductServicetype":"Software and Hardware","CustomerSegment":["B2B","B2C","B2G"],"Revenue":198270000000.0,"Competitors":["Apple","Google","Amazon","IBM","Oracle"],"MarketShares":{{"Operating Systems":"75-80%","Office Software":"85-90%","Cloud Services (Azure)":"20-25%","Enterprise Software":"15-20%","Gaming Consoles":"30-35%"}}}}""",
    },
    {
        "company": "Apple",
        "output": """{{"Sectors":["Information Technology","Consumer Electronics"],"IndustryGroups":["Technology Hardware & Equipment","Software & Services"],"Location":"Cupertino, California","GeographicScope":"Global","YearFounded":1976,"Size":164000,"PublicPrivate":"Public","ProductServicetype":"Hardware and Software","CustomerSegment":["B2C","B2B"],"Revenue":394328000000.0,"Competitors":["Samsung","Microsoft","Google","Huawei","Dell"],"MarketShares":{{"Smartphones (Global)":"15-20%","Tablets":"30-35%","Smartwatches":"35-40%","Personal Computers":"7-10%","True Wireless Stereo Earbuds":"30-35%"}}}}""",
    },
]
_prompt_example_extract_company_info = PromptTemplate(
    input_variables=["company", "output"],
    template="Example Company: {company}\nExample Output: {output}",
)

PROMPT_COMPANY_COMPERHENSIVE_ANALYSIS = PromptTemplate(
    input_variables=["company"],
    template="There are some definitions within this JSON schema, explaining what is important about companies for me:\n\""
    +_company_detail
    + "\"\nMake a comprehensive analysis of '{company}' based on provided definitions. Then analyse the company on each of the fields and describe company's current state on each.",
)
PROMPT_EXTRACT_COMPANY_DETAILS = FewShotPromptTemplate(
    examples=_company_detail_example,
    example_prompt=_prompt_example_extract_company_info,
    prefix="Based on the analysis you've done, fit the results into an JSON, regarding the provided JSON schema and the examples.\n{format_instructions}\n",
    suffix="Company: {company}\nOutput: ",
    input_variables=["company"],
    example_separator="\n",
    partial_variables={"format_instructions": COMPANY_PARSER.get_format_instructions()},
)
