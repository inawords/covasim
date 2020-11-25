from src.interventions import *
from src.scenarios.work_vs_community import utils


def create_interventions_mixed(beta, edges, intervention_start):
    """
    Args:
        beta: for work layer
        edges: for community and work layer
        intervention_start: for community and work layer
    """
    return create_interventions(
        work=create_edges_beta(add_edges_beta(work_data, intervention_start, edges, beta)),
        community=
        create_edges_beta(add_edges_beta(community_data, intervention_start, edges, utils.PARAMETER_CONST[0])),
    )


def create_interventions_home_office(beta, edges, intervention_start):
    return create_interventions(
        work=create_edges_beta(add_edges_beta(work_data, intervention_start, edges, beta)),
    )


def create_interventions_social_distancing(beta, edges, intervention_start):
    return create_interventions(
        community=create_edges_beta(add_edges_beta(community_data, intervention_start, edges, beta))
    )
