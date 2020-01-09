# Microblog Flask Web App

This is a web app built with Python and Flask from the ground up by following Miguel Grinberg's phenomenal [tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world). Most of the code is either very similar or identical to example code he provides. Anyone interested in learning about full stack web development will find the resources he provides truly invaluable. 

The app makes use of a variety of useful Flask extensions including Flask-Bootstrap, Flask-Login, Flask-Moment, Flask-WTF, as well as Flask-SQLAlchemy and Flask-Migrate for interfacing with and managing a relational database on the backend. Front end styling is acheived with Bootstrap. 

The app itself is a microblog which allows users to make accounts, login, post messages, and follow posts by other users. There is also an automatic post translation service (as of yet incomplete) and a post text search feature implemented with [Elasticsearch](https://www.elastic.co/products/elasticsearch).

To run and host locally:
```
$ conda create -n mb_flask_env python=3.7 pip
$ source activate mb_flask_env
$ git clone https://github.com/ofbennett/microblog_flask_app.git
$ pip install -r requirements.txt
$ export FLASK_APP=microblog.py
$ flask db update
$ flask run
```
The app will be available to view in a browswer at: `localhost:5000/`

In order for the text search feature to work you need Elasticsearch installed and running, available on http://localhost:9200

To include this feature run:
```
$ export ELASTICSEARCH_URL=http://localhost:9200
```
