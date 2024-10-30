# Libraries Which I Used:
from collections import deque
import random
import numpy as np
import matplotlib.pyplot as plt

# Parameters
window_size = 100  # Rolling window size for anomaly detection
stream_len = 1000  # Length of the data stream
Z_score_threshold = 1.5  # Lowered threshold for easier detection

# Data stream generator
def generate_data_point(i):
    seasonal_pattern = 10 * np.sin(2 * np.pi * i / 50)  # Seasonal pattern
    noise_gaussian = np.random.normal(0, 2)  # Gaussian noise
    anomaly = random.choice([0, 0, 0, 0, 25])  # Increased chance of anomaly

    if anomaly > 0:  # Print if an anomaly is generated
        print(f"Anomaly generated at index {i}: {anomaly}")

    return seasonal_pattern + noise_gaussian + anomaly

# Real-time anomaly detection
def detect_anomaly(data, window):
    if len(window) < window_size:
        return False  # Not enough data points
    mean = np.mean(window)
    std_dev = np.std(window)

    if std_dev == 0:  # Prevent division by zero
        return False

    z_score = abs((data - mean) / std_dev)
    print(f"Data: {data}, Mean: {mean}, Std Dev: {std_dev}, Z-Score: {z_score}")  # Debugging output
    return z_score > Z_score_threshold

# Plot setup
plt.ion()
fig, ax = plt.subplots()
data_stream, anomalies = [], []

# Rolling window for storing recent data points
window = deque(maxlen=window_size)

# Main streaming loop
for i in range(stream_len):
    # Force an anomaly for testing every 50th iteration
    if i % 50 == 0:
        data_point = 50 + np.random.normal(20, 5)  # A clear anomaly
    else:
        data_point = generate_data_point(i)

    window.append(data_point)
    data_stream.append(data_point)

    # Detect anomalies
    is_anomaly = detect_anomaly(data_point, window)
    if is_anomaly:
        anomalies.append(data_point)
    else:
        anomalies.append(np.nan)

    # Update the plot
    ax.clear()
    ax.plot(data_stream, label='Data Stream')
    ax.plot(anomalies, 'ro', label='Anomalies')
    ax.legend()
    plt.pause(0.05)

plt.ioff()
plt.show()
