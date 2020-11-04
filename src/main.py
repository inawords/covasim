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


def main():
    backup_interventions(interventions)
    vorarlberg_scenario()


if __name__ == '__main__':
    main()
