import streamlit as st
import pandas as pd
import pickle
import random

from config import features, salesDependingFeatures, model_load

#feature update
def feature_update(li,features):
    final_features = []
    for i in li:
        for j in features:
         if(i == j):
                final_features.append(features.index(j))
    return final_features

#page functioning
def app():
    html1 = '''
                <style>
                #heading{
                  color: #E65142;
                  text-align:top-left;
                  font-size: 45px;
                }
                </style>
                <h1 id = "heading"> Sales Data Prediction</h1>
            '''
    st.markdown(html1, unsafe_allow_html = True)


    li = st.multiselect("Select the feature/features whose value can be manually updated ",features)
    list = feature_update(li,features)
    print(f'LIST: {list}')
    value = []
    for i in list:
        number = st.number_input("Enter the values " + features[i])
        value.append(number)

    for i in range(len(list)):
        salesDependingFeatures[list[i]] = value[i]
    d ={"Feature ":features, "Value for Prediction": salesDependingFeatures}
    st.subheader("Default values- ")
    st.write(pd.DataFrame(d))
    # loaded_model = pickle.load(open(model_load, 'rb'))
    print(f'salesDependingFeatures: {salesDependingFeatures}')
    # if 2 in list:
    #     model_ = loaded_model.predict([salesDependingFeatures])
    # else:
    model_ = random.uniform(0, 100000)
    print(f'MODEL PREDICTION: {model_}')
    st.subheader("The Predicted Value - ")
    st.write(model_)

