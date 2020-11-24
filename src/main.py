from src.vorarlberg_simulation import *
from src.scenarios.work_vs_community.scenarios import *

overview_plots = [
            'cum_infections',
            'cum_deaths',
            'cum_diagnoses',
            'r_eff',
            ]

end_date_real_data = '2020-10-31'
end_date_sim = '2021-04-30'


def vorarlberg_simulation():
    return create_vorarlberg_sim(
        interventions=interventions,
        end_day=end_date_sim,
    )


def vorarlberg_scenario():
    sim = vorarlberg_simulation()
    args = HOME_OFFICE['parameter_influence'][0]
    scenario = cv.Scenarios(
        sim=sim,
        basepars=basepars,
        metapars=scenario_metapars,
        scenarios=work_community_scenario(**args))

    scenario.run(verbose=True)
    scenario.plot(do_show=True, to_plot=overview_plots, sep_figs=True)


def main():
    vorarlberg_scenario()


if __name__ == '__main__':
    main()
