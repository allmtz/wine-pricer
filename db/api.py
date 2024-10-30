import flask
from flask import jsonify
from db_functions import createConnection, findSubstring
from flask_cors import CORS

app = flask.Flask(__name__)

# Allow CORS for all routes
CORS(app)


@app.route('/search/all/<s>', methods=['GET'])
def getMatches(s: str):
    con = createConnection("./db/test.db")
    if not con:
        print("could not connect to db, make sure path is correct")
    matches = findSubstring(con, s)
    return jsonify(matches.fetchall())


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',     # expose all ports
        port=5000           # port the app will run on. Flask defaults to 5000
    )
