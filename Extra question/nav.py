import requests
import json
url=requests.get("https://join.navgurukul.org/api/partners")
data=url.json()
with open("data.json","w") as file:
    json.dump(data,file,indent=4)

data_list=[]
data_dict={}
for i in data["data"]:
    data_list.append((i["id"],i["name"]))
    data_dict.update(data_list)
    
print("")
def sorting():
    a=input("Enter: 1. For Ascending order  2. For Descenting order :")
    if a=="1":
        for index in sorted(data_dict):
            print(index,data_dict[index])
    elif a=="2":
        for index in sorted(data_dict,reverse=True):
            print(index,data_dict[index])
sorting()

