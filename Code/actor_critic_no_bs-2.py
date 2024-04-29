# -*- coding: utf-8 -*-
"""actor_critic_no_bs.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e3rKAo14FuXozlNqpDnSfN5rAYrx4rcG
"""

!pip install wandb
!pip install swig
!pip install gym[all]
!pip install pygame

import torch
import torch.nn as nn
import torch.optim as optim
import gym
import numpy as np
import matplotlib.pyplot as plt

# Actor Network
class Actor(nn.Module):
    def __init__(self, input_size=8, output_size=4, hidden_size=128):
        super(Actor, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        return x

# Critic Network
class Critic(nn.Module):
    def __init__(self, input_size=8, hidden_size=128):
        super(Critic, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, 1)
        self.relu = nn.ReLU()

    def forward(self, state):
        x = self.relu(self.fc1(state))
        x = self.fc2(x)
        return x

# Actor-Critic Model
class ActorCritic(nn.Module):
    def __init__(self, actor, critic, lr):
        super(ActorCritic, self).__init__()
        self.actor = actor
        self.critic = critic
        self.actor_optimizer = optim.Adam(actor.parameters(), lr=0.001)
        self.critic_optimizer = optim.Adam(critic.parameters(), lr=0.001)

    def forward(self, state):
        action_probs = torch.softmax(self.actor(state), dim=-1)
        state_value = self.critic(state)
        return action_probs, state_value



# Training loop
def update(agent, states, actions, rewards, next_states, dones, gamma=0.99):
    states = torch.tensor(states, dtype=torch.float32)
    actions = torch.tensor(actions, dtype=torch.int64).view(-1, 1)
    rewards = torch.tensor(rewards, dtype=torch.float32).view(-1, 1)
    next_states = torch.tensor(next_states, dtype=torch.float32)
    dones = torch.tensor(dones, dtype=torch.float32).view(-1, 1)

    # Compute TD targets
    with torch.no_grad():
        _, next_state_values = agent(next_states)
        td_targets = rewards + gamma * (1 - dones) * next_state_values

    # Compute advantages
    _, state_values = agent(states)
    advantages = td_targets - state_values

    # Actor loss
    action_probs, _ = agent(states)
    log_probs = torch.log(action_probs.gather(1, actions))
    actor_loss = -(log_probs * advantages.detach()).mean()

    # Critic loss
    critic_loss = nn.MSELoss()(state_values, td_targets)

    # Update actor and critic networks
    agent.actor_optimizer.zero_grad()
    actor_loss.backward()
    agent.actor_optimizer.step()

    agent.critic_optimizer.zero_grad()
    critic_loss.backward()
    agent.critic_optimizer.step()


def run(agent, env, n_episodes):
  epi_reward = []
  for i_episode in range(n_episodes):
    state = env.reset()
    done = False
    total_reward = 0
    while not done:
        action_probs, _ = agent(torch.tensor(state, dtype=torch.float32).unsqueeze(0))
        action = torch.multinomial(action_probs, num_samples=1).item()
        next_state, reward, done, _ = env.step(action)
        total_reward += reward
        update(agent, [state], [action], [reward], [next_state], [done])
        state = next_state
    print(f"Episode {i_episode + 1}, Total Reward: {total_reward}")
    epi_reward.append(total_reward)
  env.close()
  return epi_reward



def main():
  # Create Lunar Lander environment
  env = gym.make('LunarLander-v2')
  state_size = env.observation_space.shape[0]
  action_size = env.action_space.n
  n_episodes = 100

  # Create actor, critic, and agent
  actor1 = Actor(state_size, action_size)
  critic1 = Critic(state_size)
  agent1 = ActorCritic(actor1, critic1, 0.001)
  e_array = [i for i in range(1, n_episodes+1)]

  r_array1 = run(agent1, env, n_episodes)

  # Define optimizer for actor and critic

  actor2 = Actor()
  critic2 = Critic()
  agent2 = ActorCritic(actor2, critic2, 0.01)

  r_array2 = run(agent2, env, n_episodes)


  actor3 = Actor()
  critic3 = Critic()
  agent3 = ActorCritic(actor3, critic3, 0.1)

  r_array3 = run(agent2, env, n_episodes)


  plt.title("Performance of Actor-Critic with different learning rates",fontsize=22)
  plt.plot(e_array, r_array1, label = "lr = 0.001")
  plt.plot(e_array,r_array2, label = "lr = 0.01")
  plt.plot(e_array,r_array2, label = "lr = 0.1")
  plt.xlabel('Episode')
  plt.ylabel('Reward')
  plt.legend()
  plt.show()



main()