from lib.zumo_button import ZumoButton
from arbitrator import Arbitrator
from motor import Motor
from avoid_collision import AvoidCollision
from stay_inside import StayInside
import time

class BBCON(object):

    TIMESTEP_LENGTH = 250

    def __init__(self):
        self.behaviors = set()
        self.active_behaviors = set()
        self.sensors = set()
        self.motor = Motor()
        self.arbitrator = Arbitrator()

    def add_behavior(self, behavior):
        self.behaviors.add(behavior)

    def add_sensor(self, sensor):
        self.sensors.add(sensor)

    def activate_behavior(self, behavior):
        self.active_behaviors.remove(behavior)

    def deactivate_behavior(self, behavior):
        self.active_behaviors.remove(behavior)

    def get_arbitrator(self):
        return self.arbitrator

    def current_time_millis(self):
        return int(round(time.time() * 1000))

    def run_one_timestep(self):
        start = self.current_time_millis()

        for behavior in self.behaviors:
            behavior.update()

        self.arbitrator.choose_action()

        end = self.current_time_millis()
        if end - start < self.TIMESTEP_LENGTH:
            time.sleep((end - start) / 1000)

    def initialize_behaviors(self):
        # Avoid collision
        self.add_behavior(AvoidCollision(self, self.arbitrator.MAX_PRIORITY))

        # Stay inside
        self.add_behavior(StayInside(self, self.arbitrator.MAX_PRIORITY))

        # Add searching for red when it is fixed

if __name__ == "__main__":
    bbcon = BBCON()
    bbcon.initialize_behaviors()

    button = ZumoButton()
    button.wait_for_press()

    runstart = bbcon.current_time_millis()
    now = runstart
    while now - runstart < 10:
        bbcon.run_one_timestep()
        now = bbcon.current_time_millis()

