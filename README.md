# Reinforcement Learning Assignment 3

For this assignment we explore Policy Based Reinforcement Learning Algorithms, specifically with the Lunar Lander environment. 
The Lunar Lander environment is a classical rocket trajectory optimisation problem taken from OpenAI gym. 

<img width="512" alt="Screenshot 2024-04-12 at 11 21 05 AM" src="https://github.com/itismeganrms/rl-a3/assets/52709218/75c96f97-25a0-4213-9059-10313490fbea">

## Project 
We explored 4 different Policy based Reinforcement Learning algorithms: 
- Reinforce
- Actor Critic
- Actor Critic with Bootstrapping
- Actor Critic with Baseline Subtraction
- Actor Critic with Bootstrapping and Baseline Subtraction

## Execution 
### Dependencies
- Python 3.x
- OpenAI Gym
- Pytorch 
- NumPy
- Swig
- Pygame

### Installation
- Clone the repository: git clone [https://github.com/itismeganrms/rl-a3)
- Install the relevant dependencies
  
### Policy-based Reinforcement Learning
The section called Policy-based Reinforcement Learning includes the .py files, where we experiemented with the algorithms and introduced different variations in learning rates, hidden layers, neurons. 
- The reinforce_basic.py and reinforce_with_entropy_regularisation.py compares the performance of REINFORCE algorithm without and with entropy regularization. It also compares the performance of the algorithm against different learning rates.
- The actor_critic.py contains the implementation of the basic actor-critic algorithm, without bootstrapping or baseline subtraction. It also plots the performance of the algorithm against different learning rates.
- The actor_critic_baseline.py and actor_critic_entropy.py contains the implementation of the actor-critic algorithm, without and with entropy regularization. It also compares the performance of the algorithm against different learning rates.
- The bootstrapping baseline subtraction.py contains the implementation of the actor-critic algorithm, with bootstrapping and baseline subtraction in it. This also plots the performance of the algorithm for multiple learning rates.

### Hyper-Parameter Tuning
- The performance of REINFORCE algorithm has been tested against various learning rates [0.001, 0.01, 0.1], with and without entropy regularization
- Actor-Critic with bootstrapping has been tested for various learning rates [0.001, 0.01, 0.1], difference in hidden layers [1,2,3] and number of neurons [64,128,256]
- Actor-Critic with baseline subtraction has been tested against various learning rates [0.001, 0.01, 0.1], with and without entropy regularization
- Actor-Critic with bootstrapping and baseline subtraction has been tested for various learning rates [0.001, 0.01, 0.1], difference in hidden layers [1,2,3] and number of neurons [64,128,256]
