from random import uniform

class Arbitrator(object):

    MAX_PRIORITY = 100

    def __int__(self, bbcon, stochastic=False):
        self.stochastic = stochastic
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
                current += weights[i]

                if old <= choice < current:
                    # Choose behavior
                    break

                old = current

        else:
            weights.sort(key=lambda t: t[0], reverse=True)
            chosen_behavior = weights[0][1]
            motor_values = chosen_behavior.get_motor_recommendation()
            self.bbcon.motor.set_motor_values(motor_values[0], motor_values[1])
