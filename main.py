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
    # Add a text input field to the app
    input_value = st.text_input('Enter a value:', '')

    # Store the input value in a variable
    stored_value = input_value

    # Display the stored value in the app
    st.write('Stored value:', stored_value)

if __name__ == '__main__':
    main()
