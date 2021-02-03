from src.scenarios.current_situation.interventions import *

"""
Example Usage:

scenario = cv.Scenarios(
        sim=sim,
        basepars=basepars,
        metapars=scenario_metapars,
        scenarios=SCEN_CURRENT_SITUATION)
"""

CURRENT_PLOTS = [
    'cum_diagnoses',
    'cum_deaths',
    'r_eff',
    ]

SCEN_CURRENT_SITUATION = {
    'current_situation': {
        'name': 'current situation',
        'pars': {
            'interventions': INT_CURRENT_SITUATION
        },
    },
}
