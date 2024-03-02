import numpy as np
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the parameters
input_size = X_train.shape[1]
output_size = len(np.unique(y_train))
learning_rate = 0.01
epochs = 100

# Define the softmax approximation using linear Taylor expansion
def approx_softmax(x):
    linear_term = tf.reduce_max(x, axis=1, keepdims=True)
    shifted_x = x - linear_term
    softmax_values = shifted_x / tf.reduce_sum(shifted_x, axis=1, keepdims=True)
    return softmax_values

# Define the single-layer neural network with linear activation (approximated softmax)
model = tf.keras.Sequential([
    tf.keras.layers.Dense(output_size, input_shape=(input_size,), activation=approx_softmax)
])

# Compile the model
model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=epochs, batch_size=4, verbose=1)

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f'Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}')
