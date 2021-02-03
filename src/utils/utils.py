import pandas as pd
import covasim as cv
from src.parameters import intervention_file, scenario_metapars
from src.vorarlberg_simulation import create_vorarlberg_sim, basepars
from src.scenarios.current_situation.interventions import INT_CURRENT_SITUATION

overview_plots = [
            'cum_infections',
            'cum_deaths',
            'cum_diagnoses',
            'r_eff',
            ]

end_date_real_data = '2020-10-31'
end_date_sim = '2021-04-30'


def run_vorarlberg_scenario(scenarios, end_date=end_date_sim, plots=overview_plots):
    sim = create_vorarlberg_sim(
        interventions=INT_CURRENT_SITUATION,
        end_day=end_date,
    )
    scenario = cv.Scenarios(
        sim=sim,
        basepars=basepars,
        metapars=scenario_metapars,
        scenarios=scenarios)

    scenario.run(verbose=True)
    scenario.plot(do_show=True, to_plot=plots, sep_figs=True)


def backup_interventions(interventions):
    df = pd.DataFrame(interventions)
    df.to_csv(intervention_file)
