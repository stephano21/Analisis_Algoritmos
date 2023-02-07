    
lista=[['Arroz',1.00,1,1],['Azúcar',2.00,7,2],['Sal',1.00,8,1],['Cebolla',2.00,4,4],['Tomat',2.50,5,4],["Atún",5.00,9,4],['Frejol',3.00,10,2],['Fideos',2.00,11,2],['Carne',3.00,6,3],['Pollo',5.00,2,1],["Pesca",3.00,3,2]]

lista.sort(key=lambda x: x[1]/x[2], reverse=False)
for i in lista:
    print(i)

bag_limit1=6
bag_limit2=5
def compras(lista,limit):
    bag=[]
    total=0
    peso=0
    i=0
    while peso<limit and i<len(lista):
        print(peso)
        if peso+lista[i][3]<=limit:
            print('sffhhrtd')
            total+=lista[i][1]
            peso+=lista[i][3]
            bag.append((lista[i][0],lista[i][3]))
            lista.pop(i)
        else:
            cantidad=limit-peso
            print(cantidad)
            fraccion=cantidad/lista[i][3]
            total+=lista[i][1]*fraccion
            peso+=fraccion
            bag.append((lista[i][0],fraccion))
            lista[i][3]=lista[i][3]-fraccion

        i += 1
    return bag, total

bag1,total1=compras(lista,bag_limit1)
bag2, total2=compras(lista,bag_limit2)
print(bag1,total1)
print("--------------------")
print(bag2,total2)
