n="i am SNEHA abcdefghijklmnopqrstuvwxyz"
a=n.lower()
print(a)
alphabet=set("abcdefghijklmnopqrstuvwxyz")
strr=set({})
for char in n:
	if char in alphabet:
		strr.add(char)
	else:
		pass
if len(strr)==len(alphabet):
	print("True")
	
else:
	print("False")