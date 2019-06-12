from collections import namedtuple


class VoltageTimeSeries:

    def main(self):
        env = self.build_environment()

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
