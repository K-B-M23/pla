# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 12:38:01 2025

@author: BAPS
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 10:31:56 2025

@author: BAPS
"""

import numpy as np
import pickle
import streamlit as st
classifier=pickle.load(open('D:internship/savfiles/placement_models.sav','rb'))
def salary_prediction(input_data):
    input_data_arr=np.asarray(input_data)
    input_data_reshape=input_data_arr.reshape(1,-1)
    prediction=classifier.predict(input_data_reshape)
    return prediction
def main():
    st.title('Salary Prediction App')
    
    sl_no=st.text_input('Enter Student number')
    gender=st.text_input('Enter Gender(F:0,M:1)')
    ssc_p=st.text_input('Enter ssc percentage')
    ssc_b=st.text_input('Enter ssc b')
    hsc_p=st.text_input('Enter hsc percentage')
    hsc_b=st.text_input('Enter hsc b')
    hsc_s=st.text_input('Enter hsc s')
    degree_p=st.text_input('Enter degree p')
    degree_t=st.text_input('Enter degree t')
    workex=st.text_input('Enter Work exprecneie')
    etest_p=st.text_input('Enter etest_p')
    specialisation=st.text_input('Enter Specialiazation')
    mba_p=st.text_input('MBA')
    status=st.text_input('Enter status')
    salary=''
    if(st.button('Salary Prediction')):
        salary=salary_prediction([sl_no	,gender,	ssc_p,	ssc_b	,hsc_p	,hsc_b,	hsc_s	,degree_p,	degree_t	,workex,	etest_p,	specialisation,	mba_p,	status])
    st.success(salary)
main()
	