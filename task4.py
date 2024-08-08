# A simple code on nested dictionary 
bmi = {
        "Esther" : {"height": 5.1,
               "weight": 74},
               "age" : 44,
        "Glory" :  {"height": 6.1,
               "weight" : 50},
               "age" : 34,
        "Kelly" :  {"height" : 6.6,
                 "weight" : 80,
                 "age" :28}
      }     
print(bmi["Esther"]) 
print(" ")
print(bmi)  
Kate = {"height" : 6.7, "weight" : 67, "age" : 29}
bmi["kate"] = Kate 
print(bmi)                