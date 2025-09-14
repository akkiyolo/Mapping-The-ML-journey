import streamlit as st

st.title("streamlit text input")

name=st.text_input("enter your name:")

if name:
  st.write(f"hello,{name}")
