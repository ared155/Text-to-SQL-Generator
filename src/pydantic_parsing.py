from pydantic import BaseModel, Field

class SQLResponse(BaseModel):
    sql_query: str = Field(..., description="The SQL query")
    explanation: str = Field(..., description="Explanation of the query")
    tables_used: list[str] = Field(..., description="Tables referenced")
    conditions_applied: list[str] = Field(..., description="Conditions applied")