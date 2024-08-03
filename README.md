# Fruit Classification using ML Models

## Project Overview
This project aims to classify different types of fruits using machine learning models. The objective is to build a model that can accurately identify the type of fruit based on images.

## Table of Contents
- [Project Overview](#project-overview)
- [Data](#data)
- [Methodology](#methodology)
- [Results](#results)
- [Applications](#applications)
- [Contact](#contact)

## Data
The dataset used for this project consists of images of different types of fruits. Each image is labeled with the type of fruit it represents. The dataset includes a variety of fruits such as apples, bananas, oranges, and more. There are a total of 10 categories in the target.

**Sample Images of class:  apple**
![image](https://github.com/user-attachments/assets/03414756-12e6-43f5-9fd4-e7efc7364e8a)
**Sample images of class:  avocado**
![image](https://github.com/user-attachments/assets/c512d751-26c6-4e20-b55f-18ce8b809c50)
**Sample images of class:  banana**
![image](https://github.com/user-attachments/assets/3b3edd41-dd51-4f05-9db9-ca35c3ac773f)
**Sample images of class:  cherry**
![image](https://github.com/user-attachments/assets/c2a97c83-998e-426c-a76f-7add5aff0831)
**Sample images of class:  kiwi**
![image](https://github.com/user-attachments/assets/55ad0b30-c69a-485a-a439-fc05dadbfd5f)
**Sample images of class:  mango**
![image](https://github.com/user-attachments/assets/98d4b43f-a213-4a5e-a843-d64e2372f50d)
**Sample images of class:  orange**
![image](https://github.com/user-attachments/assets/39795a11-ec72-4cb0-bbf4-cbed8e73d26f)
**Sample images of class:  pineapple**
![image](https://github.com/user-attachments/assets/cc2bb176-8e8b-4a96-b840-16deb0a10c9f)
**Sample images of class:  strawberries**
![image](https://github.com/user-attachments/assets/68ccdb7f-7bd0-4bfc-baee-111f98858f3c)
**Sample images of class:  watermelon**
![image](https://github.com/user-attachments/assets/36889401-d340-4d0c-9841-e0893488dbf5)

Link to dataset: https://www.kaggle.com/datasets/karimabdulnabi/fruit-classification10-class

## Methodology
The project implements Transfer Learning using pre-trained CNN of MobileNetV2 with ImageNet weights. No image preprocessing has been done. At the time of creation of data generators, the images are resized to an input shape of (224, 224, 3). The images are RGB (colored).

The architecture is as follows:

![image](https://github.com/user-attachments/assets/eaf3c882-11c3-4ac8-8ee6-c770d919b2aa)

## Results
The model attained a training accuracy of 97.70% and a testing accuracy of 67.22% in 23 epochs. These results demonstrate the model's ability to effectively classify different types of fruits based on images.

The model predictions are as follows: 

![image](https://github.com/user-attachments/assets/c8805d35-f06f-4a75-b6af-bf086303866e)

## Applications
This fruit classification model has several potential applications:
- **Automated Sorting Systems:** Can be used in agricultural and food industries for automated sorting of fruits.
- **Retail:** Helps in automating the identification and pricing of fruits in grocery stores.
- **Dietary Tracking:** Assists in dietary tracking apps to automatically identify and log fruits.

## Contact
For any questions or suggestions, please contact on LinkedIn: https://www.linkedin.com/in/siddiquizainab/
