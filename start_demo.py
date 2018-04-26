from flask import Flask,render_template,request
from login_form_model import loginForm,login_form,query_model_form,file_model
from flask_sqlalchemy import SQLAlchemy
import register,query
from edit import edits

app = Flask(__name__)
app.secret_key='a1q1z1-s2w2x2-d3e33c3'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:15370040.lJ@127.0.0.1/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16),unique=True)

class text(db.Model):
    __tablename__='texts'
    title=db.Column(db.String(28),primary_key=True)
    text=db.Column(db.Text)

class user(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16),unique=True)
    password=db.Column(db.String(20))
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/register.html',methods=['POST','GET'])
def login():
    form = loginForm()
    if request.method=='GET':
        return render_template('register.html',form=form)
    elif form.validate_on_submit():
        username=request.form.get('user')
        password=request.form.get('password')
        register.register(username,password,1)
        return '注册成功'
@app.route('/login.html',methods=['POST','Get'])
def login2():
    form1=login_form()
    if request.method=="GET":
        return render_template('login.html',form1=form1)
    elif form1.validate_on_submit():
        username = request.form.get('user')
        password = request.form.get('password')
        cx=user.query.filter_by(name=username).first()
        '''
        测试用例
        '''
        #print(cx.password)
        #print(username)
        #登录验证
        database_password=cx.password
        if password==database_password:
            return 'login seccess'
        else:
            return '密码错误！'
@app.route('/query_form.html',methods=['GET','POST'])
def query_f():
    if request.method=='GET':
        form=query_model_form()
        return render_template('query_form.html',form=form)
    else:
        #print(request.form.get('select'))
        #return request.form.get('select')
        select=request.form.get('select')
        keyword=request.form.get('keyword')
        #list2=query.query_user(keyword,select)
        list2=user.query.filter_by(name=keyword).all()

        return render_template('query.html',list=list2)
@app.route('/query.html')
def query():
    return render_template('query.html')
@app.route('/dataanaltsis.html')
def da():
    return render_template('dataanaltsis.html')

@app.route('/edit.html',methods=['GET','POST'])
def edit():
    if request.method=='GET':
        form=file_model()
        return render_template('edit.html',form=form)
    else:
        title=request.form.get('title')
        file=request.form.get('file_area')
        #print(file)
        edits(title,file)
        return render_template('index.html')

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    role1=role(id=1,name='admin')
    role2=role(id=2,name='pt')
    db.session.add(role1)
    db.session.add(role2)
    db.session.commit()
    app.run(debug=True)