def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Mover disco 1 de torre {source} a torre {target}")
        return

    hanoi(n - 1, source, target, auxiliary)
    print(f"Mover disco {n} de torre {source} a torre {target}")
    hanoi(n - 1, auxiliary, source, target)

n = int(input("Ingrese el número de discos: "))
hanoi(n, "A", "B", "C")
