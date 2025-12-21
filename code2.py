import streamlit as st
import pandas as pd
import numpy as np
st.title ("My second streamlit app")
st.write("this is a simple app demonstarte the basic fucntionality of streamlit")
st.sidebar.header("user input feature")
user_name = st.sidebar.text_input ("Enter your name? ","Nipun Kawale")
age = st.sidebar.slider("select your age ",0,100,25)

favorite_color = st.sidebar.selectbox("What is your favourite color?",["Blue","Red","Green","Yellow"])

st.header(f"Weclcome ,{user_name}")
st.write(f"You are {age}years old and your favorite color is {favorite_color}")

st.subheader("Here some random data:")

data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

st.dataframe(data)

if st.checkbox("show raw data"):
    st.subheader("raw data")
    st.write(data)
    
if st.button("Say hello"):
    st.write("hello there!")
else:
    st.write("Goddbye")                                                            