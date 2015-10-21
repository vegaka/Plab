from robot.lib.ultrasonic import Ultrasonic
__author__ = 'Sander'

class AvoidCollision(object):

    def __init__(self, max_pri):
        self.OH_SHIT_DISTANCE = 15
        self.TURN_SPEED = 1
        self.max_pri = max_pri
        self.sensor = Ultrasonic()
        self.distance = float("inf")

    def update_sensor(self):
        self.distance = self.sensor.update()

    def get_weight(self):
        self.update_sensor()
        if self.distance <= self.OH_SHIT_DISTANCE:
            return self.max_pri
        else:
            return 0

    def get_motor_recommendation(self):
        if self.distance <= self.OH_SHIT_DISTANCE:
            return [-self.TURN_SPEED, self.TURN_SPEED]
        else:
            return False
