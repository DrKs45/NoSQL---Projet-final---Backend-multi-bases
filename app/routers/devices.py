from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.postgres import get_db
from app.models.device import Device as DeviceModel
from app.schemas.device import Device, DeviceCreate, DeviceUpdate

router = APIRouter(
    prefix="/devices",
    tags=["devices"]
)

@router.get("/", response_model=List[Device])
def get_devices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    devices = db.query(DeviceModel).offset(skip).limit(limit).all()
    return devices

@router.post("/", response_model=Device)
def create_device(device: DeviceCreate, db: Session = Depends(get_db)):
    db_device = DeviceModel(
        hostname=device.hostname,
        ip_statique=device.ip_statique,
        serial_number=device.serial_number,
        device_type=device.device_type,
        location=device.location,
        status_redis_key=device.status_redis_key
    )
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

@router.get("/{device_id}", response_model=Device)
def get_device(device_id: int, db: Session = Depends(get_db)):
    db_device = db.query(DeviceModel).filter(DeviceModel.id == device_id).first()
    if db_device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return db_device

@router.put("/{device_id}", response_model=Device)
def update_device(device_id: int, device: DeviceUpdate, db: Session = Depends(get_db)):
    db_device = db.query(DeviceModel).filter(DeviceModel.id == device_id).first()
    if db_device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    
    update_data = device.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_device, key, value)
    
    db.commit()
    db.refresh(db_device)
    return db_device

@router.delete("/{device_id}")
def delete_device(device_id: int, db: Session = Depends(get_db)):
    db_device = db.query(DeviceModel).filter(DeviceModel.id == device_id).first()
    if db_device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    
    db.delete(db_device)
    db.commit()
    return {"ok": True}
