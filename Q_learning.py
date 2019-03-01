import gym
import numpy as np 
from time import time
import matplotlib.pyplot as plt

#Loading the environment
env = gym.make('FrozenLake-v0')
Q = np.zeros([16,4])
#Setting the parameters
decay = 0.1
discount = 0.6
num_episodes = 2000
RewardList = []

# The Q-learning algorithm
def performQ(decay, discount, num_episodes):
    destination = False
    states = []
    total_epochs = 0
    for i in range(num_episodes):
    #Reset environment and get first new observation
        state = env.reset()
        states.append(state)
        it = 0
        epochs = 0
        done = False
        #Iterating
        while it < 99:
            states.append(state)
            #The greedy way
            e = 1./((it//100)+1)
            #Making a choice
            if np.random.rand(1) < e:
                action = env.action_space.sample()
            else:
                action = np.argmax(Q[state, :])
            #Getting the new state & the new reward from the environment
            state0,reward,destination,done = env.step(action)
            RewardList.append(reward)
            #Update the Q-Table with the new found knowledge
            Q[state,action] = Q[state,action] + decay*(reward + discount*np.max(Q[state0,:]) - Q[state,action]) 
            state = state0

            #Stops if destination equals True
            epochs += 1
            it += 1    
        total_epochs += epochs
    return total_epochs

if __name__ == "__main__":

	#Logging the start of the training
	training_start = time()

	total_epochs = performQ(decay, discount, num_episodes)

	#Logging the end of the training
	training_end = time()

	print('Qtable')
	print(Q)   
	print('\nNumber of Episodes: ' + str(num_episodes))
	print('Accumulated Rewards: ' + str(sum(RewardList)))
	print("Average rewards over Episodes : " + str(sum(RewardList)/num_episodes))
	print(f"Timesteps per episode: {total_epochs / num_episodes}\n")

	env.reset()

	#Running the algorithm 10 times with the optimized Q-table for testing
	for episode in range(10):
		state = env.reset()
		step = 0
		done = False
		print("############################################")
		print("EPISODE ", episode)

		for step in range(99):

			#Using the max expected reward given the state it is in, take an action
			action = np.argmax(Q[state,:])

			new_state, reward, done, info = env.step(action)

			if done:
				#Only the last state (the one where the agent is done) gets rendered (either we fall or reach the goal)
				env.render()

				#We print the number of steps it took.
				print("Number of steps", step)
				break
			state = new_state
	env.close()

	#Show the success rate for finding the Goal & used training time
	success_rate = round((sum(RewardList) / num_episodes) * 100, 2)
	training_time = int(training_end - training_start)
	print("\nThe Goal has been found in", str(success_rate), "% of times over",  str(num_episodes), "episodes during", str(training_time), "seconds of runtime")

	#Plotting the rewards and the number of steps it took
	fig = plt.figure()
	ax1 = fig.add_subplot(111)
	ax1.plot(RewardList, '-g', label = 'Reward')
	ax1.set_yticks([0,1])
	ax2 = ax1.twinx()
	ax2.plot([x for x in range(0, len(RewardList))],  label = 'Step')
	ax1.set_ylabel("Reward")
	ax1.set_xlabel("Episode")
	ax2.set_ylabel("Step")
	ax1.legend(loc=2)
	ax2.legend(loc=1)
	plt.title("Training over Time")
	plt.show()