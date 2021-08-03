import json
import sys
import os

print(str(sys.argv[1]))
data_base = {}
def exists_json(file): #run this before interacting with any json file in order to check actually has content first - if not need to dump {} into it as this is bare minimum needed for json file to work
   if os.path.exists(file):
      with open(file,'a+') as f:
         try:
            data=json.open(f)
         except:
            print("no data")
            with open(file, 'w+') as f:
               initial={}
               json.dump(initial,f)
               print("dumped")         
   else:
      with open(file, 'w+') as f:
         initial={}
         json.dump(initial,f)
         print("dumped")         
exists_json('data3.json')
jsonFile = open("data3.json", "r")
data = json.load(jsonFile)
jsonFile.close()
new_channel='dog_vids4'
new_info=['dog1','dog2']
data.update({new_channel:{'videos':{}}}) #this is syntax to add new key (videos) with empty space to be filled by vals (if dont do this cant add to it later)
print(data)
data['dog_vids4']['videos']=['bobob']
print(data)
data['dog_vids4']['videos'].append('salad')
print(data)
with open('data3.json', 'r+') as f:
   f.seek(0)        # <--- should reset file position to the beginning.
   json.dump(data, f)
#data = json.dumps(channel)
#print(data)
#print(channel['pycon']['videos'])
#with open('data.json', 'r+') as f:
 #   f.seek(0)        # <--- should reset file position to the beginning.
 #   json.dump(new_channel, f)
exists_json('data2.json')
jsonFile = open("data2.json", "a+")
#need to write something to it - check if empty and if empty add necessary boilerplate
try:
    data = json.load(jsonFile)
except:
   data={}
jsonFile.close()
data.update({'Space':{'videos':{}}})
with open('data2.json', 'r+') as f:
   f.seek(0)        # <--- should reset file position to the beginning.
   json.dump(data, f)