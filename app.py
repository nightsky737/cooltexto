#Main app
from flask import Flask, render_template, request, jsonify
import generator
from flask_session import Session
import redis
import connexion
import os
from flask_cors import CORS
# http://localhost:5500/cooltexto.html
# http://localhost:8000/api/generator
#http://localhost:8000/api/ui/#/default/generator.generate_orderings
#http://192.168.1.134:8000/
app = connexion.App(__name__, specification_dir="./")
flask_app = app.app
# CORS(flask_app, origins="http://localhost:5500")  basically stops it from tweaking when i try to access it from a html page
CORS(flask_app)  #https://medium.com/@mterrano1/cors-in-a-flask-api-38051388f8cc

app.debug = True
flask_app.secret_key = os.urandom(12)
# app.add_api("cooltexto.yml") NO THIS IS OLD AND SUCKS AND I GIVE UP ON IT

SESSION_TYPE = 'redis'
SESSION_REDIS = redis.Redis(host='localhost', port=6379)
flask_app.config.from_object(__name__)
Session(flask_app)

@app.route("/") 
def home():
    return render_template("home.html", word= "WELCOME TO THE DEFAULT PAGE")  

@app.route("/generate") 
def generate():
    generator.generate_orderings() #Returns the word but i am not supposed to put the word in js so ppl cant cheat
    return jsonify({"word": generator.get_current_word()})

@app.route("/guess", methods=["POST"]) #APparently need to do options in order to 
def guess():
    if request.method == 'POST': #request is basically the info the client sent to the server.
        users_guess = request.get_json()["guess"]
        guess_rank=generator.guess(users_guess)
        return jsonify({"rank":guess_rank})

@app.route("/get_previous_guesses") #APparently need to do options in order to 
def get_previous_guesses():
    return jsonify(generator.get_guesses())

if __name__ == "__main__":
    app.run(port=8000, debug=True)   




