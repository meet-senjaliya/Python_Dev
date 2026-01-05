import streamlit as st
st.set_page_config(page_title="Hello Streamlit",layout="centered")
st.title("Welcome to streamlit")
st.header("This is header")
st.subheader("This is subheader")

st.text("This is st.txt")
st.write("this is st.write")
st.markdown("This is **st.markdown**")
code=""""
def add(a,b):
    return a+b
print(add(3,5))


"""
st.code(code,language="python")
