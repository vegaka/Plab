from lib.reflectance_sensors import ReflectanceSensors
__author__ = 'Sander'


class StayInside(object):

    def __init__(self, BBC, max_pri):
        self.BBC = BBC
        self.sensor = ReflectanceSensors(auto_calibrate=True)
        self.max_pri = max_pri
        self.TURN_SPEED = 0.5
        self.THRESHHOLD = 150
        self.about_to_crash = False
        self.values = [self.sensor.max_val for _ in range(5)]

    def update_sensors(self):
        self.sensor.update()
        self.values = self.sensor.get_value()

    def update(self):
        self.about_to_crash = False
        self.update_sensors()
        for reading in self.values:
            if reading <= self.THRESHHOLD:
                self.BBC.activate_behavior(self)
                self.about_to_crash = True
                break
        else:
            self.BBC.deactive_behavoir(self)

    def get_weight(self):
        return self.max_pri if self.about_to_crash else 0

    def get_motor_recommendation(self):
        if self.about_to_crash:
            l, r = self.compute_turn()
            return ([l, r], 0.1)
        else:
            return (False, None)

    def compute_turn(self):
        l, r = 0, 0
        for i in range(5):
            if self.values[i] <= self.THRESHHOLD:
                if i < 2:
                        l = 1
                elif i > 2:
                        r = 1
        return [0.5, -0.5] if not l else [-0.5, 0.5]
