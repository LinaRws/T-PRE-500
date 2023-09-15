#Print all integers divisible by 7 from 10 000 to 1.

for i in range(10000,1,-1): #-1 pour aller dans l'ordre décroissant
    if (i%7==0):
        print(i)
