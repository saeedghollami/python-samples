
from flask import Flask, render_template, redirect, url_for, request

import ponydb as db

app = Flask(__name__)


@app.route('/')
def index():
	contacts = db.read_contacts()
	return render_template('index.html', contacts=contacts)


@app.route('/create', methods=['GET', 'POST'])
def create():
	if request.method == 'POST':
		db.create_contact(**dict(request.form))
		return redirect(url_for('index'))
	return redirect(url_for('index'))


@app.route('/update', methods=['GET', 'POST'])
def update():
	if request.method == 'POST':
		db.update_contact(dict(request.form))
		return redirect(url_for('index'))
	return redirect(url_for('index'))


@app.route('/delete/<int:cid>')
def delete(cid):
	db.delete_contact(cid)
	return redirect(url_for('index'))




if __name__ == "__main__":
	app.run(debug=True)