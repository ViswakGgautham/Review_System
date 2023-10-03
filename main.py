from flask import Flask, render_template, request
from database import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit_feedback', methods=['POST','GET'])
def submit_feedback():
    submit=request.form.get('feedback')
    text=request.form.get('comments')
    insert(submit,text)
    return "Feedback received: {}<br>Comments: {}".format(submit, text)
@app.route('/form.html')
def form():
    return render_template('form.html')
@app.route('/admin.html')
def admin():
    value=count()
    green,red,amber=value[0],value[1],value[2]
    l=comments()
    return render_template('admin.html',green=green,red=red,amber=amber,l=l)


if __name__ == '__main__':
    app.run(debug=True)

