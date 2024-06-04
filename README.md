# Teach an AI to Play Snake!

## Snake-Intelligence
Welcome to the Teach an AI to Play Snake project! In this project, we will build everything from scratch using Pygame for the game environment and PyTorch for the reinforcement learning (RL) algorithm. This README will guide you through setting up the project, understanding the code structure, and running the AI to play the classic Snake game.

### Introduction
The aim of this project is to teach an AI agent to play the Snake game using reinforcement learning. We will use Pygame to create the Snake game environment and PyTorch to implement the RL algorithm. By the end of this project, the AI should be able to play the Snake game autonomously and improve its performance over time.

### Prerequisites
Before you begin, ensure you have the following installed:

* Python 3.7+
* Pygame
* PyTorch
* NumPy


### Installation

1. Clone the repository:
```bash
git clone https://github.com/bsharabi/Snake-Intelligence
cd Snake-Intelligence
```
2. Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
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
│   ├── snake_game.py      # Pygame implementation of Snake
│   ├── __init__.py
│
├── ai/
│   ├── model.py           # Neural network model using PyTorch
│   ├── agent.py           # Reinforcement learning agent
│   ├── train.py           # Training loop
│   ├── __init__.py
│
├── main.py                # Entry point for running the game and AI
├── requirements.txt       # List of required packages
├── README.md              # Project documentation
└── LICENSE                # License for the project
```

### Usage
#### Running the Game
To run the Snake game manually without the AI, use the following command:
```bash
python game/snake_game.py
```

#### Running the AI
To run the Snake game with the AI controlling the snake, use:
```bash
python main.py
```

#### Training the AI
To train the AI agent from scratch, execute the training script:
```bash
python ai/train.py
```
The training script will use the reinforcement learning algorithm to improve the AI's performance over time. You can monitor the training progress through the console output.

### Contributing
We welcome contributions to this project! If you have an idea for an improvement or a bug fix, please fork the repository and submit a pull request. For major changes, please open an issue to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

### License
This project is licensed under the MIT License - see the LICENSE file for details.


