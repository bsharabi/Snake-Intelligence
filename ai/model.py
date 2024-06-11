from settings import *
class Linear_QNet(nn.Module):
    """
    A simple feedforward neural network with one hidden layer for Q-learning.

    Attributes:
    -----------
    linear1 : torch.nn.Linear
        The first linear layer.
    linear2 : torch.nn.Linear
        The second linear layer.

    Methods:
    --------
    forward(x):
        Performs a forward pass through the network.
    save(file_name='model.pth'):
        Saves the model parameters to a file.
    """
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        """
        Defines the forward pass through the network.

        Parameters:
        -----------
        x : torch.Tensor
            The input tensor.

        Returns:
        --------
        torch.Tensor
            The output tensor after passing through the network.
        """
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x

    def save(self, file_name='model.pth'):
        """
        Saves the model parameters to a file.

        Parameters:
        -----------
        file_name : str
            The name of the file where the model parameters will be saved.
        """
        model_folder_path =  os.path.join(AI,'model') 
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)

        file_name = os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(), file_name)


class QTrainer:
    """
    Trainer class for training the Q-learning neural network.

    Attributes:
    -----------
    lr : float
        Learning rate for the optimizer.
    gamma : float
        Discount factor for future rewards.
    model : nn.Module
        The Q-learning model to be trained.
    optimizer : torch.optim.Optimizer
        The optimizer used for training.
    criterion : torch.nn.MSELoss
        The loss function used for training.

    Methods:
    --------
    train_step(state, action, reward, next_state, done):
        Performs a single training step.
    """
    def __init__(self, model, lr, gamma):
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.optimizer = optim.Adam(model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()

    def train_step(self, state, action, reward, next_state, done):
        """
        Performs a single training step.

        Parameters:
        -----------
        state : list
            The current state of the environment.
        action : list
            The action taken.
        reward : list
            The reward received after taking the action.
        next_state : list
            The next state of the environment.
        done : list
            Indicates whether the episode is done.
        """
        state = torch.tensor(state, dtype=torch.float)
        next_state = torch.tensor(next_state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.long)
        reward = torch.tensor(reward, dtype=torch.float)
        # (n, x)

        if len(state.shape) == 1:
            # (1, x)
            state = torch.unsqueeze(state, 0)
            next_state = torch.unsqueeze(next_state, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            done = (done, )

        # 1: predicted Q values with current state
        pred = self.model(state)

        target = pred.clone()
        for idx in range(len(done)):
            Q_new = reward[idx]
            if not done[idx]:
                Q_new = reward[idx] + self.gamma * torch.max(self.model(next_state[idx]))

            target[idx][torch.argmax(action[idx]).item()] = Q_new
    
        # 2: Q_new = r + y * max(next_predicted Q value) -> only do this if not done
        # pred.clone()
        # preds[argmax(action)] = Q_new
        self.optimizer.zero_grad()
        loss = self.criterion(target, pred)
        loss.backward()

        self.optimizer.step()