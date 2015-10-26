__author__ = 'vegard'

class Forward(object):

    def __init__(self, bbcon, MAX_PRI):
        self.bbcon = bbcon
        self.priority = MAX_PRI / 2

    def update(self):
        self.bbcon.activate_behavior(self)

    def get_weight(self):
        return self.priority

    def get_motor_recommendation(self):
        return [0.1, 0.1], False
