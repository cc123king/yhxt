from flask import Flask,render_template,request
from login_form_model import loginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key='a1q1z1-s2w2x2-d3e33c3'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:15370040.lJ@127.0.0.1/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16),unique=True)

class user(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16),unique=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

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
    db.drop_all()
    db.create_all()
    app.run(debug=True)
