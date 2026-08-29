from langchain_core.prompts import PromptTemplate

# def get_prompt():
#     template = """
#     You are a system that converts natural language questions into SQL queries.
#     Use ONLY the schema provided. Do not assume extra columns or tables.
#     Output must strictly follow this JSON schema:
#     {{
#       "sql_query": "string",
#       "explanation": "string",
#       "tables_used": ["string"],
#       "conditions_applied": ["string"]
#     }}

#     DATABASE CONTEXT:
#     {schema}

#     QUESTION:
#     {question}
#     """
#     return PromptTemplate.from_template(template)

def get_prompt():
    template =  """
    You are a system that converts natural language questions into SQL queries.
    Use ONLY the schema provided. Do not assume extra columns or tables.
    Output must strictly follow this JSON schema:
    {{
    "sql_query": "string",
    "explanation": "string",
    "tables_used": ["string"],
    "conditions_applied": ["string"]
    }}
    DATABASE CONTEXT:
    {schema}
    QUESTION:
    {question}
    """
    return PromptTemplate.from_template(template)

