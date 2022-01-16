# CarLicensePlate-detection
This is the final project of Boston Global Education's Program. 
The goal is to detecte the car license plate from a car image.
Our Dataset is loaded by Kaggle:

https://www.kaggle.com/andrewmvd/car-plate-detection

We use faster R-CNN object detection algorithm to complete this task. This project should run by GPU. First, run voc_annotation.py to get the path and label for training, test set. Then run train.py to do training process. 

## environment
torch 1.9.0

torchvision 0.10.0
