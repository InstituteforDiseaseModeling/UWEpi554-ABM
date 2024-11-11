import starsim as ss
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Make people using the specified age distribution
n_agents = 5000
pregnancy = True

age_data = pd.DataFrame({
    'age': [0, 15, 50, 100],
    'value': [0.5, 0.3, 0.2, 0.0]
})
ppl = ss.People(n_agents, age_data=age_data)

# Deaths
death_rates = 15 # Time,Sex,AgeGrpStart,mx
deaths = ss.Deaths(death_rate=death_rates)

demog = [deaths]

if pregnancy:
    # Pregnancy
    fertility_rates = 60 # Time,AgeGrp,ASFR
    fertility_rates = pd.DataFrame({
        'Time': [2020, 2020],
        'AgeGrp': [15, 45],
        'ASFR': [60.0, 0], 
    })
    pregnancy = ss.Pregnancy(fertility_rate=fertility_rates)
    demog += [pregnancy]
else:
    # Births
    birth_rates = 15 # Year,CBR
    births = ss.Births(birth_rate=birth_rates)
    demog += [births]


# Create and initialize a simulation
sim = ss.Sim(people=ppl, demographics=demog)
sim.init()
sim.run()

fig, axv = plt.subplots(3,1)
axv[0].scatter(x=sim.people.uid, y=sim.people.female, c=sim.people.female, marker='|')
axv[1].bar(x=sim.people.uid, height=sim.people.age)
axv[2].hist(sim.people.age, bins = np.append(age_data['age'], sim.people.age.max()))

sim.plot()
plt.show()