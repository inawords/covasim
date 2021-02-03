from src.scenarios.current_situation.scenarios import SCEN_CURRENT_SITUATION, CURRENT_PLOTS
from src.utils.utils import end_date_real_data, run_vorarlberg_scenario


def main():
    run_vorarlberg_scenario(
        SCEN_CURRENT_SITUATION,
        end_date=end_date_real_data,
        plots=CURRENT_PLOTS
    )


if __name__ == '__main__':
    main()
