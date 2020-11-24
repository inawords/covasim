from src.interventions import *

PARAMETER_RANGE = [0.2, 0.4, 0.6]  # 0,0 is best case, 0.8 is worst case scenario
PARAMETER_CONST = [0.8] * len(PARAMETER_RANGE)

LABELS = dict(
    c='restricted_community',
    w='home_office',
    cw='mixed',
)

INTERVENTION_START = ['2020-11-01', '2020-10-01', '2020-09-15']

COMBINATIONS = dict(
    edges=dict(
        beta=PARAMETER_CONST,
        edges=PARAMETER_RANGE,
    ),
    both=dict(
        beta=PARAMETER_RANGE,
        edges=PARAMETER_RANGE,
    ),
    beta=dict(
        beta=PARAMETER_RANGE,
        edges=PARAMETER_CONST,
    )
)

INTERVENTION_FUNC = dict(
    c=create_interventions_restricted_community,
    w=create_interventions_home_office,
    cw=create_interventions_mixed,
)


def create_scenario_edges_beta(
        label: str,
        beta: list,
        edges: list,
        intervention_func,
        intervention_start=INTERVENTION_START[0],
):
    scenarios = {}
    for b, e in zip(beta, edges):
        scenarios['_'.join([label, str(b), str(e)])] = {
            'name': 'Beta-' + str(b) + '; Edges-' + str(e),
            'pars': {
                'interventions': intervention_func(b, e, intervention_start)
            },
        }
    return scenarios
