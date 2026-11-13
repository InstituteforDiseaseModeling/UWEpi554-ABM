# Template showing the building blocks of a Starsim simulation. Replace each
# `...` with a module (see the other scripts), or delete the line, before running.
import starsim as ss
import matplotlib.pyplot as plt

sim_pars = dict(
    start = ss.date('2024-11-12'),
    stop  = ss.date('2024-12-31'),
    unit = 'day',
    dt = 1,
)

s = ss.Sim(
    pars = sim_pars,
    people =  ...,
    demographics = ...,
    diseases = ...,
    networks = ...,
    interventions = ...,
    analyzers = ...,
    connectors = ...,
    label = 'Hello EPI554!',
)
s.run()
s.plot()
plt.show()