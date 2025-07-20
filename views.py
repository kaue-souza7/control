from main import app
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import User, Despesa, Receita, MetaPoupanca
from db import db
import hashlib
from datetime import datetime





app.secret_key= 'passtopass'

lm = LoginManager(app)
lm.login_view = 'login'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)



# ///////////// CRUD LOGIN /////////////

# function for creatng app
def hash(txt):
    hash_obj = hashlib.sha256(txt.encode('utf-8'))
    return hash_obj.hexdigest()

print(hash('Olaa'))


# view for load login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        user = request.form['userForm']
        password = request.form['passwordForm']

        user = db.session.query(User).filter_by(user=user, password=hash(password)).first()
        if not user:
            return "user or password invalid!"
        login_user(user)
        return redirect(url_for('home'))


# Function used by Flask-Login to load a user.”
@lm.user_loader
def user_loader(id):
    user = db.session.query(User).filter_by(id=id).first()
    return user

# view for load home
@app.route('/')
@login_required
def home():
    despesas = current_user.despesas
    receitas = current_user.receitas
    metas = current_user.metas
    return render_template(
        'home.html', 
        despesas=despesas, 
        receitas=receitas,
        metas=metas,
    )


# view for creating new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        name = request.form['nameForm']
        user = request.form['userForm']
        password = request.form['passwordForm']

        new_user = User(name=name, user=user, password=hash(password))
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        
        return redirect(url_for('home'))

# view for logout user
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))









# //////////////     CRUD METAS     /////////////


@app.route('/create/meta', methods=['POST'])
@login_required
def criar_meta():
    user = current_user.id
    mes = datetime.strptime(request.form['mes_referenciaForm'], "%Y-%m-%d").date()
    valor = request.form['valor_metaForm']

    nova_meta = MetaPoupanca(usuario_id=user, mes_referencia=mes, valor_meta=valor)

    db.session.add(nova_meta)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/delete/<int:meta_id>/m', methods=['POST'])
@login_required
def delete_meta(meta_id):
    meta = MetaPoupanca.query.get(meta_id)

    if meta:
        db.session.delete(meta)
        db.session.commit()

    return redirect(url_for('home'))


@app.route('/update/<int:meta_id>/<string:column>', methods=['POST'])
@login_required
def update_meta(meta_id, column):
    meta = MetaPoupanca.query.get(meta_id)

    if column == 'mes_referencia':
        data_str = request.form['mes_referenciaForm']  # '2025-07-01' vindo do input
        data_obj = datetime.strptime(data_str, "%d/%m/%Y").date()
        meta.mes_referencia = data_obj   
        db.session.commit()

    elif column == 'valor_meta':
        valor = request.form['valor_metaForm']
        meta.valor_meta = valor
        db.session.commit()


    return redirect(url_for('home'))





# //////////////     CRUD DESPESAS     /////////////



@app.route('/create/despesa', methods=['POST'])
@login_required
def criar_despesa():
    user = current_user.id
    valor = request.form['valorForm']
    categoria = request.form['categoriaForm']
    descricao = request.form['descricaoForm']
    data_pagamento = datetime.strptime(request.form['data_pagamentoForm'], "%Y-%m-%d").date()
    mes_referencia = datetime.strptime(request.form['mes_referenciaForm'], "%Y-%m-%d").date()

    # falta validar dados do fomrs, verificar se ja existe

    nova_despesa = Despesa(usuario_id=user, valor=valor, categoria=categoria, descricao=descricao, data_pagamento=data_pagamento,  mes_referencia=mes_referencia)

    db.session.add(nova_despesa)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/delete/<int:despesa_id>', methods=['POST'])
def delete_despesa(despesa_id):
    despesa = Despesa.query.get(despesa_id)

    if despesa:
        db.session.delete(despesa)
        db.session.commit()

    return redirect(url_for('home'))



@app.route('/update/<int:despesa_id>/<string:column>', methods=['POST'])
def update_despesa(despesa_id, column):
    despesa = Despesa.query.get(despesa_id)

    if column == 'categoria':
        despesa.categoria = request.form['categoriaForm']
        db.session.commit()

    elif column == 'valor':
        despesa.valor = request.form['valorForm']
        db.session.commit()

    elif column == 'data_pagamento':
        data_str = request.form['data_pagamentoForm']  # '2025-07-01' vindo do input
        data_obj = datetime.strptime(data_str, "%d/%m/%Y").date()
        despesa.data_pagamento = data_obj   
        db.session.commit()

    elif column == 'descricao':
        despesa.descricao = request.form['descricaoForm']
        db.session.commit()

    else: return 'Inválido!'




    return redirect(url_for('home'))
    






# //////////////     CRUD RECEITAS     /////////////


@app.route('/create/receita', methods=['POST'])
@login_required
def criar_receita():
    user = current_user.id
    valor = request.form['valorForm']
    categoria = request.form['categoriaForm']
    descricao = request.form['descricaoForm']
    data_recebimento = datetime.strptime(request.form['data_recebimentoForm'], "%Y-%m-%d").date()
    mes_referencia = datetime.strptime(request.form['mes_referenciaForm'], "%Y-%m-%d").date()

    # falta validar dados do fomrs, verificar se ja existe

    nova_receita = Receita(
        usuario_id=user, 
        valor=valor, 
        categoria=categoria, 
        descricao=descricao, 
        data_recebimento=data_recebimento,  
        mes_referencia=mes_referencia
    )

    db.session.add(nova_receita)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/delete/<int:receita_id>/r', methods=['POST'])
def delete_receita(receita_id):
    receita = Receita.query.get(receita_id)

    if receita:
        db.session.delete(receita)
        db.session.commit()

    return redirect(url_for('home'))



@app.route('/update/<int:receita_id>/<string:column>/r', methods=['POST'])
def update_receita(receita_id, column):
    receita = Receita.query.get(receita_id)

    if column == 'categoria':
        receita.categoria = request.form['categoriaForm']
        db.session.commit()

    elif column == 'valor':
        receita.valor = request.form['valorForm']
        db.session.commit()

    elif column == 'data_recebimento':
        data_str = request.form['data_recebimentoForm']  # '2025-07-01' vindo do input
        data_obj = datetime.strptime(data_str, "%d/%m/%Y").date()
        receita.data_recebimento = data_obj   
        db.session.commit()

    elif column == 'descricao':
        receita.descricao = request.form['descricaoForm']
        db.session.commit()

    else: return 'Inválido!'




    return redirect(url_for('home'))