from src.scenarios.work_vs_community.scenarios import SOCIAL_DISTANCING, work_community_scenario
from src.utils.utils import run_vorarlberg_scenario


def scenario(variation):
    args = SOCIAL_DISTANCING['time_influence'][variation]
    scenarios = work_community_scenario(**args)
    run_vorarlberg_scenario(scenarios)


def main():
    """
    Choose which of the three scenarios to run
    - 0: start date 01.11.2020
    - 1: start date 01.10.2020
    - 2: start date 15.09.2020
    """
    scenario(0)


if __name__ == '__main__':
    main()
