from src.scenarios.work_vs_community.scenarios import HOME_OFFICE, work_community_scenario
from src.utils.utils import run_vorarlberg_scenario


def scenario(variation):
    args = HOME_OFFICE['parameter_influence'][variation]
    scenarios = work_community_scenario(**args)
    run_vorarlberg_scenario(scenarios)


def main():
    """
    Choose which of the three scenarios to run
    - 0: both parameters are adapted
    - 1: only beta parameter is adapted
    - 2: only edges parameter is adapted
    """
    scenario(0)


if __name__ == '__main__':
    main()
