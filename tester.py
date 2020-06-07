#Visualisation d'un episode:
episodee = launcher()


for i in range(3):
    print(episodee[i])
    

#State value prediction    
from collections import defaultdict
import numpy as np
import sys

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
V_sorted

len(V_sorted)




gamma=1
returns = defaultdict(list)
episodex = launcher()
print('Episode :',episodex)
states, actions, rewards = zip(*episodex)
discounts = np.array([gamma**i for i in range(len(rewards)+1)])
print("Discount :",discounts)

for i, state in enumerate(states):
            returns[state].append(sum(rewards[i:]*discounts[:-(1+i)]))
            
            
print("Returns :",returns)
discounts[:-1]

np.array([states])



x = np.array([4, 1, 4, 4, 3, 0, 0, 4], dtype='int64')
str(x)+str(x)
