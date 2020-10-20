import covasim as cv

# Values seems to be correct as the simulation summary outputs 35510 cum_tests, when the online data outputs 35482
testStartDay_1 = 5
testStartDay_2 = 16
nrOfDailyTests_1 = 10
nrOfDailyTests_2 = 300

interventions = [
        # cv.test_prob(start_day=testStartDay, symp_prob=0.8, asymp_prob=0.05, test_delay=1.0),
        cv.test_num(start_day=testStartDay_1, end_day=testStartDay_2 - 1, daily_tests=nrOfDailyTests_1, test_delay=1),
        cv.test_num(start_day=testStartDay_2, daily_tests=nrOfDailyTests_2, test_delay=1),
        cv.change_beta(days=10, changes=0.95),  # travel restrictions
        cv.change_beta(days=13, changes=0, layers='s'),  # lockdown
        cv.change_beta(days=13, changes=0.2, layers='w'),  # lockdown
        cv.change_beta(days=13, changes=0.2, layers='c'),  # lockdown
        cv.change_beta(days=13, changes=1, layers='h'),  # lockdown
    ]