import os
from google.cloud import bigquery
import pandas as pd
import matplotlib.pyplot as plt


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/RITHIN REDDY/Downloads/halogen-goods-457111-g4-3fcb6d8aecd4.json"

client = bigquery.Client()


query1 = """
    SELECT Title, box_office_usd
    FROM `halogen-goods-457111-g4.peerislands.fact_movies`
    WHERE box_office_usd IS NOT NULL
    ORDER BY box_office_usd DESC
    LIMIT 5
"""
df1 = client.query(query1).to_dataframe()
print("Top 5 Highest Grossing Movies")
print(df1)
df1.plot(kind='bar', x='Title', y='box_office_usd', title='Top 5 Highest Grossing Movies', legend=False, color='skyblue')
plt.ylabel("Box Office (USD)")
plt.tight_layout()
plt.show()




