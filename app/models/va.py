from app.db.database import Base
from sqlalchemy import Column, Integer, String
from app.utils.cast import to_float,to_str

class VA(Base):
    __tablename__ = "va"
    left = Column()          # 6
    left_status = Column()   # 좌안정상
    right = Column()         # 7
    right_status = Column()  # 우안정상
    status = Column()        # VA정상

    @classmethod
    def from_payload(cls, p: dict) -> "VA":
        data = {
            "left":        to_float(p.get("left")),
            "left_status": to_str(p.get("left_status")),
            "right":       to_float(p.get("right")),
            "right_status":to_str(p.get("right_status")),
            "status":      to_str(p.get("status")),
        }
        return cls(**data)
