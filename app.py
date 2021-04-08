import streamlit as st
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import time





def main():
	dframe = pd.DataFrame()

	dframe_multiple = pd.DataFrame()

	st.title("Get data from Linkedⓘⓝ")
	st.sidebar.title("Provide your details here:")
	li_at = st.sidebar.text_input('Your li_at cookie:')

	JSESSIONID = st.sidebar.text_input('Your JSESSIONID:')

	company = st.sidebar.text_input('(Single) Linkedin Company Name (lowercase):')

    # GSHEET_LINK = st.sidebar.text_input('Link to "readable" GSHEET with input:')

	if st.sidebar.button('Get Data for Single Company'):
		company_dict = get_data(li_at, JSESSIONID, company)
		df = build_data(company_dict, dframe)
		write_data(df)

	companies = st.sidebar.text_area('(Multiple) Linkedin Company Names (newline separated):', value='', height=None, max_chars=None, key=None, help=None)

	if st.sidebar.button('Get Data for Multiple Companies'):
		df_m = get_build_data(li_at, JSESSIONID, companies)
		write_data(df_m)

def get_data(li_at, JSESSIONID, company):

	headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}

	company_link = "https://www.linkedin.com/voyager/api/organization/companies?decorationId=com.linkedin.voyager.deco.organization.web.WebFullCompanyMain-33&q=universalName&universalName="+str(company)


	with requests.session() as s:
	    s.cookies['li_at'] = li_at
	    s.cookies["JSESSIONID"] = JSESSIONID
	    s.headers = headers
	    s.headers["csrf-token"] = s.cookies["JSESSIONID"]
	    response = s.get(company_link)
	    company_dict = response.json()

	return company_dict
	

def build_data(company_dict, dframe):

	try:
	    Name = company_dict["elements"][0]["name"]
	   
	except:
	    Name = "NA"
	   
	    
	try:
	    Industries = company_dict["elements"][0]["companyIndustries"][0]["localizedName"]
	   
	except:
	    Industries = "NA"
	   
	    
	try:
	    Keywords = company_dict["elements"][0]["specialities"]
	    #List
	except:
	    Keywords = "NA"
	   
	    
	try:
	    Website_URL = company_dict["elements"][0]["companyPageUrl"] 
	   
	except:
	    Website_URL = "NA"
	   
	    
	try:
	    E_mail = "NA"
	   
	except:
	    E_mail = "NA"
	   
	    
	try:
	    Logo_URL_Root = company_dict["elements"][0]["logo"]["image"]["com.linkedin.common.VectorImage"]["rootUrl"].split("/")[5]
	   
	    Logo_URL_400 = company_dict["elements"][0]["logo"]["image"]["com.linkedin.common.VectorImage"]["artifacts"]
	    for width in Logo_URL_400:
	        if(width["width"]==400):
	            Logo_URL = "https://media-exp1.licdn.com/dms/image/"+Logo_URL_Root+"/company-logo_"+width["fileIdentifyingUrlPathSegment"]

	   
	except:
	    Logo_URL = "NA"
	   

	try:
	    Available_profiles = "NA"
	   
	except:
	    Available_profiles = "NA"
	   
	    
	try:
	    Primary_role = "NA"
	   
	except:
	    Primary_role = "NA"
	   
	    
	try:
	    LinkedIn_Normalized_Number = company_dict["elements"][0]["entityUrn"].split(":")[3]
	   
	except:
	    LinkedIn_Normalized_Number = "NA"
	   
	    
	try:
	    LinkedIn_Universal_Name = company_dict["elements"][0]["universalName"]
	   
	except:
	    LinkedIn_Universal_Name = "NA"
	   
	    
	try:
	    Year_Founded = company_dict["elements"][0]["foundedOn"]["year"]
	   
	except:
	    Year_Founded = "NA"
	   
	    
	try:
	    LinkedIn_URL = company_dict["elements"][0]["url"]
	   
	except:
	    LinkedIn_URL = "NA"
	   
	    
	try:
	    LinkdedIn_SalesNavigator_URL = company_dict["elements"][0]["salesNavigatorCompanyUrl"]
	   
	except:
	    LinkdedIn_SalesNavigator_URL = "NA"
	   

	try:
	    Crunchbase_URL = company_dict["elements"][0]["fundingData"]["companyCrunchbaseUrl"].split("?")[0]
	   
	except:
	    Crunchbase_URL = "NA"
	   
	    
	try:
	    Facebook_URL = "NA"
	   
	except:
	    Facebook_URL = "NA"
	   
	    
	try:
	    Twitter_URL = "NA"
	   
	except:
	    Twitter_URL = "NA"
	   
	    
	try:
	    No_of_Employees_min = company_dict["elements"][0]["staffCountRange"]["start"]
	   
	except:
	    No_of_Employees_min = "NA"
	   
	    
	try:
	    No_of_Employees_max = company_dict["elements"][0]["staffCountRange"]["end"]
	   
	except:
	    No_of_Employees_max = "NA"
	   
	    
	try:
	    No_of_Employees_actual = company_dict["elements"][0]["staffCount"]
	   
	except:
	    No_of_Employees_actual = "NA"
	   

	try:
	    HQ_Address = company_dict["elements"][0]["headquarter"]["line1"]
	   
	except:
	    HQ_Address = "NA"
	   
	    
	try:
	    Suite = "NA"
	   
	except:
	    Suite = "NA"
	   
	    
	try:
	    HQ_City = company_dict["elements"][0]["headquarter"]["city"]
	   
	except:
	    HQ_City = "NA"
	   
	    
	try:
	    HQ_Country = company_dict["elements"][0]["headquarter"]["country"]
	   
	except:
	    HQ_Country = "NA"
	   
	    
	try:
	    HQ_State = company_dict["elements"][0]["headquarter"]["geographicArea"]
	   
	except:
	    HQ_State = "NA"
	   
	    
	try:
	    HQ_Postal_Code = company_dict["elements"][0]["headquarter"]["postalCode"]
	   
	except:
	    HQ_Postal_Code = "NA"
	   
	    
	try:
	    Phone = company_dict["elements"][0]["headquarter"]["phone"]
	   
	except:
	    Phone = "NA"
	   

	try:
	    Fax = "NA"
	   
	except:
	    Fax = "NA"
	   

	try:
	    Company_Status = company_dict["elements"][0]["companyType "]["localizedName"]
	   
	except:
	    Company_Status = "NA"
	   

	try:
	    Investor_Type = "NA"
	   
	except:
	    Investor_Type = "NA"
	   
	    
	try:
	    LinkedIn_Short_Description = company_dict["elements"][0]["tagline"]
	   
	except:
	    LinkedIn_Short_Description = "NA"
	   
	    
	try:
	    LinkedIn_Long_Description = company_dict["elements"][0]["description"]
	   
	except:
	    LinkedIn_Long_Description = "NA"
	   

	    
	#For locations you have to loop through 


	Location_Address = []
	try:
	    for locations in company_dict["elements"][0]["confirmedLocations"]:
	        try:
	            Location_Address.append(locations["line1"])
	        except:
	            Location_Address.append("NA")
	except:
	    Location_Address.append("NA")




	Location_Suite = []
	try:
	    for locations in company_dict["elements"][0]["confirmedLocations"]:
	        try:
	            Location_Suite.append("NA")
	        except:
	            Location_Suite.append("NA")
	except:
	    Location_Suite.append("NA")





	Location_City = []
	try:
	    for locations in company_dict["elements"][0]["confirmedLocations"]:
	        try:
	            Location_City.append(locations["city"])
	        except:
	            Location_City.append("NA")
	except:
	    Location_City.append("NA")




	Location_Country = []
	try:
	    for locations in company_dict["elements"][0]["confirmedLocations"]:
	        try:
	            Location_Country.append(locations["country"])
	        except:
	            Location_Country.append("NA")
	except:
	    Location_Country.append("NA")




	Location_State = []
	try:
	    for locations in company_dict["elements"][0]["confirmedLocations"]:
	        try:
	            Location_State.append(locations["geographicArea"])
	        except:
	            Location_State.append("NA")
	except:
	    Location_State.append("NA")




	Location_Postal_Code = []
	try:
	    for locations in company_dict["elements"][0]["confirmedLocations"]:
	        try:
	            Location_Postal_Code.append(locations["postalCode"])
	        except:
	            Location_Postal_Code.append("NA")
	except:
	    Location_Postal_Code.append("NA")



	    
	try:
	    Headquarters = company_dict["elements"][0]["confirmedLocations"]["headquarter"]
	except:
	    Headquarters = "NA"

	d = {'Name': [Name],
	'Industries': [Industries],
	'Keywords': [Keywords],
	'Website_URL': [Website_URL],
	'E_mail': [E_mail],
	'Logo_URL': [Logo_URL],
	'Available_profiles': [Available_profiles],
	'Primary_role': [Primary_role],
	'LinkedIn_Normalized_Number': [LinkedIn_Normalized_Number],
	'LinkedIn_Universal_Name': [LinkedIn_Universal_Name],
	'Year_Founded': [Year_Founded],
	'LinkedIn_URL': [LinkedIn_URL],
	'LinkdedIn_SalesNavigator_URL': [LinkdedIn_SalesNavigator_URL],
	'Crunchbase_URL': [Crunchbase_URL],
	'Facebook_URL': [Facebook_URL],
	'Twitter_URL': [Twitter_URL],
	'No_of_Employees_min': [No_of_Employees_min],
	'No_of_Employees_max': [No_of_Employees_max],
	'No_of_Employees_actual': [No_of_Employees_actual],
	'HQ_Address': [HQ_Address],
	'Suite': [Suite],
	'HQ_City': [HQ_City],
	'HQ_Country': [HQ_Country],
	'HQ_State': [HQ_State],
	'HQ_Postal_Code': [HQ_Postal_Code],
	'Phone': [Phone],
	'Fax': [Fax],
	'Company_Status': [Company_Status],
	'Investor_Type': [Investor_Type],
	'LinkedIn_Short_Description': [LinkedIn_Short_Description],
	'LinkedIn_Long_Description': [LinkedIn_Long_Description],
	'Location_Address': [Location_Address],
	'Location_Suite': [Location_Suite],
	'Location_City': [Location_City],
	'Location_Country': [Location_Country],
	'Location_State': [Location_State],
	'Location_Postal_Code': [Location_Postal_Code],
	'Headquarters': [Headquarters],}

	dftemp = pd.DataFrame(data=d)
	dframe = dframe.append(dftemp,ignore_index=True)


	return dframe


def get_build_data(li_at, JSESSIONID, companies):
	for company in companies:
			headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}

			company_link = "https://www.linkedin.com/voyager/api/organization/companies?decorationId=com.linkedin.voyager.deco.organization.web.WebFullCompanyMain-33&q=universalName&universalName="+str(company)

			time.sleep(1)
			with requests.session() as s:
			    s.cookies['li_at'] = li_at
			    s.cookies["JSESSIONID"] = JSESSIONID
			    s.headers = headers
			    s.headers["csrf-token"] = s.cookies["JSESSIONID"]
			    response = s.get(company_link)
			    company_dict = response.json()

			try:
			    Name = company_dict["elements"][0]["name"]
			   
			except:
			    Name = "NA"
			   
			    
			try:
			    Industries = company_dict["elements"][0]["companyIndustries"][0]["localizedName"]
			   
			except:
			    Industries = "NA"
			   
			    
			try:
			    Keywords = company_dict["elements"][0]["specialities"]
			    #List
			except:
			    Keywords = "NA"
			   
			    
			try:
			    Website_URL = company_dict["elements"][0]["companyPageUrl"] 
			   
			except:
			    Website_URL = "NA"
			   
			    
			try:
			    E_mail = "NA"
			   
			except:
			    E_mail = "NA"
			   
			    
			try:
			    Logo_URL_Root = company_dict["elements"][0]["logo"]["image"]["com.linkedin.common.VectorImage"]["rootUrl"].split("/")[5]
			   
			    Logo_URL_400 = company_dict["elements"][0]["logo"]["image"]["com.linkedin.common.VectorImage"]["artifacts"]
			    for width in Logo_URL_400:
			        if(width["width"]==400):
			            Logo_URL = "https://media-exp1.licdn.com/dms/image/"+Logo_URL_Root+"/company-logo_"+width["fileIdentifyingUrlPathSegment"]

			   
			except:
			    Logo_URL = "NA"
			   

			try:
			    Available_profiles = "NA"
			   
			except:
			    Available_profiles = "NA"
			   
			    
			try:
			    Primary_role = "NA"
			   
			except:
			    Primary_role = "NA"
			   
			    
			try:
			    LinkedIn_Normalized_Number = company_dict["elements"][0]["entityUrn"].split(":")[3]
			   
			except:
			    LinkedIn_Normalized_Number = "NA"
			   
			    
			try:
			    LinkedIn_Universal_Name = company_dict["elements"][0]["universalName"]
			   
			except:
			    LinkedIn_Universal_Name = "NA"
			   
			    
			try:
			    Year_Founded = company_dict["elements"][0]["foundedOn"]["year"]
			   
			except:
			    Year_Founded = "NA"
			   
			    
			try:
			    LinkedIn_URL = company_dict["elements"][0]["url"]
			   
			except:
			    LinkedIn_URL = "NA"
			   
			    
			try:
			    LinkdedIn_SalesNavigator_URL = company_dict["elements"][0]["salesNavigatorCompanyUrl"]
			   
			except:
			    LinkdedIn_SalesNavigator_URL = "NA"
			   

			try:
			    Crunchbase_URL = company_dict["elements"][0]["fundingData"]["companyCrunchbaseUrl"].split("?")[0]
			   
			except:
			    Crunchbase_URL = "NA"
			   
			    
			try:
			    Facebook_URL = "NA"
			   
			except:
			    Facebook_URL = "NA"
			   
			    
			try:
			    Twitter_URL = "NA"
			   
			except:
			    Twitter_URL = "NA"
			   
			    
			try:
			    No_of_Employees_min = company_dict["elements"][0]["staffCountRange"]["start"]
			   
			except:
			    No_of_Employees_min = "NA"
			   
			    
			try:
			    No_of_Employees_max = company_dict["elements"][0]["staffCountRange"]["end"]
			   
			except:
			    No_of_Employees_max = "NA"
			   
			    
			try:
			    No_of_Employees_actual = company_dict["elements"][0]["staffCount"]
			   
			except:
			    No_of_Employees_actual = "NA"
			   

			try:
			    HQ_Address = company_dict["elements"][0]["headquarter"]["line1"]
			   
			except:
			    HQ_Address = "NA"
			   
			    
			try:
			    Suite = "NA"
			   
			except:
			    Suite = "NA"
			   
			    
			try:
			    HQ_City = company_dict["elements"][0]["headquarter"]["city"]
			   
			except:
			    HQ_City = "NA"
			   
			    
			try:
			    HQ_Country = company_dict["elements"][0]["headquarter"]["country"]
			   
			except:
			    HQ_Country = "NA"
			   
			    
			try:
			    HQ_State = company_dict["elements"][0]["headquarter"]["geographicArea"]
			   
			except:
			    HQ_State = "NA"
			   
			    
			try:
			    HQ_Postal_Code = company_dict["elements"][0]["headquarter"]["postalCode"]
			   
			except:
			    HQ_Postal_Code = "NA"
			   
			    
			try:
			    Phone = company_dict["elements"][0]["headquarter"]["phone"]
			   
			except:
			    Phone = "NA"
			   

			try:
			    Fax = "NA"
			   
			except:
			    Fax = "NA"
			   

			try:
			    Company_Status = company_dict["elements"][0]["companyType "]["localizedName"]
			   
			except:
			    Company_Status = "NA"
			   

			try:
			    Investor_Type = "NA"
			   
			except:
			    Investor_Type = "NA"
			   
			    
			try:
			    LinkedIn_Short_Description = company_dict["elements"][0]["tagline"]
			   
			except:
			    LinkedIn_Short_Description = "NA"
			   
			    
			try:
			    LinkedIn_Long_Description = company_dict["elements"][0]["description"]
			   
			except:
			    LinkedIn_Long_Description = "NA"
			   

			    
			#For locations you have to loop through 


			Location_Address = []
			try:
			    for locations in company_dict["elements"][0]["confirmedLocations"]:
			        try:
			            Location_Address.append(locations["line1"])
			        except:
			            Location_Address.append("NA")
			except:
			    Location_Address.append("NA")




			Location_Suite = []
			try:
			    for locations in company_dict["elements"][0]["confirmedLocations"]:
			        try:
			            Location_Suite.append("NA")
			        except:
			            Location_Suite.append("NA")
			except:
			    Location_Suite.append("NA")





			Location_City = []
			try:
			    for locations in company_dict["elements"][0]["confirmedLocations"]:
			        try:
			            Location_City.append(locations["city"])
			        except:
			            Location_City.append("NA")
			except:
			    Location_City.append("NA")




			Location_Country = []
			try:
			    for locations in company_dict["elements"][0]["confirmedLocations"]:
			        try:
			            Location_Country.append(locations["country"])
			        except:
			            Location_Country.append("NA")
			except:
			    Location_Country.append("NA")




			Location_State = []
			try:
			    for locations in company_dict["elements"][0]["confirmedLocations"]:
			        try:
			            Location_State.append(locations["geographicArea"])
			        except:
			            Location_State.append("NA")
			except:
			    Location_State.append("NA")




			Location_Postal_Code = []
			try:
			    for locations in company_dict["elements"][0]["confirmedLocations"]:
			        try:
			            Location_Postal_Code.append(locations["postalCode"])
			        except:
			            Location_Postal_Code.append("NA")
			except:
			    Location_Postal_Code.append("NA")



			    
			try:
			    Headquarters = company_dict["elements"][0]["confirmedLocations"]["headquarter"]
			except:
			    Headquarters = "NA"

			d = {'Name': [Name],
			'Industries': [Industries],
			'Keywords': [Keywords],
			'Website_URL': [Website_URL],
			'E_mail': [E_mail],
			'Logo_URL': [Logo_URL],
			'Available_profiles': [Available_profiles],
			'Primary_role': [Primary_role],
			'LinkedIn_Normalized_Number': [LinkedIn_Normalized_Number],
			'LinkedIn_Universal_Name': [LinkedIn_Universal_Name],
			'Year_Founded': [Year_Founded],
			'LinkedIn_URL': [LinkedIn_URL],
			'LinkdedIn_SalesNavigator_URL': [LinkdedIn_SalesNavigator_URL],
			'Crunchbase_URL': [Crunchbase_URL],
			'Facebook_URL': [Facebook_URL],
			'Twitter_URL': [Twitter_URL],
			'No_of_Employees_min': [No_of_Employees_min],
			'No_of_Employees_max': [No_of_Employees_max],
			'No_of_Employees_actual': [No_of_Employees_actual],
			'HQ_Address': [HQ_Address],
			'Suite': [Suite],
			'HQ_City': [HQ_City],
			'HQ_Country': [HQ_Country],
			'HQ_State': [HQ_State],
			'HQ_Postal_Code': [HQ_Postal_Code],
			'Phone': [Phone],
			'Fax': [Fax],
			'Company_Status': [Company_Status],
			'Investor_Type': [Investor_Type],
			'LinkedIn_Short_Description': [LinkedIn_Short_Description],
			'LinkedIn_Long_Description': [LinkedIn_Long_Description],
			'Location_Address': [Location_Address],
			'Location_Suite': [Location_Suite],
			'Location_City': [Location_City],
			'Location_Country': [Location_Country],
			'Location_State': [Location_State],
			'Location_Postal_Code': [Location_Postal_Code],
			'Headquarters': [Headquarters],}

			dftemp = pd.DataFrame(data=d)
			dframe_multiple = dframe_multiple.append(dftemp,ignore_index=True)			



	return dframe_multiple


def write_data(dframe):
	st.write(dframe)




if __name__ == '__main__':
	main()
 
