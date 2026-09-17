import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Vehicle Sales Data Analysis')

#add summary section: info cards across top dashboard
st.subheader('Dataset Overview')

col1, col2, col3 = st.columns(3)

col1.metric('Total Listings', len(df))
col2.metric('Average Price', f"${df['price'].mean():,.0f}")
col3.metric('Median Price', f"${df['price'].median():,.0f}")

# oldest to newest model years( for slider)
st.subheader('Filter Vehicles by Model Year')

min_year = int(df['model_year'].min())
max_year = int(df['model_year'].max())

#create model-year range slider (limit data)
year_range = st.slider(
    'Select model year range:',
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

#filtered df
filtered_df = df[
    (df['model_year'] >= year_range[0]) &
    (df['model_year'] <= year_range[1])
]

#make histogram of vehicle prices
fig = px.histogram(
    filtered_df,
    x='price',
    title='Distribution of Vehicle Prices'
)

show_histogram = st.checkbox('Show vehicle price histogram')

if show_histogram:
    st.plotly_chart(fig)


#add drop down for selectbox 

x_option = st.selectbox(
    'Choose a variable to compare with price:',
    ['odometer', 'model_year', 'cylinders']
)

#make scatter plot of vehicle price vs odometer reading
scatter_fig = px.scatter(
    filtered_df,
    x=x_option,
    y='price',
    title=f'Vehicle Price by {x_option}'
)

st.plotly_chart(scatter_fig)

