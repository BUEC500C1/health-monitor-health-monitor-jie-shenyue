import random


class Sensor:
    def __init__(self):
        self.systolic_bp = 0
        self.diastolic_bp = 0
        self.pulse = 0
        self.oxygen = 0

    def get_systolic_bp(self):
        self.systolic_bp = random.randint(120, 150)
        return self.systolic_bp

    def get_diastolic_bp(self):
        self.diastolic_bp = random.randint(80, 100)
        return self.diastolic_bp

    def get_pulse(self):
        self.pulse = random.randint(40, 150)
        return self.pulse

    def get_oxygen(self):
        self.oxygen = random.randint(70, 100)
        return self.oxygen

