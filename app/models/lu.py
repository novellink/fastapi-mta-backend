from sqlalchemy import Column, Integer, String
from app.db.database import Base
from app.utils.cast import to_str,to_float

class LU(Base):
    __tablename__ = "lu"
    # 1차
    fvc_1 = Column()
    fvc_p_1 = Column()
    fev1_1 = Column()
    fev1_p_1 = Column()
    fev1fvc_1 = Column()
    fev1fvc_status_1 = Column()
    fef2575_1 = Column()
    pef_1 = Column()
    pef_p_1 = Column()
    lung_age_1 = Column()
    # 2차
    fvc_2 = Column()
    fvc_p_2 = Column()
    fev1_2 = Column()
    fev1_p_2 = Column()
    fev1fvc_2 = Column()
    fev1fvc_status_2 = Column()
    fef2575_2 = Column()
    pef_2 = Column()
    pef_p_2 = Column()
    lung_age_2 = Column()
    # 3차
    fvc_3 = Column()
    fvc_p_3 = Column()
    fev1_3 = Column()
    fev1_p_3 = Column()
    fev1fvc_3 = Column()
    fev1fvc_status_3 = Column()
    fef2575_3 = Column()
    pef_3 = Column()
    pef_p_3 = Column()
    lung_age_3 = Column()

    @classmethod
    def from_payload(cls, p: dict) -> "LU":
        data = {
            # 1차
            "fvc_1":             to_float(p.get("fvc_1")),
            "fvc_p_1":           to_float(p.get("fvc_p_1")),
            "fev1_1":            to_float(p.get("fev1_1")),
            "fev1_p_1":          to_float(p.get("fev1_p_1")),
            "fev1fvc_1":         to_float(p.get("fev1fvc_1")),
            "fev1fvc_status_1":  to_str(p.get("fev1fvc_status_1")),
            "fef2575_1":         to_float(p.get("fef2575_1")),
            "pef_1":             to_float(p.get("pef_1")),
            "pef_p_1":           to_float(p.get("pef_p_1")),
            "lung_age_1":        to_float(p.get("lung_age_1")),
            # 2차
            "fvc_2":             to_float(p.get("fvc_2")),
            "fvc_p_2":           to_float(p.get("fvc_p_2")),
            "fev1_2":            to_float(p.get("fev1_2")),
            "fev1_p_2":          to_float(p.get("fev1_p_2")),
            "fev1fvc_2":         to_float(p.get("fev1fvc_2")),
            "fev1fvc_status_2":  to_str(p.get("fev1fvc_status_2")),
            "fef2575_2":         to_float(p.get("fef2575_2")),
            "pef_2":             to_float(p.get("pef_2")),
            "pef_p_2":           to_float(p.get("pef_p_2")),
            "lung_age_2":        to_float(p.get("lung_age_2")),
            # 3차
            "fvc_3":             to_float(p.get("fvc_3")),
            "fvc_p_3":           to_float(p.get("fvc_p_3")),
            "fev1_3":            to_float(p.get("fev1_3")),
            "fev1_p_3":          to_float(p.get("fev1_p_3")),
            "fev1fvc_3":         to_float(p.get("fev1fvc_3")),
            "fev1fvc_status_3":  to_str(p.get("fev1fvc_status_3")),
            "fef2575_3":         to_float(p.get("fef2575_3")),
            "pef_3":             to_float(p.get("pef_3")),
            "pef_p_3":           to_float(p.get("pef_p_3")),
            "lung_age_3":        to_float(p.get("lung_age_3")),
        }
        return cls(**data)
