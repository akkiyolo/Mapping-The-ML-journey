import streamlit as st
import pandas as pd
import numpy as np
st.title("streamlit text input")

name=st.text_input("enter your name:")

age=st.slider("select your age:",0,100,25)

st.write(f"your age is {age}")

options=["python","c++","flutter","java"]
choice=st.selectbox("choose your favourite language:",options)
st.write(f"you selected {choice}")

if name:
  st.write(f"hello,{name}")


data={
  "name":["jane","john","akki"],
  "age":[25,28,21],
  "city":["nyc","dubai","sf"]

}

df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file=st.file_uploader("choose a csv file",type="csv")

if uploaded_file is not None:
  df=pd.read_csv(uploaded_file)
  st.write(df)