from flask import render_template
from app import app,db

#Imporação da Tabela
from app.models.tables import User
from app.models.tables import Follow
from app.models.tables import Post


from app.models.forms import LoginForm



@app.route("/index/<user>")
@app.route("/",defaults={"user":None})
def index(user):
    return render_template('AdminLTE/index.html', 
                            user=user)


@app.route("/adm")
def adm():
    return render_template('AdminLTE/base.html')


@app.route("/ex")
def mostra():
    return render_template('AdminLTE/base_template.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
        
    return render_template('login.html',
                            form=form)






@app.route("/teste/<info>")
@app.route("/teste",defaults={"info": None})
def teste(info):
    i = User("iceghost", "1234", "Marcos",
     "marcos_henrique@outlook.com")
    db.session.add(i)
    db.session.commit()









