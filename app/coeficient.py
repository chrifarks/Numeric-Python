import math


def compute_next_n(voltage, previous_n, time_step):
    return (__compute_alpha_for_n(voltage) * (1 - previous_n) -
            __compute_beta_for_n(voltage) * previous_n) * time_step + previous_n


def compute_next_m(voltage, previous_m, time_step):
    return (__compute_alpha_for_m(voltage) * (1 - previous_m) -
            __compute_beta_for_m(voltage) * previous_m) * time_step + previous_m


def compute_next_h(voltage, previous_h, time_step):
    return (__compute_alpha_for_h(voltage) * (1 - previous_h) -
            __compute_beta_for_h(voltage) * previous_h) * time_step + previous_h


def __compute_alpha_for_n(voltage):
    return 0.01 * (voltage - 10) / (math.e ** ((voltage - 10) / 10) - 1)


def __compute_beta_for_n(voltage):
    return 0.125 * (math.e ** (voltage / 80))


def __compute_alpha_for_m(voltage):
    return 0.01 * (voltage - 25) / (math.e ** ((voltage - 25) / 10) - 1)


def __compute_beta_for_m(voltage):
    return 4 * (math.e ** (voltage / 18))


def __compute_alpha_for_h(voltage):
    return 0.07 * (math.e ** (voltage / 20))


def __compute_beta_for_h(voltage):
    return 1 / (math.e ** ((voltage - 30) / 10) - 1)
