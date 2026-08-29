# 🧠 Text‑to‑SQL Generator

An AI‑powered tool that converts **natural‑language questions** into **safe, executable SQL queries**.  
Built with **LangChain**, **Pydantic**, and **Streamlit**, this project bridges the gap between human language and structured database queries.

---

## 🚀 Features

- **Natural‑Language to SQL Conversion** – Ask questions like “Show all customers from Bangalore,” and get valid SQL instantly.  
- **Schema Awareness** – The model uses your database schema to ensure accurate table and column references.  
- **Safe Query Validation** – Automatically blocks destructive queries (`DROP`, `DELETE`, `UPDATE`, etc.).  
- **Explainable Output** – Returns a JSON object with:
  - `sql_query`
  - `explanation`
  - `tables_used`
  - `conditions_applied`
- **Streamlit Interface** – Simple, interactive UI for entering questions and viewing results.

---

## 🧩 Project Structure

    text-to-sql/
    │
    ├── src/
    │   ├── main.py               # Core logic and execution loop
    │   ├── model.py              # LLM configuration (Groq/OpenAI)
    │   ├── prompt.py             # Basic prompt template
    │   ├── pydantic_parsing.py   # Pydantic schema definition
    │   ├── pydantic_prompt.py    # Prompt + parser using PydanticOutputParser
    │   ├── parser.py             # JSON/Pydantic output parser
    │
    │── app.py                    # Streamlit UI
    ├── requirements.txt          # Python dependencies
    ├── .env                      # Environment variables (API keys)
    │── demo.db                   # Sample SQLite database
    └── README.md                 # Project documentation

---

## 🧰 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ared155/Text-to-SQL-Generator.git
   cd Text-to-SQL-Generator

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Set up environment variables**
   Create a .env file in the project root:
   ```bash
   GROQ_API_KEY=your_api_key_here

---

## 🖥️ Usage
1. **▶️ Run the Streamlit app**
   ```bash
   streamlit run src/app.py

2. **💬 Or Run from terminal**
   ```bash
   python src/main.py

--

## 🧠 Tech Stack
| Component | Purpose |
| --- | --- |
| **LangChain** | LLM orchestration and prompt chaining |
| **Pydantic** | Structured output validation |
| **Streamlit** | Interactive web interface |
| **SQLite** | Lightweight demo database |
| **Groq/OpenAI API** | LLM backend for query generation |

--

## ⚙️Example Output
```bash
{
  "sql_query": "SELECT name, age FROM employees WHERE age > 30;",
  "explanation": "Retrieves names and ages of employees older than 30.",
  "tables_used": ["employees"],
  "conditions_applied": ["age > 30"]
}

