from flask import Flask,render_template,request

from flask_wtf  import Form
from wtforms import StringField,SubmitField

FAI=Flask(__name__)

@FAI.route('/htmlform',methods=['GET','POST'])
def htmlform():

    if request.method=='POST':
        fd=request.form

        un=fd['un']

        return un

    return render_template('htmlform.html') 


class NameForm(Form):
    name=StringField()
    submit=SubmitField()

@FAI.route('/webform',methods=['GET','POST'])
def webform():
    NFO=NameForm()

    if request.method=='POST':
        NFDO=NameForm(request.form)

        if NFDO.validate():
            return NFDO.name.data

    return render_template('webform.html',NFO=NFO)


if __name__ == '__main__':
    FAI.run(debug=True)