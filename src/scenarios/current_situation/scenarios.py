from src.interventions import *

"""
Example Usage:

scenario = cv.Scenarios(
        sim=sim,
        basepars=basepars,
        metapars=scenario_metapars,
        scenarios=scenario_current_situation)
"""

scenario_current_situation = {
    'current situation': {
        'name': 'current situation',
        'pars': {
            'interventions': interventions
        },
    },
}
