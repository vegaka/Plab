from robot.arbitrator import Arbitrator


class BBCON(object):

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
        self.active_behaviors.remove(behavior)

    def run_one_timestep(self):
        pass