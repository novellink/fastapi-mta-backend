from app.db.database import Base
from sqlalchemy import Column, Integer, String
from app.utils.cast import to_float,to_str

class HS(Base):
    __tablename__ = "hs"
    height = Column() # 4
    weight = Column() # 5
    bmi = Column()    # BMI
    status = Column() # HS정상

    @classmethod
    def from_payload(cls, p: dict) -> "HS":
        data = {
            "height": to_float(p.get("height")),
            "weight": to_float(p.get("weight")),
            "bmi":    to_str(p.get("bmi")),
            "status": to_str(p.get("status")),
        }
        return cls(**data)

    