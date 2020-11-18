import copy

from src.utils.date import *
from src.data.testing import *

# starting days of interventions
lockdown = '2020-03-16'
open_stores_with_mns = '2020-05-01'
reduced_mns = '2020-06-15'
holiday_start = '2020-08-01'
school_opening = '2020-9-14'

# our own interventions
sim_intervention = '2020-11-01'
sim_intervention_october = '2020-10-01'
sim_intervention_after_school = '2020-9-15'

"""
use `clip_edges` to simulate reduced contact between people
use `change_beta` to simulate reduced transmission due to MNS, more hygiene, etc
real testing data is used in this interventions

!! important: interventions will be applied in order of definition !! 
--> result will be different if for example testing is applied before clipping edges or vice versa
"""

""" TESTING """
test_delay = 3
testing_real = [  # because `daily_tests` is an array, this doesn't need to be a sequence or have end_days
    cv.test_num(start_day='2020-03-01', test_delay=test_delay, daily_tests=daily_tests_march),
    cv.test_num(start_day='2020-04-01', test_delay=test_delay, daily_tests=daily_tests_april),
    cv.test_num(start_day='2020-05-01', test_delay=test_delay, daily_tests=daily_tests_may),
    cv.test_num(start_day='2020-06-01', test_delay=test_delay, daily_tests=daily_tests_june),
    cv.test_num(start_day='2020-07-01', test_delay=test_delay, daily_tests=daily_tests_july),
    cv.test_num(start_day='2020-08-01', test_delay=test_delay, daily_tests=daily_tests_august),
    cv.test_num(start_day='2020-09-01', test_delay=test_delay, daily_tests=daily_tests_september),
    cv.test_num(start_day='2020-10-01', test_delay=test_delay, daily_tests=daily_tests_october),
]
testing_sim = [cv.sequence(
    days=[
        '2020-11-01',
        '2020-12-01',
        '2021-01-01',
        '2021-02-01',
        '2021-03-01',
        '2021-04-01',
    ],
    interventions=[
        cv.test_num(test_delay=test_delay, daily_tests=daily_tests_november),
        cv.test_num(test_delay=test_delay, daily_tests=daily_tests_december),
        cv.test_num(test_delay=test_delay, daily_tests=daily_tests_january),
        cv.test_num(test_delay=test_delay, daily_tests=daily_tests_february),
        cv.test_num(test_delay=test_delay, daily_tests=daily_tests_march21),
        cv.test_num(test_delay=test_delay, daily_tests=daily_tests_april21),
    ])]


def create_sequence_intervention(data):
    return [cv.sequence(
        days=data['days'],
        interventions=data['interventions']
    )]


def create_edges_beta(data):
    return [
        cv.clip_edges(
            data['days'],
            data['edges'],
            layers=data['layers']),
        cv.change_beta(
            data['days'],
            data['beta'],
            layers=data['layers']),
    ]


def add_edges_beta(data, date, edges, beta):
    data_copy = copy.deepcopy(data)
    data_copy['days'].append(date)
    data_copy['edges'].append(edges)
    data_copy['beta'].append(beta)
    return data_copy


""" TRACING """
tracing_data = dict(
    days=[
        '2020-03-01',
        lockdown,
        school_opening
    ],
    interventions=[
        cv.contact_tracing(  # start pandemic
            trace_probs={'s': 0.1, 'h': 0.4, 'w': 0.1, 'c': 0.05},
            trace_time={'s': 2.0, 'h': 1.0, 'w': 2.0, 'c': 3.0}),
        cv.contact_tracing(  # lockdown
            trace_probs={'s': 0.2, 'h': 0.7, 'w': 0.2, 'c': 0.1},
            trace_time={'s': 1.0, 'h': 1.0, 'w': 2.0, 'c': 3.0}),
        cv.contact_tracing(  # school opening
            trace_probs={'s': 0.4, 'w': 0.4},
            trace_time={'s': 1.0, 'w': 2.0}),
    ]
)
tracing = create_sequence_intervention(tracing_data)

""" EDGES & BETA """
school_data = dict(
    days=[lockdown, school_opening],
    edges=[0.2, 0.78],
    beta=[0.8, 0.8],
    layers='s'
)
beta_edges_school = create_edges_beta(school_data)

work_data = dict(
    days=[lockdown, open_stores_with_mns, reduced_mns, school_opening],
    edges=[0.5, 0.6, 0.7, 0.85],
    beta=[0.5, 0.5, 0.7, 0.8],
    layers='w'
)
beta_edges_work = create_edges_beta(work_data)

community_data = dict(
    days=[lockdown, open_stores_with_mns, reduced_mns, holiday_start],
    edges=[0.2, 0.6, 0.7, 0.82],
    beta=[0.8, 0.4, 0.72, 0.82],
    layers='c'
)
beta_edges_community = create_edges_beta(community_data)


def create_beta_edges_best_case():
    school = create_edges_beta(add_edges_beta(school_data, sim_intervention, 0, 0))
    work = create_edges_beta(add_edges_beta(work_data, sim_intervention, 0, 0))
    community = create_edges_beta(add_edges_beta(community_data, sim_intervention, 0, 0))
    return school + work + community


def create_interventions_mixed(beta, edges, intervention_start):
    return (
            testing_real + testing_sim +
            beta_edges_school +
            create_edges_beta(add_edges_beta(work_data, intervention_start, edges, beta)) +
            create_edges_beta(add_edges_beta(community_data, intervention_start, edges, beta)) +
            tracing)


def create_interventions_home_office(beta, edges, intervention_start):
    return (
            testing_real + testing_sim +
            beta_edges_school +
            create_edges_beta(add_edges_beta(work_data, intervention_start, edges, beta)) +
            beta_edges_community +
            tracing)


def create_interventions_restricted_community(beta, edges, intervention_start):
    return (
            testing_real + testing_sim +
            beta_edges_school + beta_edges_work +
            create_edges_beta(add_edges_beta(community_data, intervention_start, edges, beta)) +
            tracing)


interventions = (
        testing_real +
        beta_edges_school + beta_edges_work + beta_edges_community +
        tracing)

interventions_worst_case = (
        testing_real + testing_sim +
        beta_edges_school + beta_edges_work + beta_edges_community +
        tracing)

interventions_best_case = (
        testing_real + testing_sim +
        create_beta_edges_best_case() +
        tracing)
