import pandas as pd
from matplotlib import pyplot as plt
from utils import DiscreteDistribution, name_distribution, normalize_vector

TOTALS = pd.read_csv('datasets/counts_by_age_sex_name.csv', index_col=[0,1,2])
PRIOR  = pd.read_csv('datasets/age_distribution.csv', index_col=[0])['both_sexes_percent']
SURVIVAL = pd.Series([0.99, 0.98, 0.97, 0.96, 0.96, 0.95, 0.95, 0.94, 0.93, 0.92, 0.91, 0.85, 0.80, 0.70, 0.62, 0.56, 0.51, 0.45], index=PRIOR.index)


class NameDistribution(object):
    """
    Work in Progress
    """
    def __init__(self):
        self._discrete_distribution = DiscreteDistribution(PRIOR)

    def update(self,name):
        """
        Update the model with an observed name.

        Params:
            name: string

        """
        name = self.normalize_name(name)
        self._discrete_distribution.update( SURVIVAL*name_distribution(name, TOTALS, PRIOR))
        return

    def updates(self, names):
        """
        Bulk updates.

        Params:
           names: an iterable of names.

        """
        for name in names:
            self.update(name)

    def plot(self):

        ax = plt.subplot(2,1,1)
        self.distribution.plot(kind='bar', ax=ax)
        ax.set_title('Distribution of Ages')

        #difference from prior
        ax = plt.subplot(2,1,2)
        (self.distribution - PRIOR).round(4).plot(kind='bar', ax=ax)
        ax.set_title('Absolute differences in age distribution')
        return

    def normalize_name(self,name):
        """
        Normalize a name. 

        """
        capitalize = lambda name: (name[0].upper() + name[1:].lower()).strip()
        return " ".join( map( capitalize, name.split()))

    def distribution():
        def fget(self):
            return normalize_vector(self._discrete_distribution.posterior)
        return locals()
    distribution = property(**distribution())




if __name__=="__main__":
    """
    WIP
    """
    nd = NameDistribution()
    for i in range(1000):
        nd.update('Brittany')

    nd.plot()
