from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class DeviceBase(BaseModel):
    hostname: str
    ip_statique: str
    serial_number: str
    device_type: str
    location: Optional[str] = None
    status_redis_key: Optional[str] = None

class DeviceCreate(DeviceBase):
    pass

class DeviceUpdate(BaseModel):
    hostname: Optional[str] = None
    ip_statique: Optional[str] = None
    serial_number: Optional[str] = None
    device_type: Optional[str] = None
    location: Optional[str] = None
    status_redis_key: Optional[str] = None

class Device(DeviceBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
