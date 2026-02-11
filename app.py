from flask import Flask
from flask import render_template
# Create an instance of flask

app = Flask(__name__)

#function that return content
#using the app.route decorartor to map the URL
@app.route("/")
def index():
    name_data = 'Kevin'
    year_data = 2027
    favorite_list = ['apple','banana','pear','peach']
    rating_dict = {
        'apple': 7,
        'banana': 5,
        'pear': 9,
        'peach': 10
        }

    return render_template("index.html", name=name_data, year=year_data, favorites=favorite_list, ratings=rating_dict)

#TO RUN YOUR APP enter "flask run" into your terminal
#TO STOP press ctrl+c in the terminal