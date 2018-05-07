from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField,TextAreaField
from wtforms.validators import DataRequired,EqualTo,Length

class loginForm(FlaskForm):
    user=StringField('用户名：',validators=[DataRequired()])
    password=PasswordField('密码：',validators=[DataRequired()])
    password2=PasswordField('重复密码：',validators=[DataRequired(),EqualTo('password','密码不一致')])
    submit=SubmitField('注册')

class login_form(FlaskForm):
    user=StringField('用户名：',validators=[DataRequired()])
    password=PasswordField('密码：',validators=[DataRequired()])
    yzm=StringField('验证码：',validators=[DataRequired(),Length(4,4)])
    submit=SubmitField('登录')

class query_model_form(FlaskForm):
    keyword=StringField('关键词：',validators=[DataRequired()])
    select=SelectField('类型：',validators=[],choices=(('name','姓名'),('password','密码')))
    submit=SubmitField('提交')

class file_model(FlaskForm):
    title=StringField('标题：',validators=[DataRequired()])
    file_area=TextAreaField('正文：',validators=[DataRequired()],render_kw={'rows':"20"})
    submit=SubmitField('提交')