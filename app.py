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
    st.title("Get data from LinkedIn ⓘⓝ")
    st.markdown("Should you eat this mushroom 🍄 ?")
    st.sidebar.title("Provide your details here:")
    st.sidebar.markdown("")
    li_at = st.text_input('Your li_at cookie:')
    st.write('Received value', li_at)


if __name__ == '__main__':
    main()
