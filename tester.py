#Visualisation d'un episode:
episodee = launcher_stochastic()


for i in range(3):
    print(episodee[i])
    

#Action value prediction    
from collections import defaultdict
import numpy as np
import sys




def mc_prediction_q(num_episodes, gamma=1.0):
    # initialize empty dictionaries of arrays
    returns_sum = defaultdict(lambda: np.zeros(18))
    N = defaultdict(lambda: np.zeros(18))
    Q = defaultdict(lambda: np.zeros(18))
    # loop over episodes
    for i_episode in range(1, num_episodes+1):
        # monitor progress
        if i_episode % 100 == 0:
            print("\rEpisode {}/{}.".format(i_episode, num_episodes), end="")
            sys.stdout.flush()
            
        # generate an episode
        episode = launcher_stochastic()
        # obtain the states, actions, and rewards
        states, actions, rewards = zip(*episode)
        # prepare for discounting
        discounts = np.array([gamma**i for i in range(len(rewards)+1)])
        # update the sum of the returns, number of visits, and action-value 
        # function estimates for each state-action pair in the episode
        for i, state in enumerate(states):
            returns_sum[state][Zactions[actions[i]]] += sum(rewards[i:]*discounts[:-(1+i)])
            N[state][Zactions[actions[i]]] += 1.0
            Q[state][Zactions[actions[i]]] = returns_sum[state][Zactions[actions[i]]] / N[state][Zactions[actions[i]]]
        
    return Q, N


V, N = mc_prediction_q(50000)

V_sorted = sorted(V.items(), key=lambda item:  (item[1][0]), reverse=True)
V_sorted

len(V_sorted)



returns_sum = defaultdict(lambda: np.zeros(18))
N = defaultdict(lambda: np.zeros(18))
Q = defaultdict(lambda: np.zeros(18))
# loop over episodes

         gamma = 1   
        # generate an episode
        episode = launcher_stochastic()
        # obtain the states, actions, and rewards
        states, actions, rewards = zip(*episode)
        # prepare for discounting
        discounts = np.array([gamma**i for i in range(len(rewards)+1)])
        # update the sum of the returns, number of visits, and action-value 
        # function estimates for each state-action pair in the episode
        for i, state in enumerate(states):
            i=0
            returns_sum[states[i]][Zactions[actions[i]]] += sum(rewards[i:]*discounts[:-(1+i)])
            print(returns_sum[state][0])
         
            #N[state][actions[i]] += 1.0
            #Q[state][actions[i]] = returns_sum[state][actions[i]] / N[state][actions[i]]
            


s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)

d['red']

d.items()














def mc_prediction_v(num_episodes, gamma=1.0):
    # initialize empty dictionary of lists
    returns = defaultdict(list)
    # loop over episodes
    for i_episode in range(1, num_episodes+1):
        # monitor progress
        if i_episode % 100 == 0:
            print("\rEpisode {}/{}.".format(i_episode, num_episodes), end="")
            sys.stdout.flush()
        
        ## TODO: complete the function
        # generate an episode
        episode = launcher()
        # obtain the states, actions, and rewards
        states, actions, rewards = zip(*episode)
        # prepare for discounting
        discounts = np.array([gamma**i for i in range(len(rewards)+1)])
        # calculate and store the return for each visit in the episode
        for i, state in enumerate(states):
            returns[state].append(sum(rewards[i:]*discounts[:-(1+i)]))
            
    # calculate the state-value function estimate
    V = {k: np.mean(v) for k, v in returns.items()}
        
    return V

V = mc_prediction_v(60000)

V_sorted = sorted(V.items(), key=lambda item:  (item[1]))
#V_sorted

len(V_sorted)


#Action value prediction 

