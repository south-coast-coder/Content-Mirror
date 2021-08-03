import json

jsonFile = open("data.json", "r")
data = json.load(jsonFile)
jsonFile.close()
new_channel='dog_vids4'
new_info=['dog1','dog2']
data['Cat_vids']['videos']=["cute_cat1"]
print(data['Cat_vids']['videos'])
data.update({new_channel:{'videos':{}}}) #this is syntax to add new key (videos) with empty space to be filled by vals (if dont do this cant add to it later)
data['Cat_vids']['videos']=["cute_cat2"]
print(data)
data['dog_vids4']['videos']=['bobob']
print(data)
data['dog_vids4']['videos'].append('salad')
print(data)
with open('data.json', 'r+') as f:
   f.seek(0)        # <--- should reset file position to the beginning.
   json.dump(data, f)
#data = json.dumps(channel)
#print(data)
#print(channel['pycon']['videos'])
#with open('data.json', 'r+') as f:
 #   f.seek(0)        # <--- should reset file position to the beginning.
 #   json.dump(new_channel, f)
jsonFile = open("data2.json", "a+")
#need to write something to it - check if empty and if empty add necessary boilerplate
data = json.load(jsonFile)
jsonFile.close()
data['Cat_vids']['videos']=["cute_cat1"]
with open('data.json', 'r+') as f:
   f.seek(0)        # <--- should reset file position to the beginning.
   json.dump(data, f)