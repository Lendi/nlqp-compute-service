from flask import Flask
from flask_restplus import Resource, Api, fields
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)
CORS(app)

@api.route('/index')
class Home(Resource):
    def get(self):
        return {'hello': 'world'}


@api.route('/api/v1/query/<string:query>')
class QueryResource(Resource):
	def get(self, query):
		return {'query':query}



if __name__ == "__main__":
    app.run(debug=True)
