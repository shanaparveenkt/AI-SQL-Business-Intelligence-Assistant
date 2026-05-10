import pandas as pd
from pandasql import sqldf

def run_query(query):

    sales = pd.read_csv("sales.csv")

    result = sqldf(query, locals())

    return result
