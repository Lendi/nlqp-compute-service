from flask import Flask
from flask_restplus import Resource, Api, fields
app = Flask(__name__)
api = Api(app)

@api.route('/index')
class Home(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == "__main__":
    app.run(debug=True)
