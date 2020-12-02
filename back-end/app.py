from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource
import time

app = Flask(__name__)
cors = CORS(app, resources={r'*': {'origins': '*'}})
api = Api(app)

class SomeNames(Resource):
  def get(self):
    response = [
      {"name":"Jen"},
      {"name":"Mike"},
      {"name":"Owen"},
      {"name":"Todd"}
    ]

    return jsonify(response)

class MetResTest(Resource):
  def get(self):
    param1 = None
    param2 = None

    if('param1' in request.args):
      param1 = request.args.get('param1')
    
    if('param2' in request.args):
      param2 = request.args.get('param2')

    response = {
      'status': 'success',
      'data': (param1, param2),
      'message': 'get invoked succesfully'
    }

    return jsonify(response)
  
  def post(self):
    raw_data = request.get_json()
    response = {
      'status': 'success',
      'data': raw_data,
      'message': 'post invoked succesfully'
    }

    return jsonify(response)
  
  def put(self):
    response = {
      'status': 'success',
      'message': 'put invoked succesfully'
    }

    return jsonify(response)

  def patch(self):
    response = {
      'status': 'success',
      'message': 'patch invoked succesfully'
    }

    return jsonify(response)
  
  def delete(self):
    response = {
      'status': 'success',
      'message': 'delete invoked succesfully'
    }

    return jsonify(response)
  

api.add_resource(MetResTest, '/test/metres')
api.add_resource(SomeNames, '/some/names')

if(__name__ == '__main__'):
  # app.run()
  pass
