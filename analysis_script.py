
import os, numpy as np, pandas as pd, matplotlib.pyplot as plt
from math import comb

def gambler_ruin_sim(N,p,start,trials):
    wins=0
    for _ in range(trials):
        capital=start
        while 0<capital<N:
            if np.random.rand()<p: capital+=1
            else: capital-=1
        if capital==N: wins+=1
    return wins/trials

def gambler_ruin_exact(N,p,start):
    if p==0.5: return start/N
    q=1-p
    return (1-(q/p)**start)/(1-(q/p)**N)

def random_walk(n_steps,trials):
    paths=np.zeros((trials,n_steps+1))
    for i in range(trials):
        steps=np.random.choice([-1,1],size=n_steps)
        paths[i]=np.concatenate([[0],np.cumsum(steps)])
    return paths

def main():
    os.makedirs("project4_simulation",exist_ok=True)
    base_dir="project4_simulation"

    # Gambler's Ruin
    N=20; start=10; p=0.5
    trials_list=[100,1000,5000,10000]
    results=[]
    for t in trials_list:
        approx=gambler_ruin_sim(N,p,start,t)
        exact=gambler_ruin_exact(N,p,start)
        results.append({"trials":t,"simulated_prob":approx,"exact_prob":exact,"abs_error":abs(approx-exact)})
    df=pd.DataFrame(results)
    df.to_csv(os.path.join(base_dir,"gambler_ruin_results.csv"),index=False)

    plt.figure()
    plt.plot(df["trials"],df["simulated_prob"],marker="o",label="Simulated")
    plt.axhline(df["exact_prob"].iloc[0],color="red",linestyle="--",label="Exact")
    plt.xscale("log"); plt.xlabel("Number of trials (log)")
    plt.ylabel("Probability of reaching N before 0")
    plt.title("Gambler's Ruin: Simulation vs Exact")
    plt.legend(); plt.tight_layout()
    plt.savefig(os.path.join(base_dir,"fig_gambler_ruin.png"),dpi=200); plt.close()

    # Random Walk
    n_steps=200; trials=50
    paths=random_walk(n_steps,trials)
    plt.figure()
    for i in range(10): plt.plot(range(n_steps+1),paths[i],alpha=0.7)
    plt.xlabel("Steps"); plt.ylabel("Position"); plt.title("1D Random Walk: 10 Sample Paths")
    plt.tight_layout(); plt.savefig(os.path.join(base_dir,"fig_randomwalk_paths.png"),dpi=200); plt.close()

    trials_big=10000
    paths_big=random_walk(n_steps,trials_big)
    final_pos=paths_big[:,-1]
    pd.DataFrame({"final_position":final_pos}).to_csv(os.path.join(base_dir,"randomwalk_finalpos.csv"),index=False)
    plt.figure(); plt.hist(final_pos,bins=30,density=True,alpha=0.7,label="Simulated distribution")
    mu=0; sigma=np.sqrt(n_steps)
    x=np.linspace(min(final_pos),max(final_pos),200)
    normal_pdf=(1/(sigma*np.sqrt(2*np.pi)))*np.exp(-(x-mu)**2/(2*sigma**2))
    plt.plot(x,normal_pdf,"r--",label="Normal approx")
    plt.xlabel("Final Position"); plt.ylabel("Density")
    plt.title("Random Walk Distribution vs Normal Approximation")
    plt.legend(); plt.tight_layout()
    plt.savefig(os.path.join(base_dir,"fig_randomwalk_distribution.png"),dpi=200); plt.close()

if __name__=="__main__": main()
