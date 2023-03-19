from elasticsearch import Elasticsearch
import pandas as pd


ELASTIC_PASSWORD = "type-password-here"

es = Elasticsearch(
    "https://localhost:9200",
    ca_certs="path\\http_ca.crt",
    basic_auth=("elastic", ELASTIC_PASSWORD), 
    request_timeout=600
)

if (es.ping() == True):
    print(f"Successfully connected to: {es.info().body['cluster_name']}")
else:
    print("Connection to elastic cluster unsuccessful")

    
df = pd.read_csv('imdb\\imdb_top_1000.csv')
df2 = df[['Poster_Link', 'Series_Title', 'Released_Year', 'Runtime', 'Genre', 'IMDB_Rating', 'Overview']]
df3 = df2.dropna()
df3["id"] = df.index + 1

i = 0
for i, row in df3.iterrows():
    document = {
        "poster": row["Poster_Link"], 
        "name": row["Series_Title"],
        "year": row["Released_Year"],
        "runtime": row["Runtime"],
        "rating": row["IMDB_Rating"],
        "genre": row["Genre"],
        "overview": row["Overview"]
    }
    es.index(index="movies", id=i+1, document=document)
        