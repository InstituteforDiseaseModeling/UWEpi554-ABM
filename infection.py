import starsim as ss
import matplotlib.pyplot as plt

# Make the SIR infection
sir = ss.SIR(dur_inf=10, beta=0.2,
    init_prev=0.1, p_death=0.2)

# Make the NCD disease
ncd = ss.NCD()

sim = ss.Sim(n_agents=2_000,
    diseases=[sir, ncd],
    networks=ss.RandomNet())
sim.run()

sim.plot('ncd')
sim.plot('sir')
plt.show()