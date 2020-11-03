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
        end_day='2021-04-30',
    )


def vorarlberg_scenario():
    sim = create_vorarlberg_sim(
        interventions=interventions,
        end_day='2021-01-31',
    )
    scenario = cv.Scenarios(sim=sim, basepars=basepars, metapars=scenario_metapars, scenarios=scenarios)
    scenario.run(verbose=True)
    scenario.plot(do_show=True)


def print_mean_tests():
    print('mean_daily_tests_march', np.mean(daily_tests_march))
    print('mean_daily_tests_april', np.mean(daily_tests_april))
    print('mean_daily_tests_may', np.mean(daily_tests_may))
    print('mean_daily_tests_june', np.mean(daily_tests_june))
    print('mean_daily_tests_july', np.mean(daily_tests_july))
    print('mean_daily_tests_august', np.mean(daily_tests_august))
    print('mean_daily_tests_october', np.mean(daily_tests_october))
    print('mean_daily_tests_november', np.mean(daily_tests_november))
    print('mean_daily_tests_december', np.mean(daily_tests_december))
    print('mean_daily_tests_january', np.mean(daily_tests_january))
    print('mean_daily_tests_february', np.mean(daily_tests_february))
    print('mean_daily_tests_march21', np.mean(daily_tests_march21))
    print('mean_daily_tests_april21', np.mean(daily_tests_april21))


def main():
    print_mean_tests()
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
