#!/user/bin/env/python3
myFavouriteFruits= ["banana","apple","passion","orange","pineapple"]

for fruits in myFavouriteFruits:
    print(fruits)
    print(len(fruits))
    
    friends= ["lynn","daniel","brayan","eldad","dwayne"]
    friends[0] = "lynn"
    print(friends)

new_friends= friends.copy
print(new_friends)
new_friends.sort()
print(new_friends)


new_friends.pop()
print(new_friends)

