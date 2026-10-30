# dict pop = remove 
# update = to add new data 
a = { "name" : "javeria jabeen",
     "age": 20 , 
     "city" : " bahawalpur", 
     "profession": "doctor of pharmacy"
     }
#a.update({ " car": " bmw m5", })
#a.pop("profession")
a.get("course", "ai")
print(a.get("course", "invalid result"))

print(a)