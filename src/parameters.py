import os
import datetime

data_base_path = "../data/vorarlberg"
"""data file created with data scraper, see also file in 'data/epi_data/corona-data"""
real_data_csv = os.path.join(data_base_path, "Vorarlberg_ Austria.csv")
"""file containing population created with synthpops"""
pop_file = os.path.join(data_base_path, "population.pop")
"""file to backup interventions"""
date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
intervention_file = os.path.join(data_base_path, "backups/interventions_" + date + '.csv')

pop_size = 388711
pop_type = 'synthpops'
pop_infected = 90
start_date = '2020-03-01'
end_date = '2020-10-31'


"""Scenario metaparameters"""
scenario_metapars = dict(
    n_runs=11,  # Number of parallel runs; change to 3 for quick, 11 for real
    noise=0.1,  # Use noise, optionally
    noisepar='beta',
    rand_seed=1,
    quantiles={'low': 0.4, 'high': 0.6},
)


"""parameters for synthpops to generate population"""
synthpops_pars = dict(
    save_pop=True,
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
    school_enrollment_counts_available=True,
    use_default=False,
    verbose=False
)
