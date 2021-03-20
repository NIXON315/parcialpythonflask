from src import app
from src.controllers.basedb import DatabaseController
from flask import make_response, jsonify, request
databaseController = DatabaseController()
@app.route('/datab', methods=['GET'])
def databaseList():
    dbs = databaseController.list()
    return make_response(jsonify(dbs), 200)
@app.route('/datab', methods=['POST'])
def databaseCreate():
    databases = request.json['databases']
    databaseController.create(databases)
    return make_response('database created successfully', 201)
@app.route('/tables/<datab>', methods=['GET'])
def tableList(datab):
    tables = databaseController.search(datab)
    return make_response(jsonify(tables), 200)
