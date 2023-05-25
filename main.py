import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Wheather forecast for the next days")

place = st.text_input("Place:")

days= st.slider("Forecast Days", min_value=1, max_value=5, help= "Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

try:
   if place:
      filtered_data = get_data(place, days)
      if option=="Temperature":
         temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
         dates = [dict["dt_txt"] for dict in filtered_data]
         figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"})
         st.plotly_chart(figure)

      if option=="Sky":
         images= {"Clear":"images/clear.png", "Clouds":"images/cloud.png", "Rain":"images/rain.png", "Snow":"images/snow.png"}
         sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
         image_paths = [images[condition] for condition in sky_condition]
         # st.image(image_paths, width=116)
         for num in range(len(filtered_data)):
            st.image(image_paths[num], width=116)
            st.subheader(filtered_data[num]["dt_txt"])

except KeyError:
   st.text("This country doesn't exist")

