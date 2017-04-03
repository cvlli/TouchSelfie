from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

pyasn_photo_path = '/home/pi/Pictures/'
#asndb = pyasn.pyasn(pyasn_dat_file)

class make_gif(Resource):
    def post(self):
        response = 'Made photo!'
        return response
    def __get__(self, instance, owner):
        response = 'Made photo!'
        return response

api.add_resource(make_gif, '/make_gif')

if __name__ == '__main__':
#    app.run()
    app.run(host='0.0.0.0') # To run on host IP


