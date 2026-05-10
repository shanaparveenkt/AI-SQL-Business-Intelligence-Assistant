from pandasql import sqldf

def run_query(query, sales):

    result = sqldf(query, {"sales": sales})

    return result
