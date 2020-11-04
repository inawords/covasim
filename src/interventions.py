import covasim as cv
import numpy as np
from src.utils.date import *
from src.parameters import *
from src.data.testing import *

daily_tests_until_july = daily_tests_march + daily_tests_april + daily_tests_may + daily_tests_june + daily_tests_july

# starting days of interventions
days = calc_days(start_date)
lockdown = days('2020-03-16')
open_stores_with_mns = days('2020-05-01')
reduced_mns = days('2020-06-15')
school_opening = days('2020-9-14')

# our own interventions
home_office = days('2020-11-01')
contact_tracing = days('2020-11-01')

"""
use `clip_edges` to simulate reduced contact between people
use `change_beta` to simulate reduced transmission due to MNS, more hygiene, etc
real testing data is used in this interventions

!! important: interventions will be applied in order of definition !! 
--> result will be different if for example testing is applied before clipping edges or vice versa
"""
interventions = [
    # Testing
    cv.test_num(start_day=1, daily_tests=daily_tests_until_july, test_delay=3),
    cv.test_num(start_day=days('2020-08-01'), daily_tests=daily_tests_august, test_delay=2),
    cv.test_num(start_day=days('2020-09-01'), daily_tests=daily_tests_september, test_delay=3),
    cv.test_num(start_day=days('2020-10-01'), daily_tests=daily_tests_october, test_delay=4),
    cv.test_num(start_day=days('2020-11-01'), daily_tests=daily_tests_november, test_delay=4, symp_test=750),
    cv.test_num(start_day=days('2020-12-01'), daily_tests=daily_tests_december, test_delay=4, symp_test=750),
    cv.test_num(start_day=days('2021-01-01'), daily_tests=daily_tests_january, test_delay=4, symp_test=750),
    cv.test_num(start_day=days('2021-02-01'), daily_tests=daily_tests_february, test_delay=4, symp_test=750),
    cv.test_num(start_day=days('2021-03-01'), daily_tests=daily_tests_march21, test_delay=4, symp_test=750),
    cv.test_num(start_day=days('2021-04-01'), daily_tests=daily_tests_april21, test_delay=4, symp_test=750),

    # Je mehr Leute getestet werden umso mehr asymptotische Personen werden gefunden und die Ausbreitung kann
    # eingeschränkt werden

    # school
    cv.clip_edges(
        [lockdown,  school_opening],
        [0.2,       0.8],
        layers='s'),
    cv.change_beta(
        [lockdown,  school_opening],
        [0.8,       0.8],
        layers='s'),
    # work
    cv.clip_edges(
        [lockdown,  open_stores_with_mns,   reduced_mns, school_opening],
        [0.5,       0.6,                    0.7,         0.9],
        layers='w'),
    cv.change_beta(
        [lockdown,  open_stores_with_mns,   reduced_mns,    school_opening],
        [0.5,       0.5,                    0.7,            0.85],
        layers='w'),
    # community
    cv.clip_edges(
        [lockdown,  open_stores_with_mns,   reduced_mns,    school_opening],
        [0.2,       0.6,                    0.7,            0.9],
        layers='c'),
    cv.change_beta(
        [lockdown,  open_stores_with_mns,   reduced_mns,    school_opening],
        [0.8,       0.4,                    0.72,            0.9],
        layers='c'),
    # Tracing
    cv.contact_tracing(start_day=days('2020-03-01'),
                       trace_probs={'s': 0.1, 'h': 0.4, 'w': 0.1, 'c': 0.05},
                       trace_time={'s': 2.0, 'h': 1.0, 'w': 2.0, 'c': 3.0}),
    cv.contact_tracing(start_day=lockdown,
                       trace_probs={'s': 0.2, 'h': 0.7, 'w': 0.2, 'c': 0.1},
                       trace_time={'s': 1.0, 'h': 1.0, 'w': 2.0, 'c': 3.0}),
    cv.contact_tracing(start_day=school_opening,
                       trace_probs={'s': 0.4, 'w': 0.4},
                       trace_time={'s': 1.0, 'w': 2.0}),
]
