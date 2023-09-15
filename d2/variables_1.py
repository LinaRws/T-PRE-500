a=0
res=0
for i in range (1,10):
    b=a*10+1
    a=b
    print(b)
    res+=a

print(res)

print("resultats :")

for j in range(1,8):
    print(j, res**j)

