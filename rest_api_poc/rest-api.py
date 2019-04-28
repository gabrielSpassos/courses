from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'World'}


tasks = {}


class Task(Resource):
    def get(self, task_id):
        return {task_id: tasks[task_id]}


    def post(self, task_id):
        tasks[task_id] = request.form['taskName']
        return {task_id: tasks[task_id]}


class TaskList(Resource):
    def get(self):
        return tasks


api.add_resource(HelloWorld, '/')
api.add_resource(Task, '/tasks/<int:task_id>')
api.add_resource(TaskList, '/tasks')


if __name__ == '__main__':
    app.run(debug=True)
