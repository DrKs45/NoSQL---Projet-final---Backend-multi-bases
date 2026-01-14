from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.postgres import Base

class Maintenance(Base):
    __tablename__ = "maintenances"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"), nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    description = Column(String, nullable=False)
    status = Column(String, default="planned") # planned, in_progress, completed, cancelled
    
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    device = relationship("app.models.device.Device", backref="maintenances")
    user = relationship("app.models.user.User", backref="created_maintenances")

    def __repr__(self):
        return f"<Maintenance(id={self.id}, device_id={self.device_id}, status={self.status})>"
