import  requests
import json
import os
  
if os.path.isfile("courses.json"):
    with open("courses.json","r") as saral_data:
        data = json.load(saral_data)
else:
    saral_api = " http://saral.navgurukul.org/api/courses"   #This link is a  API and url
    saral_url = requests.get(saral_api) 
    data = saral_url.json()
    with open ("courses.json","w") as saral_data:
        json.dump(data,saral_data,indent = 4)

# Here it was title welcome to navgurukul

print("")
print("** Welcome to navgurukul and Learn basic programming launguage **")
print("")

# And then find the cource name all.....

serial_no = 0
for i in data["availableCourses"]:
    print(serial_no+1 ,i["name"], i["id"])
    serial_no=serial_no+1
    
print("")
user_input =int(input("Enter your courses number that you want to learn:- "))
parent_id=data["availableCourses"][user_input-1]["id"]
parent_name = data["availableCourses"][user_input-1]["name"]
print(data["availableCourses"][user_input-1]["name"])

# And then taking userinput  in previous or next .... previous then it will be print all courses name next then it will be print parents...

user_input_1=input("if you want next or previous n/p: ")
if user_input_1=="p":
    i=0
    while i<len(data["availableCourses"]):
        Courses = (data["availableCourses"][i]["name"])
        print(i+1," ",Courses,data["availableCourses"][i]["id"])
        i=i+1
    user_input = int(input("Enter your courses number that you want to learn:-"))
    print(data["availableCourses"][user_input-1]["name"])

if os.path.isfile("parnet/"+parent_name + str(parent_id)+data["availableCourses"][user_input-1]["name"] +".json"):
    with open("parnet/"+parent_name + str(parent_id)+data["availableCourses"][user_input-1]["name"] +".json","r") as child_data:
        data_1 = json.load(child_data)
else:
    parent_api = "http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][user_input-1]["id"])+"/exercises"
    parent_url = requests.get(parent_api)
    data_1 = parent_url.json()
    with open ("parnet/"+parent_name + str(parent_id)+data["availableCourses"][user_input-1]["name"] +".json","w") as child_data:
        json.dump(data_1,child_data,indent=4)

serial_no_1=0
for i in data_1["data"]:
    print("      ",serial_no_1+1,".",i["name"])
    if len(i["childExercises"])>0:
        s= 0
        for j in i['childExercises']:
            s = s+ 1
            print( "               ",s,j['name'])
    else:
        print("                1",i["slug"])
    serial_no_1+=1
print("")

choose_topic_no = int(input("entre the specific parent exercises : "))
user_input_3=input("Enter topic number that's you want to learn previous or next:- ")
if user_input_3=="p":
    serial_no_1=0
    for i in data_1["data"]:
        print("      ",serial_no_1+1,".",i["name"])
        if len(i["childExercises"])>0:
            s= 0
            for j in i['childExercises']:
                s = s+ 1
                print( "               ",s,j['name'])
        else:
            print("                1",i["slug"])
        serial_no_1+=1
    choose_topic_no = int(input("entre the specific parent exercises : "))
parent_no = data_1["data"][choose_topic_no-1]["name"]
child_id = data_1["data"][choose_topic_no-1]["id"]
print(choose_topic_no,parent_no,child_id)

if data_1["data"][choose_topic_no-1]["childExercises"]== []:
    print("     1.",data_1["data"][choose_topic_no-1]["slug"])
else:
    l = 0
    while l < len(data_1["data"][choose_topic_no-1]["childExercises"]):
        print("     ",l+1,data_1["data"][choose_topic_no-1]["childExercises"][l]["name"])
        l = l+1  
    choose_child_no = int(input("entre the specific child exercises : "))
    slug = (data_1["data"][choose_topic_no-1]["childExercises"][choose_child_no-1]["slug"])

    if os.path.isfile("child/"+ parent_no + str(child_id)+".json"):
        with open("child/"+ parent_no + str(child_id)+".json","r") as Data3:
            data_1 = json.load(Data3)
    else:
        child_exercises_url = ("http://saral.navgurukul.org/api/courses/" +  str(parent_id) +"/exercise/getBySlug?slug=" + slug )
        Data_4 = requests.get(child_exercises_url)
        data_1 = Data_4.json()
        with open("child/"+ parent_no + str(child_id)+".json","w") as Child:
            file = json.dump(data_1,Child,indent=4)
print(data_1["content"])