__author__ = 'Sander'
from lib.ultrasonic import Ultrasonic

class AvoidCollision(object):

    def __init__(self, max_pri):
        self.PRIORITY_FACTOR = 10
        self.OH_SHIT_DISTANCE = 15
        self.max_pri = max_pri
        self.sensor = Ultrasonic()
        self.distance = float("inf")

    def update_sensor(self):
        self.distance = self.sensor.update()

    def get_weight(self):
        self.update_sensor()
        if self.distance <= self.OH_SHIT_DISTANCE:
            return self.max_pri * self.PRIORITY_FACTOR
        else:
            return (self.max_pri-self.distance) * self.PRIORITY_FACTOR