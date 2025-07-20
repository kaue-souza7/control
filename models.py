from db import db
from flask_login import UserMixin
from datetime import date

class User(UserMixin,  db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(30), unique=True)
    user = db.Column(db.String(30), unique=True)
    password = db.Column(db.String())

    # Relacionamentos
    receitas = db.relationship('Receita', backref='usuario', lazy=True)
    despesas = db.relationship('Despesa', backref='usuario', lazy=True)
    metas = db.relationship('MetaPoupanca', backref='usuario', lazy=True)



class Receita(db.Model):
    __tablename__ = 'receitas'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    categoria = db.Column(db.String(100), nullable=True)
    descricao = db.Column(db.Text, nullable=True)
    data_recebimento = db.Column(db.Date, default=date.today)
    mes_referencia = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Receita R${self.valor} - {self.mes_referencia}>"


class Despesa(db.Model):
    __tablename__ = 'despesas'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    categoria = db.Column(db.String(100), nullable=True)
    descricao = db.Column(db.Text, nullable=True)
    data_pagamento = db.Column(db.Date, default=date.today)
    mes_referencia = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Despesa R${self.valor} - {self.mes_referencia}>"


class MetaPoupanca(db.Model):
    __tablename__ = 'metas_poupanca'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    mes_referencia = db.Column(db.Date, nullable=False)
    valor_meta = db.Column(db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f"<Meta R${self.valor_meta} - {self.mes_referencia}>"