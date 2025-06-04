
from flask import Flask, render_template
import connexion

app = Flask(__name__)
app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yml")

@app.route("/") #The route decorator is what tells it that it is the home. I could call this fxn skibidi and it would still work
def home():
    return render_template("home.html") #Renders templates. Templates hold static data and placeholders for dynamic data.
#Flask uses jinja templates.   

if __name__ == "__main__":
    app.run(port=8000, debug=True) #port 8000 means server. 