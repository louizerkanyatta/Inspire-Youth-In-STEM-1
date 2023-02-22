number = 100
if (number%2 ==0):
    print ("even number")
else:
    print ("odd number")

#write all even numbers ranging from 0-100
print("***the values below are odd numbers***")
for odd_numbers in range (1,101):
    if (odd_numbers%2 !=0):
        print(odd_numbers)

#write program to list all even numbers from 1-100
print("***The values below are even numbers***")
for even_numbers in range(1,101):
    if (even_numbers%2 == 0):
        print(even_numbers)

#write a program to list all prime numbers from 1-100
print("***the values below are prime numbers***")
for prime_numbers in range (1,101):
    if prime_numbers > 1:
        for i in range (2, prime_numbers)
        if (prime_numbers % i) == 0:
            break
        else:
            print(prime_numbers) 
