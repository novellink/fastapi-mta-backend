from sqlalchemy import Column, Integer, String
from app.db.database import Base
from app.utils.cast import to_str

class CM(Base):
    __tablename__ = "cm"
    value = Column() # 색각 정상

    @classmethod
    def from_payload(cls, p: dict) -> "CM":
        return cls(value=to_str(p.get("value")) or to_int(p.get("value")))
