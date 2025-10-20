from sqlalchemy import Column, Integer, String
from app.db.database import Base

from app.utils.cast import to_float, to_str

class AL(Base):
    __tablename__ = "al"
    alcohol_result = Column() # 음주결과
    alcohol_yang = Column()   # 음주량

    @classmethod
    def from_payload(cls, p: dict) -> "AL":
        data = {
            "alcohol_result": to_str(p.get("alcohol_result")),
            "alcohol_yang":   to_float(p.get("alcohol_yang")),
        }
        return cls(**data)
