import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from database import connect_db
from ai_engine import generate_sql

st.set_page_config(page_title="AI SQL Assistant")

st.title("AI-Powered SQL Business Intelligence Assistant")

st.write("Ask business questions in natural language.")

question = st.text_input("Enter your question")

if st.button("Analyze"):

    sql_query = generate_sql(question)

    st.subheader("Generated SQL Query")

    st.code(sql_query, language="sql")

    conn = connect_db()

    try:

        result = pd.read_sql(sql_query, conn)

        st.subheader("Query Results")

        st.dataframe(result)

        if len(result.columns) >= 2:

            st.subheader("Visualization")

            x = result.columns[0]
            y = result.columns[1]

            fig, ax = plt.subplots()

            ax.bar(result[x], result[y])

            plt.xticks(rotation=45)

            st.pyplot(fig)

    except Exception as e:

        st.error(f"Error: {e}")



st.sidebar.title("AI SQL Assistant")

st.sidebar.info(
    "Ask questions about sales, profit, customers, and regions."
)


st.markdown("""
### Example Questions

- Show top 10 profitable products
- Which category has highest sales?
- Show sales by region
- Top customers by revenue
""")