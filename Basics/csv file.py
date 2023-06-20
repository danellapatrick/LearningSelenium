
import pandas as pd
df = pd.read_json('user_data.json')

# displaying sample output
import json
with open('user_data.json','r') as f:
   data = json.load(f)
#for x in data:
   #print(x[1])
#https://stackoverflow.com/questions/40827356/find-a-value-in-json-using-python
print(data.keys())
#for a in an:
 #  print(an['user'])