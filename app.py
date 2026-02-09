from flask import Flask
from flask import render_template
# Create an instance of flask

app = Flask(__name__)

#function that return content
#using the app.route decorartor to map the URL
@app.route("/")
def index():
    return render_template("index.html")

#TO RUN YOUR APP enter "flask run" into your terminal
#TO STOP press ctrl+c in the terminal