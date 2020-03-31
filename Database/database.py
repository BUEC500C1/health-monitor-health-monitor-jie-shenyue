from Sensor import sensor
import pyrebase


def data_base():
    case_info = sensor.Sensor()
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

    data = {
        'systolic_bp': case_info.get_systolic_bp(),
        'diastolic_bp': case_info.get_diastolic_bp(),
        'pulse': case_info.get_pulse(),
        'oxygen': case_info.get_oxygen()
    }

    db.child('Monitor').child('1').set(data)
    print('data added')


if __name__ == '__main__':
    data_base()
