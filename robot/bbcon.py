from robot.arbitrator import Arbitrator
import time

class BBCON(object):

    TIMESTEP_LENGTH = 250

    def __init__(self):
        self.behaviors = set()
        self.active_behaviors = set()
        self.sensors = set()
        self.motors = set()
        self.arbitrator = Arbitrator()

    def add_behavior(self, behavior):
        self.behaviors.add(behavior)

    def add_sensor(self, sensor):
        self.sensors.add(sensor)

    def activate_behavior(self, behavior):
        self.active_behaviors.remove(behavior)

    def deactivate_behavior(self, behavior):
        if behavior in self.active_behaviors:
            self.active_behaviors.remove(behavior)

    def get_arbitrator(self):
        return self.arbitrator

    def current_time_millis(self):
        return int(round(time.time() * 1000))

    def run_one_timestep(self):
        start = self.current_time_millis()

        # Do everything in a timestep here

        end = self.current_time_millis()
        if end - start < self.TIMESTEP_LENGTH:
            time.sleep((end - start) / 1000)