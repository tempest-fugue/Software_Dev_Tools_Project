import pandas as pd
import matplotlib.pyplot as plt
import math
import scipy.stats as st
import plotly.express as px
df = pd.read_csv('/Users/ericmacdougall/Downloads/vehicles_us.csv')
df.info()
display(df.isna().sum() / len(df) * 100)
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
    display(df[i].value_counts().head(10))
    print('- - - - - - - - - - - - - - -')
new = df['model'].str.split(" ", n=1, expand=True)
df['manufacturer'] = new[0]
display(df.head(15))
df['manufacturer'].value_counts().plot(kind='bar', x='manufacturer', ylabel = 'Count', xlabel='manufacturer', title='Count of Vehicles by Manufacturer')
px.histogram(df, x='manufacturer', color='condition', title='Manufacturer of Car by Car Condition')
df['manufacturer'].nunique()
px.histogram(df, x='manufacturer', color='type', title='Count of Cars by Manufacturer by Car Type')
px.histogram(df, x='days_listed', color='manufacturer', title='Days Listed per Car per Manufacturer')
px.histogram(df, x='price', color='manufacturer', title='Price per Car per Manufacturer')
px.histogram(df, x='days_listed', color='type', title='Days Listed per Car per Type')
px.histogram(df, x='price', color='type', title='Price of Car per Type')
px.histogram(df, x='days_listed', color='condition', title='Days Listed per Car Condition')
px.scatter(df, x='days_listed', y='price', title='Days Listed vs Price of Car')
px.scatter(df, y='odometer', x='price', title='Odometer Mileage vs Car Price')
px.histogram(df, x='days_listed', color='paint_color', title='Days Listed by Paint-color of Car')
px.histogram(df, x='model_year', color='type', title="Count of Car's Model Year and Vehicle Type")
px.histogram(df, x='model_year', color='cylinders', title="Count of Car's Model Year and Cylinders")
px.histogram(df, x='model_year', color='condition', title='Model Year of Car by Condition')
px.histogram(df, x='type', color='transmission', title='Type of Car Car by Transmission')
px.histogram(df, x='days_listed', color='transmission', title='Days Listed by Car by Transmission')
px.histogram(df, x='model_year', color='paint_color', title='Model Year of Car by Paint Color')
