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
    'homeOffice_0.4': {
        'name': 'Beta-Edges 0.4',
        'pars': {
            'interventions': interventions_home_office(0.4, 0.4)
        },
    },
    'homeOffice_0.6': {
        'name': 'Beta-Edges 0.6',
        'pars': {
            'interventions': interventions_home_office(0.6, 0.6)
        },
    },
    'homeOffice_0.8': {
        'name': 'Beta-Edges 0.8',
        'pars': {
            'interventions': interventions_home_office(0.8, 0.8)
        },
    },
}

scenario_community = {
    'community_0.2': {
        'name': 'Beta-Edges 0.2',
        'pars': {
            'interventions': interventions_community_adapted(0.2, 0.8)
        },
    },
    'community_0.4': {
        'name': 'Beta-Edges 0.4',
        'pars': {
            'interventions': interventions_community_adapted(0.4, 0.8)
        },
    },
    'community_0.6': {
        'name': 'Beta-Edges 0.6',
        'pars': {
            'interventions': interventions_community_adapted(0.6, 0.8)
        },
    },
    'community_0.8': {
        'name': 'Beta 0.8',
        'pars': {
            'interventions': interventions_community_adapted(0.8, 0.8)
        },
    },
}