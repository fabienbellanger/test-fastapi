"""
# My first app with Streamlit

This is a simple Streamlit app that demonstrates how to create a web application using Python.
"""

import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="My Streamlit App",
    page_icon=":crab:",  # You can use an emoji or a URL to an image
    layout="wide",  # Can be "centered" or "wide"
)

# Set the title of the app
st.title("My first Streamlit page")


# Button
def click_button():
    print("Button clicked!")
    st.toast("Button clicked!", icon="🎉")


st.button(
    "Click me!",
    key="button1",
    on_click=click_button,
    help="Click this button to see a message",
)

if st.session_state.button1:
    st.write("You clicked the button!")
