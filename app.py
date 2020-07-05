from flask import Flask, jsonify, json, render_template
import pymongo
from boto.s3.connection import S3Connection
import os

# Function to extract data from DB


def list_data(list, data):
    for result in data:
        list.append(result)


# Create a connection to MongoDB
s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])
conn = MONGODB_URI
# conn = 'mongodb://localhost:27017'
# conn = 'mongodb+srv://Enr1qu319:forelsket1@videogames.vtdkb.mongodb.net/<dbname>?retryWrites=true&w=majority'

# Client for mongo
client = pymongo.MongoClient(conn)

# Database
db = client.videogames

# Collections
games_results = db.games.find({}, {"_id": 0})
genres_results = db.genres.find({}, {"_id": 0})
top3gensales_percomp_results = db.top3gensales_percomp.find({}, {"_id": 0})
top3vgs_peryear_results = db.top3vgs_peryear.find({}, {"_id": 0})
totglobsales_percomp_results = db.totglobsales_percomp.find({}, {"_id": 0})


# Create list to storage json
games_json = []
genres_json = []
top3gensales_percomp_json = []
top3vgs_peryear_json = []
totglobsales_percomp_json = []


# Json format data
list_data(games_json, games_results)
list_data(genres_json, genres_results)
list_data(top3gensales_percomp_json, top3gensales_percomp_results)
list_data(top3vgs_peryear_json, top3vgs_peryear_results)
list_data(totglobsales_percomp_json, totglobsales_percomp_results)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


@app.route('/')
def home():

    return render_template("index.html")


@ app.route('/api/v1/games')
def games():

    return jsonify(games_json)


@ app.route('/api/v1/genres')
def genres():

    return jsonify(genres_json)


@ app.route('/api/v1/top3gensales_percomp')
def top3gensales_percomp():

    return jsonify(top3gensales_percomp_json)


@ app.route('/api/v1/top3vgs_peryear')
def top3vgs_peryear():

    return jsonify(top3vgs_peryear_json)


@ app.route('/api/v1/totglobsales_percomp')
def totglobsales_percomp():

    return jsonify(totglobsales_percomp_json)


if __name__ == "__main__":
    # @TODO: Create your app.run statement here
    app.run(debug=True)
