import requests
import random
from random import shuffle
result_list=[]
result_list_len=[]
for i in range(100):
    
    r=requests.get("https://randomuser.me/api/")
   

    name=r.json()["results"][0]["name"]["first"]
    surname=r.json()["results"][0]["name"]["last"]
    city=r.json()["results"][0]["location"]["city"]
    country=r.json()["results"][0]["location"]["country"]
    result=list((name+surname+city+country).lower().replace(" ",""))
    
    
    random.shuffle(result)
    result="".join(result)
    result_list.append(result)# String list
    result_list_len.append(len(result)) # String Length List

print(result_list[result_list_len.index(max(result_list_len))])#Index find and than indexing
input()
