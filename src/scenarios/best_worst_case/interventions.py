from src.interventions import *

INT_WORST_CASE = create_interventions()

INT_BEST_CASE = create_interventions(
    school=create_edges_beta(add_edges_beta(school_data, sim_intervention, 0, 0)),
    work=create_edges_beta(add_edges_beta(work_data, sim_intervention, 0, 0)),
    community=create_edges_beta(add_edges_beta(community_data, sim_intervention, 0, 0)))
