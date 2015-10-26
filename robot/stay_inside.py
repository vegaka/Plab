from lib.reflectance_sensors import ReflectanceSensors
__author__ = 'Sander'


class StayInside(object):

    def __init__(self, BBC, max_pri):
        self.BBC = BBC
        self.sensor = ReflectanceSensors(auto_calibrate=False, min_reading=0, max_reading=1200)
        self.max_pri = max_pri
        self.TURN_SPEED = 0.5
        self.THRESHHOLD = 0.2
        self.about_to_crash = False
        self.values = [self.sensor.max_val for _ in range(5)]

    def update_sensors(self):
        self.sensor.update()
        self.values = self.sensor.get_value()
        #print(self.values, self.sensor.value)

    def update(self):
        self.about_to_crash = False
        self.update_sensors()
        for reading in self.values:
            if reading <= self.THRESHHOLD:
                self.BBC.activate_behavior(self)
                self.about_to_crash = True
                break
        else:
            self.BBC.deactivate_behavior(self)

    def get_weight(self):
        return self.max_pri if self.about_to_crash else 0

    def get_motor_recommendation(self):
        if self.about_to_crash:
            if self.values[0] <= self.THRESHHOLD or self.values[1] <= self.THRESHHOLD:
                return [-1, -0.7], 0.5
            else:
                return [-0.7, -1], 0.5
        else:
            return False, None
