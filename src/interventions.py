import covasim as cv
import numpy as np
from src.utils.date import *
from src.parameters import *
from src.data.testing import *

# daily test data until 2020-10-19
daily_tests_until_july = daily_tests_march + daily_tests_april + daily_tests_may + daily_tests_june + daily_tests_july
daily_tests_since_august = daily_tests_august + daily_tests_september + daily_tests_october

# starting days of interventions
days = calc_days(start_date)
lockdown = days('2020-03-16')
open_stores_with_mns = days('2020-05-01')
reduced_mns = days('2020-06-15')
school_opening = days('2020-9-14')

"""
use `clip_edges` to simulate reduced contact between people
use `change_beta` to simulate reduced transmission due to MNS, more hygiene, etc
real testing data is used in this interventsions
"""
interventions = [
    # cv.contact_tracing(start_day=4, trace_probs=0.5, trace_time=1.0),

    # Testing
    cv.test_num(start_day=1, daily_tests=daily_tests_until_july, test_delay=3, symp_test=600),
    cv.test_num(start_day=days('2020-08-01'), daily_tests=daily_tests_since_august, test_delay=3, symp_test=750),
    cv.test_num(start_day=days('2020-10-20'), daily_tests=np.mean(daily_tests_october), test_delay=3, symp_test=750),

    # school
    cv.clip_edges(
        [lockdown,  school_opening],
        [0.01,      0.8],
        layers='s'),
    cv.change_beta(
        [lockdown,  school_opening],
        [0,         0.8],  # kleine Betreuungsgruppen (zB Kindergarten) -> 0 ist zu krass
        layers='s'),

    # work
    cv.clip_edges(
        [lockdown,  open_stores_with_mns,   reduced_mns],
        [0.55,      0.6,                    0.7],
        layers='w'),
    cv.change_beta(
        [lockdown,  open_stores_with_mns,   reduced_mns],
        [0.8,       0.7,                    0.8],
        layers='w'),

    # community
    cv.clip_edges(
        [lockdown,  open_stores_with_mns,   reduced_mns],
        [0.2,       0.8,                    0.8],
        layers='c'),
    cv.change_beta(
        [lockdown,  open_stores_with_mns,   reduced_mns],
        [0.8,       0.4,                    0.6],
        layers='c'),
]

"""
use `clip_edges` to simulate reduced contact between people
use `change_beta` to simulate reduced transmission due to MNS, more hygiene, etc
"""
interventions_old = [
    cv.test_num(start_day=1, daily_tests=daily_tests_march, test_delay=3, symp_test=400),  # März
    cv.test_num(start_day=32, end_day=90, daily_tests=300, test_delay=3, symp_test=400),  # April-Mai
    cv.test_num(start_day=91, end_day=120, daily_tests=350, test_delay=2, symp_test=400),  # Juni
    cv.test_num(start_day=121, end_day=150, daily_tests=500, test_delay=2, symp_test=400),  # Juli
    cv.test_num(start_day=151, daily_tests=900, test_delay=2, symp_test=400),  # ab August

    cv.clip_edges([16, 190], [0.01, 0.8], layers='s'),
    # lockdown school -> Schulschließung, Schulöffnung ohne Uni, FHV (0.8) lol Johannes
    cv.clip_edges([16, 60, 105], [0.55, 0.6, 0.7], layers='w'),
    # lockdown work -> Geschäfte schließen, Kurzarbeit, HomeOffice wenn möglich
    cv.clip_edges([16, 60, 105], [0.2, 0.8, 0.85], layers='c'),
    # lockdown community -> betreten öffentlicher Bereich verboten

    # school
    cv.change_beta(days=16, changes=0, layers='s'),  # lockdown school
    cv.change_beta(days=190, changes=0.9, layers='s'),  # school opening with additional measures (MSN, ...)

    # 16. march -> lockdown
    cv.change_beta(days=16, changes=0.8, layers='w'),
    # lockdown work -> Geschäfte schließen, Kurzarbeit, HomeOffice wenn möglich
    cv.change_beta(days=16, changes=0.8, layers='c'),  # lockdown community -> betreten öffentlicher Bereich verboten

    # 1. mai -> Öffnung Geschäfte mit MNS
    cv.change_beta(days=60, changes=0.2, layers='c'),
    cv.change_beta(days=60, changes=0.8, layers='w'),

    # 15. juni -> Großteils Entfall MNS (15.Juni)
    cv.change_beta(days=105, changes=0.7, layers='c'),
    cv.change_beta(days=105, changes=0.85, layers='w'),
]
