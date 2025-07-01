import os
from google.cloud import bigquery
import pandas as pd
import matplotlib.pyplot as plt

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/RITHIN REDDY/Downloads/halogen-goods-457111-g4-3fcb6d8aecd4.json"

client = bigquery.Client()

query5 = """
    SELECT c.company_name, AVG(f.budget_usd) AS avg_budget
    FROM `halogen-goods-457111-g4.peerislands.fact_movies` f
    JOIN `halogen-goods-457111-g4.peerislands.Company` c
    ON f.company_id = c.company_id
    WHERE f.budget_usd IS NOT NULL
    GROUP BY c.company_name
    ORDER BY avg_budget DESC
    LIMIT 5
"""
df5 = client.query(query5).to_dataframe()
print("Average Budget by Production Company")
print(df5)
df5.plot(kind='bar', x='company_name', y='avg_budget', title='Average Budget by Production Company', legend=False, color='purple')
plt.ylabel("Avg Budget (USD)")
plt.tight_layout()
plt.show()