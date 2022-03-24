r = int(input("enter the alphabet = "))
k = int(input("enter the last alphabet = "))
for i in range(r,k):
	for v in range(r,1+i):
		print(chr(i),end=" ")
	print()
