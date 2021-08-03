import json
import sys
import os
import time

try:
    channel= sys.argv[1] #Name of the Channel that User wants to mirror all this initial bit should maybe be within main prog
except:
    print("No Channel Name Provided exiting program ---")
    sys.exit()
   
file=channel+".json" 
print(file)
# At this stage need to use selenium to check channel actually exists - if not need to abort otherwise continue
def exists_json(file): #run this before interacting with any json file in order to check actually has content first - if not need to dump {} into it as this is bare minimum needed for json file to work
      with open(file,'a+') as f:
         try:
            data=json.load(f)
            print("data exists"+str(data))
            return data
         except:
            print("no data")    
            data= {}
            return data
data=exists_json(file)
with open('dog.json','r') as f:
    data=json.load(f)
    print(data)
print(data)
if data ==None:
    data=[]
print("final data"+str(data))
try:
     print(data['videos'])
except:
    print("not videos")
    data.update({'walks1':['dog','dog2']})
new_channel ="new"
new__video="new"
print(type(data))
print(data)
print(type(data))
try:
    print(data['videos']) #checks if key already exists
    data['videos'].append("boo2u") #adds new item without overwriting all old (update is for adding new key value pair or key value list)
except:
    print("no videos found")
    data.update({"videos":["my"]})  #adds key and first value
exists=False
for val in data['videos']:  #turn this into a function
    if val == "boozy":
        exists=True
if exists == False:
    data["videos"].append("boozy")

    
data=dict(data)
with open(file, 'w+') as f:
   f.seek(0)        # <--- should reset file position to the beginning.
   json.dump(data, f)
