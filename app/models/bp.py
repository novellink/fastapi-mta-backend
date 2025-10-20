from sqlalchemy import Column, Integer, String
from app.db.database import Base
from app.utils.cast import to_int,to_str

class BP(Base):
    __tablename__ = "bp"
    high = Column()   # 144
    low = Column()    # 92
    pulse = Column()  # 83
    status = Column() # 고혈압

    @classmethod
    def from_payload(cls, p: dict) -> "BP":
        data = {
            "high":  to_int(p.get("high")),
            "low":   to_int(p.get("low")),
            "pulse": to_int(p.get("pulse")),
            "status": to_str(p.get("status")),
        }
        return cls(**data)

    