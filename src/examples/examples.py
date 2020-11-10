from src.utils.plotting import *
from src.vorarlberg_simulation import *


def run_simple_vorarlberg_simulation():
    """run simple simulation with Vorarlberg data"""
    sim = create_vorarlberg_sim()
    sim.run(verbose=True)
    return sim


def vorarlberg_scenario():
    """run simple simulation with Vorarlberg data for a scenario with multiple runs"""
    sim = create_vorarlberg_sim()
    scenario = cv.Scenarios(sim=sim, basepars=basepars, metapars=scenario_metapars, scenarios=scenarios)
    scenario.run(verbose=True)
    scenario.plot(do_show=True)


def plot_with_real_data_from_csv():
    """
    run simple simulation and create a plot with simulated and real data for comparison
    uses real data from Vorarlberg and simulated data from Seattle
    """
    sim = cv.Sim(datafile=real_data_csv)
    sim.run()
    simple_plot(sim)
    return sim
