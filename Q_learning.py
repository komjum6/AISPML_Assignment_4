import gym
import numpy as np 

# Loading the environment
env = gym.make('FrozenLake-v0')
Q = np.zeros([16,4])
# Setting the parameters
decay = .659
discount = .9

frames = []

# The Q-learning algorithm
def performQ(state, frames = []):
    destination = False
    done = False
    it = 0
    
    #Iterating
    while it < 99:

        states.append(state)
        # The greedy way
        e = 1./((it//100)+1)
        # Making a choice
        if np.random.rand(1) < e:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state, :])
        #Getting the new state & the new reward from the environment
        state0,reward,destination,done = env.step(action)
        #Update the Q-Table with the new found knowledge
        Q[state,action] = Q[state,action] + decay*(reward + discount*np.max(Q[state0,:]) - Q[state,action])
        state = state0
        
        #Stops if destination equals True
        if destination == True:
            
            #Adding the new frame to frames
            frames.append({
                'frame': env.render(mode='ansi'),
                'state': state,
                'action': action,
                'reward': reward
                }
            )
            break
        it += 1    
    
    return state, frames

if __name__ == "__main__":

    state = env.reset()
    states = []

    Searching = True


    for x in range(0, 200):

        states.append(state)
        env.reset()
        state, frames = performQ(state)
        if state == 15:
            break

    for count, frame in enumerate(frames):

        print(frame['frame'].getvalue())      
        

