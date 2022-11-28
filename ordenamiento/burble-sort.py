#metodo burbuja
a=[2,1,3,4,5,6,7,8]
temp=0
for i in range(0,len(a)):
    for i in range(0,len(a)-1):
        if a[i]>a[i+1]:
            temp=a[i+1]
            a[i+1]=a[i]
            a[i]=temp
print(a)