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
    'homeOffice_0.2': {
        'name': 'Beta-Edges 0.2',
        'pars': {
            'interventions': interventions_home_office(0.2, 0.2)
        },
    },
    'homeOffice_0.3': {
        'name': 'Beta-Edges 0.3',
        'pars': {
            'interventions': interventions_home_office(0.3, 0.3)
        },
    },
    'homeOffice_0.4': {
        'name': 'Beta-Edges 0.4',
        'pars': {
            'interventions': interventions_home_office(0.4, 0.4)
        },
    },
    'homeOffice_0.5': {
        'name': 'Beta-Edges 0.5',
        'pars': {
            'interventions': interventions_home_office(0.5, 0.5)
        },
    },
    'homeOffice_0.6': {
        'name': 'Beta-Edges 0.6',
        'pars': {
            'interventions': interventions_home_office(0.6, 0.6)
        },
    },
    'homeOffice_0.7': {
        'name': 'Beta-Edges 0.7',
        'pars': {
            'interventions': interventions_home_office(0.7, 0.7)
        },
    },
    'homeOffice_0.8': {
        'name': 'Beta-Edges 0.8',
        'pars': {
            'interventions': interventions_home_office(0.8, 0.8)
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
