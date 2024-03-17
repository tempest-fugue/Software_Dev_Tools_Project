import pandas as pd
import matplotlib.pyplot as plt
import math
import scipy.stats as stats
import plotly.express as px
import streamlit as st
st.header("hello Worldies")

df = pd.read_csv('vehicles_us.csv')
df.info()
print(df.isna().sum() / len(df) * 100)
"The above represents the percent of null values in each dataframe field."
df.duplicated().sum()
df.sample(10)
df.describe()
column_list = df.columns.to_list()
for i in column_list:
    try:
        df[i].plot(kind='hist', xlabel=f'{i}', ylabel='Count', x=f'{i}', title=f'Count of Vehicles by {i.title()}', bins=50)
        plt.show()
    except:
       pass
for i in column_list:
    print(f"The number of unique values for the {i} field: {df[i].nunique()}")
    print(df[i].value_counts().head(10))
    print('- - - - - - - - - - - - - - -')
new = df['model'].str.split(" ", n=1, expand=True)
df['manufacturer'] = new[0]
st.write(df.head(15))
st.write(df['manufacturer'].value_counts().plot(kind='bar', x='manufacturer', ylabel = 'Count', xlabel='manufacturer', title='Count of Vehicles by Manufacturer'))
st.write(px.histogram(df, x='manufacturer', color='condition', title='Manufacturer of Car by Car Condition'))
st.write(df['manufacturer'].nunique())
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
