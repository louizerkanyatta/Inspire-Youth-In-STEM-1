#! user/bin/env/python3
# this is a single line comment 
# Python program to illustare the use of operators
# Name : Louizer Kanyatta
# Email : louizerkanytta@gmail.com
# Date : 17 th Feb 2023
# File :qperators.py
# use a for loop add five new musicians

favourite_musician= [          ]
for musicians in favourite_musician:
    print(favourite_musician)

favourite_musician.append("sam fischer")
favourite_musician.append("joshua basset")
favourite_musician.append("ariana grande")
favourite_musician.append("lizzo")
favourite_musician.append("doja cat")
for musician in favourite_musician:
    print(musician)

celebs= favourite_musician.copy()
print(celebs)

celebs.sort()
print(celebs)

celebs.pop()
print(celebs)

celebs.pop()
print(celebs)

celebs.count()
print(celebs)
print(len(celebs))


