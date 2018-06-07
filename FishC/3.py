def ab(n):
	if n==1 or n==2:
		return 1
	else :
		return ab(n-1)+ab(n-2)

result=ab(45)
print ('有%d:' % result)
