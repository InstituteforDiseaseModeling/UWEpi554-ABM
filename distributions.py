import starsim as ss
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sim = ss.Sim(n_agents=100).init()

# Bernoulli distribution
d = ss.bernoulli(p=0.25) \
    .init(sim=sim, trace='bernoulli')
    # ^^^ Don't have to call .init in the real model
x = d.rvs(n=25)
print('Some bernoulli random numbers:', x)

# Normal distribution
d = ss.normal(loc=10, scale=2) \
    .init(sim=sim, trace='normal')
d.plot_hist() # Let's see a histogram of the random numbers
x = d.rvs(n=15)
print('Some normal random numbers:', x)

# Normal distribution with mean based on age
def loc_by_age(self, sim, uids):
    return sim.people.age[uids]

d = ss.normal(loc=loc_by_age, scale=2) \
    .init(sim=sim, trace='fancy normal')

uids = sim.people.auids # UIDS for all agents...
x = d.rvs(uids)
pd.DataFrame({'age': sim.people.age, 'value': x}).plot.scatter(x='age', y='value')
plt.show()