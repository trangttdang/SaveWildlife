from datetime import timedelta
from flask import Flask
from flask.templating import render_template
from graph import predict_file
from emergency import ve
from table import future2

species = ["Mammals", "Birds", "Reptiles", "Amphibians", "Fishes", "Insects", "Molluscs", "Other_invertebrates"]

app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    ve("static/data/data.csv")
    for s in species:
        predict_file("static/data/data.csv", s)
        
    return render_template("home.html", title = "Dashboard", post = future2("static/data/data.csv", s))

@app.route('/campaign')
def campaign():
    return render_template("campaign.html", title = "Campaign")

@app.route('/profile')
def profile():
    return render_template("profile.html", title = "Profile")


if __name__ == '__main__':
    app.run(debug=True)