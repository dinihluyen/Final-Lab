import requests             #import thư viện Requests
import json                 #import thư viện 
import meraki_info
import meraki
organization_id = "1154033"
def get_networks():
    url = meraki_info.base_url + '/organizations/' + organization_id + '/networks'
    header = {"X-Cisco-Meraki-API-Key": meraki_info.api_key}
    resp = requests.get(url,headers=header)
    data = resp.json()
    print (json.dumps(data, indent=4))
get_networks()

