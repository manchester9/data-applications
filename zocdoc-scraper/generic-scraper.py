###############
# REQUEST ID
###############

# import requests

# url = "https://supervisor.reviewshake.com/api/v2/profiles/add"

# querystring = {"url":"https://www.zocdoc.com/doctor/nabeel-chaudhary-md-279999?LocIdent=118132&reason_visit=75&insuranceCarrier=&insurancePlan=-1&dr_specialty=153&isNewPatient=true&spoAdDecisionId=169669056&ad_decision_token=1e844a0c-f72a-4378-9716-ff87ab1cea3b","from_date":"2018-01-01"}

# headers = {
#     'spiderman-token': "bd75fad5d294638438c9c7da1eb1a8a92a89cdf2",
#     }

# response = requests.request("POST", url, headers=headers, params=querystring)

# print(response.text)


###############
# SCRAPE DATA
###############

import requests

url = "https://supervisor.reviewshake.com/api/v2/profiles/reviews"

querystring = {"job_id":"58582118"}

headers = {
    'spiderman-token': "bd75fad5d294638438c9c7da1eb1a8a92a89cdf2",
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)