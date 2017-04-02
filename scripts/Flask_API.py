from flask import Flask
app = Flask(__name__)

@app.route("/")
def do_gif():
    print "Making photo and gif!"

if __name__ == "__main__":
    app.run()