
def exponente(base,expo):
    if expo==0:
        return 1
    else:
        return base*exponente(base,expo-1)

print(exponente(2,5))