from sqlalchemy import Column, Integer, String
from app.db.database import Base
from app.utils.cast import to_float,to_str


class BC(Base):
    __tablename__ = "bc"
    weight = Column()              # 체중
    weight_result = Column()       # 체중 결과
    fatyang = Column()             # 체지방량
    fatyang_result = Column()      # 체지방량 결과
    muscleyang = Column()          # 근육량
    muscleyang_result = Column()   # 근육량 결과
    adult_bodytype = Column()      # 성인 체형판정
    basalmetabolism = Column()     # 기초대사량
    golgyeokgeunyang = Column()    # 골격근량
    bmi = Column()                 # 체질량지수
    fatryul = Column()             # 체지방률
    fatryul_result = Column()      # 체지방률 결과
    naejangfat_level = Column()    # 내장지방레벨
    wateryang = Column()           # 체수분량
    mineralsyang = Column()        # 무기질량
    proteinyang = Column()         # 단백질량
    total_grade = Column()         # 종합평점

    @classmethod
    def from_payload(cls, p: dict) -> "BC":
        data = {
            "weight":            to_float(p.get("weight")),
            "weight_result":     to_str(p.get("weight_result")),
            "fatyang":           to_float(p.get("fatyang")),
            "fatyang_result":    to_str(p.get("fatyang_result")),
            "muscleyang":        to_float(p.get("muscleyang")),
            "muscleyang_result": to_str(p.get("muscleyang_result")),
            "adult_bodytype":    to_str(p.get("adult_bodytype")),
            "basalmetabolism":   to_float(p.get("basalmetabolism")),
            "golgyeokgeunyang":  to_float(p.get("golgyeokgeunyang")),
            "bmi":               to_float(p.get("bmi")),
            "fatryul":           to_float(p.get("fatryul")),
            "fatryul_result":    to_str(p.get("fatryul_result")),
            "naejangfat_level":  to_float(p.get("naejangfat_level")),
            "wateryang":         to_float(p.get("wateryang")),
            "mineralsyang":      to_float(p.get("mineralsyang")),
            "proteinyang":       to_float(p.get("proteinyang")),
            "total_grade":       to_float(p.get("total_grade")),
        }
        return cls(**data)
