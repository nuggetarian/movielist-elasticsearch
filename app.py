from flask import Flask, request, render_template
from elasticsearch import Elasticsearch

app = Flask(__name__)

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

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('index.html')
    

@app.route("/search", methods=['GET', 'POST'])
def search():
    query = request.form["query"].lower()
    words = query.split(" ")
    
    payload = {
            "bool": {
            "must": [
                {
                "match": {
                    "name": {
                    "query": value,
                    "fuzziness": "auto"
                    }  
                }
                }
                for value in words
            ],
            "should": [
                {
                "match_phrase": {
                    "name": {
                    "query": value,
                    "slop": 2
                    }
                }
                }
                for value in words
            ]
            }
        }

    resp = es.search(index="movies", query=payload, size=5)
    return render_template('movie.html', resp=resp, words=words)

if __name__ == "__main__":
    app.run(debug=True)
