import numpy
import math
from collections import namedtuple
from app import coeficient as c
from app import report as rpt


class VoltageTimeSeries:

    def __init__(self):
        self.env = None

    def main(self):
        self.env = VoltageTimeSeries.build_environment()
        voltage_ts = VoltageTimeSeries.setup_initial_conditions(self.env)
        voltage_ts = self.compute_voltage_ts(voltage_ts)
        rpt.generate_report(self.env, voltage_ts, "voltagem-serie-temporal.csv")

    def compute_voltage_ts(self, voltage_ts):
        n, m, h = 0.3176, 0.0529, 0.5961
        voltage = 0.0

        for line in range (1, len(voltage_ts)):
            for col in range(1, len(voltage_ts[0]) - 1):
                voltage = voltage_ts[line][col] = self.compute_next_voltage(
                    voltage_ts[line-1][col-1],
                    voltage_ts[line-1][col],
                    voltage_ts[line-1][col+1],
                    n, m, h
                )

            n = c.compute_next_n(voltage, n, self.env.time_step)
            m = c.compute_next_m(voltage, m, self.env.time_step)
            h = c.compute_next_h(voltage, h, self.env.time_step)

        return voltage_ts

    def compute_next_voltage(self, volt_prev_ij, volt_ij, volt_next_ij, n, m, h):
        first_part = (volt_prev_ij - 2 * volt_ij + volt_next_ij) / (self.env.space_step ** 2)
        second_part = first_part * self.env.area / (2 * self.env.resistencia)
        third_part = second_part - self.compute_alphas_and_betas(volt_ij, n, m, h)
        return third_part * (self.env.time_step / self.env.capacitancia) + volt_ij

    def compute_alphas_and_betas(self, volt_ij, n, m, h):
        first_part = self.env.gK * (n ** 4) * (volt_ij - self.env.vK)
        second_part = self.env.gNA * (m ** 3) * h * (volt_ij - self.env.vNA)
        third_part = self.env.gL * (volt_ij - self.env.vL)
        return first_part + second_part + third_part

    @classmethod
    def setup_initial_conditions(cls, env):
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

    @classmethod
    def build_environment(cls):
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
