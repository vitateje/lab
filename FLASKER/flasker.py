from flask import Flask, render_template
app = Flask(__name__, template_folder="templates",)

@app.route("/")
def hello():
    return render_template("index.html")

teste = ['ola', 'carta']

@app.route('/home')
def home():
    """Landing page."""
    return render_template('index.html',
                           title=teste,
                           description="Smarter page templates \
                                with Flask & Jinja.")



if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)