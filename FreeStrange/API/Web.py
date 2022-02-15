"""
Web API
"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# thanks hell 2017/7/9
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '哈哈哈'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument('task')


# # 操作（put / get / delete）单一资源Todo
class Todo(Resource):
    @staticmethod
    def get(todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    @staticmethod
    def delete(todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    @staticmethod
    def put(todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# # 操作（post / get）资源列表TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    @staticmethod
    def get():
        return TODOS

    @staticmethod
    def post():
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


# 设置路由
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == '__main__':
    raise ValueError('Not for run')
else:
    print(__name__)
    app.run(debug=True)
