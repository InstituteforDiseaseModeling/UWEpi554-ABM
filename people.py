import starsim as ss
import pandas as pd
import matplotlib.pyplot as plt

# Make people using the specified age distribution
n_agents = 5000

age_data = pd.DataFrame({
    'age': [0, 15, 50, 100],
    'value': [0.5, 0.3, 0.2, 0.0]
})
ppl = ss.People(n_agents, age_data=age_data)

# Create and initialize a simulation
sim = ss.Sim(people=ppl)
sim.init()
print(sim.people)
print(sim.people.age)

under_15 = sim.people.age < 15 # Boolean array, one entry per agent
u15_uids = under_15.uids # Unique IDs of the agents where under_15 is True

print(under_15)
print(under_15.uids)

fig, axv = plt.subplots(3,1)
axv[0].scatter(x=sim.people.uid, y=sim.people.female, c=sim.people.female, marker='|')
axv[1].bar(x=sim.people.uid, height=sim.people.age)
axv[2].hist(sim.people.age, bins=age_data['age'])
plt.show()