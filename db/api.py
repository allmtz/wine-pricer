import flask
from db_functions import searchAllTables, createConnection
from flask_cors import CORS

app = flask.Flask(__name__)

# Allow CORS for all routes
CORS(app)


@app.route('/search/all/<s>', methods=['GET'])
def getMatches(s: str):
    matches = searchAllTables(createConnection("/api/test.db"), s)
    return matches


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',     # expose all ports
        port=5000           # port the app will run on. Flask defaults to 5000
    )
