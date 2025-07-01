import os
from google.cloud import bigquery
import pandas as pd
import matplotlib.pyplot as plt

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/RITHIN REDDY/Downloads/halogen-goods-457111-g4-3fcb6d8aecd4.json"

client = bigquery.Client()

query3 = """
    SELECT g.genre_name, AVG(f.Rating) AS avg_rating
    FROM `halogen-goods-457111-g4.peerislands.fact_movies` f
    JOIN `halogen-goods-457111-g4.peerislands.Genre` g
    ON f.genre_id = g.genre_id
    GROUP BY g.genre_name
    ORDER BY avg_rating DESC
"""
df3 = client.query(query3).to_dataframe()
print("Average Rating by Genre")
print(df3)
df3.plot(kind='barh', x='genre_name', y='avg_rating', title='Average Rating by Genre', legend=False, color='orange')
plt.xlabel("Average Rating")
plt.tight_layout()
plt.show()