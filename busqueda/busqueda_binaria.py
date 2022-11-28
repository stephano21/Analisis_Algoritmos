lista=[1,2,3,4,5,6,7,8,9,10]
objetivo=2
def search_binary(lista,objetivo):
    if len(lista)==0:
        return False
    else:
        pivote= len(lista)//2
        if lista[pivote]==objetivo:
            return True
        elif lista[pivote]>objetivo:
            return search_binary(lista[:pivote],objetivo)
        else:
            return search_binary(lista[pivote+1:],objetivo)

print(search_binary(lista,objetivo))
