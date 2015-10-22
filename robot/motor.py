from lib.motors import Motors

class Motor(object):

    def __init__(self):
        self.motors = Motors()

    def set_motor_values(self, val, duration):
        self.motors.set_value(val, dur=duration)
