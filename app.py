#Main app
from flask import Flask, render_template
import connexion

app = Flask(__name__)
app = connexion.App(__name__, specification_dir="./")
app.add_api("cooltexto.yml")

@app.route("/") 
def home():
    return render_template("home.html")  
 

if __name__ == "__main__":
    app.run(port=8000, debug=True)   