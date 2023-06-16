import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from streamlit_extras.switch_page_button import switch_page
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose, DecomposeResult
import plotly.tools as tls
from PIL import Image
import altair as alt

st.set_page_config(
    page_title="Decision Support System App",
    page_icon= "🤔",
    layout= "centered",
)

st.title("Sales Quantity of the Store")

def plot_seasonal_decompose(result:DecomposeResult, dates:pd.Series=None, title:str="Seasonal Decomposition"):
    x_values = dates if dates is not None else np.arange(len(result.observed))
    return (
        make_subplots(
            rows=4,
            cols=1,
            subplot_titles=["Observed", "Trend", "Seasonal", "Residuals"],
        )
        .add_trace(
            go.Scatter(x=x_values, y=result.observed, mode="lines", name='Observed'),
            row=1,
            col=1,
        )
        .add_trace(
            go.Scatter(x=x_values, y=result.trend, mode="lines", name='Trend'),
            row=2,
            col=1,
        )
        .add_trace(
            go.Scatter(x=x_values, y=result.seasonal, mode="lines", name='Seasonal'),
            row=3,
            col=1,
        )
        .add_trace(
            go.Scatter(x=x_values, y=result.resid, mode="lines", name='Residual'),
            row=4,
            col=1,
        )
        .update_layout(
            height=900, title=f'<b>{title}</b>', margin={'t':100}, title_x=0.5, showlegend=False
        )
    )

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

SalesQuantity =pd.crosstab(columns=data['Year'],
            index=data['Month'],
            values=data['Sales'],
            aggfunc='sum').melt()['value']

Months = ['Jan','Feb','Mar','Apr','May', 'Jun', 'Jul', 'Aug', 'Sep','Oct','Nov','Dec']*4
# SalesQuantity.plot(kind = 'line', figsize = (20, 8), title = 'Total Sales per month over the research period')
st.write("Total Sales per month over the research period")

# F = pd.DataFrame(SalesQuantity.values, columns = ['Sales Quantity'], index = Months)
# F['Months'] = Months
# # st.line_chart(F)
# chart = alt.Chart(F).mark_line().encode(
#             x=alt.X('Months', axis=alt.Axis(labelOverlap=False, grid=False)),
#             y=alt.Y('Sales Quantity'))
# st.altair_chart(chart, use_container_width=True)

image = Image.open("D:\HK20222\Decision_Support_System\Project\Project1/figure_1.png")
st.image(image=image)
plotLabels = plt.xticks(np.arange(0, 48, 1), Months, rotation = 90)

image_2 = Image.open("D:\HK20222\Decision_Support_System\Project\Project1/figure_2.png")
image_3 = Image.open("D:\HK20222\Decision_Support_System\Project\Project1/figure_3.png")
image_4 = Image.open("D:\HK20222\Decision_Support_System\Project\Project1/figure_4.png")
image_5 = Image.open("D:\HK20222\Decision_Support_System\Project\Project1/figure_5.png")
# Additive model
st.write("Additive model of Time series")
st.image(image = [image_2])
# ACF
st.write("ACF of Sales Quantity")
st.pyplot(plot_acf(SalesQuantity[0:42], lags = 41))
# PACF
st.write("PACF of Sales Quantity")
st.pyplot(plot_pacf(SalesQuantity[0:42], lags = 10))

st.write("Value and Prediction of Sales using SARIMAX Model")
st.image(image=[image_4])
st.write("Bar Chart for Sales of each category based on Years respectively")
st.image(image= image_5)

st.write("Bar chart for the Sales of Category")
st.bar_chart(data.groupby(['Category']).sum(numeric_only=True)['Sales'])

st.write("Bar chart for the Sales of Sub-Category")
st.bar_chart(data.groupby(['Sub-Category']).sum(numeric_only=True)['Sales'])
st.write("Which category do you choose: ")
Tech = st.button("Sales for Technology")
Fur = st.button("Sales for Furniture")
Off_Sup = st.button("Sales for Office Suppliers")
if Tech:
    switch_page("Technology")
elif Fur:
    switch_page("Furniture")
elif Off_Sup:
    switch_page("Office Suppliers")
