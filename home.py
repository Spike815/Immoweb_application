import streamlit as st
from ml_model.get_model import get_model, get_data,preprocess_new_data,predict_new_data
import pandas as pd

st.set_page_config(page_title='Immo', page_icon='🏠', layout='wide')
st.title("Find the price of your dream property")
st.subheader("First, let's have a look at the overview of the listed properties from immoweb.")

#before that, I remove the extreme prices
data=pd.read_csv(get_data())
data_normal_price = data[data["price"]<3500000]


#This is my second approch by using open stree map
import plotly.express as px
#I followed a youtube tutorial How to Make Interactive Maps with Python https://www.youtube.com/watch?v=1-6ndLqsy6M
#and this is where i pick the color palette https://plotly.com/python/builtin-colorscales/

fig = px.scatter_mapbox(data_normal_price,lon=data_normal_price["longitude"],lat=data_normal_price["latitude"],zoom = 7,
                        color="price",size="price",width = 1000,height = 750, title = "Overall view of the listed properties on map",
                        color_continuous_scale="bluered")

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":10,"t":50,"l":10,"b":10})
st.plotly_chart(figure_or_data=fig)

st.subheader("Want to find out how much your dream house costs?\n\n")

type_of_property=st.selectbox('Type of property', ['House', 'Apartment']).upper()
number_of_bedrooms = int(st.number_input('Number of bedrooms', 0, 10))
living_area=int(st.number_input("Living area",value = 0))
furnished=st.selectbox("Furnished, select 0 for no, 1 for yes",["0","1"])
terrace=int(st.selectbox("Terrace, select 0 for no, 1 for yes",["0","1"]))
terrace_area=int(st.number_input("Terrace area",value=0))
garden=int(st.selectbox("Garden, select 0 for no, 1 for yes",["0","1"]))
garden_area=int(st.number_input("Garden area",value = 0))
total_property_area=int(st.number_input("Total property area",value = 0))
total_land_area = int(st.number_input("Total land area",value = 50))
number_of_facades = int(st.number_input("Number of facades (maximum 4)",value = 0))
swimming_pool=int(st.selectbox("Swimming pool, select 0 for no, 1 for yes",["0","1"]))
state_of_the_building = st.selectbox("State of the building",["New","Just renovated","Good","to renovate"]).upper()
fully_equipped_kitch =st.selectbox("Furnished",["Hyper equipped","Equipped","Semi equipped","Not euipped"])
province=st.selectbox("Province",["Antwerpen","Oost-Vlaanderen","Vlaams-Brabant","Limburg","Hainaut","West-Vlaanderen","Liege","Luxembourg","Namur","Brabant wallon","Brussel"])
digit = int(st.number_input("Postalcode",value=1000))

clicked = st.button("Calculate for me")

text = ""
if clicked:
    property_dict={
  "type_of_property": type_of_property,
  "number_of_bedrooms": number_of_bedrooms,
  "living_area": living_area,
  "furnished": furnished,
  "terrace": terrace,
  "terrace_area": terrace_area,
  "garden": garden,
  "garden_area": garden_area,
  "total_property_area": total_property_area,
  "total_land_area": total_land_area,
  "number_of_facades": number_of_facades,
  "swimming_pool": swimming_pool,
  "state_of_the_building": state_of_the_building ,
  "province": province,
  "kitchen": fully_equipped_kitch,
  "digit": int(digit/100)
}
    model=get_model()
    X=preprocess_new_data(property_dict)
    text = predict_new_data(X,model)

st.write(text)