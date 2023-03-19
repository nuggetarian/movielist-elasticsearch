# Top 1000 imdb movies

A simple website to view the first top 1000 movies from imdb.

It utilizes elasticsearch as a database, with the dataset accessible [here](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows).

The point of using elasticsearch is to showcase how it searches for documents based on the closest match and score from the search.

The website works by typing a query into the input field and then getting a list of the closest matches.

# Set-up

- Get [elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) running
- Download the dataset and put it into the project folder
- Type your password into required variables (or set it as an environment variable)
- Copy the cert from elasticsearch config folder into the project folder and type the path into the "ca_certs" variable
- Run indexer.py to create an index and insert documents into elasticsearch
- Run app.py

# Requirements

- python -m pip install elasticsearch
- python -m pip install black (maybe)
- python -m pip install flask
- python -m pip install pandas
- python -m pip install numpy

# Screenshots

<img src="images/homepage.png" width="640" height="360">
<img src="images/search.png" width="640" height="360">
