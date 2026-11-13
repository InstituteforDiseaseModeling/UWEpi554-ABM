# UWEpi554-ABM

Example scripts introducing agent-based modeling (ABM) for UW EPI 554. They accompany a lecture on agent-based models of infectious disease transmission.

In an agent-based model, each person is simulated individually, with their own age, sex, infection state and contacts. Population-level patterns, like the epidemic curve, emerge from many individual-level random events. This makes ABMs a natural fit for questions that compartmental (ODE) models handle poorly, such as heterogeneous contact patterns, small populations where chance matters, and interventions targeted at specific individuals.

The first script builds a small ABM from scratch in plain Python. The rest use [Starsim](https://github.com/starsimhub/starsim), an open-source ABM framework developed at the Institute for Disease Modeling.

## Setup

These scripts use [uv](https://docs.astral.sh/uv/) to install Python and all required packages into a project-local environment. You don't need an existing Python installation.

1. Install uv by following the [installation instructions](https://docs.astral.sh/uv/getting-started/installation/) for your operating system.
2. Clone this repository and install the environment:

   ```bash
   git clone https://github.com/InstituteforDiseaseModeling/UWEpi554-ABM.git
   cd UWEpi554-ABM
   uv sync
   ```

The scripts are pinned to Starsim 2.2.0. The current [Starsim documentation](https://docs.starsim.org) describes Starsim 3.x, and some syntax (notably how rates and time units are specified) differs from these scripts.

## Running the scripts

Run any script with `uv run`:

```bash
uv run python agent_model.py
```

Each script opens one or more plot windows; the script finishes when you close them. If you use VS Code, open this folder and the editor should pick up the `.venv` environment automatically. You can then run scripts with the ▶ button.

## Suggested order

| Script | What it shows | Things to try |
| -- | -- | -- |
| [agent_model.py](agent_model.py) | A complete SIR agent-based model in ~100 lines of plain Python: a `Person` class with infection and recovery rules, and a `Sim` class that steps through time. | Change `seed` and rerun to see run-to-run variability. Lower `I0` to 1 and see how often the epidemic dies out by chance. Compare the curve to an ODE SIR model with the same `beta` and `gamma`. |
| [people.py](people.py) | Creating a Starsim population with a specified age distribution, and selecting agents by their attributes. | Change `age_data` to resemble a younger or older population. |
| [demographics.py](demographics.py) | Adding births and deaths (or age-specific pregnancy) so the population changes over time. | Set `pregnancy = True`. Change birth and death rates and watch the age structure shift. |
| [distributions.py](distributions.py) | Starsim's random-number distributions, including one whose parameters depend on each agent's attributes. | Make the standard deviation depend on age, too. |
| [infection.py](infection.py) | Running an infectious disease (SIR) alongside a non-communicable disease (NCD) on a random contact network. | Change `beta` and `dur_inf`; how does the final epidemic size respond? |
| [transmission.py](transmission.py) | How contact network structure affects transmission: Poisson vs. overdispersed (negative binomial) contact numbers vs. a fixed Erdős–Rényi network, all with the same mean number of contacts. | Change `lam`. Why does the highly overdispersed network behave so differently with the same average? |
| [simulation.py](simulation.py) | A template listing every building block of a Starsim simulation. Fill in the `...` placeholders using pieces from the other scripts. | Build your own model: a population, a disease, a network and an intervention. |

## Checking that everything works

A smoke test runs every script (except the `simulation.py` template) without opening plot windows:

```bash
uv run pytest
```

## Disclaimer

The code in this repository was developed by [IDM](https://idmod.org) to support teaching and our research on flexible agent-based modeling. We've made it publicly available under the MIT License to provide others with a better understanding of our research and an opportunity to build upon it for their own work. We make no representations that the code works as intended or that we will provide support, address issues that are found, or accept pull requests. You are welcome to create your own fork and modify the code to suit your own modeling needs as permitted under the MIT License.
