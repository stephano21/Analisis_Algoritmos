#diamante iterativo
n=100

for i in range(n+1):
    print(" "*(n-i),"*"*(i+i-1))

for i in range(n-1,0,-1):
    print(" "*(n-i),"*"*(i+i-1))