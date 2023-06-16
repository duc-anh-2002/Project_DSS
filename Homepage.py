import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import plotly.express as px
import import_ipynb
import matplotlib.pyplot as plt
# from  ipynb.fs.full.DSS_Sales import plotbarcharts   

st.set_page_config(
    page_title="Decision Support System App",
    page_icon= "😃",
    layout= "centered",
)

st.title("Main Page")

st.sidebar.success("\nSelect a page above.")
st.write("""Hi, my name is Duc Anh. I'm the creator of this App""")
st.write("""
We have created Web App integrated with Decision Support System about the anticipation of Super Store in the future
""")

# if "my_input" not in st.session_state:
#     st.session_state["my_input"] = ""

# my_input = st.text_input("Visualization Data", st.session_state["my_input"])
submit = st.button("Visualization Data")

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

columns_1 = ["Ship Mode", "Region"]
columns_2 = ["Category", "Sub-Category"]
columns_3 = ["Year", "Month"]
def plotbarcharts(dataset,columns):
    for column_name, plot_number in zip(columns, range(len(columns))):
        # .plot(kind = 'bar', ax = subplot[plot_number], color = colors, edgecolor = 'grey')
        st.write(f"\nBar chart for {column_name}")
        st.bar_chart(dataset[column_name].value_counts(ascending = True))
# fig = px.scatter(data, x="Sales", y="Year")
# fig.show()
if submit:   
        st.dataframe(data, width = 1000, height = 400)
        st.write("\nDescription of the Data\n")
        st.dataframe(data.columns)
        st.dataframe(data.describe(include = 'all'))
        ### Đồ thị theo bang
        plotbarcharts(data, columns_1)
        st.write("Bar chart for State")
        st.bar_chart(data.groupby(['State']).size()) 
        plotbarcharts(data, columns_2)
        plotbarcharts(data, columns_3)


