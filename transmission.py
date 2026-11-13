import matplotlib.pyplot as plt
import networkx as nx
import starsim as ss

seed = 42
n_agents = 5_000

# Make the SIR infection
sir = ss.SIR(dur_inf=10, beta=0.2, init_prev=0.1, p_death=0.2)

lam = 5
random = ss.RandomNet(n_contacts = ss.poisson(lam=lam))
sim = ss.Sim(n_agents=n_agents, diseases=sir, networks=random, label='Poisson', rand_seed=seed)
sims = [sim]

# Negative binomial with p = n/(n+lam) has the same mean (lam) as the Poisson, but
# variance lam + lam**2/n: small n gives a few highly connected agents, large n is ~Poisson
for n in [0.2, 95]:
    net = ss.RandomNet(n_contacts = ss.nbinom(n=n, p=n/(n+lam)))
    sim = ss.Sim(n_agents=n_agents, diseases=sir, networks=net, label=f'Negative Binomial (x_var {1+lam/n:.2f})', rand_seed=seed)
    sims.append(sim)

# Erdos-Renyi: each pair of agents is connected with probability p, giving mean degree ~lam.
# Unlike RandomNet, which redraws contacts every timestep, this network stays fixed
g = nx.erdos_renyi_graph(n=n_agents, p=lam/n_agents)
net = ss.StaticNet(g)
sim = ss.Sim(n_agents=n_agents, diseases=sir, networks=net, label='Erdos-Renyi', rand_seed=seed)
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