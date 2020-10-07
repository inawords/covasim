import covasim as cv
import os.path

pop_size = 400000
pop_type = 'synthpops'
start_date  = '2020-03-01'
end_date    = '2020-07-12'

testStartDay_1 = 5
testStartDay_2 = 16
nrOfDailyTests_1 = 10
nrOfDailyTests_2 = 300


# Sim options
basepars = dict(
    pop_size      = pop_size,
    pop_infected  = 25,
    verbose       = True,
    start_day=start_date,
    end_day        = end_date,
    interventions = [
        #cv.test_prob(start_day=testStartDay, symp_prob=0.8, asymp_prob=0.05, test_delay=1.0),
        cv.test_num(start_day=testStartDay_1, end_day=testStartDay_2 - 1, daily_tests=nrOfDailyTests_1, test_delay=1),
        cv.test_num(start_day=testStartDay_2, daily_tests=nrOfDailyTests_2, test_delay=1),
        cv.change_beta(days=10, changes=0.95),             # travel restrictions
        cv.change_beta(days=13, changes=0, layers='s'),    # lockdown
        cv.change_beta(days=13, changes=0.4, layers='w'),  # lockdown
        cv.change_beta(days=13, changes=0.2, layers='c'),  # lockdown
        cv.change_beta(days=13, changes=1, layers='h'),    # lockdown
    ]
)


# Scenario metaparameters
metapars = dict(
    n_runs    = 3, # Number of parallel runs; change to 3 for quick, 11 for real
    noise     = 0.1, # Use noise, optionally
    noisepar  = 'beta',
    rand_seed = 1,
    quantiles = {'low':0.1, 'high':0.9},
)

# Define the actual scenarios
scenarios = {'baseline': {
              'name':'Baseline',
              'pars': {
                  'interventions': [
                      #cv.test_prob(start_day=start_date, symp_prob=0.2, asymp_prob=0.05, test_delay=1.0, do_plot=True),
                      #cv.test_num(daily_tests=nrOfDailyTests, sensitivity=0.9, start_day=testStartDay, test_delay=1.0),
                      cv.change_beta(days=10, changes=0.95), #travel restrictions
                      cv.change_beta(days=13, changes=0.2),  #lockdown
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


def create_vorarlberg_sim(popfile="../data/population_400000.pop"):
    sim = cv.Sim(basepars)
    if not os.path.isfile(popfile):
        cv.make_people(sim,
                       save_pop=True,
                       popfile=popfile,
                       generate=True,
                       location='Vorarlberg',
                       state_location='Vorarlberg',
                       country_location='Austria',
                       sheet_name='Austria',
                       with_school_types=False,
                       school_mixing_type='random',
                       average_class_size=20,
                       inter_grade_mixing=0.1,
                       average_student_teacher_ratio=16,
                       average_teacher_teacher_degree=3,
                       teacher_age_min=25,
                       teacher_age_max=70,
                       average_student_all_staff_ratio=15,
                       average_additional_staff_degree=20,
                       staff_age_min=20,
                       staff_age_max=70,
                       verbose=False)
    return cv.Sim(basepars, popfile=popfile, load_pop=True, datafile="../data/Vorarlberg_ Austria.csv")


def plot_csv_data():
    sim = cv.Sim(datafile="../data/Vorarlberg_ Austria.csv")
    sim.run()
    sim.plot()


def vorarlberg_scenario():

    sim = create_vorarlberg_sim()
    scenario = cv.Scenarios(sim=sim, basepars=basepars, metapars=metapars, scenarios=scenarios)
    scenario.run(verbose=True)
    scenario.plot(do_show=True)


def vorarlberg_sim():
    sim = create_vorarlberg_sim()
    sim.initialize()
    sim.run(verbose=True)
    sim.plot()

    # cv.plotting.plotly_sim(sim, do_show=True)
    # cv.plotting.plotly_people(sim, do_show=True)

    print('simulation generated')


def main():
    # vorarlberg_scenario()
    vorarlberg_sim()


if __name__ == '__main__':
    main()
