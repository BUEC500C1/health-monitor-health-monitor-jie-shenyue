import pyrebase
from Alert import alert


def display():
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

    db_info = db.child('Monitor').child('1').get()
    dias_bp = db_info.each()[0].val()
    oxy = db_info.each()[1].val()
    puls = db_info.each()[2].val()
    sys_bp = db_info.each()[3].val()

    get_alert = alert.alert(sys_bp, dias_bp, puls, oxy)

    if get_alert is False:
        for data in db_info.each():
            print(data.key(), data.val())


if __name__ == '__main__':
    display()

