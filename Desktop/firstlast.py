lst=[]
n=int(input("enter length of list:"))
def first_last6():
	for i in range(1,n+1):
		a=int(input("enter a no: "))
		lst.append(a)
	if lst[0]==6 or lst[n-1]==6:
		print("True")
	else:
		print("False")
first_last6()