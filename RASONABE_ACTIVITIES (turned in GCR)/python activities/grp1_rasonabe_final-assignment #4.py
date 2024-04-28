#1 - Creation of New Dictionary
my_dict = {"name": "Chiara", "age": 21}
print(my_dict)


#2 - Accessing Items in the Dictionary
print(my_dict["name"])


#3 - Change Values in the Dictionary
my_dict["age"] = 21
print(my_dict)


#4 - Loop Through a Dictionary Values
for key in my_dict:
    print(my_dict[key])


#5 - Check if Key Exists in the Dictionary
if "name" in my_dict:
    print("Name exists in the dictionary")


#6 - Checking for Dictionary Length
print(len(my_dict))  
    

#7 - Adding Items in the Dictionary
my_dict["email"] = "rasonabechiaramae_bscs@plmun.edu.ph"
print(my_dict)


#8 - Removing Items in the Dictionary
my_dict.pop("age")
print(my_dict)


#9 - Remove an Item Using del Statement
del my_dict["name"]
print(my_dict)


#10 - The dict() Constructor
new_dict = dict(brand="LEGO", model="Bricks", year=1932)
print(new_dict)


#11 - Dictionary Methods
print(my_dict.get("name", "Default Name"))






