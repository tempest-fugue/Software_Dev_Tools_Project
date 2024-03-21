import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
st.header("Vehicles_US Dashboard")

df = pd.read_csv('vehicles_us_clean.csv')
column_list = list(df.columns)
check = st.checkbox("Check to see data on dataframe and each field.")
if check:
    st.header("Stats")
    st.write(f"Number of duplicates in dataset: {df.duplicated().sum()}")
    st.write(f"Descriptive statistics on dataframe are found below:")
    st.write(df.describe())
    st.write("The number of null values for each field is included below:")
    st.write(df.isna().sum())
check2 = st.checkbox("Check to see histograms on each field.")
if check2:
    for i in column_list:
        try:
            st.plotly(df[i].plot(kind='hist', xlabel=f'{i}', ylabel='Count', x=f'{i}', title=f'Count of Vehicles by {i.title()}', bins=50))
        except:
           pass

st.header("Visualizations")
st.write(px.histogram(df, x='manufacturer', color='condition', title='Manufacturer of Car by Car Condition'))
st.write(px.histogram(df, x='manufacturer', color='type', title='Count of Cars by Manufacturer by Car Type'))
st.write(px.histogram(df, x='days_listed', color='manufacturer', title='Days Listed per Car per Manufacturer'))
st.write(px.histogram(df, x='price', color='manufacturer', title='Price per Car per Manufacturer'))
st.write(px.histogram(df, x='days_listed', color='type', title='Days Listed per Car per Type'))
st.write(px.histogram(df, x='price', color='type', title='Price of Car per Type'))
st.write(px.histogram(df, x='days_listed', color='condition', title='Days Listed per Car Condition'))
st.write(px.scatter(df, x='days_listed', y='price', title='Days Listed vs Price of Car'))
st.write(px.scatter(df, y='odometer', x='price', title='Odometer Mileage vs Car Price'))
st.write(px.histogram(df, x='days_listed', color='paint_color', title='Days Listed by Paint-color of Car'))
st.write(px.histogram(df, x='model_year', color='type', title="Count of Car's Model Year and Vehicle Type"))
st.write(px.histogram(df, x='model_year', color='cylinders', title="Count of Car's Model Year and Cylinders"))
st.write(px.histogram(df, x='model_year', color='condition', title='Model Year of Car by Condition'))
st.write(px.histogram(df, x='type', color='transmission', title='Type of Car Car by Transmission'))
st.write(px.histogram(df, x='days_listed', color='transmission', title='Days Listed by Car by Transmission'))
st.write(px.histogram(df, x='model_year', color='paint_color', title='Model Year of Car by Paint Color'))
