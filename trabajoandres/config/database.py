import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

MYSQL_USER = os.getenv('root')
MYSQL_PASSWORD = os.getenv('root123')
MYSQL_HOST = os.getenv('localhost')
MYSQL_DB = os.getenv('board_games-inventory')
DATABASE_URI = os.getenv('DATABASE_URI')

# Verificar y crear DATABASE_URL
if DATABASE_URI:
    DATABASE_URL = DATABASE_URI
elif MYSQL_USER and MYSQL_PASSWORD and MYSQL_HOST and MYSQL_DB:
    DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
else:
    # Fallback a SQLite si MySQL no está configurado
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, '..', 'board_games.db')}"
    print("⚠️  Usando SQLite como fallback. Configura MySQL en el archivo .env")

print(f"🔗 Conectando a: {DATABASE_URL}")

try:
    engine = create_engine(DATABASE_URL, echo=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    print("✅ Conexión a base de datos configurada correctamente")
except Exception as e:
    print(f"❌ Error al conectar con la base de datos: {e}")
    # Fallback a SQLite si hay error
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, '..', 'board_games.db')}"
    print(f"🔗 Usando SQLite fallback: {DATABASE_URL}")
    engine = create_engine(DATABASE_URL, echo=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_session():
    """
    Función para obtener una sesión de base de datos.
    Se usa en los controladores para inyectar la sesión.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
