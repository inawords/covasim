from src.vorarlberg_simulation import *
from src.scenarios.current_situation.scenarios import *
from src.scenarios.current_situation.interventions import INT_CURRENT_SITUATION
from src.scenarios.best_worst_case.scenarios import *
from src.scenarios.work_vs_community.scenarios import *
from src.scenarios.discussion.scenarios import *
from src.utils.utils import overview_plots, end_date_real_data, end_date_sim


def vorarlberg_simulation():
    return create_vorarlberg_sim(
        interventions=INT_CURRENT_SITUATION,
        end_day=end_date_sim,
    )


def vorarlberg_scenario():
    sim = vorarlberg_simulation()
    scenario = cv.Scenarios(
        sim=sim,
        basepars=basepars,
        metapars=scenario_metapars,
        scenarios=SCEN_DISCUSSION)

    scenario.run(verbose=True)
    scenario.to_excel(filename=result_file_xlsx)
    scenario.plot(do_show=True, to_plot=overview_plots, sep_figs=True)


def main():
    vorarlberg_scenario()


if __name__ == '__main__':
    main()
