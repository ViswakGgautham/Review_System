from flask import Flask, render_template, request,redirect, url_for
from database import *


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit_feedback', methods=['POST','GET'])
def submit_feedback():
    submit=request.form.get('feedback')
    text=request.form.get('comments')
    class1=request.form.get('class_id')
    print(submit, class1, text)
    insert(class1,submit,text)

    return "Feedback received: {}<br>Comments: {}".format(class1,submit)
@app.route('/form.html')
def form():
    x=classnames()
    return render_template('form.html',classes=x)
'''@app.route('/admin.html')
def admin():
    value=count()
    green,red,amber=value[0],value[1],value[2]
    l=comments()
    return render_template('admin.html',green=green,red=red,amber=amber,l=l)'''
@app.route('/admin_choice.html')
def admin_choice():
    return render_template('admin_choice.html')
@app.route('/add_class.html', methods=['GET'])
def add_class():
    return render_template('add_class.html')
@app.route('/add_class.html', methods=['POST'])
def add_class_submit():
    class_id = request.form['class_id']
    no_of_students = request.form['no_of_students']
    year = request.form['year']
    insert_class(class_id,no_of_students,year)
    return redirect(url_for('class_added'))
@app.route('/class_added')
def class_added():
    return 'Class added successfully.'
@app.route('/view_class_details')
def view_class_details():
    l=classnames()
    return render_template('view_class_details.html',classes=l)
@app.route('/view_class_details', methods=['POST'])
def view_class_details1():
    class_id = request.form.get('class_id')
    value = count(class_id)
    green, red, amber = value[0], value[1], value[2]
    l = comments(class_id)
    return render_template('/admin.html',green=green,red=red,amber=amber,l=l)



if __name__ == '__main__':
    app.run(debug=True)

