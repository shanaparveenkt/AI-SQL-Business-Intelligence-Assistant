from groq import Groq
import streamlit as st

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

def generate_sql(user_question):

    prompt = f"""
    You are an expert SQL generator.

    Database table name: sales

    Columns:
    Row_ID, Order_ID, Order_Date, Ship_Date,
    Customer_Name, Segment, Country, City,
    State, Region, Product_Name, Category,
    Sub_Category, Sales, Quantity, Discount, Profit

    Convert the following question into a valid SQLite/MySQL SQL query.

    Question:
    {user_question}

    Only return SQL query.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    sql_query = response.choices[0].message.content

    sql_query = sql_query.replace("```sql", "")
    sql_query = sql_query.replace("```", "")

    return sql_query.strip()
