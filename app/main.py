from fastapi import FastAPI
from app.db.postgres import engine, Base
from app.models import device # Import important pour que SQLAlchemy voit le modèle
from app.models import mongo
# Crée les tables dans la base de données si elles n'existent pas
Base.metadata.create_all(bind=engine)

# Initialise MongoDB


app = FastAPI(title="NetOps Inventory API")

@app.get("/")
def read_root():
    return {"status": "NetOps API is running"}