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

graph.randomConnections()

graph.randomRequests()

@app.route('/')
def index():
     return redirect(url_for('users'))

@app.route('/users')
def users():
    """
        Description: Base Route, here we will have all the users so we can see each of their pages
    """
    return render_template('users.html',users=graph.getNodes())

@app.route('/register', methods=['POST'])
def register():
    """
        This request is a post, wont be accesible via browser, more of a API type of call
        Description: Register a new user
        Param: Name
        return id or error
    """
    name = request.args.get("name")
    if name:
        node = Node(name)
        graph.add(node)
        return str(node.id)
    else:
        return "ERROR"


@app.route('/delete', methods=['POST'])
def delete():
    """
        This request is a post, wont be accesible via browser, more of a API type of call
        Description: delete a user
        Param: id
        return none
    """
    id = request.args.get("id")
    if id:
        node = graph.getNode(id)
        graph.delete(node)
        return "done"
    else:
        return "ERROR"

@app.route('/accept', methods=['POST'])
def accept():
    """
        This request is a post, wont be accesible via browser, more of a API type of call
        Description: accept a user
        Param: sender, recipient
        return none
    """
    sender = request.args.get("sender")
    recipient = request.args.get("recipient")
    if sender and recipient:
        sender_node = graph.getNode(sender)
        recipient_node = graph.getNode(recipient)
        graph.acceptRequest(sender_node,recipient_node)
        return "done"
    else:
        return "ERROR"


@app.route('/user/<user>')
def user(user):
    user_object = graph.getNode(user)
    if user_object:
        return render_template('user.html',user=user_object,friends=graph.connections(user_object),requests=graph.friendReceivedRequests(user_object))
    else:
        return redirect(url_for('users'))

@app.route('/static/<path:path>')
def send_static_files(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
   app.run(debug=True)