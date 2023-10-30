import torch
import pandas as pd

columns = []

def load_model():
    # load in model
    model = torch.load('model.model.pth')
    # set the model to eval mode
    model.eval()
    return model

def get_user_input(user_input_df):
    inputs = []
    for column in columns:
        value = input(f"Enter a value for {column}")
        inputs.append(value)
        return pd.DataFrame([inputs], columns=columns)