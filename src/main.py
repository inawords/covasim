from src.examples.examples import plot_with_real_data_from_csv, run_simple_vorarlberg_simulation, vorarlberg_scenario
from src.utils.plotting import *
from src.vorarlberg_simulation import *
from src.examples import *


def main():
    sim = run_simple_vorarlberg_simulation()
    simple_plot(sim)


if __name__ == '__main__':
    main()
