materiales=[['Cemento',5,1,20],['Bloques',300,7,20],['Tablas',100,8,10],['cuartones',100,4,40],['Clavos',1500,5,4],['Moto Sierra',1,9,4],['Zinc',30,10,40],['Tubos eléctricos',50,11,20],['Tubos Cañeria',200,6,30],['Taladro',2,2,5],['Pulidora',1,3,20]]

kg_limit=300
camioneta=[]
peso_act=0
materiales.sort(key=lambda x: x[1]/x[2], reverse=True)
i=0

while peso_act<kg_limit and i<len(materiales):
    if peso_act+(materiales[i][3]*materiales[i][1])<= kg_limit:
        kg=materiales[i][3]*materiales[i][1]
        peso_act+=kg
        camioneta.append((materiales[i][0],kg))
    else:
        Tem_peso=kg_limit-(materiales[i][3]*materiales[i][1])
        print(Tem_peso)
        fraccion=Tem_peso//(materiales[i][3]*materiales[i][1])
        kg=materiales[i][1]*fraccion
        peso_act+=kg
        camioneta.append((materiales[i][0],kg))

    i+=1


print(camioneta)