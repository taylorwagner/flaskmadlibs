from flask import Flask, request, render_template
from stories import stories
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "madlibs-app"

debug = DebugToolbarExtension(app)

@app.route('/')
def index():
    """List of stories form"""

    return render_template("index.html", stories=stories.values())

@app.route('/questions')
def questions():
    """Form to ask for words"""

    story_id = request.args["story_id"]
    story = stories[story_id]

    prompts = story.prompts
    
    return render_template("questions.html", story_id=story_id, title=story.title, prompts=prompts)

@app.route('/story')
def story_page():
    """Function to take the user to the page where they will see the madlib story"""
    story_id = request.args["story_id"]
    story = stories[story_id]

    text = story.generate(request.args)

    return render_template("story.html", title=story.title, text=text)