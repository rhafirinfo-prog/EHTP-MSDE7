#app for the 2 options : input parameters or load data file

import streamlit as st
import pandas as pd
import pickle

st.image("http://www.ehtp.ac.ma/images/lo.png")
st.write("""
## MSDE : ML Course
### Iris Flower Prediction App
This app predicts the **Iris flower** type
""")

st.sidebar.image("https://cdn.britannica.com/39/91239-004-44353E32/Diagram-flowering-plant.jpg",width=300)

option = st.selectbox(
     'How would you like to use the prediction model?',
     ('','input parameters directly', 'Load a file of data'))

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.0, 8.0, 5.0)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 5.0, 3.0)
    petal_length = st.sidebar.slider('Petal length', 1.0, 7.0, 2.0)
    petal_width = st.sidebar.slider('Petal width', 0.1, 3.0, 0.5)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

def show_results():
    st.subheader('User Input Parameters: ')
    st.write(df)
    model_iris=pickle.load(open("modeliris6.pkl", "rb"))
    prediction = model_iris.predict(df)
    prediction_proba = model_iris.predict_proba(df)

    st.subheader('Class labels and their corresponding index number')
    st.write(pd.DataFrame(model_iris.classes_))

    st.subheader('Prediction')
    st.write(prediction)

    st.subheader('Prediction Probability')
    st.write(prediction_proba)
  
if option=='input parameters directly':
    st.sidebar.header('User Input Parameters')
    df = user_input_features()
    show_results()    
    
elif option=='Load a file of data':
    uploaded_file = st.file_uploader("Choose a file to load")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file,header=None)
        show_results()
    


