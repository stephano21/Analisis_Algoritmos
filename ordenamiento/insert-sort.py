#ordenamiento por insersion
#
a=[7,5,1,3,8,4,9,2,6]


for i in range(0,len(a)): #for i in range(0.len(a)):
    actual=a[i]
    indice=i
    while indice>0 and a[indice-1]>actual:
        a[indice]= a[indice-1]
        indice=indice-1
    a[indice]= actual

print (a)