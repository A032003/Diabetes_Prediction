import numpy as np
import streamlit as st
import pickle 


loaded_model = pickle.load(open('C:/Users/91885/OneDrive/Desktop/lab3/Diabetes_Prediction/trained_model.sav', 'rb'))

def diabetes_prediction(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)
    
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    
    print(prediction)
    
    if (prediction[0] == 0):
        return 'The person is not Diabetic'
    else:
        return 'The person is Diabetic'
        

def main():
    st.title("Diabetes Prediction")
 			
    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose=st.text_input('Glucose Level')
    BloodPressure=st.text_input('Blood Pressure Level')
    SkinThickness=st.text_input('SkinThickness Value')
    Insulin=st.text_input('Insulin Level')
    BMI=st.text_input('BMI Value')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function')
    Age=st.text_input('Age of the Person')
    
    diagnosis=''
    
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
        st.success(diagnosis)
        
if __name__=='__main__':
    main()        
        
    
    
    
    
    
            