# Sign Language Recognition using Deep Learning
> A system to recognize American Sign language from a custom generated dataset.

## Table of contents
* [General info](#general-info)
* [Dataset](#dataset)
* [Screenshots](#screenshots)
* [Technologies and Tools](#technologies-and-tools)
* [Setup](#setup)
* [Models](#features)
* [Status](#status)

## General Info

## Dataset
Link to Dataset - [Link](https://drive.google.com/drive/u/0/folders/1xN_20z27PJDt9bASUOHGIELpJjTtZyMl). 
Kaggle Link - [Link](https://www.kaggle.com/datasets/joannracheljacob/american-sign-language-dataset).

## Technologies and Tools
* Python 
* TensorFlow
* Keras
* OpenCV

## Setup

data_collection.py can be run to capture data for each class using the command python data_collection.py 

Trained model h5 file link - [Link](https://drive.google.com/file/d/1ZSEqRN4lgzfp_1_6nQ_4nlzq5rZ7DSeD/view?usp=sharing)

1. Add the h5 model on kaggle as a dataset into the input directory.
2. Add the dataset from kaggle itself using this link - [Link](https://www.kaggle.com/datasets/joannracheljacob/american-sign-language-dataset)
3. 


## Models

* Simple CNN model using Sign Language MNIST dataset
* Simple CNN model using ASL Kaggle dataset
* VGG16 using ASL Kaggle dataset
* ResnNet50 using ASL Kaggle dataset
* ResNet50 using Custom ASL Dataset
