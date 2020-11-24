from src.scenarios.best_worst_case.interventions import *

"""
Example Usage:

scenario = cv.Scenarios(
        sim=sim,
        basepars=basepars,
        metapars=scenario_metapars,
        scenarios=SCEN_BEST_CASE)
"""

SCEN_BEST_CASE = {
    'best_case': {
        'name': 'best case',
        'pars': {
            'interventions': INT_BEST_CASE
        },
    },
}

SCEN_WORST_CASE = {
    'worst_case': {
        'name': 'worst case',
        'pars': {
            'interventions': INT_WORST_CASE
        }
    }
}

SCEN_BEST_WORST = {
    **SCEN_BEST_CASE,
    **SCEN_WORST_CASE,
}
