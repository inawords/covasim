import synthpops as sp
import covasim as cova

n = 50000
country_location = 'usa'
state_location = 'Washington'
location = 'seattle_metro'
sheet_name = 'United States of America'

options_args = {}
options_args['use_microstructure'] = True
options_args['use_industry_code'] = False
options_args['use_long_term_care_facilities'] = False
options_args['use_two_group_reduction'] = True
options_args['with_school_types'] = False
options_args['with_non_teaching_staff'] = False

network_distr_args = {}
network_distr_args['Npop'] = int(n)
network_distr_args['average_LTCF_degree'] = 20
network_distr_args['average_class_size'] = 20
network_distr_args['average_student_teacher_ratio'] = 20
network_distr_args['average_teacher_teacher_degree'] = 3
network_distr_args['inter_grade_mixing'] = 0.1
network_distr_args['average_student_all_staff_ratio'] = 15
network_distr_args['average_additional_staff_degree'] = 20
network_distr_args['school_mixing_type'] = 'random'

with_school_types = False
school_mixing_type = 'random'
average_class_size = 20
inter_grade_mixing = 0.1
average_student_teacher_ratio = 20
average_teacher_teacher_degree = 3
teacher_age_min = 25
teacher_age_max = 75
average_student_all_staff_ratio = 15
average_additional_staff_degree = 20
staff_age_min = 20
staff_age_max = 75

### Create Files for generate=False (!!! write=True !!!) ###
### Executed by sp.make_population if generate=True ###
# population = sp.generate_synthetic_population(
#     n, sp.datadir, location=location, state_location=state_location,
#     country_location=country_location, sheet_name=sheet_name,
#     with_school_types=with_school_types,
#     school_mixing_type=school_mixing_type,
#     average_class_size=average_class_size,
#     inter_grade_mixing=inter_grade_mixing,
#     average_student_teacher_ratio=average_student_teacher_ratio,
#     average_teacher_teacher_degree=average_teacher_teacher_degree,
#     teacher_age_min=teacher_age_min, teacher_age_max=teacher_age_max,
#     average_student_all_staff_ratio=average_student_all_staff_ratio,
#     average_additional_staff_degree=average_additional_staff_degree,
#     staff_age_min=staff_age_min, staff_age_max=staff_age_max,
#     return_popdict=True,
#     write=True,
# )

### Executed by sp.make_population if generate=False ###
# population = sp.make_contacts(location=location, state_location=state_location,
#                               country_location=country_location, sheet_name=sheet_name,
#                               options_args=options_args,
#                               network_distr_args=network_distr_args)


sp.make_population(generate=False)


pop_size = 50000
pop_type = 'synthpops'

pars = {
    'pop_size': pop_size,
    'pop_type': pop_type,
}
sim = cova.Sim(pars=pars)
# cova.make_synthpop(sim, generate=False)
popdict = cova.make_people(sim, generate=False)
sim = cova.Sim(pars, popfile=popdict, load_pop=True)

print('Done!')