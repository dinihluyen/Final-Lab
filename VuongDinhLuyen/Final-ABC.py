import requests             #import thư viện Requests
import json                 #import thư viện 
import meraki_info
import meraki

#print (meraki_info.base_url)  #in ra thử biến
#print (meraki_info.api_key)  #in ra thử biến
print("Cau A")
def get_organizations():
    url = meraki_info.base_url + '/organizations'
    header = {"X-Cisco-Meraki-API-Key": meraki_info.api_key}
    resp = requests.get(url,headers=header)
    data = resp.json()
    print (json.dumps(data, indent=4))
get_organizations()

print("Cau B")
organization_id = "1154033"
def get_networks():
    url = meraki_info.base_url + '/organizations/' + organization_id + '/networks'
    header = {"X-Cisco-Meraki-API-Key": meraki_info.api_key}
    resp = requests.get(url,headers=header)
    data = resp.json()
    print (json.dumps(data, indent=4))
    for net_id in data:
            print (net_id['id'])
get_networks()
