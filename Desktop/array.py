lst=[]
count=0
n=int(input("enter length of list:"))
for i in range(0,n):
	a=int(input("enter a no: "))
	lst.append(a)
	
	if lst[i]==9:
		count+=1
print(count)
