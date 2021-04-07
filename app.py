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
    li_at = st.sidebar.text_input('Your li_at cookie:')

    JSESSIONID = st.sidebar.text_input('Your JSESSIONID:')

    GSHEET_LINK = st.sidebar.text_input('Link to "readable" GSHEET with input:')
    if st.sidebar.button('Get Data'):
    	get_data()


def get_data():
	st.write(li_at)
	st.write(JSESSIONID)
	st.write(GSHEET_LINK)




 #    headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",}

	# link = "https://www.linkedin.com/voyager/api/organization/companies?decorationId=com.linkedin.voyager.deco.organization.web.WebFullCompanyMain-33&q=universalName&universalName=google"


	# with requests.session() as s:
	#     s.cookies['li_at'] = "AQEDATSFZz0CXt1mAAABd_L_CocAAAF4zCnn_04AHq07sDygbSzxI7_4nYjtt-ubRDtm4MFm5dC7EujzH7OIb1hDIdgI5KYcAtVcFp1EMsxLOzA8cs6EWgqvTyI4zvvcJ0FsNzIlT2QVR7aRMMQ_jiNp"
	#     s.cookies["JSESSIONID"] = "ajax:6241714341907323726"
	#     s.headers = headers
	#     s.headers["csrf-token"] = s.cookies["JSESSIONID"]
	#     response = s.get(link)
	#     c_data = response.json()


if __name__ == '__main__':
    main()
