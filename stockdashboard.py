import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache
# This is used so that the load func is not run everytime / saved to streamlit cache
def load_data():
    "This will be the function which is used for loading the data / itsAbdulKhadar"
    df = pd.read_csv("C:/Users/iamkh/PycharmProjects/stocksdashboard/data/all_stocks_5yr.csv", index_col="date")

    numeric_df = df.select_dtypes(['float','int'])
    numeric_cols = numeric_df.columns

    text_df = df.select_dtypes(['object'])
    text_cols = text_df.columns

    stock_column = df['Name']
    unique_stocks = stock_column.unique()

    return df, numeric_cols, text_cols, unique_stocks

df, numeric_cols, text_cols, unique_stocks = load_data()

# Title of the stock Dashboard
st.title("Stock Dashboard - itsAbdulKhadar")

# Adding checkbox to the side bar
check_box = st.sidebar.checkbox(label="Display dataset")

if check_box:
        # show the dataset
        st.write(df)
# giving the sidebar a title
st.sidebar.title("Settings")
st.sidebar.subheader("Timeseries Settings")
feature_selection = st.sidebar.multiselect(label="Features to plot", options=numeric_cols)
stock_dropdown = st.sidebar.selectbox(label="Stock Ticker", options=unique_stocks)

print(feature_selection)

df = df[df['Name']==stock_dropdown]
df_features = df[feature_selection]
plotly_figure = px.line(data_frame=df_features, x=df_features.index, y=feature_selection, title=(str(stock_dropdown) + ' ' +'timeline'))
st.plotly_chart(plotly_figure)