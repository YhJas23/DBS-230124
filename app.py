from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        rate = float(request.form.get("rates"))
        return(render_template("index.html", result = 90.2-(50.6*rate)))
    else:
        return render_template("index.html", result ="Waiting……….")
if __name__=="__main__":
    app.run()
