import numpy as np
import pandas as pd
import pyrebase


def prediction():
    diastolic_bp = []
    systolic_bp = []
    pulse = []
    oxygen = []

    config = {
        "apiKey": "AIzaSyBnia2_MDilXrlvFUsIxjs4_xnBoicNkqw",
        "authDomain": "icu-ec500.firebaseapp.com",
        "databaseURL": "https://icu-ec500.firebaseio.com",
        "projectId": "icu-ec500",
        "storageBucket": "icu-ec500.appspot.com",
        "messagingSenderId": "954586536411",
        "appId": "1:954586536411:web:177f46e30ff4326c936ffe",
        "measurementId": "G-CLR7QW22MX"
    };

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    db_info = db.child('Monitor').get()

    for data in db_info.each():
        if data.val() is None:
            continue
        else:
            diastolic_bp.append(data.val()['diastolic_bp'])
            systolic_bp.append(data.val()['systolic_bp'])
            oxygen.append(data.val()['oxygen'])
            pulse.append(data.val()['pulse'])

    data = {
        'diastolic_bp': diastolic_bp,
        'oxygen': oxygen,
        'pulse': pulse,
        'systolic_bp': systolic_bp
    }

    df = pd.DataFrame(data)

    diastolic_bp_all = df.loc[:,'diastolic_bp'].values
    oxygen_all = df.loc[:, 'oxygen'].values
    pulse_all = df.loc[:, 'pulse'].values
    systolic_bp_all = df.loc[:, 'systolic_bp'].values

    predict_dias_bp = np.mean(diastolic_bp_all)
    predict_oxygen = np.mean(oxygen_all)
    predict_pulse = np.mean(pulse_all)
    predict_syst_bp = np.mean(systolic_bp_all)
    print('Prediction of the diastolic_bp:', predict_dias_bp)
    print('Prediction of the oxygen:' + str(predict_oxygen) + '%')
    print('Prediction of the pulse:' + str(predict_pulse))
    print('Prediction of the diastolic_bp:' + str(predict_syst_bp))


if __name__ == '__main__':
    prediction()



