import os
import streamlit as st
from dotenv import load_dotenv
from src.main import generate_sql, run_query, get_schema, is_safe_sql

# ✅ Load environment variables from .env in the project root
BASE_DIR = os.path.dirname(__file__)
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=ENV_PATH)

DB_PATH = os.getenv("DB_PATH")

st.set_page_config(page_title="Text‑to‑SQL Demo", layout="centered")

st.title("🧠 Text‑to‑SQL Generator")
st.write("Enter a natural‑language question about your database below.")

# --- Input section ---
question = st.text_input("💬 Your question:", placeholder="e.g. Show all users older than 25")

# --- Action button ---
if st.button("Generate SQL"):
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        try:
            schema = get_schema(DB_PATH)
            output = generate_sql(schema, question)

            st.subheader("🧾 Generated SQL Query")
            st.code(output.sql_query, language="sql")

            st.subheader("📊 Explanation")
            st.write(output.explanation)

            st.subheader("📋 Tables Used")
            tables = [t.title() for t in output.tables_used]
            st.write(", ".join(tables) or "None detected")

            st.subheader("🔍 Conditions Applied")
            conditions = [c.title() for c in output.conditions_applied]
            st.write(", ".join(conditions) or "None detected")

            if is_safe_sql(output.sql_query):
                st.subheader("📈 Query Results")
                results = run_query(output.sql_query, db_path=DB_PATH)
                if results:
                    st.dataframe(results)
                else:
                    st.info("No results found for this query.")
            else:
                st.error("⚠️ Unsafe SQL detected. Query displayed but not executed.")
        except Exception as e:
            st.error(f"Error: {e}")

        #     if is_safe_sql(output["sql_query"]):
        #         st.subheader("📈 Query Results")
        #         results = run_query(output["sql_query"], db_path=DB_PATH)
        #         st.dataframe(results)
        #     else:
        #         st.error("⚠️ Unsafe SQL detected. Query displayed but not executed.")
        # except Exception as e:
        #     st.error(f"Error: {e}")

        #     st.subheader("📈 Query Results")
        #     results = run_query(output["sql_query"], db_path=DB_PATH)
            # if results:
            #     st.dataframe(results)
            # else:
            #     st.info("No results found for this query.")
        # except Exception as e:
        #     st.error(f"Error: {e}")

