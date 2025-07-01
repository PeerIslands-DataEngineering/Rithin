import os
from google.cloud import bigquery
import pandas as pd
import matplotlib.pyplot as plt

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/RITHIN REDDY/Downloads/halogen-goods-457111-g4-3fcb6d8aecd4.json"

client = bigquery.Client()

query2 = """
    SELECT a.actor_name, SUM(f.num_awards) as total_awards
    FROM `halogen-goods-457111-g4.peerislands.fact_movies` f
    JOIN `halogen-goods-457111-g4.peerislands.Actor` a
    ON f.actor_id = a.actor_id
    GROUP BY a.actor_name
    ORDER BY total_awards DESC
    LIMIT 1
"""
df2 = client.query(query2).to_dataframe()
print("Most Awarded Actor")
print(df2)
df2.plot(kind='bar', x='actor_name', y='total_awards', title='Most Awarded Actor', legend=False, color='green')
plt.ylabel("Total Awards")
plt.tight_layout()
plt.show()