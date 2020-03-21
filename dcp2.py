a=[1, 2, 3, 4, 5]
b=[]
k1=a[1]*a[2]*a[3]*a[4]
k2=a[0]*a[2]*a[3]*a[4]
k3=a[1]*a[0]*a[3]*a[4]
k4=a[1]*a[0]*a[2]*a[4]
k5=a[0]*a[1]*a[2]*a[3]
b.append(k1)
b.append(k2)
b.append(k3)
b.append(k4)
b.append(k5)
print(b)
