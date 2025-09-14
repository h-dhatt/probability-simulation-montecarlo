
# Simulation & Probability Models — Random Walks and Gambler's Ruin

**Author:** Harleen Dhatt (B.Sc. (Honours) Math & Stats, McMaster)  

## Objectives
1. Simulate **stochastic processes** (random walk, gambler’s ruin) and compare against theoretical results.
2. Demonstrate **law of large numbers** (convergence of simulated probability to exact value).
3. Illustrate **Central Limit Theorem**: distribution of a random walk approaches Normal.

## Key Results
- **Gambler’s Ruin**: Simulation converges to exact probability of 0.500 as trials increase (see log-scale plot).
- **Random Walk**: Distribution after 200 steps closely matches Normal(0,14.14).

## Deliverables
- **gambler_ruin_results.csv** — simulated vs exact probabilities
- **randomwalk_finalpos.csv** — final positions of 10,000 random walks
- **fig_gambler_ruin.png** — convergence plot
- **fig_randomwalk_paths.png** — 10 sample paths
- **fig_randomwalk_distribution.png** — histogram vs Normal

## Highlights
- Implemented Monte Carlo simulations of **stochastic processes** from scratch.
- Verified convergence to exact probability laws and **CLT** empirically.
- Produced reproducible results and clear visuals.

## How to Run
```bash
pip install numpy pandas matplotlib
python analysis_script.py
```

## Talking Points
- Gambler’s Ruin connects to **Markov chains** with absorbing states; exact solution matches simulations by law of large numbers.
- Random walk distribution illustrates **Central Limit Theorem** — scaled sums of independent steps tend to Normal.
- Simulations provide intuition bridging **probability theory** and computation.
