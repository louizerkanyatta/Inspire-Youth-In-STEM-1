stationaries =("pencil","pen","ruler")

#REPLACE THE WHOLE TUPLE

stationaries +("papers", "clipboard", "eraser")
for stationaries in stationaries:
    print(stationaries)

#3) Dictionaries 
#Uses keys in pair values
student={"name":"Louizer","age": "18", "gender": "female","is short":True}
print (student["name"])
print(student["age"])
print(student["gender"])
print(student["is short"])

friends = {"fav_colour":"pink", "hobby": "football", "course": "computer science", "weight":"60", "height":"5'6"}
print(friends["fav_colour"])
print(friends["hobby"])
print(friends["course"])
print(friends["weight"])
print(friends["height"])

print(student.values())
print(student.keys())


 #SETS
my_fruits =("apple","banana","passion")
for fruits in my_fruits:
    print(fruits)

    print(type(my_fruits))
    print(len(my_fruits))