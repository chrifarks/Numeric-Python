import math
from collections import namedtuple

import numpy


class VoltageTimeSeries:

    def main(self):
        env = self.build_environment()
        voltage_ts = self.setup_initial_conditions(env)


    def setup_initial_conditions(self, env):
        lines = 1 + int(env.duration / env.time_step)
        cols = 1 + int(env.bar_length / env.space_step)
        voltage_ts = numpy.zeros((lines, cols))

        # Setting up voltage for the FIRST line
        for col in range(0, len(voltage_ts[0])):
            space_in_cm = col * 10
            voltage_ts[0][col] = 100 * (math.e ** (-0.2 * space_in_cm))

        # Setting up voltage for the FIRST and LAST cols
        for line in range(0, len(voltage_ts)):
            voltage_ts[line][0] = -65.002
            voltage_ts[line][cols - 1] = 0.0

        return voltage_ts

    def build_environment(self):
        env = namedtuple('environment', [
            'area', 'resistencia', 'capacitancia',
            'gK', 'gNA', 'gL',
            'vK', 'vNA', 'vL',
            'bar_length', 'space_step',
            'duration', 'time_step'
        ])
        env.area = 180000.0
        env.resistencia = 35.4
        env.capacitancia = 1.0
        env.gK = 3.60
        env.gNA = 12.0
        env.gL = 0.03
        env.vK = -77.0
        env.vNA = 50.0
        env.vL = -54.402
        env.bar_length = 100
        env.space_step = 5
        env.duration = 1.0
        env.time_step = 0.001
        return env


if __name__ == '__main__':
    VoltageTimeSeries().main()
