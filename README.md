# AI-Powered SQL Business Intelligence Assistant using Llama 3

An intelligent Business Intelligence (BI) assistant that converts natural language questions into SQL queries using Llama 3 (Groq API), executes them on a MySQL database, and visualizes business insights through interactive dashboards and charts.

---

## Project Overview

This project combines Artificial Intelligence, SQL, Data Analytics, and Business Intelligence into a single interactive application.

Users can ask business-related questions in plain English such as:

- "Show top 5 products by sales"
- "Monthly profit trend"
- "Top customers by quantity"
- "Sales by region"

The application automatically:
1. Converts the question into SQL using Llama 3
2. Executes the query on a MySQL database
3. Displays results in tables and visual charts
4. Generates business insights interactively

---

## Features

- Natural Language to SQL Conversion using Llama 3
- Real-time SQL Query Generation
- MySQL Database Integration
- Interactive Streamlit Dashboard
- Business KPI Analysis
- Automated Data Visualization
- Sales & Profit Analysis
- Customer & Product Insights
- Region-wise and Monthly Trend Analysis
- Dynamic Query Execution
- AI-assisted Business Intelligence Workflow

---

## Tech Stack

### Programming & Libraries
- Python
- Pandas
- Matplotlib
- Streamlit
- MySQL Connector
- Groq API

### AI / LLM
- Llama 3.1 8B Instant
- Prompt Engineering
- Natural Language Query Processing

### Database
- MySQL

---

## Project Structure

```bash
AI_SQL_Business_Assistant/
│
├── app.py
├── ai_engine.py
├── database.py
├── sales.csv
├── requirements.txt
├── README.md
└── screenshots/
```

---

## How It Works

### Step 1 — User Question
The user enters a business question in natural language.

Example:
```text
Top 5 products by sales
```

### Step 2 — Llama 3 Generates SQL
The AI model converts the question into an SQL query.

Example:
```sql
SELECT Product_Name,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 5;
```

### Step 3 — SQL Execution
The generated query is executed on the MySQL database.

### Step 4 — Visualization
Results are displayed using:
- tables
- charts
- business insights

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/AI_SQL_Business_Assistant.git
cd AI_SQL_Business_Assistant
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows
```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup MySQL Database

Create database:

```sql
CREATE DATABASE business_db;
```

Import dataset into MySQL table named:
```text
sales
```

---

### 5. Add Groq API Key

Create `.streamlit/secrets.toml`

```toml
GROQ_API_KEY="your_api_key"
```

---

### 6. Run Application

```bash
streamlit run app.py
```

---

## Example Questions

- Show sales by region
- Top 10 customers by profit
- Monthly sales trend
- Highest profit category
- Top products by quantity
- Sales in South region
- Average discount by category
- Top cities by sales

---

## Future Improvements

- Advanced Prompt Engineering
- Query Validation Layer
- Conversational Memory
- Voice-based BI Assistant
- Advanced Dashboard UI
- Multi-table Database Support
- Export Reports to PDF/Excel
- Role-based Access System

---

## Skills Demonstrated

- Artificial Intelligence Integration
- Large Language Models (LLMs)
- Prompt Engineering
- SQL Query Generation
- Business Intelligence
- Data Analytics
- Data Visualization
- Streamlit App Development
- MySQL Database Management
- API Integration
- End-to-End Project Development

---

## Author

**Shana Parveen KT**

- LinkedIn: https://linkedin.com/in/shanaparveenkt
- GitHub: https://github.com/shanaparveenkt

---

## License

This project is developed for educational and portfolio purposes.
