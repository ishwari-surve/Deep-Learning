# 11 Real-time Image Classification

## About
This program opens the webcam and classifies the object in front of it in real time.
It uses MobileNetV2, a ready-made CNN already trained on the ImageNet dataset (1000 classes).
The model is not trained in this program. It is only used for prediction.

## Steps
1. Load the pre-trained MobileNetV2 model.
2. Open the webcam using OpenCV.
3. Read one frame at a time.
4. Preprocess the frame:
   - Convert BGR to RGB.
   - Resize to 224x224.
   - Add a batch dimension.
   - Apply preprocess_input.
5. Predict the class using the model.
6. Decode the top prediction into a name and percentage.
7. Write the label on the video frame.
8. Press q to quit.

## Files
| File | What it does |
|---|---|
| 01_realtime_image_classification.py | Live webcam classification using pre-trained MobileNetV2 |

## Concepts covered
- Pre-trained CNN model (transfer of a trained model for direct use)
- cv2.VideoCapture, cap.read, cv2.imshow, cv2.waitKey
- cv2.cvtColor (BGR to RGB), cv2.resize
- np.expand_dims for the batch dimension
- preprocess_input and decode_predictions
- cv2.putText to show the label on the frame

## Requirements
- Python 3
- TensorFlow
- OpenCV (opencv-python)
- NumPy
- A working webcam
- Internet on the first run, to download the model weights

## Run
python 01_realtime_image_classification.py

Press q to close the webcam window.
