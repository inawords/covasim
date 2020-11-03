import covasim as cv
import numpy as np
from src.utils.plotting import *
from src.vorarlberg_simulation import *
from src.examples import *
from src.interventions import *


def vorarlberg_real_sim():
    """
    bis 2020-10-27, annähernd die tatsächlichen Zahlen simuliert (Daten im csv-Format liegen bis 2020-10-27 vor)
    """
    return create_vorarlberg_sim(
        interventions=interventions,
    )


def vorarlberg_simulation_extended():
    return create_vorarlberg_sim(
        interventions=interventions,
        end_day='2020-11-03',
    )


def vorarlberg_scenario():
    sim = create_vorarlberg_sim(
        interventions=interventions,
        end_day='2020-11-03',
    )
    scenario = cv.Scenarios(sim=sim, basepars=basepars, metapars=scenario_metapars, scenarios=scenarios)
    scenario.run(verbose=True)
    scenario.plot(do_show=True)


def main():
    sim = vorarlberg_simulation_extended()
    # sim = vorarlberg_real_sim()
    sim.run(verbose=True)
    # fit = cv.Fit(sim)
    # fit.plot()
    # agehist = sim.make_age_histogram()
    # agehist.plot()
    simple_plot(sim)

    # vorarlberg_scenario()


if __name__ == '__main__':
    main()
