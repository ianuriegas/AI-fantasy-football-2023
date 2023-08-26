import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Define a simple neural network model using nn.Module


class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(7, 10)
        self.fc2 = nn.Linear(10, 5)
        self.fc3 = nn.Linear(5, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x


def get_qb_pytorch_stats(data):
    max_defense_rank = 32  # Assuming 32 is the worst rank
    max_offense_rank = 32  # Assuming 32 is the worst rank

    # Load data from CSV
    # df = pd.read_csv('data/position_data/rb.csv')
    df = pd.DataFrame(data)

    # Splitting features and target
    X = df[['opponent_defense_rank',
            'team_offense_rank',
            'weather_condition',
            'days_since_last_game',
            'avg_points',
            'is_home_game',
            'injury_status']]
    y = df['next_game_points']

    # Convert to PyTorch tensors
    X_tensor = torch.tensor(X.values, dtype=torch.float32)
    # Reshaping to align dimensions
    y_tensor = torch.tensor(y.values, dtype=torch.float32).view(-1, 1)

    player_selections = {}

    # Run the process 100 times
    for _ in range(100):
        # Instantiate the model and define loss and optimizer
        model = SimpleNN()
        criterion = nn.MSELoss()
        # Added learning rate
        optimizer = optim.Adam(model.parameters(), lr=0.001)

        # Train the model
        epochs = 100
        for epoch in range(epochs):
            optimizer.zero_grad()
            outputs = model(X_tensor)
            loss = criterion(outputs, y_tensor)
            loss.backward()
            optimizer.step()

        # Predict using the trained model
        predictions = model(X_tensor)

        # Adding predictions back to DataFrame
        df['predicted_points'] = predictions.detach().numpy()

        # Select the player with the highest predicted points
        selected_player = df.loc[df['predicted_points'].idxmax(),
                                 'player_name']

        if selected_player in player_selections:
            player_selections[selected_player] += 1
        else:
            player_selections[selected_player] = 1

    # Print the tally of player selections
    sorted_selections = sorted(player_selections.items(),
                               key=lambda x: x[1], reverse=True)
    # for player, count in sorted_selections:
    #     print(f"{player}: {count} times")

    print(sorted_selections)
    return sorted_selections


def get_rb_pytorch_stats(data):
    max_defense_rank = 32  # Assuming 32 is the worst rank
    max_offense_rank = 32  # Assuming 32 is the worst rank

    # Load data from CSV
    # df = pd.read_csv('data/position_data/rb.csv')
    df = pd.DataFrame(data)

    # Splitting features and target
    X = df[['opponent_defense_rank',
            'team_offense_rank',
            'weather_condition',
            'days_since_last_game',
            'avg_points',
            'is_home_game',
            'injury_status']]
    y = df['next_game_points']

    # Convert to PyTorch tensors
    X_tensor = torch.tensor(X.values, dtype=torch.float32)
    # Reshaping to align dimensions
    y_tensor = torch.tensor(y.values, dtype=torch.float32).view(-1, 1)

    player_selections = {}

    # Run the process 100 times
    for _ in range(100):
        # Instantiate the model and define loss and optimizer
        model = SimpleNN()
        criterion = nn.MSELoss()
        # Added learning rate
        optimizer = optim.Adam(model.parameters(), lr=0.001)

        # Train the model
        epochs = 100
        for epoch in range(epochs):
            optimizer.zero_grad()
            outputs = model(X_tensor)
            loss = criterion(outputs, y_tensor)
            loss.backward()
            optimizer.step()

        # Predict using the trained model
        predictions = model(X_tensor)

        # Adding predictions back to DataFrame
        df['predicted_points'] = predictions.detach().numpy()

        # Select the player with the highest predicted points
        selected_player = df.loc[df['predicted_points'].idxmax(),
                                 'player_name']

        if selected_player in player_selections:
            player_selections[selected_player] += 1
        else:
            player_selections[selected_player] = 1

    # Print the tally of player selections
    sorted_selections = sorted(player_selections.items(),
                               key=lambda x: x[1], reverse=True)
    # for player, count in sorted_selections:
    #     print(f"{player}: {count} times")

    print(sorted_selections)
    return sorted_selections


def get_wr_pytorch_stats(data):
    max_defense_rank = 32  # Assuming 32 is the worst rank
    max_offense_rank = 32  # Assuming 32 is the worst rank

    # Load data from CSV
    # df = pd.read_csv('data/position_data/rb.csv')
    df = pd.DataFrame(data)

    # Splitting features and target
    X = df[['opponent_defense_rank',
            'team_offense_rank',
            'weather_condition',
            'days_since_last_game',
            'avg_points',
            'is_home_game',
            'injury_status']]
    y = df['next_game_points']

    # Convert to PyTorch tensors
    X_tensor = torch.tensor(X.values, dtype=torch.float32)
    # Reshaping to align dimensions
    y_tensor = torch.tensor(y.values, dtype=torch.float32).view(-1, 1)

    player_selections = {}

    # Run the process 100 times
    for _ in range(100):
        # Instantiate the model and define loss and optimizer
        model = SimpleNN()
        criterion = nn.MSELoss()
        # Added learning rate
        optimizer = optim.Adam(model.parameters(), lr=0.001)

        # Train the model
        epochs = 100
        for epoch in range(epochs):
            optimizer.zero_grad()
            outputs = model(X_tensor)
            loss = criterion(outputs, y_tensor)
            loss.backward()
            optimizer.step()

        # Predict using the trained model
        predictions = model(X_tensor)

        # Adding predictions back to DataFrame
        df['predicted_points'] = predictions.detach().numpy()

        # Select the player with the highest predicted points
        selected_player = df.loc[df['predicted_points'].idxmax(),
                                 'player_name']

        if selected_player in player_selections:
            player_selections[selected_player] += 1
        else:
            player_selections[selected_player] = 1

    # Print the tally of player selections
    sorted_selections = sorted(player_selections.items(),
                               key=lambda x: x[1], reverse=True)
    # for player, count in sorted_selections:
    #     print(f"{player}: {count} times")

    print(sorted_selections)
    return sorted_selections


def get_te_pytorch_stats(data):
    max_defense_rank = 32  # Assuming 32 is the worst rank
    max_offense_rank = 32  # Assuming 32 is the worst rank

    # Load data from CSV
    # df = pd.read_csv('data/position_data/rb.csv')
    df = pd.DataFrame(data)

    # Splitting features and target
    X = df[['opponent_defense_rank',
            'team_offense_rank',
            'weather_condition',
            'days_since_last_game',
            'avg_points',
            'is_home_game',
            'injury_status']]
    y = df['next_game_points']

    # Convert to PyTorch tensors
    X_tensor = torch.tensor(X.values, dtype=torch.float32)
    # Reshaping to align dimensions
    y_tensor = torch.tensor(y.values, dtype=torch.float32).view(-1, 1)

    player_selections = {}

    # Run the process 100 times
    for _ in range(100):
        # Instantiate the model and define loss and optimizer
        model = SimpleNN()
        criterion = nn.MSELoss()
        # Added learning rate
        optimizer = optim.Adam(model.parameters(), lr=0.001)

        # Train the model
        epochs = 100
        for epoch in range(epochs):
            optimizer.zero_grad()
            outputs = model(X_tensor)
            loss = criterion(outputs, y_tensor)
            loss.backward()
            optimizer.step()

        # Predict using the trained model
        predictions = model(X_tensor)

        # Adding predictions back to DataFrame
        df['predicted_points'] = predictions.detach().numpy()

        # Select the player with the highest predicted points
        selected_player = df.loc[df['predicted_points'].idxmax(),
                                 'player_name']

        if selected_player in player_selections:
            player_selections[selected_player] += 1
        else:
            player_selections[selected_player] = 1

    # Print the tally of player selections
    sorted_selections = sorted(player_selections.items(),
                               key=lambda x: x[1], reverse=True)
    # for player, count in sorted_selections:
    #     print(f"{player}: {count} times")

    print(sorted_selections)
    return sorted_selections

def get_kicker_pytorch_stats(data):
    max_defense_rank = 32  # Assuming 32 is the worst rank
    max_offense_rank = 32  # Assuming 32 is the worst rank

    # Load data from CSV
    # df = pd.read_csv('data/position_data/rb.csv')
    df = pd.DataFrame(data)

    # Splitting features and target
    X = df[['opponent_defense_rank',
            'team_offense_rank',
            'weather_condition',
            'days_since_last_game',
            'avg_points',
            'is_home_game',
            'injury_status']]
    y = df['next_game_points']

    # Convert to PyTorch tensors
    X_tensor = torch.tensor(X.values, dtype=torch.float32)
    # Reshaping to align dimensions
    y_tensor = torch.tensor(y.values, dtype=torch.float32).view(-1, 1)

    player_selections = {}

    # Run the process 100 times
    for _ in range(100):
        # Instantiate the model and define loss and optimizer
        model = SimpleNN()
        criterion = nn.MSELoss()
        # Added learning rate
        optimizer = optim.Adam(model.parameters(), lr=0.001)

        # Train the model
        epochs = 100
        for epoch in range(epochs):
            optimizer.zero_grad()
            outputs = model(X_tensor)
            loss = criterion(outputs, y_tensor)
            loss.backward()
            optimizer.step()

        # Predict using the trained model
        predictions = model(X_tensor)

        # Adding predictions back to DataFrame
        df['predicted_points'] = predictions.detach().numpy()

        # Select the player with the highest predicted points
        selected_player = df.loc[df['predicted_points'].idxmax(),
                                 'player_name']

        if selected_player in player_selections:
            player_selections[selected_player] += 1
        else:
            player_selections[selected_player] = 1

    # Print the tally of player selections
    sorted_selections = sorted(player_selections.items(),
                               key=lambda x: x[1], reverse=True)
    # for player, count in sorted_selections:
    #     print(f"{player}: {count} times")

    print(sorted_selections)
    return sorted_selections

def get_defense_pytorch_stats(data):
    max_defense_rank = 32  # Assuming 32 is the worst rank
    max_offense_rank = 32  # Assuming 32 is the worst rank

    # Load data from CSV
    # df = pd.read_csv('data/position_data/rb.csv')
    df = pd.DataFrame(data)

    # Splitting features and target
    X = df[['opponent_defense_rank',
            'team_offense_rank',
            'weather_condition',
            'days_since_last_game',
            'avg_points',
            'is_home_game',
            'injury_status']]
    y = df['next_game_points']

    # Convert to PyTorch tensors
    X_tensor = torch.tensor(X.values, dtype=torch.float32)
    # Reshaping to align dimensions
    y_tensor = torch.tensor(y.values, dtype=torch.float32).view(-1, 1)

    player_selections = {}

    # Run the process 100 times
    for _ in range(100):
        # Instantiate the model and define loss and optimizer
        model = SimpleNN()
        criterion = nn.MSELoss()
        # Added learning rate
        optimizer = optim.Adam(model.parameters(), lr=0.001)

        # Train the model
        epochs = 100
        for epoch in range(epochs):
            optimizer.zero_grad()
            outputs = model(X_tensor)
            loss = criterion(outputs, y_tensor)
            loss.backward()
            optimizer.step()

        # Predict using the trained model
        predictions = model(X_tensor)

        # Adding predictions back to DataFrame
        df['predicted_points'] = predictions.detach().numpy()

        # Select the player with the highest predicted points
        selected_player = df.loc[df['predicted_points'].idxmax(),
                                 'player_name']

        if selected_player in player_selections:
            player_selections[selected_player] += 1
        else:
            player_selections[selected_player] = 1

    # Print the tally of player selections
    sorted_selections = sorted(player_selections.items(),
                               key=lambda x: x[1], reverse=True)
    # for player, count in sorted_selections:
    #     print(f"{player}: {count} times")

    print(sorted_selections)
    return sorted_selections
