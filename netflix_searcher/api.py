from flask import Flask, jsonify
import netflix_data

app = Flask(__name__)

@app.route("/")
def api_entry():
  return "This is the netflix searcher api."

@app.route("/all")
def get_all():
  return jsonify(netflix_data.get_movies())

@app.route('/title/<title>')
def search_by_title(title):
  return jsonify(netflix_data.search({'title': title}))

@app.route('/year/<year>')
def search_by_year(year):
  return jsonify(netflix_data.search({'release_year': year}))

@app.route('/director/<director>')
def search_by_director(director):
  return jsonify(netflix_data.search({'director': director}))

@app.route('/cast/<cast>')
def search_by_cast(cast):
  return jsonify(netflix_data.search({'cast': cast}))

@app.route('/duration/<duration>')
def search_by_duration(duration):
  return jsonify(netflix_data.search({'duration': duration}))

@app.route('/description/<description>')
def search_by_description(description):
  return jsonify(netflix_data.search({'description': description}))
