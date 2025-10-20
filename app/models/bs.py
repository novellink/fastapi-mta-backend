from sqlalchemy import Column, Integer, String
from app.db.database import Base
from app.utils.cast import to_int,to_str

class BS(Base):
    __tablename__ = "bs"
    status = Column()          # 측정상태
    bloodsugar_type = Column() # 식전
    bloodsugar = Column()      # 혈당
    col_total = Column()       # 콜레스테롤 Total
    col_tri = Column()         # 중성지방
    col_ldl = Column()         # LDL
    col_hdl = Column()         # HDL

    @classmethod
    def from_payload(cls, p: dict) -> "BS":
        data = {
            "status":          to_str(p.get("status")),
            "bloodsugar_type": to_str(p.get("bloodsugar_type")),
            "bloodsugar":      to_int(p.get("bloodsugar")),
            "col_total":       to_int(p.get("col_total")),
            "col_tri":         to_int(p.get("col_tri")),
            "col_ldl":         to_int(p.get("col_ldl")),
            "col_hdl":         to_int(p.get("col_hdl")),
        }
        return cls(**data)
