from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flasgger import Swagger
from marshmallow import fields, validate, ValidationError

app = Flask(__name__)

# Configuração do SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuração do Swagger
swagger = Swagger(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)

# -------------------------------------------------------------------
# MODELO DO BANCO DE DADOS
# -------------------------------------------------------------------
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

# Criar o banco de dados na inicialização
with app.app_context():
    db.create_all()

# -------------------------------------------------------------------
# SCHEMA COM MARSHMALLOW (Validação e Serialização)
# -------------------------------------------------------------------
class UsuarioSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True, validate=validate.Length(min=2, max=100))
    email = fields.Email(required=True)

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

# -------------------------------------------------------------------
# TRATAMENTO DE ERROS GLOBAL
# -------------------------------------------------------------------
@app.errorhandler(404)
def recurso_nao_encontrado(e):
    return jsonify({"erro": "Recurso não encontrado"}), 404

@app.errorhandler(500)
def erro_interno(e):
    return jsonify({"erro": "Erro interno no servidor"}), 500

# -------------------------------------------------------------------
# ROTAS DA API
# -------------------------------------------------------------------

@app.route('/saudacao', methods=['GET'])
def saudacao():
    """
    Rota de saudação básica.
    ---
    responses:
      200:
        description: Retorna uma mensagem de boas-vindas.
    """
    return jsonify({"mensagem": "Bem-vindo à API de Gerenciamento de Usuários!"}), 200


@app.route('/usuarios', methods=['GET'])
def obter_usuarios():
    """
    Retorna todos os usuários cadastrados.
    ---
    responses:
      200:
        description: Lista de usuários.
    """
    todos_usuarios = Usuario.query.all()
    resultado = usuarios_schema.dump(todos_usuarios)
    return jsonify(resultado), 200


@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    """
    Cadastra um novo usuário.
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
            email:
              type: string
    responses:
      201:
        description: Usuário criado com sucesso.
      400:
        description: Erro de validação nos dados.
    """
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "Nenhum dado JSON foi fornecido"}), 400

    # Validação dos dados com Marshmallow
    try:
        dados_validados = usuario_schema.load(dados)
    except ValidationError as err:
        return jsonify({"erros_validacao": err.messages}), 400

    # Verificar se email já existe
    if Usuario.query.filter_by(email=dados_validados['email']).first():
        return jsonify({"erro": "E-mail já cadastrado"}), 400

    novo_usuario = Usuario(nome=dados_validados['nome'], email=dados_validados['email'])
    db.session.add(novo_usuario)
    db.session.commit()

    return usuario_schema.jsonify(novo_usuario), 201


@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    """
    Atualiza um usuário existente.
    ---
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
            email:
              type: string
    responses:
      200:
        description: Usuário atualizado com sucesso.
      404:
        description: Usuário não encontrado.
    """
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    dados = request.get_json()

    try:
        dados_validados = usuario_schema.load(dados)
    except ValidationError as err:
        return jsonify({"erros_validacao": err.messages}), 400

    usuario.nome = dados_validados['nome']
    usuario.email = dados_validados['email']

    db.session.commit()
    return usuario_schema.jsonify(usuario), 200


@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    """
    Exclui um usuário pelo ID.
    ---
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Usuário removido com sucesso.
      404:
        description: Usuário não encontrado.
    """
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"erro": "Usuário não encontrado"}), 404

    db.session.delete(usuario)
    db.session.commit()

    return jsonify({"mensagem": f"Usuário {id} deletado com sucesso"}), 200


if __name__ == '__main__':
    app.run(debug=True)