a=1
pi=0
d=1

for i in range(1,10000):
    a = 2*(i%2)-1
    pi+=a*4/d

    d+=2
print(round(pi,10))


      
