class BP(Base):
    __tablename__ = "bp"
    high = Column()   # 144
    low = Column()    # 92
    pulse = Column()  # 83
    status = Column() # 고혈압


class HS(Base):
    __tablename__ = "hs"
    height = Column() # 4
    weight = Column() # 5
    bmi = Column()    # BMI
    status = Column() # HS정상


class VA(Base):
    __tablename__ = "va"
    left = Column()          # 6
    left_status = Column()   # 좌안정상
    right = Column()         # 7
    right_status = Column()  # 우안정상
    status = Column()        # VA정상


class CM(Base):
    __tablename__ = "cm"
    value = Column() # 색각 정상


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


class AL(Base):
    __tablename__ = "al"
    alcohol_result = Column() # 음주결과
    alcohol_yang = Column()   # 음주량


class BS(Base):
    __tablename__ = "bs"
    status = Column()          # 측정상태
    bloodsugar_type = Column() # 식전
    bloodsugar = Column()      # 혈당
    col_total = Column()       # 콜레스테롤 Total
    col_tri = Column()         # 중성지방
    col_ldl = Column()         # LDL
    col_hdl = Column()         # HDL


class LU(Base):
    __tablename__ = "lu"
    # 1차 측정
    fvc_1 = Column()               # 노력성 폐활량
    fvc_p_1 = Column()             # fvc 정상예측치
    fev1_1 = Column()              # 1초간 노력성호기량
    fev1_p_1 = Column()            # fev1 정상예측치
    fev1fvc_1 = Column()           # fev1/fvc 1초율
    fev1fvc_status_1 = Column()    # fev1/fvc 결과
    fef2575_1 = Column()           # FEF25-75
    pef_1 = Column()               # 최고호기기류
    pef_p_1 = Column()             # pef 정상 예측치
    lung_age_1 = Column()          # 폐 나이

    # 2차 측정
    fvc_2 = Column()               # 노력성 폐활량
    fvc_p_2 = Column()             # fvc 정상예측치
    fev1_2 = Column()              # 1초간 노력성호기량
    fev1_p_2 = Column()            # fev1 정상예측치
    fev1fvc_2 = Column()           # fev1/fvc 1초율
    fev1fvc_status_2 = Column()    # fev1/fvc 결과
    fef2575_2 = Column()           # FEF25-75
    pef_2 = Column()               # 최고호기기류
    pef_p_2 = Column()             # pef 정상 예측치
    lung_age_2 = Column()          # 폐 나이

    # 3차 측정
    fvc_3 = Column()               # 노력성 폐활량
    fvc_p_3 = Column()             # fvc 정상예측치
    fev1_3 = Column()              # 1초간 노력성호기량
    fev1_p_3 = Column()            # fev1 정상예측치
    fev1fvc_3 = Column()           # fev1/fvc 1초율
    fev1fvc_status_3 = Column()    # fev1/fvc 결과
    fef2575_3 = Column()           # FEF25-75
    pef_3 = Column()               # 최고호기기류
    pef_p_3 = Column()             # pef 정상 예측치
    lung_age_3 = Column()          # 폐 나이