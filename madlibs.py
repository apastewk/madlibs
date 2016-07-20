from random import choice, sample

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

MADLIB_FILE = ["/madlib.html", "/madlib2.html"]


@app.route('/')
def start_here():
    """Homepage."""

    return """
    <!doctype html>
    <html>
        <head>
        </head>
        <body>
            <a href="/hello">Welcome!</a>
         </body>
    </html>
    """


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """Play madlibs."""

    game = request.args.get("game")

    if game == "yes":
        return render_template("game.html")
    elif game == "no":
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """Madlib game."""

    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.getlist("noun")
    adjective = request.args.get("adjective")

    madlib_file = choice(MADLIB_FILE)

    return render_template(madlib_file, 
                            person=person, 
                            color=color, 
                            noun=noun, 
                            adjective=adjective)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
