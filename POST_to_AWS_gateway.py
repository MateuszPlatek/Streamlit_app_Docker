"""
Created on Tue Dec 24 12:31:52 2024
First Streamlit app
@author: M Platek
"""


import streamlit as st
import pandas as pd
# =============================================================================
# from sklearn import datasets
# from sklearn.ensemble import RandomForestClassifier
# =============================================================================
import requests
import json
import ast



st.write("""
# Simple Iris Flower Prediction App

This app predicts the **Iris flower** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'x1': sepal_length,
             'x2': sepal_width,
             'x3': petal_length,
             'x4': petal_width}
    #features = pd.DataFrame(data, index=[0])
    return data

input = user_input_features()
#df = user_input_features()

URL = "https://99p97o6c3a.execute-api.us-east-1.amazonaws.com/dev"

# =============================================================================
# data = {'x1': 7,
#         'x2': 4.2,
#         'x3': 3.1,
#         'x4': 1.4}
# =============================================================================
data_json = json.dumps(input)

r = requests.post(URL, data_json)
# print(r)
# ast.literal_eval(r.text)['prediction']

st.subheader('User Input parameters')
st.write(pd.DataFrame(input, index=[0]))

# =============================================================================
# iris = datasets.load_iris()
# X = iris.data
# Y = iris.target
# 
# clf = RandomForestClassifier()
# clf.fit(X, Y)
# 
# prediction = clf.predict(df)
# prediction_proba = clf.predict_proba(df)
# =============================================================================

target_names = ['setosa', 'versicolor', 'virginica']
st.subheader('Class labels and their corresponding index number')
st.write(target_names)

st.subheader('Prediction')
st.write(ast.literal_eval(r.text)['prediction'])
#st.write(prediction)

# =============================================================================
# st.subheader('Prediction Probability')
# st.write(prediction_proba)
# =============================================================================

