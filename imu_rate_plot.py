#!/usr/bin/env python3

import rosbag
import numpy as np
import matplotlib.pyplot as plt

def read_imu_timestamps(bag_file, imu_topic):
    timestamps = []
    bag = rosbag.Bag(bag_file, 'r')
    
    for topic, msg, t in bag.read_messages(topics=[imu_topic]):
        timestamps.append(t.to_sec())
    
    bag.close()
    return timestamps

def compute_sample_rate(timestamps):
    time_intervals = np.diff(timestamps)
    sample_rates = 1.0 / time_intervals  
    return time_intervals, sample_rates

def plot_imu_rate(time_intervals, sample_rates):
    time_mid_points = np.cumsum(time_intervals)  # Midpoints in time
    sample_rate_ms = (1.0 / sample_rates) * 1000  # Convert Hz to ms

    plt.figure(figsize=(10, 5))
    plt.scatter(time_mid_points, sample_rate_ms, c='blue', marker='o')
    # plt.plot(time_mid_points, sample_rate_ms)
    plt.xlabel('Time (s)')
    plt.ylabel('Sample Rate (ms)')
    plt.title('IMU Sample Rate Over Time')
    plt.grid()
    plt.show()

# Configuration
bag_file = '2024-08-06-15-32-46.bag' 
imu_topic = '/uavcanRosBridge/uavcan_ros_bridge/Imu'  

# Execution
timestamps = read_imu_timestamps(bag_file, imu_topic)
time_intervals, sample_rates = compute_sample_rate(timestamps)
plot_imu_rate(time_intervals, sample_rates)