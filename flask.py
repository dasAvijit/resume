from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def conspectus():
    return render_template("conspectus.html")

@app.route('/experience/')
def experience():
    return render_template("experience.html")

@app.route('/achievements/')
def achievements():
    return render_template("achievements.html")

@app.route('/contactinfo/')
def contactinfo():
    return render_template("contactinfo.html")

@app.route('/skills/')
def skills():
    return render_template("skills.html")

@app.route('/training/')
def training():
    return render_template("training.html")

if __name__=="__main__":
    app.run(debug=True)
