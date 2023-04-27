a = [1, 4, 6]
b = [11, 33, 22]
b1 = [y for x,y in sorted(zip(b,a))]
a1 = [x for x,y in sorted(zip(b,a))]
print (list(b1))