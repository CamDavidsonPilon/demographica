import pandas as pd
from string import capwords

from os.path import dirname, abspath

PATH = '%s/' % (dirname(abspath(__file__)),)

NAME_DISTRIBUTIONS = pd.read_csv(PATH + 'datasets/NameDistributions.csv', index_col=[0,1])
VALID_NAMES = set(NAME_DISTRIBUTIONS.index.levels[0])
SEX_DISTRIBUTIONS = pd.read_csv(PATH + 'datasets/SexDistributions.csv', index_col=[0,1])
US_AGE = pd.read_csv(PATH + 'datasets/US Age Dist.csv', index_col=[0])


def age_calculator(name_frequencies):
    prob = 0.
    for name, freq in name_frequencies.iteritems():
        try:
            prob += NAME_DISTRIBUTIONS.ix[name]*freq
        except:
            pass
    return prob

def sex_calculator(name_frequencies):
    prob = 0.
    for name, freq in name_frequencies.iteritems():
        try:
            prob += SEX_DISTRIBUTIONS.ix[name]*freq
        except KeyError as e:
            pass
    return prob

def compute_name_frequencies(names):
    """
    Parameters:
        names: a list or iterable of first names
    """

    data = pd.Series(names).map(capwords)
    data = data.ix[data.map( lambda r: r in VALID_NAMES )]
    data_normalized = data.groupby(data.values).count()/data.shape[0]
    return data_normalized

def pplot(age_distribution, label='Inferred age distribution', plot_US_age=True):
    try:
        from matplotlib import pyplot as plt
    except ImportError:
        raise ImportError("Please pip install matplotlib to use the pplot function")

    ax = age_distribution['probability'].plot(rot=25, label=label)
    ax.set_ylabel('Percent')
    ax.set_xlabel('Age')
    ax.set_title('Age Distribution')

    if plot_US_age:
        ax = US_AGE['probability'].plot(ax=ax, rot=25, label='US age distribution')

    ax.legend()
    return ax

if __name__=="__main__":
    names = pd.read_csv(PATH + '../datasets/sample_first_names.tsv', delimiter="\t")['first_name']
    names = names.ix[pd.notnull(names)]

    name_distribution = compute_name_frequencies(names)

    age_distribution = age_calculator(name_distribution)
    sex_distribution = sex_calculator(name_distribution)

    print names.head(10)
    print
    print age_distribution
    print
    print sex_distribution

    # plotting 
    # pplot(age_distribution)
