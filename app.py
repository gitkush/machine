
    JSESSIONID = st.sidebar.text_input('Your JSESSIONID:')

    GSHEET_LINK = st.sidebar.text_input('Link to "readable" GSHEET with input:')
    if st.sidebar.button('Get Data'):
    	get_data(li_at, JSESSIONID, GSHEET_LINK)


def get_data(li_at, JSESSIONID, GSHEET_LINK):

	headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}

	company_link = "https://www.linkedin.com/voyager/api/organization/companies?decorationId=com.linkedin.voyager.deco.organization.web.WebFullCompanyMain-33&q=universalName&universalName=google"


	with requests.session() as s:
	    s.cookies['li_at'] = li_at
	    s.cookies["JSESSIONID"] = JSESSIONID
	    s.headers = headers
	    s.headers["csrf-token"] = s.cookies["JSESSIONID"]
	    response = s.get(company_link)
	    company_dict = response.json()
	
	st.write(li_at)
	st.write(JSESSIONID)
	st.write(GSHEET_LINK)

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

if __name__ == '__main__':
    main()
