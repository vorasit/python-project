from flask import Flask,render_template,request,session
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField,SubmitField,TextAreaField,BooleanField,RadioField,SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'


class MyForm(FlaskForm):
    name    = TextAreaField('Full Name',validators=[DataRequired()])
    isAccept = BooleanField("ยอมรับเงื่อนไขบริการข้อมูล")
    gender = RadioField('เพศ',choices=[('male','ชาย'),('female','หญิง'),('other','อื่นๆ')])
    skill = SelectField('ความสามารถพิเศษ',choices=[('english','ภาษาอังกฤษ'),('ร้องเพลง','ร้องเพลง'),('ทำเว็บ','ทำเว็บ')])
    address = TextAreaField('ที่อยู่')
    submit = SubmitField('save')
    
    

@app.route('/',methods=['GET','POST'])
def index():

    form = MyForm()
    session['isAccept'] = form.isAccept.data
    session['gender'] = form.gender.data
    session['skill'] = form.skill.data
    session['address'] = form.address.data
    if form.validate_on_submit():
        session['name'] = form.name.data
    return render_template("index.html",form = form)



if __name__ == "__main__":
    app.run(debug=True)

