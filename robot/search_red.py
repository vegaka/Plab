__author__ = 'Johannes'
from Plab.robot.lib.camera import Camera
from Plab.robot.helpers import Helpers as h


class SearchRed(object):

    def __init__(self,red_thr, pollution_thr, speed):
        self.red_thr = red_thr
        self.pollution_thr = pollution_thr
        self.camera = Camera()
        self.image = None
        self.speed = speed
        self.weight = 0
        self.recommendation = None

    def update_sensor(self):
        self.image = self.sensor.update()
        self.weight, pos = h.get_red(self.image)
        if pos < 0:
            self.recommendation = [self.speed+pos, self.speed]
        elif pos > 0:
            self.recommendation = [self.speed, self.speed-pos]
        else:
            self.recommendation = [self.speed, self.speed]

    def get_weight(self):
        return self.weight

    def get_motor_recommendation(self):
        return self.recommendation, None
