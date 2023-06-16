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

st.title("Sales Quantity of Furniture Category of the Store")

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

FurnitureSales_Data = data[data['Category'] == 'Furniture']

SalesQuantity_Fur=pd.crosstab(columns=FurnitureSales_Data['Year'],
                        index=FurnitureSales_Data['Month'],
                        values=FurnitureSales_Data['Sales'],
                        aggfunc='sum').melt()['value']

Months = ['Jan','Feb','Mar','Apr','May', 'Jun', 'Jul', 'Aug', 'Sep','Oct','Nov','Dec']*4
# SalesQuantity.plot(kind = 'line', figsize = (20, 8), title = 'Total Sales per month over the research period')
st.write("Total Sales per month over the research period")
Plot_Fur = Image.open("D:\HK20222\Decision_Support_System\Project\Project1/Plot_Fur.png")
st.image(image = Plot_Fur)

# Additive model
st.write("Additive model of Time series")
Plot_Fur_2 = Image.open("D:\HK20222\Decision_Support_System\Project\Project1/Plot_Fur_2.png")
st.image (image = Plot_Fur_2)
#ACF
st.write("ACF of Sales Quantity towards Furniture category")
st.pyplot(plot_acf(SalesQuantity_Fur[0:42], lags = 41))
#PACF
st.write("PACF of Sales Quantity towards Furniture category")
st.pyplot(plot_pacf(SalesQuantity_Fur[0:42]))

image = Image.open("D:\HK20222\Decision_Support_System\Project\Project1/figure_1_Fur.png")
st.write("Value and Prediction of Sales of Technology Category")
st.image(image=[image])

