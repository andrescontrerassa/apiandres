from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Game(Base):
    """
    La clase Game representa un juego de mesa en el inventario.
    Almacena información como título, descripción, precio y cantidad en stock.
    """
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, default=0)
    category_id = Column(Integer, ForeignKey('categories.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    
    # Relaciones
    category = relationship('Category', back_populates='games')
    publisher = relationship('Publisher', back_populates='games')

class Category(Base):
    """
    La clase Category representa una categoría de juegos de mesa.
    Ejemplos: Estrategia, Familiar, Party, Cooperativo, etc.
    """
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    
    games = relationship('Game', back_populates='category')

class Publisher(Base):
    """
    La clase Publisher representa una editorial de juegos de mesa.
    """
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    website = Column(String(255))
    
    games = relationship('Game', back_populates='publisher')