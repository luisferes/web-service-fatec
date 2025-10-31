# 1. Importe a classe Flask
from flask import Flask

# 2. Crie uma instância da classe Flask
# __name__ é uma variável especial do Python
app = Flask(__name__)

# 3. Defina uma rota (caminho) e a função que ela chamará
# O decorador @app.route('/') liga a URL raiz a função home()
@app.route('/')
def home():
  return 'Olá, Mundo Real!'

@app.route('/usuarios')
def usuarios():
  return 'Olá, Usuários!'

@app.route('/produtos')
def usuarios():
  return 'Todos os produtos deverão ser listados aqui!'

# 4. Execute o aplicativo
if __name__ == '__main__':
  # app.run() inicia o servidor web de desenvolvimento
  # debug=True permite que o servidor reinicie automaticamente ao salvar o arquivo
  app.run(debug=True)
