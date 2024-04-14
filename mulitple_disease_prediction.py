# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 16:56:08 2024

@author: seeni
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved models

diabetes_model = pickle.load(open('C:\Users\seeni\OneDrive\Desktop\Re_Project\diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:\Users\seeni\OneDrive\Desktop\Re_Project\heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('C:\Users\seeni\OneDrive\Desktop\Disease Prediction\Project File disease\parkinsons_model.sav', 'rb'))

# sidebar for navigate

with st.sidebar:
    selected = option_menu('mulitple_disease_prediction',
                            ['Diabetes Prediction',
                             'Heart Disease Prediction', 
                             'Parkinsons Prediction'],
                            default_index = 0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        gender_options = ['0', '1']
        gender = st.selectbox('Gender [0 - Male, 1 - Female]', gender_options)


    with col2:
        age = st.text_input('Age ')

    with col3:
        bp_options = ['0', '1']
        BloodPressure = st.selectbox('Hypertension [0 - <130/80, 1 - >130/80]', bp_options)

    with col1:
        heart_options = ['0', '1']
        heart = st.selectbox('Heart_Disease [0 - Absence, 1 - Presence]', heart_options)


    with col2:
        smoke_options = ['0', '1']
        smoke = st.selectbox('Smoking_History [0 - No, 1 - Yes]', heart_options)


    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        Hb = st.text_input('HbA1c_Level')

    with col2:
        glu = st.text_input('Blood_Glucose_Level')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [gender, age, BloodPressure, heart, smoke,
                      BMI, Hb, glu]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex_options = ['0', '1']
        sex = st.selectbox('Gender [0 - Male, 1 - Female]', sex_options)


    with col3:
        cp_options = ['1', '2', '3', '4']
        cp = st.selectbox('Chest Pain types [1 - Angina, 2 - Pericarditis, 3 - Myocarditis, 4 - Cardiomyopathy]', cp_options)
            

    with col1:
        trestbps = st.text_input('Systolic Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs_options = ['0', '1']
        fbs = st.selectbox('Fasting Blood Sugar [0 - <120 mg/dl, 1 - >120 mg/dl]', fbs_options)

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang_options = ['0', '1']
        exang = st.selectbox('Exercise Induced Angina [0 - Normal, 1 - Abnormal]', exang_options)

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('Thallium Scan')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == "Presence":
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP RAP')

    with col2:
        PPQ = st.text_input('MDVP PPQ')

    with col3:
        DDP = st.text_input('Jitter DDP')

    with col4:
        Shimmer = st.text_input('MDVP Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer APQ5')

    with col3:
        APQ = st.text_input('MDVP APQ')

    with col4:
        DDA = st.text_input('Shimmer DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)


