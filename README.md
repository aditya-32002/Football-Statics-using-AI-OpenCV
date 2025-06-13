# Football Analysis Project
# Introduction
The goal of this project is to detect and track players, referees, and footballs in a video using YOLO, one of the best AI object detection models available. We will also train the model to improve its performance. Additionally, we will assign players to teams based on the colors of their t-shirts using Kmeans for pixel segmentation and clustering. With this information, we can measure a team's ball acquisition percentage in a match. We will also use optical flow to measure camera movement between frames, enabling us to accurately measure a player's movement. Furthermore, we will implement perspective transformation to represent the scene's depth and perspective, allowing us to measure a player's movement in meters rather than pixels. Finally, we will calculate a player's speed and the distance covered. This project covers various concepts and addresses real-world problems, making it suitable for both beginners and experienced machine learning engineers.
 
# Standard YOLO without trained
![image](https://github.com/user-attachments/assets/ee67d2e7-046e-4f2a-b4e6-02f9cb09c0e6)
# Final Form
![image](https://github.com/user-attachments/assets/c6238c52-16b4-4f5c-838d-eb86131bc9d7)
# Modules Used
The following modules are used in this project:

- YOLO: AI object detection model
- Kmeans: Pixel segmentation and clustering to detect t-shirt color
- Optical Flow: Measure camera movement
- Perspective Transformation: Represent scene depth and perspective
- Speed and distance calculation per player

# Final Project Video
- <a href = "https://drive.google.com/file/d/1EQL2UW2PzMpeCtrJdHwq-fxGhDoMhBkP/view?usp=drive_link">CLick To play </a>
# Requirements
To run this project, you need to have the following requirements installed:

- Python 3.x
- ultralytics
- supervision
- OpenCV
- NumPy
- Matplotlib
- Pandas
