from flask import Blueprint, request, jsonify
from services.game_service import GameService
from config.database import SessionLocal

# Crear sesión de base de datos
db_session = SessionLocal()
service = GameService(db_session)

game_bp = Blueprint('game_bp', __name__)

# Rutas para juegos
@game_bp.route('/games', methods=['GET'])
def get_games():
    """
    GET /games
    Recupera y retorna todos los juegos de mesa registrados en el sistema.
    """
    games = service.listar_juegos()
    return jsonify([{
        'id': g.id,
        'title': g.title,
        'description': g.description,
        'price': g.price,
        'stock_quantity': g.stock_quantity,
        'category': g.category.name if g.category else None,
        'publisher': g.publisher.name if g.publisher else None
    } for g in games]), 200

@game_bp.route('/games/<int:game_id>', methods=['GET'])
def get_game(game_id):
    """
    GET /games/<game_id>
    Recupera la información de un juego específico por su ID.
    """
    game = service.obtener_juego(game_id)
    if game:
        return jsonify({
            'id': game.id,
            'title': game.title,
            'description': game.description,
            'price': game.price,
            'stock_quantity': game.stock_quantity,
            'category_id': game.category_id,
            'category': game.category.name if game.category else None,
            'publisher_id': game.publisher_id,
            'publisher': game.publisher.name if game.publisher else None
        }), 200
    return jsonify({'error': 'Juego no encontrado'}), 404

@game_bp.route('/games', methods=['POST'])
def create_game():
    """
    POST /games
    Crea un nuevo juego de mesa.
    Parámetros esperados (JSON):
        title (str): Título del juego
        description (str): Descripción del juego
        price (float): Precio del juego
        stock_quantity (int): Cantidad en stock
        category_id (int): ID de la categoría
        publisher_id (int): ID de la editorial
    """
    data = request.get_json()
    required_fields = ['title', 'price', 'category_id', 'publisher_id']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'El campo {field} es obligatorio'}), 400
    
    game = service.crear_juego(
        title=data['title'],
        description=data.get('description', ''),
        price=data['price'],
        stock_quantity=data.get('stock_quantity', 0),
        category_id=data['category_id'],
        publisher_id=data['publisher_id']
    )
    return jsonify({
        'id': game.id,
        'title': game.title,
        'description': game.description,
        'price': game.price,
        'stock_quantity': game.stock_quantity,
        'category_id': game.category_id,
        'publisher_id': game.publisher_id
    }), 201

@game_bp.route('/games/<int:game_id>', methods=['PUT'])
def update_game(game_id):
    """
    PUT /games/<game_id>
    Actualiza la información de un juego existente.
    """
    data = request.get_json()
    game = service.actualizar_juego(game_id, **data)
    if game:
        return jsonify({
            'id': game.id,
            'title': game.title,
            'description': game.description,
            'price': game.price,
            'stock_quantity': game.stock_quantity,
            'category_id': game.category_id,
            'publisher_id': game.publisher_id
        }), 200
    return jsonify({'error': 'Juego no encontrado'}), 404

@game_bp.route('/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    """
    DELETE /games/<game_id>
    Elimina un juego específico por su ID.
    """
    game = service.eliminar_juego(game_id)
    if game:
        return jsonify({'message': 'Juego eliminado'}), 200
    return jsonify({'error': 'Juego no encontrado'}), 404

@game_bp.route('/games/<int:game_id>/stock', methods=['PATCH'])
def update_game_stock(game_id):
    """
    PATCH /games/<game_id>/stock
    Actualiza el stock de un juego.
    Parámetros esperados (JSON):
        quantity (int): Nueva cantidad en stock
    """
    data = request.get_json()
    if 'quantity' not in data:
        return jsonify({'error': 'La cantidad es obligatoria'}), 400
    
    game = service.actualizar_stock(game_id, data['quantity'])
    if game:
        return jsonify({
            'id': game.id,
            'title': game.title,
            'stock_quantity': game.stock_quantity
        }), 200
    return jsonify({'error': 'Juego no encontrado'}), 404

# Rutas para categorías
@game_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = service.listar_categorias()
    return jsonify([{
        'id': c.id,
        'name': c.name,
        'description': c.description
    } for c in categories]), 200

@game_bp.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'El nombre es obligatorio'}), 400
    
    category = service.crear_categoria(
        name=data['name'],
        description=data.get('description')
    )
    return jsonify({
        'id': category.id,
        'name': category.name,
        'description': category.description
    }), 201

# Rutas para editoriales
@game_bp.route('/publishers', methods=['GET'])
def get_publishers():
    publishers = service.listar_editoriales()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'website': p.website
    } for p in publishers]), 200

@game_bp.route('/publishers', methods=['POST'])
def create_publisher():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'El nombre es obligatorio'}), 400
    
    publisher = service.crear_editorial(
        name=data['name'],
        website=data.get('website')
    )
    return jsonify({
        'id': publisher.id,
        'name': publisher.name,
        'website': publisher.website
    }), 201
