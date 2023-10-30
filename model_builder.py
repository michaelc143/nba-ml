import pandas as pd

# Replace 'nba_data.csv' with the actual path to your CSV file
df = pd.read_csv('nba23boxscores/basic.csv')

from sklearn.preprocessing import LabelEncoder, StandardScaler

# Fill missing values with 0
df.fillna(0, inplace=True)

# Convert categorical variables to numerical variables
label_encoder = LabelEncoder()

for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = label_encoder.fit_transform(df[column])

# Normalize the data
scaler = StandardScaler()
df_normalized = scaler.fit_transform(df)

import torch
import torch.nn as nn

class LinearRegression(nn.Module):
    def __init__(self, input_size):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(input_size, 1)

    def forward(self, x):
        return self.linear(x)

# Split the data into features (X) and target (y)
X = torch.tensor(df_normalized[:, :-1], dtype=torch.float32)
y = torch.tensor(df_normalized[:, -1], dtype=torch.float32)
y = y.squeeze()
# Create the model
model = LinearRegression(input_size=X.shape[1])

# Define the loss function and the optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Training loop
num_epochs = 100

for epoch in range(num_epochs):
    # Forward pass
    outputs = model(X)
    loss = criterion(outputs, y)

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Print loss for every 10 epochs
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# export model in evaluation mode to run predictions against model file
model.eval()
torch.save(model.state_dict(), "model.pth")