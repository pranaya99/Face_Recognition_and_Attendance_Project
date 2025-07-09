# Attendance Project utilising Facial Recognition with OpenCV

## Features

- Real-time face detection and recognition
- Automatic attendance recording to Excel with name and time of joining
- High accuracy facial recognition using deep learning
- Webcam integration for live processing

## How It Works

The system uses a 4-step pipeline:

1. **Face Detection**: Uses HOG (Histogram of Oriented Gradients) to locate faces in images
2. **Face Alignment**: Identifies 68 facial landmarks to normalize face pose and orientation
3. **Face Encoding**: Generates 128 unique measurements for each face using a pre-trained neural network
4. **Face Recognition**: Compares face encodings to identify known individuals

## Requirements

- Python 3.11
- OpenCV
- cmake
- dlib
- face-recognition
- face-recognition-models
- NumPy

## Installation

```bash
pip install opencv-python
pip install dlib
pip install face_recognition
pip install numpy
```

## Quick Start

1. Clone the repository
2. Install dependencies
3. Add reference images of people to recognize in the `ImagesAttendance` folder
4. Run the main script on PyCharm
   
## Usage

- After providing access to your webcam, it will be able to recognize what the webcam sees and record the time at which the webcam sees the identifier.
- Attendance data is saved to an Excel file


## Credits

Based on the OpenFace library and modern deep learning techniques for facial recognition.

## Resources
- [Machine Learning is Fun! Medium article](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78)
- [OpenFace Documentation](https://cmusatyalab.github.io/openface/)
- [Original Research Paper](https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Schroff_FaceNet_A_Unified_2015_CVPR_paper.pdf)
