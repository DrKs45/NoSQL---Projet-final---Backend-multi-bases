from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.postgres import get_db
from app.models.maintenance import Maintenance as MaintenanceModel
from app.schemas.maintenance import Maintenance, MaintenanceCreate, MaintenanceUpdate

router = APIRouter(
    prefix="/maintenances",
    tags=["maintenances"]
)

@router.get("/", response_model=List[Maintenance])
def get_maintenances(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    maintenances = db.query(MaintenanceModel).offset(skip).limit(limit).all()
    return maintenances

@router.post("/", response_model=Maintenance)
def create_maintenance(maintenance: MaintenanceCreate, db: Session = Depends(get_db)):
    db_maintenance = MaintenanceModel(
        device_id=maintenance.device_id,
        description=maintenance.description,
        status=maintenance.status,
        start_time=maintenance.start_time,
        end_time=maintenance.end_time,
        created_by=maintenance.created_by
    )
    db.add(db_maintenance)
    db.commit()
    db.refresh(db_maintenance)
    return db_maintenance

@router.get("/{maintenance_id}", response_model=Maintenance)
def get_maintenance(maintenance_id: int, db: Session = Depends(get_db)):
    db_maintenance = db.query(MaintenanceModel).filter(MaintenanceModel.id == maintenance_id).first()
    if db_maintenance is None:
        raise HTTPException(status_code=404, detail="Maintenance not found")
    return db_maintenance

@router.put("/{maintenance_id}", response_model=Maintenance)
def update_maintenance(maintenance_id: int, maintenance: MaintenanceUpdate, db: Session = Depends(get_db)):
    db_maintenance = db.query(MaintenanceModel).filter(MaintenanceModel.id == maintenance_id).first()
    if db_maintenance is None:
        raise HTTPException(status_code=404, detail="Maintenance not found")
    
    update_data = maintenance.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_maintenance, key, value)
    
    db.commit()
    db.refresh(db_maintenance)
    return db_maintenance

@router.delete("/{maintenance_id}")
def delete_maintenance(maintenance_id: int, db: Session = Depends(get_db)):
    db_maintenance = db.query(MaintenanceModel).filter(MaintenanceModel.id == maintenance_id).first()
    if db_maintenance is None:
        raise HTTPException(status_code=404, detail="Maintenance not found")
    
    db.delete(db_maintenance)
    db.commit()
    return {"ok": True}
