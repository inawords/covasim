import covasim as cv
import os.path

from src.interventions import *
from src.parameters import *
from src.scenarios import *

pop_size = 400000
pop_type = 'synthpops'
start_date = '2020-03-01'
end_date = '2020-07-12'

# Sim options
basepars = dict(
    pop_size=pop_size,
    pop_type=pop_type,
    verbose=True,
    pop_infected=25,
    start_day=start_date,
    end_day=end_date,
    interventions=interventions
)


def create_vorarlberg_sim(popfile=pop_file):
    sim = cv.Sim(basepars)
    if not os.path.isfile(popfile):
        cv.make_people(sim,
                       synthpops_pars,
                       popfile=popfile)
    return cv.Sim(basepars, popfile=popfile, load_pop=True, datafile=real_data_csv)
