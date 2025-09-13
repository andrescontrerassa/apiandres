from models.game_model import Game, Category, Publisher
from sqlalchemy.orm import Session

class GameRepository:
    """
    Repositorio para la gestión de juegos de mesa en la base de datos.
    Proporciona métodos para crear, consultar, actualizar y eliminar juegos,
    así como para gestionar categorías y editoriales.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_games(self):
        """
        Recupera todos los juegos de mesa almacenados en la base de datos.
        Incluye información de categoría y editorial mediante joins.
        """
        return self.db.query(Game).join(Category).join(Publisher).all()

    def get_game_by_id(self, game_id: int):
        """
        Busca y retorna un juego específico según su identificador único (ID).
        Incluye información de categoría y editorial.
        """
        return self.db.query(Game).filter(Game.id == game_id).first()

    def create_game(self, title: str, description: str, price: float, 
                   stock_quantity: int, category_id: int, publisher_id: int):
        """
        Crea y almacena un nuevo juego de mesa en la base de datos.
        """
        new_game = Game(
            title=title,
            description=description,
            price=price,
            stock_quantity=stock_quantity,
            category_id=category_id,
            publisher_id=publisher_id
        )
        self.db.add(new_game)
        self.db.commit()
        self.db.refresh(new_game)
        return new_game

    def update_game(self, game_id: int, **kwargs):
        """
        Actualiza la información de un juego existente en la base de datos.
        """
        game = self.get_game_by_id(game_id)
        if game:
            for key, value in kwargs.items():
                if hasattr(game, key) and value is not None:
                    setattr(game, key, value)
            self.db.commit()
            self.db.refresh(game)
        return game

    def delete_game(self, game_id: int):
        """
        Elimina un juego de mesa de la base de datos según su ID.
        """
        game = self.get_game_by_id(game_id)
        if game:
            self.db.delete(game)
            self.db.commit()
        return game

    def update_stock(self, game_id: int, quantity: int):
        """
        Actualiza la cantidad en stock de un juego.
        """
        game = self.get_game_by_id(game_id)
        if game:
            game.stock_quantity = quantity
            self.db.commit()
            self.db.refresh(game)
        return game

    # Métodos para categorías
    def get_all_categories(self):
        return self.db.query(Category).all()

    def get_category_by_id(self, category_id: int):
        return self.db.query(Category).filter(Category.id == category_id).first()

    def create_category(self, name: str, description: str = None):
        new_category = Category(name=name, description=description)
        self.db.add(new_category)
        self.db.commit()
        self.db.refresh(new_category)
        return new_category

    # Métodos para editoriales
    def get_all_publishers(self):
        return self.db.query(Publisher).all()

    def get_publisher_by_id(self, publisher_id: int):
        return self.db.query(Publisher).filter(Publisher.id == publisher_id).first()

    def create_publisher(self, name: str, website: str = None):
        new_publisher = Publisher(name=name, website=website)
        self.db.add(new_publisher)
        self.db.commit()
        self.db.refresh(new_publisher)
        return new_publisher
    # Métodos para categorías
    def get_all_categories(self):
        """Obtener todas las categorías"""
        return self.db.query(Category).all()

    def get_category_by_id(self, category_id: int):
        """Obtener categoría por ID"""
        return self.db.query(Category).filter(Category.id == category_id).first()

    def create_category(self, name: str, description: str = None):
        """Crear nueva categoría"""
        new_category = Category(name=name, description=description)
        self.db.add(new_category)
        self.db.commit()
        self.db.refresh(new_category)
        return new_category

    # Métodos para editoriales
    def get_all_publishers(self):
        """Obtener todas las editoriales"""
        return self.db.query(Publisher).all()

    def get_publisher_by_id(self, publisher_id: int):
        """Obtener editorial por ID"""
        return self.db.query(Publisher).filter(Publisher.id == publisher_id).first()

    def create_publisher(self, name: str, website: str = None):
        """Crear nueva editorial"""
        new_publisher = Publisher(name=name, website=website)
        self.db.add(new_publisher)
        self.db.commit()
        self.db.refresh(new_publisher)
        return new_publisher
