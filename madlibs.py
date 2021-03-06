from random import choice, sample
from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module; Flask wants
# to know this to know what any imported things are relative to.
app = Flask(__name__)

# List of complimentary terms. Note that variable names in ALL CAPS are almost always
# constants; things that aren't changed during the program run, like this one.
AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely',
]


@app.route('/hello')
def say_hello():
    return "Hello!"


@app.route('/compliment')
def say_something_nice():
    """Return a complimentary sentence, choosing a random adjective."""

    return "You look %s" % choice(AWESOMENESS)


@app.route('/')
def show_form():
    """Show the form."""

    return render_template('form.html')


@app.route('/result')
def show_results():
    """Return MadLib results along with a possible list of compliments."""

    # Get things from GET requests with request.args.get(fieldname)
    person = request.args.get("person")
    noun = request.args.get("noun")
    adjective = request.args.get('adjective')
    color = request.args.get('color')

    if not person or not noun or not adjective or not color:
        return "Please answer all questions!"

    # did they check the box for wanting compliments?
    if request.args.get('wants_compliments'):
        compliments = choose_compliments()
    else:
        compliments = None

    return render_template("result.html",
                           person=person,
                           noun=noun,
                           adjective=adjective,
                           color=color,
                           compliments=compliments)


def choose_compliments():
    """Return list of random compliments."""

    return sample(AWESOMENESS, 3)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
