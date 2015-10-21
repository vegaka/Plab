from robot.lib.ultrasonic import Ultrasonic
__author__ = 'Sander'


class AvoidCollision(object):

    def __init__(self, BBC,  max_pri):
        self.BBC = BBC
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
            self.BBC.activate_behavior(self)
            return self.max_pri
        else:
            self.BBC.deactivate_behavior(self)
            return 0

    def get_motor_recommendation(self):
        if self.distance <= self.OH_SHIT_DISTANCE:
            return ([-self.TURN_SPEED, self.TURN_SPEED], 0.2)
        else:
            return (False, None)
