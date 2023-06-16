import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_extras.switch_page_button import switch_page
import numpy as np
from PIL import Image
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

st.set_page_config(
    page_title="Decision Support System App",
    page_icon= "🤔",
    layout= "centered",
)

st.title("Sales Quantity of Technology Category of the Store")

# Data preprocessing
url = "D:\HK20222\Decision_Support_System\Project\Project1"
data = pd.read_csv(url + "\Sample - Superstore.csv", encoding='windows-1252')
data.drop(columns = 'Row ID', axis = 1, inplace = True)
data['Order Date'] = pd.to_datetime(data['Order Date'], format= '%m/%d/%Y')
# Function to get month from a date
def Function_get_month(inpDate):
    return(inpDate.month)

# Function to get Year from a date
def Function_get_year(inpDate):
    return(inpDate.year)
# Creating new columns
data['Month']=data['Order Date'].apply(Function_get_month)
data['Year']=data['Order Date'].apply(Function_get_year)

TechnologySales_Data = data[data['Category'] == 'Technology']

SalesQuantity_Tech=pd.crosstab(columns=TechnologySales_Data['Year'],
                        index=TechnologySales_Data['Month'],
                        values=TechnologySales_Data['Sales'],
                        aggfunc='sum').melt()['value']

Months = ['Jan','Feb','Mar','Apr','May', 'Jun', 'Jul', 'Aug', 'Sep','Oct','Nov','Dec']*4
# SalesQuantity.plot(kind = 'line', figsize = (20, 8), title = 'Total Sales per month over the research period')
st.write("Total Sales per month over the research period")
# st.line_chart(SalesQuantity_Tech.values, x= Months)
Plot_Tech = Image.open("D:\HK20222\Decision_Support_System\Project\Project1/Plot_Tech.png")
st.image(image = Plot_Tech)

# Additive model
st.write("Additive model of Time series")
Plot_Tech_2 = Image.open("D:\HK20222\Decision_Support_System\Project\Project1/Plot_Tech_2.png")
st.image (image = Plot_Tech_2)
#ACF
st.write("ACF of Sales Quantity towards Technology category")
st.pyplot(plot_acf(SalesQuantity_Tech[0:42], lags = 41))
#PACF
st.write("PACF of Sales Quantity category")
st.pyplot(plot_pacf(SalesQuantity_Tech[0:42]))

image = Image.open("D:\HK20222\Decision_Support_System\Project\Project1/figure_1_Tech.png")
st.write("Value and Prediction of Sales of Technology Category")
st.image(image=[image])

