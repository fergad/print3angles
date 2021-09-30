def tri(n,tricount):
	for x in range(n):
		print(" ",end='')
	for x in range(tricount):
		print("^", end='')


def full(n):
	for x in range(n):
		tri(n,1+2*x)
		n-=1
		print()


