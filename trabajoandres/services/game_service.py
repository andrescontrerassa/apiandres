from repositories.game_repository import GameRepository
from models.game_model import Game, Category, Publisher
from sqlalchemy.orm import Session

class GameService:
    """
    Capa de servicios para la gestión del inventario de juegos de mesa.
    Esta clase orquesta la lógica de negocio relacionada con los juegos,
    utilizando el repositorio para acceder a los datos.
    """
    def __init__(self, db_session: Session):
        self.repository = GameRepository(db_session)

    def listar_juegos(self):
        """
        Recupera y retorna todos los juegos de mesa registrados en el sistema.
        """
        return self.repository.get_all_games()

    def obtener_juego(self, game_id: int):
        """
        Busca y retorna un juego específico por su ID.
        """
        return self.repository.get_game_by_id(game_id)

    def crear_juego(self, title: str, description: str, price: float, 
                   stock_quantity: int, category_id: int, publisher_id: int):
        """
        Crea un nuevo juego de mesa con la información proporcionada.
        """
        return self.repository.create_game(
            title, description, price, stock_quantity, category_id, publisher_id
        )

    def actualizar_juego(self, game_id: int, **kwargs):
        """
        Actualiza la información de un juego existente.
        """
        return self.repository.update_game(game_id, **kwargs)

    def eliminar_juego(self, game_id: int):
        """
        Elimina un juego de mesa del sistema según su ID.
        """
        return self.repository.delete_game(game_id)

    def actualizar_stock(self, game_id: int, quantity: int):
        """
        Actualiza la cantidad en stock de un juego.
        """
        return self.repository.update_stock(game_id, quantity)

    # Métodos para categorías
    def listar_categorias(self):
        return self.repository.get_all_categories()

    def obtener_categoria(self, category_id: int):
        return self.repository.get_category_by_id(category_id)

    def crear_categoria(self, name: str, description: str = None):
        return self.repository.create_category(name, description)

    # Métodos para editoriales
    def listar_editoriales(self):
        return self.repository.get_all_publishers()

    def obtener_editorial(self, publisher_id: int):
        return self.repository.get_publisher_by_id(publisher_id)

    def crear_editorial(self, name: str, website: str = None):
        return self.repository.create_publisher(name, website)
    # Métodos para categorías
    def listar_categorias(self):
        return self.repository.get_all_categories()

    def obtener_categoria(self, category_id: int):
        return self.repository.get_category_by_id(category_id)

    def crear_categoria(self, name: str, description: str = None):
        return self.repository.create_category(name, description)

    # Métodos para editoriales
    def listar_editoriales(self):
        return self.repository.get_all_publishers()

    def obtener_editorial(self, publisher_id: int):
        return self.repository.get_publisher_by_id(publisher_id)

    def crear_editorial(self, name: str, website: str = None):
        return self.repository.create_publisher(name, website)

    # Métodos para categorías
    def listar_categorias(self):
        """Listar todas las categorías"""
        return self.repository.get_all_categories()

    def obtener_categoria(self, category_id: int):
        """Obtener categoría por ID"""
        return self.repository.get_category_by_id(category_id)

    def crear_categoria(self, name: str, description: str = None):
        """Crear nueva categoría"""
        return self.repository.create_category(name, description)

    # Métodos para editoriales
    def listar_editoriales(self):
        """Listar todas las editoriales"""
        return self.repository.get_all_publishers()

    def obtener_editorial(self, publisher_id: int):
        """Obtener editorial por ID"""
        return self.repository.get_publisher_by_id(publisher_id)

    def crear_editorial(self, name: str, website: str = None):
        """Crear nueva editorial"""
        return self.repository.create_publisher(name, website)
