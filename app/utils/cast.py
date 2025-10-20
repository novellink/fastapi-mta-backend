from datetime import datetime
from typing import Any, Optional

def to_int(v: Any) -> Optional[int]:
    if v is None or v == "":
        return None
    try:
        if isinstance(v, bool):
            return int(v)
        return int(float(v))  # "55", "55.0" 모두 처리
    except (ValueError, TypeError):
        return None

def to_float(v: Any) -> Optional[float]:
    if v is None or v == "":
        return None
    try:
        if isinstance(v, bool):
            return float(int(v))
        return float(v)
    except (ValueError, TypeError):
        return None

def to_str(v: Any) -> Optional[str]:
    if v is None:
        return None
    s = str(v).strip()
    return s if s != "" else None

def to_dt(v: Any) -> Optional[datetime]:
    # ISO8601 "2025-10-14T09:01:42.000Z" 같은 형태 처리
    if v in (None, ""):
        return None
    try:
        # 필요 시 zoneinfo/pendulum로 확장 가능
        return datetime.fromisoformat(str(v).replace("Z", "+00:00"))
    except Exception:
        return None
