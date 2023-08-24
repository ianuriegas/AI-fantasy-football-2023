import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

max_defense_rank = 32  # Assuming 32 is the worst rank
max_offense_rank = 32  # Assuming 32 is the worst rank

# Create mock data using pandas
data = {
    'player_name': ['Trevor Lawrence', 'Anthony Richardson'],
    'opponent_defense_rank': [max_defense_rank - 23 + 1, max_defense_rank - 15 + 1],
    'team_offense_rank': [max_offense_rank - 9 + 1, max_offense_rank - 27 + 1],
    'weather_condition': [0, 1],
    'days_since_last_game': [0, 0],
    'player_past_avg_points': [17.6, 16.3],
    'is_home_game': [0, 1],
    'injury_status': [0, 0],
    'next_game_points': [18.5, 17.1]
}

df = pd.DataFrame(data)

# Splitting features and target
X = df[['opponent_defense_rank',
        'team_offense_rank',
        'weather_condition',
        'days_since_last_game',
        'player_past_avg_points',
        'is_home_game',
        'injury_status']]
y = df['next_game_points']

# Convert to PyTorch tensors
X_tensor = torch.tensor(X.values, dtype=torch.float32)
# Reshaping to align dimensions
y_tensor = torch.tensor(y.values, dtype=torch.float32).view(-1, 1)

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


player_selections = {}

# Run the process 100 times
for _ in range(100):
    # Instantiate the model and define loss and optimizer
    model = SimpleNN()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)  # Added learning rate

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
    selected_player = df.loc[df['predicted_points'].idxmax(), 'player_name']

    if selected_player in player_selections:
        player_selections[selected_player] += 1
    else:
        player_selections[selected_player] = 1

# Print the tally of player selections
sorted_selections = sorted(player_selections.items(),
                           key=lambda x: x[1], reverse=True)
for player, count in sorted_selections:
    print(f"{player}: {count} times")
