from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/application-form')
def application_form():

    return render_template('application-form.html',
                            jobs = ["Software Engineer - Front End",
                            "Software Engineer - Back End",
                            "Software Engineer - Full Stack", "QA Engineer",
                            "Product Manager"])


@app.route('/application-response', methods=["POST"])
def application_response():

    first_name = request.form["first"]
    last_name = request.form["last"]
    salary = request.form["salary"]
    position = request.form["preferred"]

    return render_template('application-response.html', name=first_name,
                            surname=last_name, minimum=salary,
                            job=position, method="POST")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
