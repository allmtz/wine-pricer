import flask
from db_functions import searchAllTables, createConnection

app = flask.Flask(__name__)


@app.route('/search/all/<s>', methods=['GET'])
def getMatches(s: str):
    matches = searchAllTables(createConnection(), s)
    return matches


if __name__ == '__main__':
    app.run(debug=True)
