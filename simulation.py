import starsim as ss
import matplotlib.pyplot as plot

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