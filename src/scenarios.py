import covasim as cv

# Define the actual scenarios
scenarios = {'baseline': {
    'name': 'Baseline',
    'pars': {
        'interventions': [
            # cv.test_prob(start_day=start_date, symp_prob=0.2, asymp_prob=0.05, test_delay=1.0, do_plot=True),
            # cv.test_num(daily_tests=nrOfDailyTests, sensitivity=0.9, start_day=testStartDay, test_delay=1.0),
            cv.change_beta(days=10, changes=0.95),  # travel restrictions
            cv.change_beta(days=13, changes=0.2),  # lockdown
        ]
    }
},
    # 'distance': {
    #   'name':'Social distancing',
    #   'pars': {
    #       'interventions': cv.change_beta(days=start_day, changes=0.7)
    #       }
    #   },
    # 'ttq': {
    #   'name':'Test-trace-quarantine',
    #   'pars': {
    #       'interventions': [
    #
    #             # cv.contact_tracing(start_day=start_day, trace_probs=0.8, trace_time=1.0),
    #         ]
    #       }
    #   },
}
