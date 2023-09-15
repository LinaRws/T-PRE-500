def sum(n):
    if n // 10 == 0:
        return n 
    else:
        return n % 10 + sum(n//10)
    
print(sum(123434565))
print(sum(345567426))
print(sum(44490320097))