import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template("home.html")


@app.route('/listOfTours')
def list_of_tours():
    return flask.render_template("listOfTours.html")


@app.route('/asstana')
def asstana():
    return flask.render_template("Asstana.html")


if __name__ == '__main__':
    app.run()
