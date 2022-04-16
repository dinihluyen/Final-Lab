import requests             #import thư viện Requests
import json                 #import thư viện 
import meraki_info
import meraki

#base_url = "https://api.meraki.com/api/v1"

print (meraki_info.base_url)  #in ra thử biến
print (meraki_info.api_key)  #in ra thử biến

def get_organizations():
    url = meraki_info.base_url + '/organizations'
    header = {"X-Cisco-Meraki-API-Key": meraki_info.api_key}
    resp = requests.get(url,headers=header)
    data = resp.json()
    print (json.dumps(data, indent=4))

get_organizations()