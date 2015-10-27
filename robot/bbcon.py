from lib.zumo_button import ZumoButton
from arbitrator import Arbitrator
from motor import Motor
from avoid_collision import AvoidCollision
from stay_inside import StayInside
from forward import Forward
from search_red import SearchRed
import time

class BBCON(object):

    TIMESTEP_LENGTH = 50

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
        self.active_behaviors.add(behavior)

    def deactivate_behavior(self, behavior):
        if behavior in self.active_behaviors:
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
            print("Sleep")
            time.sleep((end - start) / 1000)

    def initialize_behaviors(self):
        # Forward
        self.add_behavior(Forward(self))

        # Avoid collision
        self.add_behavior(AvoidCollision(self, self.arbitrator.MAX_PRIORITY))

        # Stay inside
        self.add_behavior(StayInside(self, self.arbitrator.MAX_PRIORITY))

        # Add searching for red when it is fixed
        self.add_behavior(SearchRed(self, self.arbitrator.MAX_PRIORITY))

if __name__ == "__main__":
    bbcon = BBCON()
    bbcon.initialize_behaviors()
    bbcon.arbitrator.set_controller(bbcon)

    button = ZumoButton()
    x = button.check_pressed()
    print(x)
    button.wait_for_press()

    runstart = time.time()
    now = runstart
    button_clicked = False
    while not button_clicked:
        bbcon.run_one_timestep()
        button_clicked = not button.check_pressed() == 1
        print(button_clicked)

    bbcon.motor.set_motor_values([0, 0], False)
