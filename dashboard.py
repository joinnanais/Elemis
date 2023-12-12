import streamlit as st
import pandas as pd
import datetime

# Set up date variables 

current_date = datetime.datetime.now()
next_year = current_date.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)


# Set up the landing page
st.set_page_config(
    page_title= "Sales Dashboard",
    page_icon= ":bar_chart:",
    layout = "wide"
)

#Create a file path
csv_file_path = 'C:\\Users\\joinna.patiag\\OneDrive - Elemis Ltd\\Documents\\Scripts\\Sprint 13\\Sample - Superstore.csv'

#Read csv file and select encoding 
data = pd.read_csv(csv_file_path, encoding='latin1')

df = pd.DataFrame(data)

#Print dataframe
print(df)

# Assuming df is your DataFrame

category_filter = st.selectbox("Filter by Category", pd.unique(df["Category"]))
subcategory_filter = st.selectbox("Filter by Sub-Category", pd.unique(df["Sub-Category"]))

