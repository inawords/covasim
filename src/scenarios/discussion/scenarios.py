from src.scenarios.work_vs_community.interventions import *
from src.scenarios.best_worst_case.interventions import *

INTERVENTION_START = "2020-11-01"

SCEN_DISCUSSION = {
    'best_case': {
        'name': 'best',
        'pars': {
            'interventions': INT_BEST_CASE
        },
    },

    'worst_case': {
        'name': 'worst',
        'pars': {
            'interventions': INT_WORST_CASE
        },
    },

    'home_office': {
        'name': 'home office',
        'pars': {
            'interventions': create_interventions_home_office(0.5, 0.5, INTERVENTION_START)
        },
    },

    'social_distancing': {
        'name': 'social distancing',
        'pars': {
            'interventions': create_interventions_social_distancing(0.8, 0.5, INTERVENTION_START)
        },
    },

    'mixed': {
        'name': 'combined',
        'pars': {
            'interventions': create_interventions_mixed(0.6, 0.6, INTERVENTION_START)
        },
    },
}

