from flask import Flask,render_template,request
from login_form_model import loginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key='a1q1z1-s2w2x2-d3e33c3'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:15370040.lJ@127.0.0.1/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login.html',methods=['POST','GET'])
def login():
    form = loginForm()
    if request.method=='GET':
        return render_template('login.html',form=form)
    elif form.validate_on_submit():
        return 'seccess'

if __name__ == '__main__':
    app.run(debug=True)
