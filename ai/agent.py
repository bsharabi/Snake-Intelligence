from settings import *
from .snake_ai import SnakeGameAI, Direction, Point
from .model import Linear_QNet, QTrainer
from .plot import plot
import numpy as np
import random
from collections import deque
import torch

class Agent:
    """
    Agent class that handles the decision-making process and training for the Snake AI.

    Attributes:
    -----------
    n_games : int
        The number of games played.
    epsilon : float
        The exploration rate.
    gamma : float
        The discount factor for future rewards.
    memory : deque
        Memory buffer for storing experience tuples.
    model : Linear_QNet
        The Q-learning model.
    trainer : QTrainer
        The trainer for the Q-learning model.

    Methods:
    --------
    get_state(game):
        Returns the current state of the game.
    remember(state, action, reward, next_state, done):
        Stores an experience tuple in the memory buffer.
    train_long_memory():
        Trains the model on a batch of experiences from the memory buffer.
    train_short_memory(state, action, reward, next_state, done):
        Trains the model on a single experience tuple.
    get_action(state):
        Determines the next action to take based on the current state.
    """
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0  # randomness
        self.gamma = 0.9  # discount rate
        self.memory = deque(maxlen=MAX_MEMORY)  # popleft()
        self.model = Linear_QNet(11, 256, 3)
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)

    def get_state(self, game: SnakeGameAI):
        """
        Returns the current state of the game.

        Parameters:
        -----------
        game : SnakeGameAI
            The Snake game instance.

        Returns:
        --------
        np.ndarray
            The current state of the game.
        """
        head = game.snake[0]
        point_l = Point(head.x - BLOCK_SIZE, head.y)
        point_r = Point(head.x + BLOCK_SIZE, head.y)
        point_u = Point(head.x, head.y - BLOCK_SIZE)
        point_d = Point(head.x, head.y + BLOCK_SIZE)
        
        dir_l = game.direction == Direction.LEFT
        dir_r = game.direction == Direction.RIGHT
        dir_u = game.direction == Direction.UP
        dir_d = game.direction == Direction.DOWN

        state = [
            # Danger straight
            (dir_r and game.is_collision(point_r)) or 
            (dir_l and game.is_collision(point_l)) or 
            (dir_u and game.is_collision(point_u)) or 
            (dir_d and game.is_collision(point_d)),

            # Danger right
            (dir_u and game.is_collision(point_r)) or 
            (dir_d and game.is_collision(point_l)) or 
            (dir_l and game.is_collision(point_u)) or 
            (dir_r and game.is_collision(point_d)),

            # Danger left
            (dir_d and game.is_collision(point_r)) or 
            (dir_u and game.is_collision(point_l)) or 
            (dir_r and game.is_collision(point_u)) or 
            (dir_l and game.is_collision(point_d)),
            
            # Move direction
            dir_l,
            dir_r,
            dir_u,
            dir_d,
            
            # Food location 
            game.food.x < game.head.x,  # food left
            game.food.x > game.head.x,  # food right
            game.food.y < game.head.y,  # food up
            game.food.y > game.head.y  # food down
        ]

        return np.array(state, dtype=int)

    def remember(self, state, action, reward, next_state, done):
        """
        Stores an experience tuple in the memory buffer.

        Parameters:
        -----------
        state : np.ndarray
            The current state.
        action : list
            The action taken.
        reward : float
            The reward received.
        next_state : np.ndarray
            The next state.
        done : bool
            Whether the episode has ended.
        """
        self.memory.append((state, action, reward, next_state, done))  # popleft if MAX_MEMORY is reached

    def train_long_memory(self):
        """
        Trains the model on a batch of experiences from the memory buffer.
        """
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)  # list of tuples
        else:
            mini_sample = self.memory

        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)

    def train_short_memory(self, state, action, reward, next_state, done):
        """
        Trains the model on a single experience tuple.

        Parameters:
        -----------
        state : np.ndarray
            The current state.
        action : list
            The action taken.
        reward : float
            The reward received.
        next_state : np.ndarray
            The next state.
        done : bool
            Whether the episode has ended.
        """
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):
        """
        Determines the next action to take based on the current state.

        Parameters:
        -----------
        state : np.ndarray
            The current state.

        Returns:
        --------
        list
            The action to be taken.
        """
        # Random moves: tradeoff exploration / exploitation
        self.epsilon = 80 - self.n_games
        final_move = [0, 0, 0]
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 2)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1

        return final_move


def train():
    """
    Trains the Snake AI using a Deep Q-learning algorithm.
    """
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI()

    while True:
        # Get old state
        state_old = agent.get_state(game)

        # Get move
        final_move = agent.get_action(state_old)

        # Perform move and get new state
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)

        # Train short memory
        agent.train_short_memory(state_old, final_move, reward, state_new, done)

        # Remember
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            # Train long memory, plot result
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
                agent.model.save()

            print('Game', agent.n_games, 'Score', score, 'Record:', record)

            plot_scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            plot_mean_scores.append(mean_score)
            plot(plot_scores, plot_mean_scores)


if __name__ == '__main__':
    train()
