import streamlit as st
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re


def main():
    st.title("Get data from Linkedⓘⓝ")
    st.sidebar.title("Provide your details here:")
    li_at = st.sidebar.text_input('Your li_at cookie:')

    JSESSIONID = st.sidebar.text_input('Your JSESSIONID:')

    GSHEET_LINK = st.sidebar.text_input('Link to "readable" GSHEET with input:')
    if st.sidebar.button('Get Data'):
    	get_data(li_at, JSESSIONID, GSHEET_LINK)


def get_data(li_at, JSESSIONID, GSHEET_LINK):
	st.write(li_at)
	st.write(JSESSIONID)
	st.write(GSHEET_LINK)

if __name__ == '__main__':
    main()
