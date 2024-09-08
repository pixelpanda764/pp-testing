import streamlit as st

st.title("Things about goats :goat:")
st.write("Let's get started! Answer this question to start...")

col1, col2, col3, col4 = st.columns([2, 1, 1, 5])

with col1:
    st.write("Are goats amazing?")

with col2:
    button1 = st.button('Yes')
    
with col3:
    button2 = st.button('No')
    
if button1:
    q_agreement = True
    st.write("You clicked yes!")

if button2:
    q_agreement = False
    st.write("Sorry you need to agree to continue")
