import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import plotly as px
from streamlit.hello.utils import show_code
import altair as alt

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Sales Dashboard",
        page_icon=":bar_chart:",
    )

    st.write("# Sales Dashboard :bar_chart:")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        This is a prototype dashboard to demonstrate the concept of Streamlit for CDP purposes.
        

        The data is from an open-source.
        
        
        The data used is a sample data from Kaggle.
        """
    )

if __name__ == "__main__":
    run()

github_csv_url = 'https://raw.githubusercontent.com/joinnanais/Elemis/main/Sample%20-%20Superstore.csv'
df = pd.read_csv(github_csv_url, encoding='latin1')

st.sidebar.header("Filters")

# Select category filter
category_filter = st.sidebar.multiselect("Select Category", df['Category'].unique(), df['Category'].unique())

# Select sub-category filter
sub_category_filter = st.sidebar.multiselect("Select Sub-Category", df['Sub-Category'].unique(), df['Sub-Category'].unique())

filtered_df = df[(df['Category'].isin(category_filter)) & 
                 (df['Sub-Category'].isin(sub_category_filter))]

# Display the filtered dataframe
st.subheader("Filtered Data")
st.write(filtered_df)
