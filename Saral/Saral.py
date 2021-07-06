import requests
import json

# from requests.api import request

saral_api=requests.get("http://saral.navgurukul.org/api/courses")
data= saral_api.json()
with open("saral_data.json","w") as f:
    json.dump(data,f,indent=5)

def get_data():
    serial_no = 1
    for courses in data["availableCourses"]:
        print(serial_no ,".",courses["name"],courses["id"])
        serial_no += 1
    
get_data()

course = int(input("ENTER YOUR COURES : "))
print(data["availableCourses"][course-1]["name"])
user_input1=input("Do you want to previous : ").lower()
if user_input1=="p":
    get_data()

saral_api_1 = ("http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][course-1]["id"])+"/exercises")
saral_url_1=requests.get(saral_api_1)
data_1 = saral_url_1.json()
with open ("parents.json","w") as saral_data_1 :
    json.dump(data_1,saral_data_1,indent=4)  

def saral_data():
    no=0
    print("slu",data_1["data"][1]["slug"])
    for child in range(len(data_1["data"])):
        no+=1
        print("        ",no,".",data_1["data"][child]["name"])
        serial_no_1=1
        if data_1["data"][child]["childExercises"] == []:
            print("             ",serial_no_1,".",data_1["data"][child]["slug"])
            serial_no_1 += 1
        else:

            serial_no=1
            for Question in range(len(data_1["data"][child]["childExercises"])):
                print("              ",serial_no,".",data_1["data"][child]["childExercises"][Question]["name"])
                serial_no+=1 
saral_data()

Slug= int(input("ENTER THE NUMBER of PARENTS NO :"))
print(data_1["data"][Slug-1]["name"])
number1=input("Do you want to p or n: ").lower()
if number1 == "p":
    saral_data()
slug_ind=[]
no=0
List=[] 
for child in range(len(data_1["data"])):
    no+=1
    serial_no_1=1
    if data_1["data"][child]["childExercises"] == List:
        serial_no_1 += 1

        serial_no=1
        for Question in range(len(data_1["data"][Slug-1]["childExercises"])):
            if data_1["data"][child]["childExercises"] == List:
                print("              ",serial_no,".",data_1["data"][Slug-1]["childExercises"][Question]["name"])
                slug = data_1["data"][Slug-1]["childExercises"][Question]["slug"]
                parent = data_1["data"][Slug-1]["childExercises"][Question]['id']
                slug1 = requests.get(" http://saral.navgurukul.org/api/courses/"+parent+"/exercise/getBySlug?slug="+slug)

                slug2 = slug1.json()
                slug_ind.append(slug2["content"])
                serial_no+=1
        break
question_1 = int(input(" YOUR QUESTION NUMBER: "))
question=question_1-1
print(slug_ind[question])
while question_1 > 0:
    next_question = input("DO YOU WANT n or p: ").lower()
    if next_question == "p":
        if  question_1 == 1:
            print("no more question")
            break
        elif question_1 > 0:
            question_1 = question_1 - 2
            print(slug_ind[question_1])
    elif next_question == "n":
        if  question_1 < len(slug_ind):
            index = question_1 + 1
            print(slug_ind[index-1])
            question += 1
            question_1 = question_1 + 1
            if question == (len(slug_ind)-1):
                print("no more question here::")
            break