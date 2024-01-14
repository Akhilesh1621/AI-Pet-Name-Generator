import langchain_helper as lch
import streamlit as st


st.title(" Ai Pet Name Generator")

user_animal_type = st.sidebar.selectbox("what is your pet?",("cat", "Dog","Cow","Tiger","Lion"))

if user_animal_type == "cat":
    user_pet_color = st.sidebar.text_area(label="What color is your cat ?", max_chars=10)

if user_animal_type == "Dog":
    user_pet_color = st.sidebar.text_area(label="What color is your Dog ?", max_chars=10)
    
if user_animal_type == "Cow":
    user_pet_color = st.sidebar.text_area(label="What color is your Cow ?", max_chars=10)
    
if user_animal_type == "Tiger":
    user_pet_color = st.sidebar.text_area(label="What color is your Tiger ?", max_chars=10)
    
if user_animal_type == "Lion":
    user_pet_color = st.sidebar.text_area(label="What color is your Lion ?", max_chars=10)
    

if user_pet_color: 
    response = lch.genrate_pet_name(user_animal_type,user_pet_color)
    st.text(response['pet_name'])