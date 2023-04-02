from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/contactus')
def contactus():
    return render_template("contactus.html")





if __name__ == "__main__":
    app.run(debug=True)


app.static_folder = "static"