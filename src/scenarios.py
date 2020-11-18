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


def create_scenario_edges_beta(label: str, beta: list, edges: list, intervention_func):
    scenarios = {}
    for b, e in zip(beta, edges):
        scenarios['_'.join([label, str(b), str(e)])] = {
            'name': 'Beta-' + str(b) + '; Edges-' + str(e),
            'pars': {
                'interventions': intervention_func(b, e)
            },
        }
    return scenarios


scenario_range = [0.2, 0.4, 0.6, 0.8]
scenario_community = create_scenario_edges_beta(
    label='restricted_community',
    beta=[0.8] * len(scenario_range),
    edges=scenario_range,
    intervention_func=create_interventions_restricted_community)
scenario_home_office = create_scenario_edges_beta(
    label='home_office',
    beta=scenario_range,
    edges=scenario_range,
    intervention_func=create_interventions_home_office)
scenario_mixed = create_scenario_edges_beta(
    label='mixed',
    beta=scenario_range,
    edges=scenario_range,
    intervention_func=create_interventions_mixed)
