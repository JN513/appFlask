import os

basedir = os.path.abspath(os.path.dirname(__file__))  # Diretorio do projeto

class Config(object):
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "um-nome-bem-seguro"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PAGINATION = 10