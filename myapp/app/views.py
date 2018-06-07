from flask import render_template,request,flash
from forms import SearchForm

from app import app

@app.route('/', methods=['GET', 'POST'])
def google():
    form=SearchForm(request.form)
    #process what is entered at the press of enter
    if form.validate() and request.method=='POST':
        input=form.input.data
        if input == "":
            error="I cant search nothing, Please type or drop a link "
            return render_template("google.html",form=form,error=error)
        else:
            msg="Searching......."+ input
            return render_template('google.html',form=form,msg=msg)
    return render_template('google.html',form=form)