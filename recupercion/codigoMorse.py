def numero_morse(num):
    NcuentaEncode = ""
    numero_morse = {
    
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", 
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    }
    for c in num:
        if c != " " and c.lower() in numero_morse:
            NcuentaEncode += numero_morse[c.lower()]+" "
        else:
            NcuentaEncode += c
    return NcuentaEncode

def morse_numero(num):
    num=num.split(" ")
    NcuentaDecode = ""
    morse_numero = {
    
    "-----":"0",  ".----":"1",  "..---":"2",  "...--":"3",  "....-":"4", 
     ".....":"5",  "-....":"6",  "--...":"7",  "---..":"8",  "----.":"9",
    }
    for c in num:
        if c != " " and c.lower() in morse_numero:
            NcuentaDecode += morse_numero[c.lower()]
        else:
            NcuentaDecode += c
    return NcuentaDecode


def menu():
    print("-"*50,"\n"," "*20,"Menu principal")
    print("[1] CODIFICAR #CUENTA\n[2] DECODIFICAR #CUENTA\n[0] SALIR")
    return int(input("==>"))



while True:
    op=menu()
    if op==1:
        Ncuenta = input("Numero de cuenta: ")
        while len(str(Ncuenta))!=4:
            print("El numero de cuenta damitido es de 4 digitos")
            Ncuenta = input("Numero de cuenta: ")
        print("Texto codificado: {}".format(numero_morse(Ncuenta)))
    elif op==2:
        morse=input("Numero de cuenta: ")
        print("Texto decodificado: {}".format(morse_numero(morse)))
    elif op==0:
        exit()


