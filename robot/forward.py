__author__ = 'vegard'

class Forward(object):

    def __init__(self, bbcon):
        self.bbcon = bbcon
        self.priority = 1

    def update(self):
        self.bbcon.activate_behavior(self)

    def get_weight(self):
        return self.priority

    def get_motor_recommendation(self):
        return [0.2, 0.2], False
