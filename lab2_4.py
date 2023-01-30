n=int(input("Enter list size : "))
print("Enter list elements : ")
list=[]
for i in range(0,n):
    j=int(input())
    list.append(j)
a=min(list)
b=max(list)
c=(a+b)/2
print("Avg. : ",c)