import streamlit as st
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
# from sklearn.svm import SVC
# from sklearn.linear_model import LogisticRegression
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve
# from sklearn.metrics import precision_score, recall_score 




def main():
    st.title("Get data from Linkedⓘⓝ")
    st.sidebar.title("Provide your details here:")

    if st.button('Get Data'):
    	get_data()


def get_data():
	li_at = st.sidebar.text_input('Your li_at cookie:')
	JSESSIONID = st.sidebar.text_input('Your JSESSIONID:')
	GSHEET_LINK = st.sidebar.text_input('Link to "readable" GSHEET with input:')
	st.write(li_at)
	st.write(JSESSIONID)
	st.write(GSHEET_LINK)

