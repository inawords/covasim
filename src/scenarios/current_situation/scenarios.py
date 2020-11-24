from src.scenarios.current_situation.interventions import *

"""
Example Usage:

scenario = cv.Scenarios(
        sim=sim,
        basepars=basepars,
        metapars=scenario_metapars,
        scenarios=SCEN_CURRENT_SITUATION)
"""

SCEN_CURRENT_SITUATION = {
    'current_situation': {
        'name': 'current situation',
        'pars': {
            'interventions': INT_CURRENT_SITUATION
        },
    },
}
