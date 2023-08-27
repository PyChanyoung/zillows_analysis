import streamlit as st
import pandas as pd
import pydeck as pdk
import time
import numpy as np
import altair as alt

from urllib.error import URLError


def main():
    st.title("# Zillow Analysis Tool")
    st.sidebar.success("Select a feature above.")

    st.markdown(
        """
        Light-weight no-code solution to retrieve listings and property details.

        **👈 Select a feature from the dropdown on the left**

        ### Features

        - Listings Search
        - Property Detail
        - Analystics
    """
    )


def get_listings():
    st.title("# Listings Search")

    st.markdown("## 1. Enter Web Link")
    listing_url = st.text_input(
        'url', 'https://www.zillow.com/...', key='placeholder')

    st.markdown("## 2. Enter your API Key")
    st.text('API Key')

    st.markdown("## 3. Enter your E-Mail")
    st.text('E-Mail')


def mapping_demo():
    pass


def data_frame_demo():
    pass


page_names_to_funcs = {
    "Home": main,
    "Listings Search": get_listings,
    "Mapping Demo": mapping_demo,
    "DataFrame Demo": data_frame_demo
}

feature_name = st.sidebar.selectbox(
    "Choose a feature", page_names_to_funcs.keys())
page_names_to_funcs[feature_name]()
