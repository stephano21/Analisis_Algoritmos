import string
#abc=["a","b","c","d","e","f","g","h","i","j","k","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
texto=input("Ingrese texto:")
abc=list(string.ascii_lowercase)
def decifrado_texto(alfabeto,n,texto):
    pass
def cifrado_cesar(alfabeto,n,texto):
    texto_cifrado=" "
    for i in texto:
        if i in alfabeto:
            indiceAtual=alfabeto.index(i)
            indiceCesar=indiceAtual+n
            if indiceCesar>len(alfabeto)-1:
                indiceCesar-=len(alfabeto)-2
                #texto_cifrado=alfabeto[indiceCesar-len(alfabeto)]
    
            texto_cifrado+=alfabeto[indiceCesar]
        else:
            texto_cifrado+=i
    return texto_cifrado


print(cifrado_cesar(abc,3,texto))
