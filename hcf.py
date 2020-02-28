x=int(input())
y=int(input())
hcf=0
for i in range(1,(min(x,y)+1)):
    if x%i ==0 and y%i==0:
        hcf=i

print(hcf)