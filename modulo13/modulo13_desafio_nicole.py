from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 1. Inicializa o app Flask
app = Flask(__name__)

# 2. Configura o banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 3. CRIA A VARIÁVEL 'db' (que estava faltando!)
db = SQLAlchemy(app)

# -------------------------------------------------------------------
# MODELOS DO BANCO DE DADOS (Agora 'db' já existe!)
# -------------------------------------------------------------------

class UsuarioBlog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    posts = db.relationship('Post', backref='autor', lazy=True)
    comentarios = db.relationship('Comentario', backref='autor', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario_blog.id'), nullable=False)
    comentarios = db.relationship('Comentario', backref='post', lazy=True)

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario_blog.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

# Criar as tabelas no banco de dados se não existirem
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)