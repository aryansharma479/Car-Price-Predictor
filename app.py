import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st

model=pk.load(open('model.pkl','rb'))
st.header('CAR PRICE PREDICTION IN ML MODEL')

cars_data=pd.read_csv('Cardetails.csv')
#cars_data.drop(columns=['index'],inplace=True)
def getBrandName(car_name):
    car_name=car_name.split(' ')[0]
    #print(car_name)
    return car_name.strip()              
cars_data['name']=cars_data['name'].apply(getBrandName) 
models=cars_data['name'].unique()    
fuel=cars_data['fuel'].unique()
seller_type=cars_data['seller_type'].unique() 
transmission_type=cars_data['transmission'].unique()  
owner=cars_data['owner'].unique()

name=st.selectbox('Select Car Brand',models)
year=st.slider('Car Manufacture Year',1994,2024)
km_driven=st.slider('Number of Kms Driven',11,200000)
fuel=st.selectbox('Fuel Type',fuel)
seller_type=st.selectbox('Seller Type',seller_type)
transmission=st.selectbox('Transmission Type',transmission_type)
owner=st.select_slider('Owner',owner)
mileage=st.slider('Car Mileage',10,40)
engine=st.slider('Engine CC',700,5000)
max_power=st.slider('Max Power',0,200)
seats=st.slider('Number Of Seats',5,10)

if st.button("PREDICT PRICE"):
    input_data_model=pd.DataFrame([[name,year,km_driven,fuel,seller_type,transmission,owner,mileage,
                                    engine,max_power,seats]],
                                    columns=['name','year','km_driven','fuel','seller_type',
                                    'transmission','owner','mileage','engine','max_power','seats'])
    
    input_data_model['fuel'].replace(['Diesel', 'Petrol', 'LPG', 'CNG'],[1,2,3,4],inplace=True)
    input_data_model['name'].replace(['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
       'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
       'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
       'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
       'Ambassador', 'Ashok', 'Isuzu', 'Opel'],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
                          inplace=True)
    input_data_model['transmission'].replace(['Manual', 'Automatic'],[1,2],inplace=True)
    input_data_model['seller_type'].replace(['Individual', 'Dealer', 'Trustmark Dealer'],[1,2,3],inplace=True)
    input_data_model['owner'].replace(['First Owner','Second Owner','Third Owner','Fourth & Above Owner',
                            'Test Drive Car'],[1,2,3,4,5],inplace=True)
    
    car_price= model.predict(input_data_model)
    st.markdown('Car Price Is Gonna Be: '+str(car_price[0]))