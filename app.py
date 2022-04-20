from flask import Flask, render_template, abort
app = Flask(__name__)	

@app.route('/')
def ():
    return render_template("")

@app.route('/')
def ():
    return render_template("")

@app.route('/')
def ():
    return render_template("")


app.run("0.0.0.0",5000,debug=True)
