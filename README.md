## flight_customer_prediction
This repository contains a Machine Learning model to predict customer satisfaction levels in the airline industry. The model takes into account various factors such as flight experience, in-flight services, customer demographics, and other relevant features to determine customer satisfaction levels (e.g., "Satisfied" or "Dissatisfied"). This project can be useful for airlines seeking to improve customer service by identifying key drivers of satisfaction and enhancing targeted areas.

## Table of Contents
1. Overview
2. Dataset
3. Features
4. Modeling
5. Requirements
6. Installation
7. Usage
8. Results
9. License

## Overview
This project aims to build a predictive model that accurately classifies customers as either satisfied or dissatisfied based on their feedback and details related to their flight. Airlines can use this model to predict customer sentiment and improve service in key areas.

## Dataset
The model was trained on a dataset containing customer reviews and related attributes for airline flights. The data includes both numerical and categorical features, such as age, travel type, class, flight distance, inflight service ratings, etc.

## Target Variable
Satisfaction: A binary label indicating whether the customer is "Satisfied" or "Dissatisfied".

## Features
Below are some key features used in the model:
Age: The age of the customer
Travel Type: Personal or Business travel
Delay minutes
Arrival minutes
Class: Economy, Business, or First class
Flight Distance: Total flight distance
Inflight Entertainment: Rating for entertainment options on board
Food and Drink: Rating for food and beverage quality
Customer Type: First-time flyer or returning customer

## Modeling
The model is developed using various machine learning algorithms, with a focus on accuracy and interpretability. Techniques like Decision Trees, Random Forests, and Gradient Boosting were explored. Feature importance analysis was also performed to identify key predictors of satisfaction.

## Requirements
Python 3.8+
Scikit-Learn
Pandas
NumPy
Matplotlib
Seaborn
Jupyter Notebook (optional for interactive exploration)
