import streamlit as st

st.title("My fisrt streamlit app created by Nipun Kawale")

st.write("Welcome this app calculate the square of a number")

st.header("Select a Number")

number = st.slider("Pick a number ",0,100,25)

st.subheader("Result")
squared_number = number * number
st.write(f"the square of **{number}** is **{squared_number}**.")