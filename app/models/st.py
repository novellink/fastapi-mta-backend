from sqlalchemy import Column, Integer, String
from app.db.database import Base
from app.utils.cast import to_int,to_str,to_float

class ST(Base):
    __tablename__ = "st"
    heartrate_avg = Column()            # 평균_심박수
    heartrate_score = Column()          # 심박수 점수
    heartrate_step = Column()           # 심박수 단계
    heartrate_ng = Column()             # 이상 심박수
    jayul_activity_score = Column()     # 자율신경_활성도_점수
    jayul_activity_step = Column()      # 자율신경_활성도_단계
    piro_score = Column()               # 피로도_점수
    piro_step = Column()                # 피로도_단계
    heart_stability_score = Column()    # 심장_안정도_점수
    heart_stability_step = Column()     # 심장_안정도_단계
    jayul_balance_step = Column()       # 자율신경_균형도_단계
    physical_stress_score = Column()    # 신체적_스트레스_점수
    physical_stress_step = Column()     # 신체적_스트레스_단계
    mental_stress_score = Column()      # 정신적_스트레스_점수
    mental_stress_step = Column()       # 정신적_스트레스_단계
    stress_ability_score = Column()     # 스트레스_대처능력_점수
    stress_ability_step = Column()      # 스트레스_대처능력_단계
    total_grade = Column()              # 종합점수
    dongmaek_tansung_score = Column()   # 동맥혈관탄성도_점수
    dongmaek_tansung_step = Column()    # 동맥혈관탄성도_단계
    malcho_tansung_score = Column()     # 말초혈관탄성도_점수
    malcho_tansung_step = Column()      # 말초혈관탄성도_단계
    bloodvessel_age = Column()          # 혈관연령
    bloodvessel_score = Column()        # 혈관건강 점수
    bloodvessel_step = Column()         # 대표_혈관_단계
    bloodvessel_step_status = Column()  # 대표_혈관_등급

    @classmethod
    def from_payload(cls, p: dict) -> "ST":
        data = {
            "heartrate_avg":            to_float(p.get("heartrate_avg")),
            "heartrate_score":          to_float(p.get("heartrate_score")),
            "heartrate_step":           to_str(p.get("heartrate_step")),
            "heartrate_ng":             to_int(p.get("heartrate_ng")),
            "jayul_activity_score":     to_float(p.get("jayul_activity_score")),
            "jayul_activity_step":      to_str(p.get("jayul_activity_step")),
            "piro_score":               to_float(p.get("piro_score")),
            "piro_step":                to_str(p.get("piro_step")),
            "heart_stability_score":    to_float(p.get("heart_stability_score")),
            "heart_stability_step":     to_str(p.get("heart_stability_step")),
            "jayul_balance_step":       to_float(p.get("jayul_balance_step")),
            "physical_stress_score":    to_float(p.get("physical_stress_score")),
            "physical_stress_step":     to_str(p.get("physical_stress_step")),
            "mental_stress_score":      to_float(p.get("mental_stress_score")),
            "mental_stress_step":       to_str(p.get("mental_stress_step")),
            "stress_ability_score":     to_float(p.get("stress_ability_score")),
            "stress_ability_step":      to_str(p.get("stress_ability_step")),
            "total_grade":              to_float(p.get("total_grade")),
            "dongmaek_tansung_score":   to_float(p.get("dongmaek_tansung_score")),
            "dongmaek_tansung_step":    to_str(p.get("dongmaek_tansung_step")),
            "malcho_tansung_score":     to_float(p.get("malcho_tansung_score")),
            "malcho_tansung_step":      to_str(p.get("malcho_tansung_step")),
            "bloodvessel_age":          to_float(p.get("bloodvessel_age")),
            "bloodvessel_score":        to_float(p.get("bloodvessel_score")),
            "bloodvessel_step":         to_str(p.get("bloodvessel_step")),
            "bloodvessel_step_status":  to_str(p.get("bloodvessel_step_status")),
        }
        return cls(**data)
