# -*- coding: utf-8 -*-
"""Assignment2 Q2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KZIxmiZr9ptXryRkCZnv0TQoxtuBlPfa
"""

#MODEL DEVELOPMENT
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam
def build_autoencoder(input_dim, encoding_dim=32):
    # Encoder
    input_layer = Input(shape=(input_dim,))
    encoded = Dense(encoding_dim, activation='relu')(input_layer)
    # Decoder
    decoded = Dense(input_dim, activation='sigmoid')(encoded)

    # Autoencoder Model
    autoencoder = Model(inputs=input_layer, outputs=decoded)
    optimizer=Adam(learning_rate=0.0001)
    # Compile the model
    autoencoder.compile(optimizer, loss='mse')
    return autoencoder

import numpy as np
labels = np.random.choice([0, 1], size=len(normalized_df), p=[0.7, 0.3])
normalized_df['labels'] = labels
normal_data = normalized_df[normalized_df['labels'] == 0]
normalized_df.head()

from sklearn.model_selection import train_test_split
train_data, val_data = train_test_split(normal_data, test_size=0.2, random_state=42)
# Convert to NumPy arrays for training
train_data = train_data.values
val_data = val_data.values

# Check for NaN or infinite values in your dataset
X_train=train_data
if np.any(np.isnan(X_train)) or np.any(np.isinf(X_train)):
    print("Input data contains NaN or infinite values. Cleaning the data.")
    X_train = np.nan_to_num(X_train)  # Replace NaN with 0 and inf with large numbers
train_data=X_train

X_val=val_data
if np.any(np.isnan(X_val)) or np.any(np.isinf(X_val)):
    print("Input data contains NaN or infinite values. Cleaning the data.")
    X_val = np.nan_to_num(X_val)  # Replace NaN with 0 and inf with large numbers
val_data=X_val

