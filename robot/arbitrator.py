from random import uniform

class Arbitrator(object):

    MAX_PRIORITY = 100

    def __init__(self, stochastic=False):
        self.stochastic = stochastic
        self.bbcon = None

    def set_controller(self, bbcon):
        self.bbcon = bbcon

    def choose_action(self):
        weights = []
        total_weight = 0.0
        for behavior in self.bbcon.active_behaviors:
            weight = behavior.get_weight()
            total_weight += weight
            weights.append((weight, behavior))

        if self.stochastic:
            choice = uniform(0, total_weight)
            old = current = 0

            for i in range(len(weights)):
                current += weights[i][0]

                if old <= choice < current:
                    self.activate_behavior(weights[i][1])
                    break

                old = current

        else:
            weights.sort(key=lambda t: t[0], reverse=True)
            self.activate_behavior(weights[0][1])

    def activate_behavior(self, behavior):
        print(behavior)
        motor_values = behavior.get_motor_recommendation()
        self.bbcon.motor.set_motor_values(motor_values[0], motor_values[1])
