# Teach an AI to Play Snake!

## Snake-Intelligence

Welcome to the Teach an AI to Play Snake project! In this project, we will build everything from scratch using Pygame for the game environment and PyTorch for the reinforcement learning (RL) algorithm. This README will guide you through setting up the project, understanding the code structure, and running the AI to play the classic Snake game.

### Introduction

The aim of this project is to teach an AI agent to play the Snake game using reinforcement learning. We will use Pygame to create the Snake game environment and PyTorch to implement the RL algorithm. By the end of this project, the AI should be able to play the Snake game autonomously and improve its performance over time.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7+
- Pygame
- PyTorch
- NumPy

### Installation

1. Clone the repository:

```bash
git clone https://github.com/bsharabi/Snake-Intelligence
cd Snake-Intelligence
```

2. Create a virtual environment and activate it:

```bash
conda create -n venv python=3.12
conda activate venv  
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

### Project Structure

The project is organized as follows:
```bash
Snake-Intelligence/
│
├── game/
│ ├── snake.py # Pygame implementation of Snake
│ ├── init.py
│
├── ai/
│ ├── model.py # Neural network model using PyTorch
│ ├── agent.py # Reinforcement learning agent
│ ├── train.py # Training loop
│ ├── init.py
│ ├── plot.py
│
├── main.py # Entry point for running the game and AI
├── requirements.txt # List of required packages
├── README.md # Project documentation
├── settings.py # Project settings
└── LICENSE # License for the project
```

### Usage

#### Running the Menu
To run the Menu game manually, use the following command:
```bash
python ./
```
#### Running the Game

To run the Snake game manually without the AI, use the following command:

```bash
python game/snake.py
```

Running the AI
To run the Snake game with the AI controlling the snake, use:
```bash
python __main__.py
```
Training the AI
To train the AI agent from scratch, execute the training script:
```bash
python ai/train.py
```

The training script will use the reinforcement learning algorithm to improve the AI's performance over time. You can monitor the training progress through the console output.

## How It Works
### The Game
The Snake game is implemented using Pygame. The snake is controlled using the arrow keys, and the objective is to eat the food that appears randomly on the screen. Every time the snake eats the food, it grows longer. The game ends if the snake collides with the walls or itself.

### The AI
The AI uses a Deep Q-Learning algorithm to learn how to play the game. Here's a high-level overview of how the training works:

1. State Representation: The state is represented as an 11-dimensional vector capturing the current direction of the snake, the location of the food relative to the snake, and potential dangers (e.g., collisions).

2. Neural Network: A simple neural network is used to approximate the Q-function. It takes the state as input and outputs Q-values for possible actions (straight, left, right).

3. Training:

* Short-term Memory: The AI makes a move based on the current state and stores the experience tuple (state, action, reward, next state, done) in its memory.
* Long-term Memory: The AI is periodically trained on a batch of experiences sampled from its memory to improve its decision-making over time.
* Exploration vs. Exploitation: The AI balances exploration (trying new actions) and exploitation (choosing the best-known action) to gradually improve its performance.
4. Reward System: The AI receives positive rewards for eating food and negative rewards for dying, which guides it to maximize its score.

## Contributing
* We welcome contributions to this project! If you have an idea for an improvement or a bug fix, please fork the repository and submit a pull request. For major changes, please open an issue to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.


