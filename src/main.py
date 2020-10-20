import covasim as cv
import numpy as np
from src.utils.plotting import *
from src.vorarlberg_simulation import *
from src.examples import *
from src.interventions import *


def vorarlberg_real_sim():
    """
    bis 2020-07-12, annähernd die tatsächlichen Zahlen simuliert (Daten im csv-Format liegen nur bis 2020-07-12 vor)
    """
    return create_vorarlberg_sim(
        interventions=interventions,
    )


def vorarlberg_simulation_extended():
    return create_vorarlberg_sim(
        interventions=interventions,
        end_day='2020-10-20',
    )


def main():
    # sim = vorarlberg_simulation_extended()
    sim = vorarlberg_real_sim()

    sim.run(verbose=True)
    simple_plot(sim)


if __name__ == '__main__':
    main()
