"""
# Day 3
st.button
st.button allows the display of a button widget.
What we're building?
A simple app that performs conditionally prints out alternative messages depending on whether the button was pressed or not.
Flow of the app:
1.	By default, the app prints Goodbye
2.	Upon clicking on the button, the app displays the alternative message Why hello there
"""
# Code: Here's the code to implement the above mentioned app:
import streamlit as st

st.header('Streamlit Button Message')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')
