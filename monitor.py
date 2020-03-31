from Database import database
from Display import display
from Prediction import prediction


def monitor():
    try:
        # store the data from sensor in our database
        database.data_base()
        # display if normal, or will send the alert to the terminal
        display.display()
        # prediction
        prediction.prediction()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    monitor()
