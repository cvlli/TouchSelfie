from flask import Flask, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return '<html><body><h1>Hello World</h1></body></html>'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

photo_path = '/home/pi/Pictures/'

class make_gif(Resource):
    def post(self):
        response = 'Made photo!'
        return response
    def get(self, instance, owner):
        response = 'Made photo!'
        return response


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #do_the_login()
        return 'post sdnjsadshfavsdhhfd'
    else:
        return 'get methode'
        #show_the_login_form()

api.add_resource(make_gif, '/login')

if __name__ == '__main__':
#    app.run()
    app.run(host='0.0.0.0',debug = True) # To run on host IP


