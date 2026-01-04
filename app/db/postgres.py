from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Création de l'engine SQLAlchemy
# L'engine est le point d'entrée vers la base de données
engine = create_engine(settings.sqlalchemy_database_url)

# Création d'une classe de session
# Chaque instance de cette classe sera une session de base de données réelle
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base de classe pour nos modèles de données (models/device.py, etc.)
Base = declarative_base()

# Fonction helper pour récupérer une session de DB (utilisée par FastAPI)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()