from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

from src.pydantic_parsing import SQLResponse


def get_prompt():
    parser = PydanticOutputParser(pydantic_object=SQLResponse)
    template = """
    You are a system that converts natural language questions into SQL queries.
    Use ONLY the schema provided. Do not assume extra columns or tables.
    {format_instructions}
    DATABASE CONTEXT:
    {schema}
    QUESTION:
    {question}
    """
    return PromptTemplate(
        template=template,
        input_variables=["schema", "question"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    ), parser