def is_happy(n):
	while n!=1 and n!=4:
		a=0
		while n:
			r=n%10
			a+=r*r
			n//=10
		n=a
	if n==1:
		return True
	else:
		return False
while True:
	x=input("Check or Range: ")
	if x =="Check" or x=="check":
		n=int(input("Enter a num: "))
		if is_happy(n):
			print("Happy")
		else:
			print("Unhappy")
	elif x=="Range" or x=="range":
		p,q=map(int,input("Enter range: ").split())
		if p>q:
			p,q=q,p
		y=input("Happy or Unhappy: ")
		for i in range(p,q+1):
			if y=="Happy" or y=="happy":
					if is_happy(i):
						print(i,end=' ')
			elif y=="Unhappy" or y=="unhappy":
					if not is_happy(i) :
						print(i,end=' ')
			else:
				print("innvalid input")
		print()
	else:
			print("invalid input")
			break		