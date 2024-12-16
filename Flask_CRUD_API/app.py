from flask import Flask
from laptops_blueprint import laptops_blueprint

app = Flask(__name__)

Register the laptops blueprint
app.register_blueprint(laptops_blueprint, url_prefix='/laptops')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
