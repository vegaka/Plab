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
        self.weight_thr = 10
        self.recommendation = None
        self.max_pri = max_pri

    def update_sensor(self):
        self.image = self.camera.update()
        self.weight, pos = h.get_red(self.image)
        if pos < 0:
            self.recommendation = [self.speed-pos, self.speed]
        elif pos > 0:
            self.recommendation = [self.speed, self.speed-pos]
        else:
            self.recommendation = [self.speed, self.speed]

    def update(self):
        self.update_sensor()
        self.BBC.activate_behavior(self)
        return
        if self.weight > self.weight_thr:
            self.BBC.activate_behavior(self)
        else:
            self.BBC.deactivate_behavior(self)

    def get_weight(self):
        print("W: " + str(self.weight))
        return self.weight * self.max_pri

    def get_motor_recommendation(self):
        print("R: " + str(self.recommendation))
        return self.recommendation, None

