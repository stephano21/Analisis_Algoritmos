print("[1] Celcius a Fahreinth\n[2] Fahreinth a Celcius")
op= int(input("Ingrese una opcion =>"))
if op==1:
    C=float(input("Grados Celcius: "))
    F= C*(9/5)+32
    print(f"Los grados Fahreinth son {F}")
elif op==2:
    F=float(input("Grados Fahreinth: "))
    C=(F-32)*(5/9)
    print(f"Los grados Celcius son {C}")
else:
    print("Ingrese una opcion Válida")