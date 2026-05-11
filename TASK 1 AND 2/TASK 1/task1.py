import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

print(f"Training samples: {x_train.shape[0]}")   
print(f"Test samples:     {x_test.shape[0]}")     
print(f"Image shape:      {x_train.shape[1:]}")   

# Normalize pixel values to [0, 1]
x_train, x_test = x_train / 255.0, x_test / 255.0

# (b) Build and train model to distinguish digits 0-9
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

# Evaluate on test set
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"\nTest accuracy: {test_acc:.4f}")

# Predict a few samples
predictions = model.predict(x_test[:5])
print("\nSample predictions:", np.argmax(predictions, axis=1))
print("Actual labels:     ", y_test[:5])