from src.interventions import *

# Define the actual scenarios

scenario_current_situation = {
    'current situation': {
        'name': 'current situation',
        'pars': {
            'interventions': interventions
        },
    },
}

scenario_best_case = {
    'best case': {
        'name': 'best case',
        'pars': {
            'interventions': interventions_best_case
        },
    },
}

scenario_worst_case = {
    'worst case': {
        'name': 'worst case',
        'pars': {
            'interventions': interventions_worst_case
        }
    }
}

scenario_home_office = {
    'homeOffice': {
        'name': 'HomeOffice',
        'pars': {
            'interventions': interventions_home_office
        },
    },
    # 'distance': {
    #   'name':'Social distancing',
    #   'pars': {
    #       'interventions': cv.change_beta(days=start_day, changes=0.7)
    #       }
    #   },
    # 'ttq': {
    #   'name':'Test-trace-quarantine',
    #   'pars': {
    #       'interventions': [
    #
    #             # cv.contact_tracing(start_day=start_day, trace_probs=0.8, trace_time=1.0),
    #         ]
    #       }
    #   },
}
