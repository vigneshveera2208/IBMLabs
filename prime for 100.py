a=[]
for i in range(1,101):
    for j in range(2,i//2+1):
        if(i%j==0):print("{} is not prime".format(i));break
    else:a.append(i);print(i," is prime")
print(a)