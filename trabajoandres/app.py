import sys
import os

# Agregar todas las carpetas al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'controllers'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'repositories'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'services'))

from flask import Flask
from config.database import engine, SessionLocal
from models.game_model import Base
from controllers.game_controller import game_bp

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = Flask(__name__)
app.register_blueprint(game_bp)

@app.route('/')
def home():
    return "API de Juegos de Mesa funcionando!"

if __name__ == '__main__':
    print("Iniciando servidor Flask...")
    print("Routes disponibles:")
    print("- GET /games")
    print("- GET /games/<id>")
    print("- POST /games")
    print("- PUT /games/<id>")
    print("- DELETE /games/<id>")
    app.run(debug=True, host='0.0.0.0', port=5000)
