#Visualisation d'un episode:
Q = defaultdict(lambda: np.zeros(18))
episodee = launcher_stochastic(Q)


epsilon = 0.00 
counter = 0
round_num = 1000
for i in range(round_num):
    counter += launcher_stochastic(Q, epsilon)[-1][2]
print(counter / round_num) 

for i in range(3):
    print(episodee[i])
    

#Action value prediction    
from collections import defaultdict
import numpy as np
import sys



#Action Values
def mc_prediction_q(num_episodes, gamma=1.0, Q = defaultdict(lambda: np.zeros(18)), N = defaultdict(lambda: np.zeros(18))):
    # initialize empty dictionaries of arrays
    
    # loop over episodes
    for i_episode in range(1, num_episodes+1):
        # monitor progress
        if i_episode % 100 == 0:
            print("\rEpisode {}/{}.".format(i_episode, num_episodes), end="")
            sys.stdout.flush()
        
        # set the value of epsilon
        epsilon = 1.0/((i_episode/8000)+1)    
        
        # generate an episode
        episode = launcher_stochastic(Q, epsilon)
        # obtain the states, actions, and rewards
        states, actions, rewards = zip(*episode)
        # prepare for discounting
        discounts = np.array([gamma**i for i in range(len(rewards)+1)])
        # update the sum of the returns, number of visits, and action-value 
        # function estimates for each state-action pair in the episode
        for i, state in enumerate(states):
            old_Q = Q[state][Zactions[actions[i]]] 
            old_N = N[state][Zactions[actions[i]]]
            Q[state][Zactions[actions[i]]] = old_Q + (sum(rewards[i:]*discounts[:-(1+i)]) - old_Q)/(old_N+1)
            N[state][Zactions[actions[i]]] += 1
            
        
    return Q, N


Q, N = mc_prediction_q(1000000, Q = defaultdict(lambda: np.zeros(18)), N = defaultdict(lambda: np.zeros(18)))
 Q, N = mc_prediction_q(10000, 1.0, Q, N)
len(Q)
 



