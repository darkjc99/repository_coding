nombre=input("Ingresar nombre:")
ventas=float(input("Ingresar cantidad de ventas:"))

comision=round(ventas*13/100,2)

print(f"OK {nombre}. Este mes ganaste {comision}")