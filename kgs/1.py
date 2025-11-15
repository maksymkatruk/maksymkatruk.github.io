# h/a heron verfahren mit quadratwurzel

print("=== Heron-Verfahren: Berechnung der Quadratwurzel ===")

a = float(input("Geben sie eine zahl a ein: "))

eps = 1e-6 

if a < 0:
    print("Fehler: die quadratwurzel einer negativen zahl kann nicht sein.")
else:
    x = a if a >= 1 else 1.0
    iteration = 0

    print("\nIterationsschritte:")
    print(f"{'Nr.':>3} | {'Näherung x':>18} | {'Differenz':>12}")
    print("-" * 40)

    while True:
        iteration += 1
        x_next = 0.5 * (x + a / x)
        diff = abs(x_next - x)
        print(f"{iteration:3d} | {x_next:18.12f} | {diff:12.6g}")
        if diff < eps:
            break
        x = x_next

    print("\nErgebnis:")
    print(f"√{a} ≈ {x_next:.12f}")
    print(f"Anzahl der iterationen: {iteration}")
