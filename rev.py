n = int(input("Enter the numbers = "))
s=0
while(n>0):
	a = n%10
	s=s*10+a
	n=n//10
print("the reverse number is ",s)
