# Load and explore the Uber dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Load the data
df = pd.read_csv('uber.csv', encoding='ascii')

print("Dataset shape:", df.shape)
print("\
Column names:")
print(df.columns.tolist())
print("\
First few rows:")
print(df.head())