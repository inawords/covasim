import covasim as cv
import numpy as np
import pandas as pd
from src.utils.plotting import *
from src.vorarlberg_simulation import *
from src.examples import *
from src.interventions import *
from src.utils.utils import *

overview_plots = [
            'cum_infections',
            'cum_deaths',
            'cum_diagnoses',
            'new_infections',
            'new_deaths',
            'new_diagnoses',
            'n_infectious',
            'n_quarantined',
            'r_eff',
            ]


def vorarlberg_simulation():
    return create_vorarlberg_sim(
        interventions=interventions,
        end_day='2020-10-31',
    )


def vorarlberg_scenario():
    sim = vorarlberg_simulation()
    scenario = cv.Scenarios(sim=sim, basepars=basepars, metapars=scenario_metapars, scenarios=scenarios)
    scenario.run(verbose=True)
    scenario.plot(do_show=True, to_plot=overview_plots, sep_figs=True)


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
    backup_interventions(interventions)
    vorarlberg_scenario()


if __name__ == '__main__':
    main()
