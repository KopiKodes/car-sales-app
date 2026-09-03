import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Vehicle Sales Data Analysis')

#make histogram of vehicle prices
fig = px.histogram(
    df,
    x='price',
    title='Distribution of Vehicle Prices'
)

show_histogram = st.checkbox('Show vehicle price histogram')

if show_histogram:
    st.plotly_chart(fig)


#make scatter plot of vehicle price vs odometer reading

scatter_fig = px.scatter(
    df,
    x='odometer',
    y='price',
    title='Vehicle Price by Odometer Reading'
)

st.plotly_chart(scatter_fig)

