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



def main():
    # Create a list to store the input values
    input_values = []

    # Add a button to the app that allows users to add a new input field
    if st.button('Add Input'):
        input_values.append('')

    # Add a text input field for each value in the input_values list
    for i, value in enumerate(input_values):
        input_values[i] = st.text_input(f'Input {i + 1}:', value)

    # Display the input values in the app
    st.write('Input Values:', input_values)

if __name__ == '__main__':
    main()
