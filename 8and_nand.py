import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

# 1. DATASET PREPARATION
X_and = np.array([[0,0], [0,1], [1,0], [1,1]])
y_and = np.array([[0], [0], [0], [1]])

X_nand = np.array([[0,0], [0,1], [1,0], [1,1]])
y_nand = np.array([[1], [1], [1], [0]])

# 2. MODEL LOGIC
def create_and_train_model(X, y):
    model = Sequential([
        Dense(2, input_dim=2, activation='sigmoid'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X, y, epochs=5000, verbose=0)
    return model

# 3. TRAINING & PREDICTION
and_model = create_and_train_model(X_and, y_and)
print("AND Gate Predictions:", and_model.predict(X_and))

nand_model = create_and_train_model(X_nand, y_nand)
print("NAND Gate Predictions:", nand_model.predict(X_nand))

# 4. VISUALIZATION
def plot_predictions(model, X, title):
    predictions = model.predict(X)
    plt.figure()

    plt.scatter(X[:, 0], X[:, 1], c=predictions.flatten(), cmap='coolwarm', s=100)

    plt.title(title)
    plt.xlabel('Input 1'); 
    plt.ylabel('Input 2')

    plt.colorbar(label='Output')

    plt.xlim(-0.5, 1.5); 
    plt.ylim(-0.5, 1.5)

    plt.axhline(0.5, color='grey', lw=0.5, ls='--')
    plt.axvline(0.5, color='grey', lw=0.5, ls='--')
    
    plt.show()

plot_predictions(and_model, X_and, "AND Gate Predictions")
plot_predictions(nand_model, X_nand, "NAND Gate Predictions")