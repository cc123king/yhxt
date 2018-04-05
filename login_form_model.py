from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo

class loginForm(FlaskForm):
    user=StringField('用户名：',validators=[DataRequired()])
    password=PasswordField('密码：',validators=[DataRequired()])
    password2=PasswordField('重复密码：',validators=[DataRequired(),EqualTo('password','密码不一致')])
    submit=SubmitField('注册')