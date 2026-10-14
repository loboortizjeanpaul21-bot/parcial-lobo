vehiculos = []

while True:
    print("\nMenú:")
    print("1. Registrar vehículo")
    print("2. Reporte de vehículos reparados")
    print("3. Reporte de todos los vehículos")
    print("4. Salir")

    opcion = input("Elija una opción: ")

    if opcion == '1':
        if len(vehiculos) >= 30:
            print("No se pueden ingresar más vehículos.")
            continue
        placa = input("Placa del vehículo: ")
        nombre = input("Nombre del propietario: ")
        celular = input("Número celular: ")
        dia_ingreso = int(input("Día de ingreso (1-31): "))
        dia_salida = int(input("Día de salida (0 si no ha salido): "))
        dias_reparacion = 0
        if dia_salida != 0:
            dias_reparacion = dia_salida - dia_ingreso
        vehiculos.append([placa, nombre, celular, dia_ingreso, dia_salida, dias_reparacion])
        print("Vehículo registrado.")

    elif opcion == '2':
        print("\nVehículos reparados:")
        cont = 0
        for v in vehiculos:
            if v[4] != 0:
                print(f"Placa: {v[0]}, Días de reparación: {v[5]}")
                cont += 1
        print(f"Total vehículos reparados: {cont}")

    elif opcion == '3':
        print("\nTodos los vehículos ingresados en el mes:")
        for v in vehiculos:
            print(f"Placa: {v[0]}, Propietario: {v[1]}, Celular: {v[2]}")

    elif opcion == '4':
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida. Intente de nuevo.")
