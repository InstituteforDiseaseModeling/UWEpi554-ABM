import starsim as ss
import networkx as nx
import matplotlib.pyplot as plt

seed = 42

# Make the SIR infection
sir = ss.SIR(dur_inf=10, beta=0.2, init_prev=0.1, p_death=0.2)

lam = 5
random = ss.RandomNet(n_contacts = ss.poisson(lam=lam))
sim = ss.Sim(n_agents=5_000, diseases=sir, networks=random, label='Poisson')
sims = [sim]

for n in [0.2, 95]:
    net = ss.RandomNet(n_contacts = ss.nbinom(n=n, p=n/(n+lam)))
    sim = ss.Sim(n_agents=5_000, diseases=sir, networks=net, label=f'Negative Binomial (x_var {1+lam/n:.2f})', rand_seed=seed)
    sims.append(sim)

g = nx.erdos_renyi_graph(n=5_000, p=lam/5_000)
net = ss.StaticNet(g)
sim = ss.Sim(n_agents=5_000, diseases=sir, networks=net, label='Erdos-Renyi', rand_seed=seed)
sims.append(sim)

msim = ss.MultiSim(sims)
msim.run()

plt.figure()
for sim in msim.sims:
    rnr = sim.networks[0].results
    plt.plot(rnr.timevec, rnr.n_edges, label=sim.label)
plt.legend()

msim.plot()
plt.show()