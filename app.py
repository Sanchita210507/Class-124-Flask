from flask import Flask

# variable app is now a Flask object
app = Flask(__name__)

# use route() decorator to tell Flask what URL should trigger our function.
@app.route("/")
def helloWorld():
    return "Hello World..."
    
# creating one more end point
@app.route("/intro")
def intro():
    return "Hey this is Sanchita!!"

if __name__ == "__main__":
    #app.run(debug = True)
    app.run(debug=True , port = 8000)