def fibo_pd(n,cache={0:0,1:1}):
    if n in cache:
        return cache[n]
    else:
        cache[n]=fibo_pd(n-1,cache)+fibo_pd(n-2,cache)
        return cache[n]

print(fibo_pd(500))