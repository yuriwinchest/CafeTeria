from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os
from config import DATABASE_CONFIG

app = Flask(__name__, static_folder='src/static', template_folder='templates')

# Configuração da conexão com o banco de dados
db = mysql.connector.connect(**DATABASE_CONFIG)

# Certifique-se de que o diretório 'src/static/img' existe
if not os.path.exists('src/static/img'):
    os.makedirs('src/static/img')

def sanitize_filename(filename):
    return "".join(c for c in filename if c.isalnum() or c in (' ', '.', '_', '-')).rstrip()

@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos ORDER BY data_criacao DESC")
    produtos = cursor.fetchall()
    cursor.close()
    return render_template('index.html', produtos=produtos)

@app.route('/admin')
def admin():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos ORDER BY data_criacao DESC")
    produtos = cursor.fetchall()
    cursor.close()
    return render_template('admin.html', produtos=produtos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()
        cursor.close()
        if user:
            return redirect(url_for('admin'))
        else:
            return 'Credenciais inválidas'
    return render_template('login.html')

@app.route('/cardapio', methods=['GET', 'POST'])
def cardapio():
    if request.method == 'POST':
        return 'Pedido recebido!'
    else:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cardapio")
        cardapio_items = cursor.fetchall()
        cursor.close()
        return render_template('cardapio.html', cardapio_items=cardapio_items)

@app.route('/cadastrar-produto', methods=['GET', 'POST'])
def cadastrar_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        tipo = request.form['tipo']
        descricao = request.form['descricao']
        preco = request.form['preco'].replace(',', '.')  # Substitui vírgula por ponto
        imagem = request.files['imagem']
        imagem_filename = sanitize_filename(imagem.filename)
        imagem_path = os.path.join(app.static_folder, 'img', imagem_filename)
        imagem.save(imagem_path)
        # Salvar o caminho relativo da imagem
        imagem_rel_path = 'img/' + imagem_filename
        cursor = db.cursor()
        cursor.execute("INSERT INTO produtos (nome, tipo, descricao, preco, imagem, data_criacao) VALUES (%s, %s, %s, %s, %s, NOW())",
                       (nome, tipo, descricao, preco, imagem_rel_path))
        db.commit()
        cursor.close()
        return redirect(url_for('admin'))
    return render_template('cadastrar-produto.html')

@app.route('/editar-produto/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos WHERE id=%s", (id,))
    produto = cursor.fetchone()
    cursor.close()

    if produto is None:
        return "Produto não encontrado", 404

    if request.method == 'POST':
        novo_nome = request.form['nome']
        novo_tipo = request.form['tipo']
        nova_descricao = request.form['descricao']
        novo_preco = request.form['preco'].replace(',', '.')  # Substitui vírgula por ponto
        imagem = request.files['imagem']
        cursor = db.cursor()
        if imagem:
            imagem_filename = sanitize_filename(imagem.filename)
            imagem_path = os.path.join(app.static_folder, 'img', imagem_filename)
            imagem.save(imagem_path)
            imagem_rel_path = 'img/' + imagem_filename
            cursor.execute("UPDATE produtos SET nome=%s, tipo=%s, descricao=%s, preco=%s, imagem=%s, data_criacao=NOW() WHERE id=%s",
                           (novo_nome, novo_tipo, nova_descricao, novo_preco, imagem_rel_path, id))
        else:
            cursor.execute("UPDATE produtos SET nome=%s, tipo=%s, descricao=%s, preco=%s, data_criacao=NOW() WHERE id=%s",
                           (novo_nome, novo_tipo, nova_descricao, novo_preco, id))
        db.commit()
        cursor.close()
        return redirect(url_for('admin'))

    return render_template('editar-produto.html', produto=produto)

@app.route('/excluir-produto', methods=['POST'])
def excluir_produto():
    produto_id = request.form['produto_id']
    cursor = db.cursor()
    cursor.execute("DELETE FROM produtos WHERE id=%s", (produto_id,))
    db.commit()
    cursor.close()
    return redirect(url_for('admin'))

@app.route('/baixar-relatorio', methods=['POST'])
def baixar_relatorio():
    # Lógica para gerar e baixar relatório
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True, port=3000)
