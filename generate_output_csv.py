import csv
import numpy as np

# Simulating data stream output
def generate_data_stream(num_points=100):
    data_stream = []
    for i in range(num_points):
        value = np.random.normal(50, 5)  # Normal value around 50 with small random variations
        is_anomaly = False

        # Introduce anomalies at random points
        if np.random.rand() < 0.1:  # 10% chance to be an anomaly
            value = np.random.normal(100, 10)  # Higher value for anomaly
            is_anomaly = True

        # Append data point with anomaly flag
        data_stream.append({"timestamp": i, "value": value, "is_anomaly": is_anomaly})

    return data_stream

# Save data to output.csv
def save_to_csv(data_stream, filename="output.csv"):
    # Define CSV header
    header = ["timestamp", "value", "is_anomaly"]

    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()  # Write the header row
        writer.writerows(data_stream)  # Write data rows

# Generate and save data stream
data_stream = generate_data_stream(100)
save_to_csv(data_stream)
print("Data saved to output.csv")