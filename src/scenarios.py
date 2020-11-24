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


""" PARAMETER VARYING """

scenario_range = [0.2, 0.4, 0.6]  # 0,0 is best case, 0.8 is worst case scenario
scenario_fixed_value = [0.8] * len(scenario_range)
combinations = dict(
    edges=dict(
        beta=[0.8] * len(scenario_range),
        edges=scenario_range,
    ),
    both=dict(
        beta=scenario_range,
        edges=scenario_range,
    ),
    beta=dict(
        beta=scenario_range,
        edges=[0.8] * len(scenario_range),
    )
)

labels = dict(
    c='restricted_community',
    w='home_office'
)

create_intervention_func = dict(
    c=create_interventions_restricted_community,
    w=create_interventions_home_office
)


def parameter_influence(parameter='edges', layer='c'):
    # combination: 'beta' | 'edges' | 'both' -> parameter to be varied
    # layer: 'c' | 'w'
    return create_scenario_edges_beta(
        label=labels[layer],
        beta=combinations[parameter]['beta'],
        edges=combinations[parameter]['edges'],
        intervention_func=create_intervention_func[layer])
