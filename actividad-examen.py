vehiculos = []

while True:
    print("\ntaller de carros")
    print("1. ingresar vehiculo")
    print("2. registrar salida")
    print("3. reporte de vehiculos reparados")
    print("4. reporte de los vehiculos")
    print("5. salir")

    opcion = input("selecciona una opcion: ")

    if opcion == "1":
        if len(vehiculos) < 30:
            placa = input("digite la placa del vehiculo: ")
            propietario = input("digite el nombre del propietario: ")
            celular = input("digite el numero de celular: ")
            dia = int(input("digite el dia de ingreso del mes: "))

            vehiculo = [placa, propietario, celular, dia, 0, 0]
            vehiculos.append(vehiculo)

            print("vehiculo registrado correctamente")
        else:
            print("ya se registraron los 30 vehiculos")

    elif opcion == "2":
        placa_buscar = input("ingrese la placa del vehiculo: ")
        encontrado = False

        for vehiculo in vehiculos:
            if vehiculo[0] == placa_buscar:
                encontrado = True

                if vehiculo[4] == 0:
                    salida = int(input("digite el dia de salida del mes: "))

                    vehiculo[4] = salida

                    if salida >= vehiculo[3]:
                        vehiculo[5] = salida - vehiculo[3]
                    else:
                        vehiculo[5] = (30 - vehiculo[3]) + salida

                    print("salida registrada correctamente")
                else:
                    print("este vehiculo ya tiene salida registrada")

                break

        if encontrado == False:
            print("vehiculo no encontrado")

    elif opcion == "3":
        print("\n--- vehiculos reparados ---")
        cantidad = 0

        for vehiculo in vehiculos:
            if vehiculo[4] != 0:
                print("placa:", vehiculo[0])
                print("propietario:", vehiculo[1])
                print("dias en el taller:", vehiculo[5])
                print("--------------------")
                cantidad += 1

        print("total de vehiculos reparados:", cantidad)

    elif opcion == "4":
        print("\n--- todos los vehiculos ingresados ---")

        if len(vehiculos) == 0:
            print("no hay vehiculos registrados")
        else:
            for vehiculo in vehiculos:
                print("placa:", vehiculo[0])
                print("propietario:", vehiculo[1])
                print("celular:", vehiculo[2])
                print("--------------------")

    elif opcion == "5":
        print("saliendo del programa...")
        break

    else:
        print("opcion no valida, intente nuevamente")
