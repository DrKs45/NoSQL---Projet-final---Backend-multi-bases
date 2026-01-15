from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.postgres import engine, Base
from app.models import device, user, maintenance  # Import important pour que SQLAlchemy voit le modèle
from app.models import mongo
from app.routers import devices, users, maintenance as maintenance_router
# Crée les tables dans la base de données si elles n'existent pas
Base.metadata.create_all(bind=engine)

# Initialise MongoDB


app = FastAPI(title="NetOps Inventory API")

# Configuration CORS
origins = [
    "http://localhost",
    "http://localhost:5173", # Vite dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(devices.router)
app.include_router(users.router)
app.include_router(maintenance_router.router)

@app.get("/")
def read_root():
    return {"status": "NetOps API is running"}