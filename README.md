# Car Sales Dashboard

This project is an interactive web application for exploring a dataset of used vehicle advertisements in the United States. The dashboard allows users to visualize patterns in vehicle prices, model years, and odometer readings.

## Features

- Interactive histogram showing the distribution of vehicle prices
- Scatter plot showing the relationship between vehicle price and odometer reading
- Checkbox that allows users to show or hide the vehicle price histogram
- Exploratory data analysis of the vehicle dataset

## Technologies Used

- Python
- Pandas for data manipulation and analysis
- Plotly Express for interactive data visualizations
- Streamlit for building the web application
- Jupyter Notebook for exploratory data analysis

## Running the Project Locally

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python packages:

   pip install -r requirements.txt

4. Run the Streamlit application:

   streamlit run app.py

5. Open the local URL provided by Streamlit in your web browser.

## Dataset

The application uses `vehicles_us.csv`, which contains advertisements for used vehicles, including information such as price, model year, mileage, vehicle condition, and other characteristics.