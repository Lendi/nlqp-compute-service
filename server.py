from flask import Flask
from flask_restplus import Resource, Api, fields
app = Flask(__name__)
api = Api(app)

@api.route('/index')
class Home(Resource):
    def get(self):
        return {'hello': 'world'}

<<<<<<< HEAD
@api.route('/api/v1/query/<string:query>')
class QueryResource(Resource):
	def get(self, query):
		return{'query':query}


=======
>>>>>>> 39b9e750c9c3918fc5bb8743ae17a939cbe71996
if __name__ == "__main__":
    app.run(debug=True)
