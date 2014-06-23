import glob
import datetime
import string

import pandas as pd

current_year = datetime.datetime.today().year

def age_binner(age):
    if age < 5:
        return "04 and under"
    elif 5 <= age <= 9:
        return "05 to 09 years" 
    elif 10 <= age <= 14:
        return "10 to 14 years" 
    elif 15 <= age <= 19:
        return "15 to 19 years" 
    elif 20 <= age <= 24:
        return "20 to 24 years" 
    elif 25 <= age <= 29:
        return "25 to 29 years" 
    elif 30 <= age <= 34:
        return "30 to 34 years" 
    elif 35 <= age <= 39:
        return "35 to 39 years" 
    elif 40 <= age <= 44:
        return "40 to 44 years" 
    elif 45 <= age <= 49:
        return "45 to 49 years" 
    elif 50 <= age <= 54:
        return "50 to 54 years" 
    elif 55 <= age <= 59:
        return "55 to 59 years" 
    elif 60 <= age <= 64:
        return "60 to 64 years" 
    elif 65 <= age <= 69:
        return "65 to 69 years" 
    elif 70 <= age <= 74:
        return "70 to 74 years" 
    elif 75 <= age <=79:
        return "75 to 79 years" 
    elif 80 <= age <=84:
        return "80 to 84 years" 
    else:
        return "85 years and over"

def get_data():
    d = {}
    columns = ['state', 'sex', 'year', 'name', 'occurences']
    for file in glob.glob('namesbystate/*.TXT'):
        print file
        state = file.replace(".TXT","").replace('namesbystate/','')
        df = pd.read_csv(file, names=columns, header=None)
        df['current_age'] = current_year - df['year']
        df['age_bin'] = df['current_age'].apply(age_binner)
        df['name'] = df['name'].apply(string.lower)
        d[state] = df[['age_bin', 'name', 'sex','occurrences']].groupby(['age_bin', 'name', 'sex']).sum()

    by_state = pd.Panel.from_dict(d)
    total = by_state.minor_xs('occurrences').sum(1)
    return by_state, total


class DiscreteDistribution(object):

    def __init__(self, prior):
        self.posterior = prior
        self._prior = prior

    def update(self, p):
        #P(age_bin) = P(age_bin | 'Sara')*P('Sara' | Alive)*P(Alive) + .. 
        # boils down to the below formula.
        self.posterior = p.fillna(0) + self.posterior
        return

def normalize_vector(v):
    return v/v.sum()

def name_distribution(name, data, prior):
    try:
        return normalize_vector(data.ix[name,:, :]['occurrences'].sum(level='age_bin').reindex(prior.index))
    except KeyError:
        return prior


