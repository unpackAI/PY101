import streamlit as st

st.title("Simple App")

name = st.text_input("What is your name?")
sex = st.radio("What describes you best?", ["Male", "Female", "Other"])
age = st.slider("How old are you?", min_value=0, max_value=100)

st.write("---")  # for an horizontal line

sex_as_string = ""
if sex != "Other":
    sex_as_string = "(M)" if sex == "Male" else "(F)"
st.write(f"Hello, {name} {sex_as_string}. You are {age} but you look gorgeous!🌞")


st._main

from subprocess import run

print(__file__)