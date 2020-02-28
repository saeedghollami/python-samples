
from flask import Flask, render_template

import ponydb as db

app = Flask(__name__)


@app.route('/')
def index():
	contacts = db.read_contacts()
	return render_template('index.html', contacts=contacts)


if __name__ == "__main__":
	app.run(debug=True)