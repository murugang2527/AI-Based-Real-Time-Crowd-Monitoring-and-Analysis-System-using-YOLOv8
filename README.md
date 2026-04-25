# AI-Based-Real-Time-Crowd-Monitoring-and-Analysis-System-using-YOLOv8
AI-based real-time crowd monitoring system using YOLOv8 and OpenCV. Detects and counts people from webcam feed, displays live bounding boxes, and triggers alerts when crowd exceeds a limit. Includes real-time graph visualization for crowd analysis. Suitable for smart surveillance and safety applications.


# 1.Introduction

Crowd management is a critical aspect in public places such as railway stations, temples, shopping malls, and events. Overcrowding can lead to safety hazards, stampedes, and inefficient management of resources. With advancements in Artificial Intelligence (AI) and Computer Vision, automated crowd monitoring systems can be developed to address these challenges.

This project presents a real-time crowd monitoring and analysis system using YOLOv8 (You Only Look Once), a state-of-the-art object detection algorithm. The system detects humans using a webcam, counts them in real-time, and provides alerts when the crowd exceeds a predefined threshold.


# 2. Objectives


To develop a real-time human detection system using YOLOv8.
To count the number of people present in a given frame.
To generate alerts when crowd density exceeds a limit.
To visualize crowd data using graphs.
To provide a scalable solution for smart surveillance systems.


# 4. Literature Survey

Recent advancements in computer vision have enabled efficient crowd analysis. Traditional methods relied on manual observation or simple motion detection techniques, which were inaccurate and inefficient.

Modern approaches use deep learning models such as:

Convolutional Neural Networks (CNNs)
Region-based CNN (R-CNN)
YOLO (You Only Look Once)

Among these, YOLOv8 offers high accuracy and speed, making it suitable for real-time applications.


# 4. System Overview

The proposed system consists of the following components:

Camera (Webcam)
YOLOv8 Model
OpenCV for image processing
Alert system
Graph visualization module

The system captures video frames, processes them using YOLOv8, detects humans, counts them, and displays the results.


# 5. Methodology

Step 1: Video Capture

The webcam captures real-time video frames.

Step 2: Object Detection

Each frame is passed to the YOLOv8 model to detect objects.

Step 3: Human Identification

Only objects classified as "person" are considered.

Step 4: Counting

The number of detected persons is counted.

Step 5: Alert Generation

If the count exceeds a threshold, an alert is triggered.

Step 6: Data Visualization

The count is plotted over time using a graph.


# 6. Tools and Technologies
Programming Language: Python
Libraries:
Ultralytics YOLOv8
OpenCV
Matplotlib
Platform: VS Code


# 7. Implementation

The system is implemented using Python. The YOLOv8 model is used for object detection, while OpenCV handles video processing. Matplotlib is used for plotting the crowd data.

Key Features:
Real-time detection
Human counting
Alert system using sound
Graph visualization


# 8. Results and Discussion

The system successfully detects and counts humans in real-time. The alert mechanism works efficiently when the crowd exceeds the threshold. The graph provides a clear visualization of crowd variations over time.

# Advantages:

High accuracy
Real-time processing
Easy to implement

# Limitations:

Requires good lighting conditions
May count the same person multiple times


# 9. Applications


Crowd control in public places
Smart surveillance systems
Event management
Traffic monitoring
Smart city applications


# 10. Future Enhancements
Integration with IoT devices (ESP32)
Unique person tracking using DeepSORT
Mobile alerts (Telegram/Email)
Cloud data storage
Web dashboard for monitoring


# 11. Conclusion

The AI-based crowd monitoring system using YOLOv8 provides an efficient and scalable solution for real-time crowd analysis. It helps in improving safety, reducing risks, and enabling smart decision-making in public environments.

# 12. References
Ultralytics YOLOv8 Documentation
OpenCV Documentation
Research papers on crowd analysis and computer vision
