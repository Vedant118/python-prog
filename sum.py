n = int(input("Enter the numbers = "))
t=n
s=0
while(n>0):
	a = n%10
	s=s+a*a*a
	n=n//10
if(t==s):
	print("the armstrong number is ",s)
else:
	print(n," is not armstrong")
