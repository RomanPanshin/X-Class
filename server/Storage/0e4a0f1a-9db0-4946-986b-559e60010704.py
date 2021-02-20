x= 100
n = 0
while(n != 30):
	L = 2*x-30
	M = 2*x+30
	while L != M:
  		if L > M:
    			L = L - M
  		else:
    			M = M - L
	n = M
	x+=1
print(n, " ", x)
