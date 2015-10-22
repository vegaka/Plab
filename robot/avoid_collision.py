from lib.ultrasonic import Ultrasonic
__author__ = 'Sander'

class AvoidCollision(object):

    def __init__(self, BBC,  max_pri):
        self.BBC = BBC
        self.OH_SHIT_DISTANCE = 15
        self.TURN_SPEED = 1
        self.turn = False
        self.max_pri = max_pri
        self.sensor = Ultrasonic()
        self.distance = float("inf")

    def update_sensor(self):
        self.distance = self.sensor.update()

    def update(self):
        self.update_sensor()
        if self.distance <= self.OH_SHIT_DISTANCE:
            self.turn = True
            self.BBC.activate_behavior()
        else:
            self.turn = False
            self.BBC.deactivate_behavior()

    def get_weight(self):
        return self.max_pri if self.turn else 0

    def get_motor_recommendation(self):
        if self.distance <= self.OH_SHIT_DISTANCE:
            return ([-self.TURN_SPEED, self.TURN_SPEED], 0.2)
        else:
            return (False, None)
