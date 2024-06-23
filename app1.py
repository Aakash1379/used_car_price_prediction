import numpy as np
import joblib
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)


pipe4 = joblib.load("Car Price Prediction.pkl")

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_used_car_price(brand,year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,max_power,seats):
    
   
    prediction=pipe4.predict([[brand,year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,max_power,seats]])
    print(prediction)
    return prediction



def main():
    st.title("Used Car Price")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    brand = st.text_input("brand","Type Here")
    year = st.text_input("year","Type Here")
    km_driven = st.text_input("km_driven","Type Here")
    fuel = st.text_input("fuel","Type Here")
    seller_type = st.text_input("seller_type","Type Here")
    transmission = st.text_input("transmission","Type Here")
    owner = st.text_input("owner","Type Here")
    mileage = st.text_input("mileage","Type Here")
    engine = st.text_input("engine","Type Here")
    max_power = st.text_input("max_power","Type Here")
    seats = st.text_input("seats","Type Here")
    


    result=""
    if st.button("Predict"):
        result=predict_used_car_price(brand,year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,max_power,seats)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()