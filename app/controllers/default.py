import warnings
from flask import Flask
from flask import render_template 
from flask import flash
from flask_login import login_user , login_manager
from app import app,db , lm

#from flask_login import LoginManager

#Imporação da Tabela
from app.models.tables import User
from app.models.tables import Follow
from app.models.tables import Post


from app.models.forms import LoginForm


@lm.user_loader
def user_loader(user_id):
    return User.query.get(user_id)
    #return User.get(user_id)

    

@app.route("/index/<user>")
@app.route("/",defaults={"user":None})
def index(user):
    return render_template('AdminLTE/index.html', 
                            user=user)


@app.route("/analise")
def analise():
    return render_template('AdminLTE/base_template.html')


@app.route("/ex")
def mostra():
    return render_template('AdminLTE/base_template.html')



@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user =  User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
        else:
            flash("Invalid Login")    
    else:
        flash(form.errors)  
 
    return render_template('login.html', form=form)



@app.route("/teste/<info>")
@app.route("/teste",defaults={"info": None})
def teste(info):
    #Create
    #i = User("Lek", "1234", "Yuzo",
    # "marcos@lovemilkshake.com")
    #db.session.add(i)
    #db.session.commit()
    #return 'OK'
    #read
    r = User.query.filter_by(username="Marcos").first()
    print(r.username, r.name)
    return 'ok'




