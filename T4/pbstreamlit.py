import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.set_page_config(page_title="Streamlit example of pb",layout="wide")
st.title("Streamlit example of pb")
st.header("user profile app")

name = st.text_input("Enter name")
age = st.slider("Select age",10,100)
gender = st.radio("Choose Gender",['male','female','other'])
hobbies = st.multiselect(
"select hobbies",
['reading','sport','music','travel','games','cooking']
)
photo = st.file_uploader("upload profile pic ",type=['jpg','png','jpeg'])

if st.button("submit profile"):
    st.subheader("profile details")
    st.write("Name ",name)
    st.write("age ",age)
    st.write("Gender ",gender)
    st.write("hobbies ",", ".join(hobbies))
    
    if photo:
        st.image(photo,caption="profile pic",width=200)
