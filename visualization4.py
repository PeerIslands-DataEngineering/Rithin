import os
from google.cloud import bigquery
import pandas as pd
import matplotlib.pyplot as plt

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/RITHIN REDDY/Downloads/halogen-goods-457111-g4-3fcb6d8aecd4.json"

client = bigquery.Client()

query4 = """
    SELECT l.language_name, COUNT(*) as movie_count
    FROM `halogen-goods-457111-g4.peerislands.fact_movies` f
    JOIN `halogen-goods-457111-g4.peerislands.Language` l
    ON f.language_id = l.language_id
    GROUP BY l.language_name
    ORDER BY movie_count DESC
    LIMIT 3
"""
df4 = client.query(query4).to_dataframe()
print("Top 3 Languages by Number of Movies")
print(df4)
df4.plot(kind='pie', y='movie_count', labels=df4['language_name'], title='Top 3 Languages by Number of Movies', legend=False, autopct='%1.1f%%')
plt.ylabel("")
plt.tight_layout()
plt.show()