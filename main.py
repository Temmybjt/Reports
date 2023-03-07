# Import libraries

#Import Streamlit library
import streamlit as st
#Import pandas library
import pandas as pd

import requests 
#Import Sqlite3 library
import sqlite3
#Import numpy library
import numpy as np



import streamlit as st

def main():
    # Initialize an empty list to store the input values
    values = []

    # Add a text input field to the app
    input_value = st.text_input('Enter a value:', '')

    # If a value is entered, append it to the list of values
    if input_value:
        values.append(input_value)

    # Display the list of values in the app
    st.write('Values:', values)

    # Add a button with a plus sign to generate a new input field
    if st.button('+'):
        # If the button is clicked, add a new input field
        new_value = st.text_input('Enter a value:', '')
        # If a value is entered, append it to the list of values
        if new_value:
            values.append(new_value)

    # Display the updated list of values in the app
    st.write('Updated values:', values)

if __name__ == '__main__':
    main()
