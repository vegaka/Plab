from robot.lib.reflectance_sensors import ReflectanceSensors
__author__ = 'Sander'


class StayInside(object):

    def __init__(self, max_pri):
        self.sensor = ReflectanceSensors(auto_calibrate=True)
        self.max_pri = max_pri
        self.TURN_SPEED = 0.5
        self.THRESHHOLD = 150
        self.about_to_crash = False
        self.values = [self.sensor.max_val for _ in range(5)]

    def update_sensors(self):
        self.sensor.update()
        self.values = self.sensor.get_value()

    def get_weight(self):
        self.about_to_crash = False
        self.update_sensors()
        for reading in self.values:
            if reading <= self.THRESHHOLD:
                self.about_to_crash = True
                return self.max_pri
        return 0

    def get_motor_recommendation(self):
        if self.about_to_crash:
            l, r = self.compute_turn()
            return ([l, r], 0.1)
        else:
            return False

    def compute_turn(self):
        direction = 0
        for i in range(-2, 3):
            if self.values[i+2] <= self.THRESHHOLD:
                direction += i
        return [1/direction, -1/direction]
