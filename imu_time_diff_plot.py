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

def compute_time_differences(timestamps):
    time_intervals = np.diff(timestamps)
    return time_intervals

def plot_time_differences(time_intervals):
    time_indices = np.arange(len(time_intervals))
    
    plt.figure(figsize=(10, 5))
    # plt.scatter(time_indices, time_intervals * 1000, c='blue', marker='o', s=10)  # Convert time differences to ms
    plt.plot(time_indices, time_intervals * 1000)
    plt.xlabel('Sample Index')
    plt.ylabel('Time Difference (ms)')
    plt.title('Time Differences Between Consecutive IMU Messages')
    plt.grid()
    plt.show()

# Configuration
bag_file = '2024-08-06-15-32-46.bag'  
imu_topic = '/uavcanRosBridge/uavcan_ros_bridge/Imu' 

# Execution
timestamps = read_imu_timestamps(bag_file, imu_topic)
time_intervals = compute_time_differences(timestamps)
plot_time_differences(time_intervals)
