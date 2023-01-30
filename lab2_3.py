list=[1,2,3,4,5,6]
n=j=len(list)
for i in range (0,n):
    j-=1
    tmp=list[i]
    list[i]=list[j]
    list[j]=tmp
    if(j==i+1):
        break
print(list)