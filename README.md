# Real-Time Sign Language Detection (RTSLD)

This project uses TensorFlow and OpenCV to detect and interpret sign language gestures in real-time.

## Features
- Real-time detection of various sign language gestures
- Customizable to add more gestures
- Training and detection notebooks for setting up the model

## Project Structure
- **Image Collection.ipynb**: For collecting training images of different gestures.
- **Training and Detection.ipynb**: Used for training the model on the collected images and running detections.
- **app.py**: GUI application to start the sign language detection.
- **opencam.py**: Script for accessing the camera and running real-time detection.

## Installation
1. Clone the repository:
	
	git clone https://github.com/jodayyy/Real-Time-Sign-Language-Detection-RTSLD-.git

2. Navigate into the project folder:
	
	cd Real-Time-Sign-Language-Detection-RTSLD-

3. Install the required dependencies:

	pip install -r requirements.txt

Usage

Run app.py to start the GUI.

Use opencam.py for direct access to real-time detection without the GUI.