from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    name = 'tommy'
    return render_template('index.html', name=name)

@app.route('/home')
def home():
    return "This is home page"

app.run(debug=True)