import covasim as cv
from src.interventions import interventions

# Define the actual scenarios

scenarios = {'homeOffice': {
    'name': 'HomeOffice',
    'pars': {
        'interventions': interventions
    }
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
