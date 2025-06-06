#Main app
from flask import Flask, render_template, request, jsonify
import generator
from flask_session import Session
import redis
import connexion
import os
from flask_cors import CORS

app = connexion.App(__name__, specification_dir="./")
flask_app = app.app
CORS(flask_app, origins="http://localhost:5500")  #https://medium.com/@mterrano1/cors-in-a-flask-api-38051388f8cc

flask_app.secret_key = os.urandom(12)
app.add_api("cooltexto.yml")

SESSION_TYPE = 'redis'
SESSION_REDIS = redis.Redis(host='localhost', port=6379)
flask_app.config.from_object(__name__)
Session(flask_app)

@app.route("/") 
def home():
    generator.generate_orderings()
    return render_template("home.html")  

@app.route("/guess", methods=["POST"])
def guess():
    if request.method == 'POST':
        guess_rank=generator.guess(request.form.get("guess"))
        return jsonify({'rank': guess_rank})
        # return render_template("guess.html", guess=request.form.get("guess"), guess_ranking=guess_rank) 
 
if __name__ == "__main__":
    app.run(port=8000, debug=True)   




