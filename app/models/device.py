from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.postgres import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String, unique=True, index=True, nullable=False)
    ip_statique = Column(String, unique=True, nullable=False)
    serial_number = Column(String, unique=True, nullable=False)
    
    # Type d'équipement (ex: 'router', 'switch', 'server')
    device_type = Column(String, nullable=False)
    
    # Localisation physique (ex: 'Datacenter-A', 'Salle-IT-01')
    location = Column(String)
    
    # Nom de la clé utilisée dans Redis pour le statut live
    # Exemple : "status:device:1"
    status_redis_key = Column(String)
    
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Device(hostname={self.hostname}, ip={self.ip_statique})>"