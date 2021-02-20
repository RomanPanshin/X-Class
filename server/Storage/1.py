res = 0
sx = 0 
while(res!=7):
	sx = sx + 1
	x = sx
	a=0; b=10
	while x > 0:
    		d = x % 6
    		if d > a: a = d
    		if d < b: b = d
    		x = x // 6
	res = a + b
	print(res, " ", sx)
