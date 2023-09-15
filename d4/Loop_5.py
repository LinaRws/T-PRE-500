#Write a program that takes an n integer as input and displays, for each integer from 2 to n/2, the
#list of its multiples strictly smaller than n, in descending order

n=int(input("Saisir un nombre :"))

for i in range(2, n/2):
    if n%i==0:
        print(i)