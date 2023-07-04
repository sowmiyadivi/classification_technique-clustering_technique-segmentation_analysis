# -*- coding: utf-8 -*-
"""CLASSIFICATION TECHNIQUE FOR ADMISSION PREDICTION DATASET.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kx1imKpaFRS-a_znD-UcMO4abyFVaKkq
"""

!pip install scikit-learn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix


# Load your dataset
data = pd.read_csv('Admission_Predict.csv')

# Split the dataset into features (X) and target variable (y)
data = pd.DataFrame({'Chance of Admit': [0.8, 0.7, 0.9], 'GRE Score': [320, 310, 330]})

X = data.drop('Chance of Admit', axis=1)
y = data['Chance of Admit']

# Check the unique classes in y
unique_classes = y.unique()
num_classes = len(unique_classes)

if num_classes < 2:
    raise ValueError("The number of classes has to be greater than one; got 1 class")

# Convert the target variable to numeric labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an instance of the Decision Tree classifier
classifier = DecisionTreeClassifier()

# Train the classifier on the training data
classifier.fit(X_train, y_train)

# Perform predictions on the test set
y_pred = classifier.predict(X_test)

# Evaluate the model
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))