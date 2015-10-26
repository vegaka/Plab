__author__ = 'Johannes'
from lib.camera import Camera
from helpers import Helpers as h


class SearchRed(object):

    def __init__(self, BBC, max_pri):
        self.BBC = BBC
        self.camera = Camera()
        self.image = None
        self.speed = 0.2
        self.weight = 0
        self.weight_thr = 20
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

    def update(self):
        self.update_sensor()
        if self.weight > self.weight_thr:
            self.BBC.activate_behaviour(self)
        else:
            self.BBC.deactivate_behaviour(self)

    def get_weight(self):
        return self.weight

    def get_motor_recommendation(self):
        return self.recommendation, None

