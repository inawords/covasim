from src.utils.date import *
from src.data.testing import *

daily_tests_until_july = daily_tests_march + daily_tests_april + daily_tests_may + daily_tests_june + daily_tests_july

# starting days of interventions
lockdown = '2020-03-16'
open_stores_with_mns = '2020-05-01'
reduced_mns = '2020-06-15'
holiday_start = '2020-08-01'
school_opening = '2020-9-14'

# our own interventions
home_office = '2020-11-01'
contact_tracing = '2020-11-01'

"""
use `clip_edges` to simulate reduced contact between people
use `change_beta` to simulate reduced transmission due to MNS, more hygiene, etc
real testing data is used in this interventions

!! important: interventions will be applied in order of definition !! 
--> result will be different if for example testing is applied before clipping edges or vice versa
"""
test_delay = 3
testing_real = [  # because `daily_tests` is an array, this doesn't need to be a sequence or have end_days
    cv.test_num(start_day='2020-03-01', test_delay=test_delay, daily_tests=daily_tests_until_july),
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

tracing = [cv.sequence(
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
    ])]

beta_edges = [
    # school
    cv.clip_edges(
        [lockdown, school_opening],
        [0.2, 0.78],
        layers='s'),
    cv.change_beta(
        [lockdown, school_opening],
        [0.8, 0.8],
        layers='s'),
    # work
    cv.clip_edges(
        [lockdown, open_stores_with_mns, reduced_mns, school_opening],
        [0.5, 0.6, 0.7, 0.85],
        layers='w'),
    cv.change_beta(
        [lockdown, open_stores_with_mns, reduced_mns, school_opening],
        [0.5, 0.5, 0.7, 0.8],
        layers='w'),
    # community
    cv.clip_edges(
        [lockdown, open_stores_with_mns, reduced_mns, holiday_start],
        [0.2, 0.6, 0.7, 0.82],
        layers='c'),
    cv.change_beta(
        [lockdown, open_stores_with_mns, reduced_mns, holiday_start],
        [0.8, 0.4, 0.72, 0.82],
        layers='c'),
]

beta_edges_best_case = [
    # school
    cv.clip_edges(
        [lockdown, school_opening, home_office],
        [0.2, 0.78, 0],
        layers='s'),
    cv.change_beta(
        [lockdown, school_opening, home_office],
        [0.8, 0.8, 0],
        layers='s'),
    # work
    cv.clip_edges(
        [lockdown, open_stores_with_mns, reduced_mns, school_opening, home_office],
        [0.5, 0.6, 0.7, 0.85, 0],
        layers='w'),
    cv.change_beta(
        [lockdown, open_stores_with_mns, reduced_mns, school_opening, home_office],
        [0.5, 0.5, 0.7, 0.8, 0],
        layers='w'),
    # community
    cv.clip_edges(
        [lockdown, open_stores_with_mns, reduced_mns, holiday_start, home_office],
        [0.2, 0.6, 0.7, 0.82, 0],
        layers='c'),
    cv.change_beta(
        [lockdown, open_stores_with_mns, reduced_mns, holiday_start, home_office],
        [0.8, 0.4, 0.72, 0.82, 0],
        layers='c'),
]

beta_edges_home_office_school = [
    # school
    cv.clip_edges(
        [lockdown, school_opening],
        [0.2, 0.78],
        layers='s'),
    cv.change_beta(
        [lockdown, school_opening],
        [0.8, 0.8],
        layers='s'),
]

beta_edges_work = [
    cv.clip_edges(
        [lockdown, open_stores_with_mns, reduced_mns, school_opening],
        [0.5, 0.6, 0.7, 0.85],
        layers='w'),
    cv.change_beta(
        [lockdown, open_stores_with_mns, reduced_mns, school_opening],
        [0.5, 0.5, 0.7, 0.8],
        layers='w'),
]

beta_edges_home_office_community = [
    # community
    cv.clip_edges(
        [lockdown, open_stores_with_mns, reduced_mns, holiday_start],
        [0.2, 0.6, 0.7, 0.82],
        layers='c'),
    cv.change_beta(
        [lockdown, open_stores_with_mns, reduced_mns, holiday_start],
        [0.8, 0.4, 0.72, 0.82],
        layers='c'),
]

beta_edges_home_office_work = [
    # work
    cv.clip_edges(
        [lockdown, open_stores_with_mns, reduced_mns, school_opening, home_office],
        [0.5, 0.6, 0.7, 0.85, 0.5],
        layers='w'),
    cv.change_beta(
        [lockdown, open_stores_with_mns, reduced_mns, school_opening, home_office],
        [0.5, 0.5, 0.7, 0.8, 0.5],
        layers='w'),
]


def beta_edges_home_office(beta_work, clip_work):
    return [
        # work
        cv.clip_edges(
            [lockdown, open_stores_with_mns, reduced_mns, school_opening, home_office],
            [0.5, 0.6, 0.7, 0.85, clip_work],
            layers='w'),
        cv.change_beta(
            [lockdown, open_stores_with_mns, reduced_mns, school_opening, home_office],
            [0.5, 0.5, 0.7, 0.8, beta_work],
            layers='w'),
    ]


def interventions_home_office(beta, edges):
    return (testing_real + testing_sim + (
            beta_edges_home_office_school + beta_edges_home_office_community + beta_edges_home_office(beta, edges))
            + tracing)


def calc_beta_edges_community(beta, edges):
    return [
        # community
        cv.clip_edges(
            [lockdown, open_stores_with_mns, reduced_mns, holiday_start, home_office],
            [0.2, 0.6, 0.7, 0.82, edges],
            layers='c'),
        cv.change_beta(
            [lockdown, open_stores_with_mns, reduced_mns, holiday_start, home_office],
            [0.8, 0.4, 0.72, 0.82, beta],
            layers='c'),
    ]


def interventions_community_adapted(beta, edges):
    return (testing_real + testing_sim + (
            beta_edges_home_office_school + beta_edges_work + calc_beta_edges_community(beta, edges))
            + tracing)


interventions = testing_real + beta_edges + tracing
interventions_worst_case = testing_real + testing_sim + beta_edges + tracing
interventions_best_case = testing_real + testing_sim + beta_edges_best_case + tracing
#interventions_home_office = testing_real + testing_sim + (beta_edges_home_office_school +
#                            beta_edges_home_office_community + beta_edges_home_office_work) + tracing
