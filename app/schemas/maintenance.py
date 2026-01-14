from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class MaintenanceBase(BaseModel):
    device_id: int
    description: str
    status: Optional[str] = "planned"
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

class MaintenanceCreate(MaintenanceBase):
    created_by: int

class MaintenanceUpdate(BaseModel):
    device_id: Optional[int] = None
    description: Optional[str] = None
    status: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    created_by: Optional[int] = None

class Maintenance(MaintenanceBase):
    id: int
    created_by: int
    created_at: datetime

    class Config:
        orm_mode = True
