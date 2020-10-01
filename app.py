from flask_api import FlaskAPI, status, exceptions

app = FlaskAPI(__name__)

@app.route("/qualifyingoffer", methods=['GET'])
def get():
