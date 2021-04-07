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

    # GSHEET_LINK = st.sidebar.text_input('Link to "readable" GSHEET with input:')

    if st.sidebar.button('Get Data'):
    	get_data(li_at, JSESSIONID)


def get_data(li_at, JSESSIONID):

	headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}

	company_link = "https://www.linkedin.com/voyager/api/organization/companies?decorationId=com.linkedin.voyager.deco.organization.web.WebFullCompanyMain-33&q=universalName&universalName=google"


	with requests.session() as s:
	    s.cookies['li_at'] = li_at
	    s.cookies["JSESSIONID"] = JSESSIONID
	    s.headers = headers
	    s.headers["csrf-token"] = s.cookies["JSESSIONID"]
	    response = s.get(company_link)
	    company_dict = response.json()
	

	try:
	    Name = company_dict["elements"][0]["name"]
	    st.write(Name)
	except:
	    Name = "NA"
	    st.write(Name)
	    
	try:
	    Industries = company_dict["elements"][0]["companyIndustries"][0]["localizedName"]
	    st.write(Industries)
	except:
	    Industries = "NA"
	    st.write(Industries)
	    
	try:
	    Keywords = company_dict["elements"][0]["specialities"]
	    st.write(Keywords) #List
	except:
	    Keywords = "NA"
	    st.write(Keywords)
	    
	try:
	    Website_URL = company_dict["elements"][0]["companyPageUrl"] 
	    st.write(Website_URL)
	except:
	    Website_URL = "NA"
	    st.write(Website_URL)


	try:
	    Logo_URL_Root = company_dict["elements"][0]["logo"]["image"]["com.linkedin.common.VectorImage"]["rootUrl"].split("/")[5]
	    st.write(Logo_URL_Root)
	    Logo_URL_400 = company_dict["elements"][0]["logo"]["image"]["com.linkedin.common.VectorImage"]["artifacts"]
	    for width in Logo_URL_400:
	        if(width["width"]==400):
	            Logo_URL = "https://media-exp1.licdn.com/dms/image/"+Logo_URL_Root+"/company-logo_"+width["fileIdentifyingUrlPathSegment"]

	    st.write(Logo_URL)
	except:
	    Logo_URL = "NA"
	    st.write(Logo_URL)

	try:
	    Available_profiles = "NA"
	    st.write(Available_profiles)
	except:
	    Available_profiles = "NA"
	    st.write(Available_profiles)
	    
	try:
	    Primary_role = "NA"
	    st.write(Primary_role)
	except:
	    Primary_role = "NA"
	    st.write(Primary_role)
	    
	try:
	    LinkedIn_Normalized_Number = company_dict["elements"][0]["entityUrn"].split(":")[3]
	    st.write(LinkedIn_Normalized_Number)
	except:
	    LinkedIn_Normalized_Number = "NA"
	    st.write(LinkedIn_Normalized_Number)
	    
	try:
	    LinkedIn_Universal_Name = company_dict["elements"][0]["universalName"]
	    st.write(LinkedIn_Universal_Name)
	except:
	    LinkedIn_Universal_Name = "NA"
	    st.write(LinkedIn_Universal_Name)
	    
	try:
	    Year_Founded = company_dict["elements"][0]["foundedOn"]["year"]
	    st.write(Year_Founded)
	except:
	    Year_Founded = "NA"
	    st.write(Year_Founded)
	    
	try:
	    LinkedIn_URL = company_dict["elements"][0]["url"]
	    st.write(LinkedIn_URL)
	except:
	    LinkedIn_URL = "NA"
	    st.write(LinkedIn_URL)
	    
	try:
	    LinkdedIn_SalesNavigator_URL = company_dict["elements"][0]["salesNavigatorCompanyUrl"]
	    st.write(LinkdedIn_SalesNavigator_URL)
	except:
	    LinkdedIn_SalesNavigator_URL = "NA"
	    st.write(LinkdedIn_SalesNavigator_URL)

	try:
	    Crunchbase_URL = company_dict["elements"][0]["fundingData"]["companyCrunchbaseUrl"].split("?")[0]
	    st.write(Crunchbase_URL)


if __name__ == '__main__':
	main()
