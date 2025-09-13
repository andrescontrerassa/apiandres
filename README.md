# apiandres
desarrollo de la creacion de el crud de la api
Proyecto de Gestión de Inventario de Juegos de Mesa
Este proyecto es un sistema completo para la gestión de inventario de juegos de mesa, implementado siguiendo el patrón arquitectónico por capas. Utiliza Python, Flask como framework web y SQLAlchemy como ORM para la interacción con bases de datos MySQL.

Descripción General
El sistema permite registrar, consultar, actualizar y eliminar juegos de mesa, así como gestionar categorías y editoriales asociadas. La arquitectura por capas facilita la separación de responsabilidades, mejorando la mantenibilidad, escalabilidad y flexibilidad del código.

Características principales:
API RESTful completa para gestión de juegos, categorías y editoriales

Modelos bien definidos con relaciones entre juegos, categorías y editoriales

Patrón Repository para acceso a datos desacoplado de la lógica de negocio

Servicios que orquestan la lógica de negocio

Controladores con endpoints REST bien documentados

Soporte para MySQL con fallback a SQLite

Documentación detallada para facilitar la comprensión y extensión

🏗 Estructura del Proyecto
text
trabajoandres/
├── app.py                
├── .env                  
├── config/
│   └── database.py      
├── models/
│   └── game_model.py     
├── repositories/
│   └── game_repository.py 
├── services/
│   └── game_service.py   
├── controllers/
│   └── game_controller.py 
└── requirements.txt       
 Instalación y Configuración
1. Clonar o crear el proyecto
bash
mkdir trabajoandres
cd trabajoandres
2. Crear entorno virtual
bash
python -m venv venv
3. Activar entorno virtual
Windows:

4. Instalar dependencias
bash
pip install flask sqlalchemy pymysql python-dotenv
5. Configurar base de datos
Crear archivo .env en la raíz del proyecto:

env
MYSQL_USER=root
MYSQL_PASSWORD=root123
MYSQL_HOST=localhost
MYSQL_DB=board_games_inventory
DATABASE_URI=mysql+pymysql://root:tu_password_mysql@localhost/board_games_inventory
6. Ejecutar la aplicación
bash
python app.py
Endpoints de la API
Juegos
GET /games - Obtener todos los juegos

GET /games/<id> - Obtener juego por ID

POST /games - Crear nuevo juego

PUT /games/<id> - Actualizar juego

DELETE /games/<id> - Eliminar juego

PATCH /games/<id>/stock - Actualizar stock

Categorías
GET /categories - Obtener todas las categorías

POST /categories - Crear nueva categoría

Editoriales
GET /publishers - Obtener todas las editoriales

POST /publishers - Crear nueva editorial

 Ejemplos de Uso
Crear una categoría
bash
curl -X POST http://localhost:5000/categories \
  -H "Content-Type: application/json" \
  -d '{"name":"Estrategia", "description":"Juegos de estrategia"}'
Crear una editorial
bash
curl -X POST http://localhost:5000/publishers \
  -H "Content-Type: application/json" \
  -d '{"name":"Devir", "website":"https://www.devir.es"}'
Crear un juego
bash
curl -X POST http://localhost:5000/games \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Catan",
    "description": "Juego de estrategia y comercio",
    "price": 45.99,
    "stock_quantity": 15,
    "category_id": 1,
    "publisher_id": 1
  }'
Modelo de Datos
Game
id 

title 

description 

price 

stock_quantity 

category_id 

publisher_id 

Category
id 
name 

description 

Publisher
id 

name 

website 

 Configuración de Base de Datos
 
Este proyecto es de uso libre para fines educativos y de aprendizaje.

