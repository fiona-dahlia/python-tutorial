f = [10, 13, 38, 43]
print (type(f))
print (len(f))
print (f)
print (f[0])
print (f[3])
f.append(20)
print (f)
f.append(56)
print (f)
f[0] = True
print (f[0])
f[1] = "Jerrick"
print (f[1:3])
print (f[4])
print (f[5])
j = [True, "Hi", 9]
k = f + j
print (k)
print (type(k))
print (len(k))