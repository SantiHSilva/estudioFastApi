from sqlalchemy.orm import Session
from pydantic import BaseModel
from config.db import SessionTemp

class CRUD():

    def __init__(self, model):
        self.Model = model
        self.db = SessionTemp()

    
    def get_model_by_id(self, model_id: int):
        # De la base de datos, de la tabla
        return self.db.query(self.Model).get(model_id)

    def get_all(self):
        return self.db.query(self.Model).all()

    def get_one(self, model_id: int):
        return self.get_model_by_id(model_id)

    def create(self, model_created: BaseModel):
        new_model = self.Model(**model_created.model_dump())
        
        self.db.add(new_model)
        self.db.commit()
        self.db.refresh(new_model)
        
        return new_model

    def update(self, model_id: int, model_updated: BaseModel):
        model_item = self.get_model_by_id(model_id)
        
        for key, value in model_updated.model_dump().items():
            if value is not None:
                setattr(model_item, key, value)
                
        self.db.commit()
        self.db.refresh(model_item)
        
        return model_item

    def delete(self, model_id: int):
        model_item = self.get_model_by_id(model_id)
        
        self.db.delete(model_item)
        self.db.commit()
        
        return {}