from src.interventions import *

"""
Example Usage:

scenario = cv.Scenarios(
        sim=sim,
        basepars=basepars,
        metapars=scenario_metapars,
        scenarios=scenario_best_case)
"""

scenario_best_case = {
    'best_case': {
        'name': 'best case',
        'pars': {
            'interventions': interventions_best_case
        },
    },
}

scenario_worst_case = {
    'worst_case': {
        'name': 'worst case',
        'pars': {
            'interventions': interventions_worst_case
        }
    }
}

combined = {
    'best_case': {
        'name': 'best case',
        'pars': {
            'interventions': interventions_best_case
        },
    },
    'worst_case': {
        'name': 'worst case',
        'pars': {
            'interventions': interventions_worst_case
        }
    }
}
