import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
st.header("Vehicles_US Dashboard")

df = pd.read_csv('vehicles_us_clean.csv')
column_list = list(df.columns)
column_list.remove('Unnamed: 0')
column_list.remove('model')
column_list.remove('date_posted')

check = st.checkbox("Check to see data on dataframe and each field.")
check2 = st.checkbox("Check to see histograms on each field.")

if check:
    st.header("Stats")
    st.write(f"Number of duplicates in dataset: {df.duplicated().sum()}")
    st.write(f"Descriptive statistics on dataframe are found below:")
    st.write(df.describe())
    st.write("The number of null values for each field is included below:")
    st.write(df.isna().sum())
    st.write(f"The dataset was cleaned in the EDA (i.e. Exploratory Data Analysis) notebook hosted
             on Gihub. The initial data file and the cleaned data file are hosted there
             as well. Every piece of data in the streamlit app is based on the cleaned dataset.")

if check2:
    st.write(column_list)
    for i in column_list:
        try:
            fig, ax = plt.subplots()
            ax.hist(df[i], bins=50)
            plt.title(label=f'Count of Vehicles by {i.title()}')
            plt.xticks(rotation=45, ha='right')
            plt.xlabel(xlabel=f'{i}')
            plt.ylabel(ylabel='Count')
            st.pyplot(fig)
        except:
            pass
    st.write("Histograms for the index, date_posted, and model were unitelligeible and excised.")

     

st.header("Visualizations")
st.write(px.histogram(df, x='manufacturer', color='condition', title='Manufacturer of Car by Car Condition'))
st.write("The plurality of Chevrolet and Ford cars are listed as in excellent condition.")
st.write(px.histogram(df, x='manufacturer', color='type', title='Count of Cars by Manufacturer by Car Type'))
st.write("The plurality of Chevrolet and Ford cars trucks.")
st.write(px.histogram(df, x='days_listed', color='manufacturer', title='Days Listed per Car per Manufacturer'))
st.write("All manufacturers' days_listed field follow similar behaviors and peak around the same interval.")
st.write(px.histogram(df, x='price', color='manufacturer', title='Price per Car per Manufacturer'))
st.write("This is a relationship worth exploring but there's too much going on in this graph to tell much.")
st.write(px.histogram(df, x='days_listed', color='type', title='Days Listed per Car per Type'))
st.write("A similar distribution is shown accross car types especially the four main ones: SUV, pickup, sedan, and truck.")
st.write(px.histogram(df, x='price', color='type', title='Price of Car per Type'))
st.write("This is another busy graph. It is included for the sake of possible future exploration.")
st.write(px.histogram(df, x='days_listed', color='condition', title='Days Listed per Car Condition'))
st.write("Cars in excellent condition sell more and they sell more quickly than the other condition types.")
st.write(px.scatter(df, x='days_listed', y='price', title='Days Listed vs Price of Car'))
st.write("Most cars sell within 100 days irrespective of the price.")
st.write(px.scatter(df, y='odometer', x='price', title='Odometer Mileage vs Car Price'))
st.write("We can see a slowly sloping downward trend in odometer readout compared to price.")
st.write(px.histogram(df, x='days_listed', color='paint_color', title='Days Listed by Paint-color of Car'))
st.write("There does not seem to be different behaviors between colors.")
st.write(px.histogram(df, x='model_year', color='type', title="Count of Car's Model Year and Vehicle Type"))
st.write(px.histogram(df, x='model_year', color='cylinders', title="Count of Car's Model Year and Cylinders"))
st.write(px.histogram(df, x='model_year', color='condition', title='Model Year of Car by Condition'))
st.write(px.histogram(df, x='type', color='transmission', title='Type of Car Car by Transmission'))
st.write(px.histogram(df, x='days_listed', color='transmission', title='Days Listed by Car by Transmission'))
st.write("The number of automatic transmissions dwarves the other types at every point in this histogram. ")
st.write(px.histogram(df, x='model_year', color='paint_color', title='Model Year of Car by Paint Color'))
st.write("The relative distribution of colors seems consistent throughout the years.")

st.write(px.histogram(df, x='model_year', color='condition', title='Model Year of Car by Condition'))
st.write(px.histogram(df, x='type', color='transmission', title='Type of Car Car by Transmission'))
st.write(px.histogram(df, x='days_listed', color='transmission', title='Days Listed by Car by Transmission'))
st.write(px.histogram(df, x='model_year', color='paint_color', title='Model Year of Car by Paint Color'))
