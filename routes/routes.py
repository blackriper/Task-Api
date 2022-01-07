from re import M
from bson.objectid import ObjectId
from flask import Blueprint,request,Response
from bson import json_util
from flask.json import jsonify
from config.db import db

taskes = Blueprint('tasks', __name__)

@taskes.route('/newtask',methods=['POST'])
def createtask():
   title=request.json["title"] 
   description=request.json["description"]
   leader=request.json["leader"]
   date_created=request.json["date_created"]

   if date_created and title and  description and leader:
       id=db.tasks.insert_one({
           'date_created':date_created,
           'title':title,
           'description':description,
           'leader':leader,
           'completed':False}).inserted_id
       response=jsonify({'_id':str(id)})
       response.status_code=201
       return response
   else:
      return handle_bad_request

@taskes.route('/tasks',methods=['GET'])
def get_all_tasks():
      alltasks=db.tasks.find()
      all_tasks=[]
      for task in alltasks:
          all_tasks.append({
              'id':str(task['_id']),
              'date_created':task['date_created'],
              'title':task['title'],
              'description':task['description'],
              'leader':task['leader'],
              'completed':task['completed']})
      response = json_util.dumps(all_tasks)
      return Response(response, mimetype="application/json")

@taskes.route('/tasks/<id>',methods=['GET'])
def get_one_task(id):
      task=db.tasks.find_one({'_id':ObjectId(id)})
      onetask={
              'id':str(task['_id']),
              'date_created':task['date_created'],
              'title':task['title'],
              'description':task['description'],
              'leader':task['leader'],
              'completed':task['completed']}
      response = json_util.dumps(onetask)
      return Response(response, mimetype="application/json")



@taskes.route('/tasks/<id>',methods=['DELETE'])
def delete_task(id):
    db.tasks.delete_one({'_id':ObjectId(id)})     
    return jsonify({"message":f"{id} task deleted"})



@taskes.route('/task/completed/<id>',methods=['PUT'])
def task_complete(id):
    completed=request.json["completed"]
    db.tasks.update_one({'_id':ObjectId(id)},{"$set":{"completed":completed}})     
    return jsonify({"message":f"Task {id} completed successfully"})



@taskes.route('/tasks/update',methods=['PUT'])
def update_task():
    id=request.json["id"]
    description=request.json["description"]
    title=request.json["title"]
    leader=request.json["leader"]
   
    newvalues={"$set":{
              "title":title,
              "description":description,
              "leader":leader }}

    db.tasks.update_one({'_id':ObjectId(id)}, newvalues)     
    return jsonify({"message":f"{id} task update"})



#error handlers 

@taskes.errorhandler(KeyError)
def handle_bad_request(e):
    message={
        'message':'Error request',
        'status':400
    }
    response= jsonify(message)
    response.status=400
    return response


@taskes.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response