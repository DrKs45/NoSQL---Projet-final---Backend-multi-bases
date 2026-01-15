from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.postgres import engine, Base
from app.models import device, user, maintenance  # SQLAlchemy models
from app.models import mongo  # pour initialiser MongoDB
from app.routers import devices, users, maintenance as maintenance_router, status, logs

# Crée les tables PostgreSQL si elles n'existent pas
Base.metadata.create_all(bind=engine)


app = FastAPI(title="NetOps Inventory API")

# Configuration CORS
origins = [
    "http://localhost",
    "http://localhost:5173",  # Vite dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclure tous les routers existants
app.include_router(devices.router)
app.include_router(users.router)
app.include_router(maintenance_router.router)
app.include_router(status.router)
app.include_router(logs.router)    

@app.get("/")
def read_root():
    return {"status": "NetOps API is running"}
