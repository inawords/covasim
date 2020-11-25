from src.scenarios.work_vs_community.utils import *

"""
Example Usage:

args = HOME_OFFICE['parameter_influence'][0]
scenario = cv.Scenarios(
        sim=sim,
        basepars=basepars,
        metapars=scenario_metapars,
        scenarios=work_community_scenario(**args))
"""


def work_community_scenario(parameter='edges', layer='c', start_date=INTERVENTION_START[0]):
    # combination: 'beta' | 'edges' | 'both' -> parameter to be varied
    # layer: 'c' | 'w' | 'cw'
    # start_date -> day when new intervention starts
    return create_scenario_edges_beta(
        label=LABELS[layer],
        beta=COMBINATIONS[parameter]['beta'],
        edges=COMBINATIONS[parameter]['edges'],
        intervention_start=start_date,
        intervention_func=INTERVENTION_FUNC[layer])


""" SCENARIO PARAMETERS FOR WORK_COMMUNITY_SCENARIO """

HOME_OFFICE = dict(
    parameter_influence=[
        dict(layer='w', start_date=INTERVENTION_START[0], parameter='both'),  # winner
        dict(layer='w', start_date=INTERVENTION_START[0], parameter='beta'),
        dict(layer='w', start_date=INTERVENTION_START[0], parameter='edges'),
    ],
    time_influence=[
        dict(layer='w', start_date=INTERVENTION_START[0], parameter='both'),
        dict(layer='w', start_date=INTERVENTION_START[1], parameter='both'),
        dict(layer='w', start_date=INTERVENTION_START[2], parameter='both'),
    ]
)

SOCIAL_DISTANCING = dict(
    parameter_influence=[
        dict(layer='c', start_date=INTERVENTION_START[0], parameter='both'),
        dict(layer='c', start_date=INTERVENTION_START[0], parameter='beta'),
        dict(layer='c', start_date=INTERVENTION_START[0], parameter='edges'),  # winner
    ],
    time_influence=[
        dict(layer='c', start_date=INTERVENTION_START[0], parameter='edges'),
        dict(layer='c', start_date=INTERVENTION_START[1], parameter='edges'),
        dict(layer='c', start_date=INTERVENTION_START[2], parameter='edges'),
    ]
)

MIXED = dict(
    time_influence=[
        dict(layer='cw', start_date=INTERVENTION_START[0], parameter='both'),
        dict(layer='cw', start_date=INTERVENTION_START[1], parameter='both'),
        dict(layer='cw', start_date=INTERVENTION_START[2], parameter='both'),
    ]
)
