import os.path
from src.scenarios import *


# Sim options
basepars = dict(
    pop_size=pop_size,
    pop_type=pop_type,
    verbose=True,
)


def create_vorarlberg_sim(popfile=pop_file, interventions=None,
                          start_day=start_date, end_day=end_date, pop_infected=pop_infected):
    sim = cv.Sim(basepars)
    if not os.path.isfile(popfile):
        cv.make_people(sim,
                       synthpops_pars,
                       popfile=popfile)
    return cv.Sim(
        dict(
            basepars,
            interventions=interventions,
            start_day=start_day,
            end_day=end_day,
            pop_infected=pop_infected
        ),
        popfile=popfile,
        load_pop=True,
        datafile=real_data_csv)
