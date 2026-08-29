import sqlite3
# from src.prompt import get_prompt
from src.pydantic_prompt import get_prompt
from src.model import get_llm
# from src.parser import get_parser

# def generate_sql(schema: str, question: str):
#     prompt = get_prompt()
#     llm = get_llm()
#     parser = get_parser()
#     chain = prompt | llm | parser
#     # print(chain)
#     return chain.invoke({"schema": schema, "question": question})

def generate_sql(schema: str, question: str):
    prompt, parser = get_prompt()
    llm = get_llm()
    chain = prompt | llm | parser
    return chain.invoke({"schema": schema, "question": question})


def get_schema(db_path="demo.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [t[0] for t in cursor.fetchall()]
    schema_parts = []
    for table in tables:
        cursor.execute(f"PRAGMA table_info({table});")
        columns = [col[1] for col in cursor.fetchall()]
        schema_parts.append(f"Table {table}({', '.join(columns)})")
    conn.close()
    return "\n".join(schema_parts)

def is_safe_sql(sql_query: str) -> bool:
    forbidden = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "TRUNCATE"]
    return not any(word in sql_query.upper() for word in forbidden)


def run_query(sql_query: str, db_path="demo.db"):
    conn = sqlite3.connect(db_path)
    print('Connection established with demo.py')
    cursor = conn.cursor()
    cursor.execute(sql_query)
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    while True:
        question = input("Enter your question: ")
        if question.lower() == 'exit':
            break
        schema = get_schema("demo.db")
        print('-'*50)
        print(schema)
        output = generate_sql(schema, question)
        print('-'*50)
        print("Generated JSON Output:\n", output)
        # if not is_safe_sql(output['sql_query']):
        #     print("\n⚠️ The query is potentially destructive and will NOT be executed.")
        #     print("Generated SQL:\n", output['sql_query'])
        # else:
        #     results = run_query(output["sql_query"])
        #     print("\nQuery Results:\n", results)
        if not is_safe_sql(output.sql_query):
            print("\n⚠️ The query is potentially destructive and will NOT be executed.")
            print("Generated SQL:\n", output.sql_query)
        else:
            results = run_query(output.sql_query)
            print("\nQuery Results:\n", results)
