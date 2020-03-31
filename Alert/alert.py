
def alert(systolic_bp, diastolic_bp, pulse, oxygen):
    alert_info = False
    # if 140 > systolic_bp > 130 and 90 > diastolic_bp > 80 : Hypertension
    if 140 > systolic_bp > 130 and 90 > diastolic_bp > 80:
        print('Alert! The patient got Hypertension!!!')
        alert_info = True
    # if 129 > systolic_bp > 120 and diastolic_bp < 80: elevated blood pressure
    elif 129 > systolic_bp > 120 and diastolic_bp < 80:
        print('Alert! The patient got elevated blood pressure!!!')
        alert_info = True
    # pulse
    if pulse > 100:
        print('Alert! The patient is in fast heart rate!!!')
        alert_info = True
    elif pulse < 60:
        print('Alert! The patient is in slow heart rate!!!')
        alert_info = True
    # oxygen： 95% - 99% normal
    if oxygen < 95:
        print('Alert! Oxygen is under the Normal!')
        alert_info = True

    return alert_info

