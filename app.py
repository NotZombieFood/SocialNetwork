# coding=utf-8

from flask import render_template, redirect, url_for, request, send_from_directory, request, Flask
import datetime, os
from structure import Node, Graph

# %% Flask app
app = Flask(__name__)

graph = Graph()
example_users = ["Antonio Pedrero", "Miguel Triana", "Gerardo Cruz", "Mariana Lopez", "Fernanda Gonzalez"]
for example_user in example_users:
    graph.add(Node(example_user))


@app.route('/users')
def users():
    return render_template('users.html',users=graph.getNodes())

@app.route('/user/<user>')
def user(user):
    user_object = graph.getNode(user)
    if user_object:
        return render_template('user.html',user=user_object)
    else:
        return redirect(url_for('users'))

@app.route('/static/<path:path>')
def send_static_files(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
   app.run(debug=True)