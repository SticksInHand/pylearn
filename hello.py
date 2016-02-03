# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:none@127.0.0.1/qingkexuetang'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'qkxt_user'
    ID = db.Column(db.BigInteger,primary_key = True)
    UserName = db.Column(db.String(255))
    UserMobile = db.Column(db.String(11))
    UserEmail = db.Column(db.String(100))
    UserImg = db.Column(db.String(32))
    psssword = db.Column(db.String(255))
    passhash = db.Column(db.String(32))
    token = db.Column(db.String(32))
    def __repr__(self):
        return '<User %r>'%self.UserName

