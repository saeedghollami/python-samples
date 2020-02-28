
from flask import Flask, render_template, redirect, url_for

import ponydb as db

app = Flask(__name__)


@app.route('/')
def index():
	contacts = db.read_contacts()
	return render_template('index.html', contacts=contacts)


@app.route('/delete/<int:cid>')
def delete(cid):
	db.delete_contact(cid)
	return redirect(url_for('index'))


if __name__ == "__main__":
	app.run(debug=True)