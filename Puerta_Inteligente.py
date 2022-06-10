# INSTRUCCIONES
# Ingrese las ubicaciones HABITACION1/HABITACION2/HABITACION3/HABITACION4/HABITACION5/HABITACION6/HABITACION7 con letras mayusculas
# Ingrese el estado 0/1 respectivamente donde 0 significa abrir y 1 significa cerrar

def puerta_Inteligente():
    """
    La función puerta inteligente nos permitirá ingresar a las distintas ubicaciones, las cuales son:
    HABITACION1, HABITACION2, HABITACION3, HABITACION4, HABITACION5, HABITACION6, HABITACION7.
    
    Tomando en cuenta que para poder acceder a las distintas Habitaciones establecidas se de tener la llave de acceso dentro del rango, 
    y dependiendo del estado que se encuentre se puede acceder a dicha habitacion.
    Nota: El estado objetivo del agente puerta inteligente es el estado abierto. 
    """

        
    try:
          # inicializamos estadoObjetivo
        # 0 idica abrir y 1 indica cerrar
        estadoObjetivo = {'HABITACION1': '0', 'HABITACION2': '0', 'HABITACION3': '0',
            'HABITACION4': '0', 'HABITACION5': '0', 'HABITACION6': '0', 'HABITACION7': '0'}
        costo = 0 
       
        

        # el usuario indica la ubicación en donde se encuentra la puerta inteligente.
        ubicacion = input("Inserte la ubicación de la puerta Inteligente: ")
        # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
        estado = input("Inserte el estado de la: "+ubicacion + " ")
        llave = input("La llave se encuentra dentro del rango (si o no): ")

        if (llave == 'si'):
            if (ubicacion == 'HABITACION1'):
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion2 = input("Inserte el estado de la HABITACION 2 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion3 = input("Inserte el estado de la HABITACION 3 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion4 = input("Inserte el estado de la HABITACION 4 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion5 = input("Inserte el estado de la HABITACION 5 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion6 = input("Inserte el estado de la HABITACION 6 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion7 = input("Inserte el estado de la HABITACION 7 ")

                # Se muestran los resultados deseados.
                print("Objetivo Deseado:" + str(estadoObjetivo))
                # Se muestra la habitación en la que se encuentra la puerta Inteligente
                print("La Puerta Inteligente se encuentra en la HABITACION 1")

                if(estado == '1'):
                    # La puerta Inteligente de la HABITACION1 se encuentra cerrada
                    print("La puerta Inteligente de la HABITACION1 se encuentra cerrada")
                    # La puerta Inteligente empezará abrirse
                    estadoObjetivo['HABITACION1'] = '0'
                    costo += 1  # El costo incrementará cada que la puerta Inteligente se abra
                    print("La puerta Inteligente esta abierta en la HABITACION 1")
                    # Muestra el costo actual.
                    print("El costo actual es: " + str(costo))
                    llave = input(
                        "La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):

                        if(ubicacion2 == '1'):
                            # Si la puerta inteligente de la HABITACION2 se encuentra cerrado.
                            print(
                                "La puerta Inteligente de la HABITACION 2 se encuentra cerrado")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION2'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print(
                                "La puerta inteligente se encuentra abierta en la HABITACION 2")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print(
                                "La puerta Inteligente de la HABITACION 2 se encuentra abierta")
                            print(
                                "No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion3 == '1'):
                            # Si la puerta inteligente de la HABITACION3 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 3 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION3'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 3")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 3 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input(
                        "La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion4 == '1'):
                            # Si la puerta inteligente de la HABITACION4 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 4 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION4'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print(
                                "La puerta inteligente se encuentra abierta en la HABITACION 4")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 4 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input(
                        "La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion5 == '1'):
                            # Si la puerta inteligente de la HABITACION5 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 5 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION5'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 5")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 5 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input(
                        "La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion6 == '1'):
                            # Si la puerta inteligente de la HABITACION6 se encuentra cerrado.
                            print(
                                "La puerta Inteligente de la HABITACION 6 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION6'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print(
                                "La puerta inteligente se encuentra abierta en la HABITACION 6")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print(
                                "La puerta Inteligente de la HABITACION 6 se encuentra abierta")
                            print(
                                "No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input(
                        "La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion7 == '1'):
                            # Si la puerta inteligente de la HABITACION7 se encuentra cerrado.
                            print(
                                "La puerta Inteligente de la HABITACION 7 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION7'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print(
                                "La puerta inteligente se encuentra abierta en la HABITACION 7")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print(
                                "La puerta Inteligente de la HABITACION 7 se encuentra abierta")
                            print(
                                "No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

            elif (estado == '0'):
                # La puerta Inteligente se encuentra abierta
                print("La puerta Inteligente de la HABITACION1 se encuentra abierta")
                print("No se ejecuta ninguna acción. El costo actual es: " + str(costo))

                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):

                    if(ubicacion2 == '1'):
                        # Si la puerta inteligente de la HABITACION2 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 2 se encuentra cerrado")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1  # Incrementa el costo por moverse de locacion
                        # Muestra el costo actual
                        print("El costo actual es: " + str(costo))
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION2'] = '0'
                        costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 2")
                        # Muestra el costo actual
                        print("El costo actual es: " + str(costo))
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 2 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))
                        
                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")

                        
                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):
                    if(ubicacion3 == '1'):
                        # Si la puerta inteligente de la HABITACION3 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 3 se encuenta cerrada")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1 #Incrementa el costo por moverse de locacion
                        print("El costo actual es: " +str(costo))#Muestra el costo actual
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION3'] = '0'
                        costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 3")
                        print("El costo actual es: " +str(costo)) #Muestra el costo actual
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 3 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")


                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):
                    if(ubicacion4 == '1'):
                        # Si la puerta inteligente de la HABITACION4 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 4 se encuenta cerrada")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1 #Incrementa el costo por moverse de locacion
                        print("El costo actual es: " +str(costo))#Muestra el costo actual
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION4'] = '0'
                        costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 4")
                        print("El costo actual es: " +str(costo)) #Muestra el costo actual
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 4 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")

                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):
                    if(ubicacion5 == '1'):
                        # Si la puerta inteligente de la HABITACION5 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 5 se encuenta cerrada")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1 #Incrementa el costo por moverse de locacion
                        print("El costo actual es: " +str(costo))#Muestra el costo actual
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION5'] = '0'
                        costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 5")
                        print("El costo actual es: " +str(costo)) #Muestra el costo actual
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 5 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")

                    
                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):
                    if(ubicacion6 == '1'):
                        # Si la puerta inteligente de la HABITACION6 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 6 se encuenta cerrada")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1 #Incrementa el costo por moverse de locacion
                        print("El costo actual es: " +str(costo))#Muestra el costo actual
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION6'] = '0'
                        costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 6")
                        print("El costo actual es: " +str(costo)) #Muestra el costo actual
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 6 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")

                    
                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):
                    if(ubicacion7 == '1'):
                        # Si la puerta inteligente de la HABITACION7 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 7 se encuenta cerrada")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1 #Incrementa el costo por moverse de locacion
                        print("El costo actual es: " +str(costo))#Muestra el costo actual
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION7'] = '0'
                        costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 7")
                        print("El costo actual es: " +str(costo)) #Muestra el costo actual
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 7 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")

            #HABITACION 2
            
            if (ubicacion == 'HABITACION2'):
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion2 = input("Inserte el estado de la HABITACION 1 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion3 = input("Inserte el estado de la HABITACION 3 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion4 = input("Inserte el estado de la HABITACION 4 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion5 = input("Inserte el estado de la HABITACION 5 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion6 = input("Inserte el estado de la HABITACION 6 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion7 = input("Inserte el estado de la HABITACION 7 ")

                # Se muestran los resultados deseados.
                print("Objetivo Deseado:" + str(estadoObjetivo))
                # Se muestra la habitación en la que se encuentra la puerta Inteligente
                print("La Puerta Inteligente se encuentra en la HABITACION 1")

                if(estado == '1'):
                    # La puerta Inteligente de la HABITACION1 se encuentra cerrada
                    print("La puerta Inteligente se encuentra cerrada")
                    # La puerta Inteligente empezará abrirse
                    estadoObjetivo['HABITACION2'] = '0'
                    costo += 1  # El costo incrementará cada que la puerta Inteligente se abra
                    print("La puerta Inteligente esta abierta en la HABITACION 2")
                    # Muestra el costo actual.
                    print("El costo actual es: " + str(costo))
                    llave = input("La llave se encuentra dentro del rango (si o no): ")
                    


                    if (llave == 'si'):

                        if(ubicacion2 == '1'):
                            # Si la puerta inteligente de la HABITACION1 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 1 se encuentra cerrado")
                            print("El usuario se dirige a la siguiente HABITACION1")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION1'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 1")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 1 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion3 == '1'):
                            # Si la puerta inteligente de la HABITACION3 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 3 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION3'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 3")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 3 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion4 == '1'):
                            # Si la puerta inteligente de la HABITACION4 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 4 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION4'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 4")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 4 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion5 == '1'):
                            # Si la puerta inteligente de la HABITACION5 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 5 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION5'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 5")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 5 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input(
                        "La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion6 == '1'):
                            # Si la puerta inteligente de la HABITACION6 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 6 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION6'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 6")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 6 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion7 == '1'):
                            # Si la puerta inteligente de la HABITACION7 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 7 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION7'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 7")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 7 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                elif (estado == '0'):
                    # La puerta Inteligente de la HABITACION2 se encuentra abierta
                    print("La puerta Inteligente de la HABITACION2 se encuentra abierta")
                    print("No se ejecuta ninguna acción. El costo actual es: " + str(costo))

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):

                        if(ubicacion2 == '1'):
                            # Si la puerta inteligente de la HABITACION1 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 1 se encuentra cerrado")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION1'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 1")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 1 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))
                            
                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                            
                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion3 == '1'):
                            # Si la puerta inteligente de la HABITACION3 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 3 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1 #Incrementa el costo por moverse de locacion
                            print("El costo actual es: " +str(costo))#Muestra el costo actual
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION3'] = '0'
                            costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 3")
                            print("El costo actual es: " +str(costo)) #Muestra el costo actual
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 3 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")


                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion4 == '1'):
                            # Si la puerta inteligente de la HABITACION4 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 4 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1 #Incrementa el costo por moverse de locacion
                            print("El costo actual es: " +str(costo))#Muestra el costo actual
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION4'] = '0'
                            costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 4")
                            print("El costo actual es: " +str(costo)) #Muestra el costo actual
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 4 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")


                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion5 == '1'):
                            # Si la puerta inteligente de la HABITACION5 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 5 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1 #Incrementa el costo por moverse de locacion
                            print("El costo actual es: " +str(costo))#Muestra el costo actual
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION5'] = '0'
                            costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 5")
                            print("El costo actual es: " +str(costo)) #Muestra el costo actual
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 5 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                        
                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion6 == '1'):
                            # Si la puerta inteligente de la HABITACION6 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 6 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1 #Incrementa el costo por moverse de locacion
                            print("El costo actual es: " +str(costo))#Muestra el costo actual
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION6'] = '0'
                            costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 6")
                            print("El costo actual es: " +str(costo)) #Muestra el costo actual
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 6 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                        
                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion7 == '1'):
                            # Si la puerta inteligente de la HABITACION7 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 7 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1 #Incrementa el costo por moverse de locacion
                            print("El costo actual es: " +str(costo))#Muestra el costo actual
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION7'] = '0'
                            costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 7")
                            print("El costo actual es: " +str(costo)) #Muestra el costo actual
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 7 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")



        #HABITACION3
        if (ubicacion == 'HABITACION3'):
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion2 = input("Inserte el estado de la HABITACION 1 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion3 = input("Inserte el estado de la HABITACION 2 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion4 = input("Inserte el estado de la HABITACION 4 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion5 = input("Inserte el estado de la HABITACION 5 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion6 = input("Inserte el estado de la HABITACION 6 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion7 = input("Inserte el estado de la HABITACION 7 ")

                # Se muestran los resultados deseados.
                print("Objetivo Deseado:" + str(estadoObjetivo))
                # Se muestra la habitación en la que se encuentra la puerta Inteligente
                print("La Puerta Inteligente se encuentra en la HABITACION 3")

                if(estado == '1'):
                    # La puerta Inteligente de la HABITACION1 se encuentra cerrada
                    print("La puerta Inteligente se encuentra cerrada")
                    # La puerta Inteligente empezará abrirse
                    estadoObjetivo['HABITACION3'] = '0'
                    costo += 1  # El costo incrementará cada que la puerta Inteligente se abra
                    print("La puerta Inteligente esta abierta en la HABITACION 3")
                    # Muestra el costo actual.
                    print("El costo actual es: " + str(costo))
                    llave = input("La llave se encuentra dentro del rango (si o no): ")
                    


                    if (llave == 'si'):

                        if(ubicacion2 == '1'):
                            # Si la puerta inteligente de la HABITACION1 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 1 se encuentra cerrado")
                            print("El usuario se dirige a la siguiente HABITACION1")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION1'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 1")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 1 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input(
                        "La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion3 == '1'):
                            # Si la puerta inteligente de la HABITACION2 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 2 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION2'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 2")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 2 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion4 == '1'):
                            # Si la puerta inteligente de la HABITACION4 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 4 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION4'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 4")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 4 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input(
                        "La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion5 == '1'):
                            # Si la puerta inteligente de la HABITACION5 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 5 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION5'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 5")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 5 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion6 == '1'):
                            # Si la puerta inteligente de la HABITACION6 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 6 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION6'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 6")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 6 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion7 == '1'):
                            # Si la puerta inteligente de la HABITACION7 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 7 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION7'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 7")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 7 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                elif (estado == '0'):
                    # La puerta Inteligente de la HABITACION3 se encuentra abierta
                    print("La puerta Inteligente de la HABITACION3 se encuentra abierta")
                    print("No se ejecuta ninguna acción. El costo actual es: " + str(costo))

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):

                        if(ubicacion2 == '1'):
                            # Si la puerta inteligente de la HABITACION1 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 1 se encuentra cerrado")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION1'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 1")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 1 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))
                        
                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                        
                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion3 == '1'):
                            # Si la puerta inteligente de la HABITACION2 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 2 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1 #Incrementa el costo por moverse de locacion
                            print("El costo actual es: " +str(costo))#Muestra el costo actual
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION2'] = '0'
                            costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 2")
                            print("El costo actual es: " +str(costo)) #Muestra el costo actual
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 2 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")


                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion4 == '1'):
                            # Si la puerta inteligente de la HABITACION4 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 4 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1 #Incrementa el costo por moverse de locacion
                            print("El costo actual es: " +str(costo))#Muestra el costo actual
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION4'] = '0'
                            costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 4")
                            print("El costo actual es: " +str(costo)) #Muestra el costo actual
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 4 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")


                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion5 == '1'):
                            # Si la puerta inteligente de la HABITACION5 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 5 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1 #Incrementa el costo por moverse de locacion
                            print("El costo actual es: " +str(costo))#Muestra el costo actual
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION5'] = '0'
                            costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 5")
                            print("El costo actual es: " +str(costo)) #Muestra el costo actual
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 5 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                        
                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion6 == '1'):
                            # Si la puerta inteligente de la HABITACION6 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 6 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1 #Incrementa el costo por moverse de locacion
                            print("El costo actual es: " +str(costo))#Muestra el costo actual
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION6'] = '0'
                            costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 6")
                            print("El costo actual es: " +str(costo)) #Muestra el costo actual
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 6 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                        
                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion7 == '1'):
                            # Si la puerta inteligente de la HABITACION7 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 7 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1 #Incrementa el costo por moverse de locacion
                            print("El costo actual es: " +str(costo))#Muestra el costo actual
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION7'] = '0'
                            costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 7")
                            print("El costo actual es: " +str(costo)) #Muestra el costo actual
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 7 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")
                        
        #HABITACION 4
        if (ubicacion == 'HABITACION4'):
            # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
            ubicacion2 = input("Inserte el estado de la HABITACION 1 ")
            # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
            ubicacion3 = input("Inserte el estado de la HABITACION 2 ")
            # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
            ubicacion4 = input("Inserte el estado de la HABITACION 3 ")
            # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
            ubicacion5 = input("Inserte el estado de la HABITACION 5 ")
            # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
            ubicacion6 = input("Inserte el estado de la HABITACION 6 ")
            # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
            ubicacion7 = input("Inserte el estado de la HABITACION 7 ")

            # Se muestran los resultados deseados.
            print("Objetivo Deseado:" + str(estadoObjetivo))
            # Se muestra la habitación en la que se encuentra la puerta Inteligente
            print("La Puerta Inteligente se encuentra en la HABITACION 4")

            if(estado == '1'):
                # La puerta Inteligente de la HABITACION4 se encuentra cerrada
                print("La puerta Inteligente se encuentra cerrada")
                # La puerta Inteligente empezará abrirse
                estadoObjetivo['HABITACION4'] = '0'
                costo += 1  # El costo incrementará cada que la puerta Inteligente se abra
                print("La puerta Inteligente esta abierta en la HABITACION 4")
                # Muestra el costo actual.
                print("El costo actual es: " + str(costo))
                llave = input("La llave se encuentra dentro del rango (si o no): ")
                        

                if (llave == 'si'):

                    if(ubicacion2 == '1'):
                        # Si la puerta inteligente de la HABITACION1 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 1 se encuentra cerrado")
                        print("El usuario se dirige a la siguiente HABITACION1")
                        costo += 1  # Incrementa el costo por moverse de locacion
                        # Muestra el costo actual
                        print("El costo actual es: " + str(costo))
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION1'] = '0'
                        costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 1")
                        # Muestra el costo actual
                        print("El costo actual es: " + str(costo))
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 1 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion3 == '1'):
                            # Si la puerta inteligente de la HABITACION2 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 2 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION2'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 2")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 2 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion4 == '1'):
                            # Si la puerta inteligente de la HABITACION3 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 3 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION3'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 3")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 3 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion5 == '1'):
                            # Si la puerta inteligente de la HABITACION5 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 5 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION5'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 5")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 5 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion6 == '1'):
                            # Si la puerta inteligente de la HABITACION6 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 6 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION6'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 6")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 6 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion7 == '1'):
                            # Si la puerta inteligente de la HABITACION7 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 7 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION7'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 7")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 7 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

            elif (estado == '0'):
                # La puerta Inteligente se encuentra abierta
                print("La puerta Inteligente de la HABITACION4 se encuentra abierta")
                print("No se ejecuta ninguna acción. El costo actual es: " + str(costo))

                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):

                    if(ubicacion2 == '1'):
                        # Si la puerta inteligente de la HABITACION1 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 1 se encuentra cerrado")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1  # Incrementa el costo por moverse de locacion
                        # Muestra el costo actual
                        print("El costo actual es: " + str(costo))
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION1'] = '0'
                        costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 1")
                        # Muestra el costo actual
                        print("El costo actual es: " + str(costo))
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 1 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))
                        
                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")

                        
                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):
                    if(ubicacion3 == '1'):
                        # Si la puerta inteligente de la HABITACION2 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 2 se encuenta cerrada")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1 #Incrementa el costo por moverse de locacion
                        print("El costo actual es: " +str(costo))#Muestra el costo actual
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION2'] = '0'
                        costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 2")
                        print("El costo actual es: " +str(costo)) #Muestra el costo actual
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 2 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")


                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):
                    if(ubicacion4 == '1'):
                        # Si la puerta inteligente de la HABITACION3 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 3 se encuenta cerrada")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1 #Incrementa el costo por moverse de locacion
                        print("El costo actual es: " +str(costo))#Muestra el costo actual
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION3'] = '0'
                        costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 3")
                        print("El costo actual es: " +str(costo)) #Muestra el costo actual
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 3 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")


                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):
                    if(ubicacion5 == '1'):
                        # Si la puerta inteligente de la HABITACION5 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 5 se encuenta cerrada")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1 #Incrementa el costo por moverse de locacion
                        print("El costo actual es: " +str(costo))#Muestra el costo actual
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION5'] = '0'
                        costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 5")
                        print("El costo actual es: " +str(costo)) #Muestra el costo actual
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 5 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")

                        
                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):
                    if(ubicacion6 == '1'):
                        # Si la puerta inteligente de la HABITACION6 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 6 se encuenta cerrada")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1 #Incrementa el costo por moverse de locacion
                        print("El costo actual es: " +str(costo))#Muestra el costo actual
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION6'] = '0'
                        costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 6")
                        print("El costo actual es: " +str(costo)) #Muestra el costo actual
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 6 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")

                        
                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):
                    if(ubicacion7 == '1'):
                        # Si la puerta inteligente de la HABITACION7 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 7 se encuenta cerrada")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1 #Incrementa el costo por moverse de locacion
                        print("El costo actual es: " +str(costo))#Muestra el costo actual
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION7'] = '0'
                        costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 7")
                        print("El costo actual es: " +str(costo)) #Muestra el costo actual
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 7 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")

            #HABITACION 5
            if (ubicacion == 'HABITACION5'):
                    # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                    ubicacion2 = input("Inserte el estado de la HABITACION 1 ")
                    # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                    ubicacion3 = input("Inserte el estado de la HABITACION 2 ")
                    # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                    ubicacion4 = input("Inserte el estado de la HABITACION 3 ")
                    # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                    ubicacion5 = input("Inserte el estado de la HABITACION 4 ")
                    # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                    ubicacion6 = input("Inserte el estado de la HABITACION 6 ")
                    # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                    ubicacion7 = input("Inserte el estado de la HABITACION 7 ")

                    # Se muestran los resultados deseados.
                    print("Objetivo Deseado:" + str(estadoObjetivo))
                    # Se muestra la habitación en la que se encuentra la puerta Inteligente
                    print("La Puerta Inteligente se encuentra en la HABITACION 5")

                    if(estado == '1'):
                        # La puerta Inteligente de la HABITACION5 se encuentra cerrada
                        print("La puerta Inteligente de la HABITACION 5 se encuentra cerrada")
                        # La puerta Inteligente empezará abrirse
                        estadoObjetivo['HABITACION5'] = '0'
                        costo += 1  # El costo incrementará cada que la puerta Inteligente se abra
                        print("La puerta Inteligente esta abierta en la HABITACION 5")
                        # Muestra el costo actual.
                        print("El costo actual es: " + str(costo))
                        llave = input("La llave se encuentra dentro del rango (si o no): ")
                        


                        if (llave == 'si'):

                            if(ubicacion2 == '1'):
                                # Si la puerta inteligente de la HABITACION1 se encuentra cerrado.
                                print("La puerta Inteligente de la HABITACION 1 se encuentra cerrado")
                                print("El usuario se dirige a la siguiente HABITACION1")
                                costo += 1  # Incrementa el costo por moverse de locacion
                                # Muestra el costo actual
                                print("El costo actual es: " + str(costo))
                                # La puerta inteligente se abrirá
                                estadoObjetivo['HABITACION1'] = '0'
                                costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                                print("La puerta inteligente se encuentra abierta en la HABITACION 1")
                                # Muestra el costo actual
                                print("El costo actual es: " + str(costo))
                            else:
                                # La puerta inteligente se encuentra abierta
                                print("La puerta Inteligente de la HABITACION 1 se encuentra abierta")
                                print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                        elif (llave == 'no'):
                            print("No se encuentra dentro del rango establecido!")

                        else:
                            print("Opción Inválida!!!")

                        llave = input("La llave se encuentra dentro del rango (si o no): ")

                        if (llave == 'si'):
                            if(ubicacion3 == '1'):
                                # Si la puerta inteligente de la HABITACION2 se encuentra cerrado.
                                print("La puerta Inteligente de la HABITACION 2 se encuenta cerrada")
                                print("El usuario se dirige a la siguiente HABITACION")
                                costo += 1  # Incrementa el costo por moverse de locacion
                                # Muestra el costo actual
                                print("El costo actual es: " + str(costo))
                                # La puerta inteligente se abrirá
                                estadoObjetivo['HABITACION2'] = '0'
                                costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                                print("La puerta inteligente se encuentra abierta en la HABITACION 2")
                                # Muestra el costo actual
                                print("El costo actual es: " + str(costo))
                            else:
                                # La puerta inteligente se encuentra abierta
                                print("La puerta Inteligente de la HABITACION 2 se encuentra abierta")
                                print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                        elif (llave == 'no'):
                            print("No se encuentra dentro del rango establecido!")

                        else:
                            print("Opción Inválida!!!")

                        llave = input("La llave se encuentra dentro del rango (si o no): ")

                        if (llave == 'si'):
                            if(ubicacion4 == '1'):
                                # Si la puerta inteligente de la HABITACION3 se encuentra cerrado.
                                print("La puerta Inteligente de la HABITACION 3 se encuenta cerrada")
                                print("El usuario se dirige a la siguiente HABITACION")
                                costo += 1  # Incrementa el costo por moverse de locacion
                                # Muestra el costo actual
                                print("El costo actual es: " + str(costo))
                                # La puerta inteligente se abrirá
                                estadoObjetivo['HABITACION3'] = '0'
                                costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                                print("La puerta inteligente se encuentra abierta en la HABITACION 3")
                                # Muestra el costo actual
                                print("El costo actual es: " + str(costo))
                            else:
                                # La puerta inteligente se encuentra abierta
                                print("La puerta Inteligente de la HABITACION 3 se encuentra abierta")
                                print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                        elif (llave == 'no'):
                            print("No se encuentra dentro del rango establecido!")

                        else:
                            print("Opción Inválida!!!")

                        llave = input("La llave se encuentra dentro del rango (si o no): ")

                        if (llave == 'si'):
                            if(ubicacion5 == '1'):
                                # Si la puerta inteligente de la HABITACION4 se encuentra cerrado.
                                print("La puerta Inteligente de la HABITACION 4 se encuenta cerrada")
                                print("El usuario se dirige a la siguiente HABITACION")
                                costo += 1  # Incrementa el costo por moverse de locacion
                                # Muestra el costo actual
                                print("El costo actual es: " + str(costo))
                                # La puerta inteligente se abrirá
                                estadoObjetivo['HABITACION4'] = '0'
                                costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                                print("La puerta inteligente se encuentra abierta en la HABITACION 4")
                                # Muestra el costo actual
                                print("El costo actual es: " + str(costo))
                            else:
                                # La puerta inteligente se encuentra abierta
                                print("La puerta Inteligente de la HABITACION 4 se encuentra abierta")
                                print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                        elif (llave == 'no'):
                            print("No se encuentra dentro del rango establecido!")

                        else:
                            print("Opción Inválida!!!")

                        llave = input("La llave se encuentra dentro del rango (si o no): ")

                        if (llave == 'si'):
                            if(ubicacion6 == '1'):
                                # Si la puerta inteligente de la HABITACION6 se encuentra cerrado.
                                print("La puerta Inteligente de la HABITACION 6 se encuenta cerrada")
                                print("El usuario se dirige a la siguiente HABITACION")
                                costo += 1  # Incrementa el costo por moverse de locacion
                                # Muestra el costo actual
                                print("El costo actual es: " + str(costo))
                                # La puerta inteligente se abrirá
                                estadoObjetivo['HABITACION6'] = '0'
                                costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                                print("La puerta inteligente se encuentra abierta en la HABITACION 6")
                                # Muestra el costo actual
                                print("El costo actual es: " + str(costo))
                            else:
                                # La puerta inteligente se encuentra abierta
                                print("La puerta Inteligente de la HABITACION 6 se encuentra abierta")
                                print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                        elif (llave == 'no'):
                            print("No se encuentra dentro del rango establecido!")

                        else:
                            print("Opción Inválida!!!")

                        llave = input("La llave se encuentra dentro del rango (si o no): ")

                        if (llave == 'si'):
                            if(ubicacion7 == '1'):
                                # Si la puerta inteligente de la HABITACION7 se encuentra cerrado.
                                print("La puerta Inteligente de la HABITACION 7 se encuenta cerrada")
                                print("El usuario se dirige a la siguiente HABITACION")
                                costo += 1  # Incrementa el costo por moverse de locacion
                                # Muestra el costo actual
                                print("El costo actual es: " + str(costo))
                                # La puerta inteligente se abrirá
                                estadoObjetivo['HABITACION7'] = '0'
                                costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                                print("La puerta inteligente se encuentra abierta en la HABITACION 7")
                                # Muestra el costo actual
                                print("El costo actual es: " + str(costo))
                            else:
                                # La puerta inteligente se encuentra abierta
                                print("La puerta Inteligente de la HABITACION 7 se encuentra abierta")
                                print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                        elif (llave == 'no'):
                            print("No se encuentra dentro del rango establecido!")

                        else:
                            print("Opción Inválida!!!")

                    elif (estado == '0'):
                        # La puerta Inteligente de la HABITACION5 se encuentra abierta
                        print("La puerta Inteligente de la HABITACION5 se encuentra abierta")
                        print("No se ejecuta ninguna acción. El costo actual es: " + str(costo))

                        llave = input("La llave se encuentra dentro del rango (si o no): ")

                        if (llave == 'si'):

                            if(ubicacion2 == '1'):
                                # Si la puerta inteligente de la HABITACION1 se encuentra cerrado.
                                print("La puerta Inteligente de la HABITACION 1 se encuentra cerrado")
                                print("El usuario se dirige a la siguiente HABITACION")
                                costo += 1  # Incrementa el costo por moverse de locacion
                                # Muestra el costo actual
                                print("El costo actual es: " + str(costo))
                                # La puerta inteligente se abrirá
                                estadoObjetivo['HABITACION1'] = '0'
                                costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                                print("La puerta inteligente se encuentra abierta en la HABITACION 1")
                                # Muestra el costo actual
                                print("El costo actual es: " + str(costo))
                            else:
                                # La puerta inteligente se encuentra abierta
                                print("La puerta Inteligente de la HABITACION 1 se encuentra abierta")
                                print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))
                            
                        elif (llave == 'no'):
                            print("No se encuentra dentro del rango establecido!")

                        else:
                            print("Opción Inválida!!!")

                            
                        llave = input("La llave se encuentra dentro del rango (si o no): ")

                        if (llave == 'si'):
                            if(ubicacion3 == '1'):
                                # Si la puerta inteligente de la HABITACION2 se encuentra cerrado.
                                print("La puerta Inteligente de la HABITACION 2 se encuenta cerrada")
                                print("El usuario se dirige a la siguiente HABITACION")
                                costo += 1 #Incrementa el costo por moverse de locacion
                                print("El costo actual es: " +str(costo))#Muestra el costo actual
                                # La puerta inteligente se abrirá
                                estadoObjetivo['HABITACION2'] = '0'
                                costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                                print("La puerta inteligente se encuentra abierta en la HABITACION 2")
                                print("El costo actual es: " +str(costo)) #Muestra el costo actual
                            else:
                                # La puerta inteligente se encuentra abierta
                                print("La puerta Inteligente de la HABITACION 2 se encuentra abierta")
                                print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                        elif (llave == 'no'):
                            print("No se encuentra dentro del rango establecido!")

                        else:
                            print("Opción Inválida!!!")


                        llave = input("La llave se encuentra dentro del rango (si o no): ")

                        if (llave == 'si'):
                            if(ubicacion4 == '1'):
                                # Si la puerta inteligente de la HABITACION3 se encuentra cerrado.
                                print("La puerta Inteligente de la HABITACION 3 se encuenta cerrada")
                                print("El usuario se dirige a la siguiente HABITACION")
                                costo += 1 #Incrementa el costo por moverse de locacion
                                print("El costo actual es: " +str(costo))#Muestra el costo actual
                                # La puerta inteligente se abrirá
                                estadoObjetivo['HABITACION3'] = '0'
                                costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                                print("La puerta inteligente se encuentra abierta en la HABITACION 3")
                                print("El costo actual es: " +str(costo)) #Muestra el costo actual
                            else:
                                # La puerta inteligente se encuentra abierta
                                print("La puerta Inteligente de la HABITACION 3 se encuentra abierta")
                                print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                        elif (llave == 'no'):
                            print("No se encuentra dentro del rango establecido!")

                        else:
                            print("Opción Inválida!!!")


                        llave = input("La llave se encuentra dentro del rango (si o no): ")

                        if (llave == 'si'):
                            if(ubicacion5 == '1'):
                                # Si la puerta inteligente de la HABITACION4 se encuentra cerrado.
                                print("La puerta Inteligente de la HABITACION 4 se encuenta cerrada")
                                print("El usuario se dirige a la siguiente HABITACION")
                                costo += 1 #Incrementa el costo por moverse de locacion
                                print("El costo actual es: " +str(costo))#Muestra el costo actual
                                # La puerta inteligente se abrirá
                                estadoObjetivo['HABITACION4'] = '0'
                                costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                                print("La puerta inteligente se encuentra abierta en la HABITACION 4")
                                print("El costo actual es: " +str(costo)) #Muestra el costo actual
                            else:
                                # La puerta inteligente se encuentra abierta
                                print("La puerta Inteligente de la HABITACION 4 se encuentra abierta")
                                print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                        elif (llave == 'no'):
                            print("No se encuentra dentro del rango establecido!")

                        else:
                            print("Opción Inválida!!!")

                            
                        llave = input("La llave se encuentra dentro del rango (si o no): ")

                        if (llave == 'si'):
                            if(ubicacion6 == '1'):
                                # Si la puerta inteligente de la HABITACION6 se encuentra cerrado.
                                print("La puerta Inteligente de la HABITACION 6 se encuenta cerrada")
                                print("El usuario se dirige a la siguiente HABITACION")
                                costo += 1 #Incrementa el costo por moverse de locacion
                                print("El costo actual es: " +str(costo))#Muestra el costo actual
                                # La puerta inteligente se abrirá
                                estadoObjetivo['HABITACION6'] = '0'
                                costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                                print("La puerta inteligente se encuentra abierta en la HABITACION 6")
                                print("El costo actual es: " +str(costo)) #Muestra el costo actual
                            else:
                                # La puerta inteligente se encuentra abierta
                                print("La puerta Inteligente de la HABITACION 6 se encuentra abierta")
                                print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                        elif (llave == 'no'):
                            print("No se encuentra dentro del rango establecido!")

                        else:
                            print("Opción Inválida!!!")

                            
                        llave = input("La llave se encuentra dentro del rango (si o no): ")

                        if (llave == 'si'):
                            if(ubicacion7 == '1'):
                                # Si la puerta inteligente de la HABITACION7 se encuentra cerrado.
                                print("La puerta Inteligente de la HABITACION 7 se encuenta cerrada")
                                print("El usuario se dirige a la siguiente HABITACION")
                                costo += 1 #Incrementa el costo por moverse de locacion
                                print("El costo actual es: " +str(costo))#Muestra el costo actual
                                # La puerta inteligente se abrirá
                                estadoObjetivo['HABITACION7'] = '0'
                                costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                                print("La puerta inteligente se encuentra abierta en la HABITACION 7")
                                print("El costo actual es: " +str(costo)) #Muestra el costo actual
                            else:
                                # La puerta inteligente se encuentra abierta
                                print("La puerta Inteligente de la HABITACION 7 se encuentra abierta")
                                print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                        elif (llave == 'no'):
                            print("No se encuentra dentro del rango establecido!")

                        else:
                            print("Opción Inválida!!!")

            #HABITACION 6
            if (ubicacion == 'HABITACION6'):
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion2 = input("Inserte el estado de la HABITACION 1 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion3 = input("Inserte el estado de la HABITACION 2 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion4 = input("Inserte el estado de la HABITACION 3 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion5 = input("Inserte el estado de la HABITACION 4 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion6 = input("Inserte el estado de la HABITACION 5 ")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion7 = input("Inserte el estado de la HABITACION 7 ")

                # Se muestran los resultados deseados.
                print("Objetivo Deseado:" + str(estadoObjetivo))
                # Se muestra la habitación en la que se encuentra la puerta Inteligente
                print("La Puerta Inteligente se encuentra en la HABITACION 6")

                if(estado == '1'):
                    # La puerta Inteligente de la HABITACION6 se encuentra cerrada
                    print("La puerta Inteligente de la HABITACION6 se encuentra cerrada")
                    # La puerta Inteligente empezará abrirse
                    estadoObjetivo['HABITACION6'] = '0'
                    costo += 1  # El costo incrementará cada que la puerta Inteligente se abra
                    print("La puerta Inteligente esta abierta en la HABITACION 6")
                    # Muestra el costo actual.
                    print("El costo actual es: " + str(costo))
                    llave = input("La llave se encuentra dentro del rango (si o no): ")
                        

                    if (llave == 'si'):

                        if(ubicacion2 == '1'):
                            # Si la puerta inteligente de la HABITACION1 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 1 se encuentra cerrado")
                            print("El usuario se dirige a la siguiente HABITACION1")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION1'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 1")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 1 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion3 == '1'):
                            # Si la puerta inteligente de la HABITACION2 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 2 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION2'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 2")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 2 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion4 == '1'):
                            # Si la puerta inteligente de la HABITACION3 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 3 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION3'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 3")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 3 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion5 == '1'):
                            # Si la puerta inteligente de la HABITACION4 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 4 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION4'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 4")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 4 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion6 == '1'):
                            # Si la puerta inteligente de la HABITACION5 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 5 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION5'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 5")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 5 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion7 == '1'):
                            # Si la puerta inteligente de la HABITACION7 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 7 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION7'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 7")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 7 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                elif (estado == '0'):
                    # La puerta Inteligente se encuentra abierta
                    print("La puerta Inteligente de la HABITACION 6 se encuentra abierta")
                    print("No se ejecuta ninguna acción. El costo actual es: " + str(costo))

                
                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):

                    if(ubicacion2 == '1'):
                        # Si la puerta inteligente de la HABITACION1 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 1 se encuentra cerrado")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1  # Incrementa el costo por moverse de locacion
                        # Muestra el costo actual
                        print("El costo actual es: " + str(costo))
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION1'] = '0'
                        costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 1")
                        # Muestra el costo actual
                        print("El costo actual es: " + str(costo))
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 1 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))
                    
                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")

                    
                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):
                    if(ubicacion3 == '1'):
                        # Si la puerta inteligente de la HABITACION2 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 2 se encuenta cerrada")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1 #Incrementa el costo por moverse de locacion
                        print("El costo actual es: " +str(costo))#Muestra el costo actual
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION2'] = '0'
                        costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 2")
                        print("El costo actual es: " +str(costo)) #Muestra el costo actual
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 2 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")


                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):
                    if(ubicacion4 == '1'):
                        # Si la puerta inteligente de la HABITACION3 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 3 se encuenta cerrada")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1 #Incrementa el costo por moverse de locacion
                        print("El costo actual es: " +str(costo))#Muestra el costo actual
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION3'] = '0'
                        costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 3")
                        print("El costo actual es: " +str(costo)) #Muestra el costo actual
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 3 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")


                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):
                    if(ubicacion5 == '1'):
                        # Si la puerta inteligente de la HABITACION4 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 4 se encuenta cerrada")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1 #Incrementa el costo por moverse de locacion
                        print("El costo actual es: " +str(costo))#Muestra el costo actual
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION4'] = '0'
                        costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 4")
                        print("El costo actual es: " +str(costo)) #Muestra el costo actual
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 4 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")

                    
                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):
                    if(ubicacion6 == '1'):
                        # Si la puerta inteligente de la HABITACION5 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 5 se encuenta cerrada")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1 #Incrementa el costo por moverse de locacion
                        print("El costo actual es: " +str(costo))#Muestra el costo actual
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION5'] = '0'
                        costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 5")
                        print("El costo actual es: " +str(costo)) #Muestra el costo actual
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 5 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")

                    
                llave = input("La llave se encuentra dentro del rango (si o no): ")

                if (llave == 'si'):
                    if(ubicacion7 == '1'):
                        # Si la puerta inteligente de la HABITACION7 se encuentra cerrado.
                        print("La puerta Inteligente de la HABITACION 7 se encuenta cerrada")
                        print("El usuario se dirige a la siguiente HABITACION")
                        costo += 1 #Incrementa el costo por moverse de locacion
                        print("El costo actual es: " +str(costo))#Muestra el costo actual
                        # La puerta inteligente se abrirá
                        estadoObjetivo['HABITACION7'] = '0'
                        costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                        print("La puerta inteligente se encuentra abierta en la HABITACION 7")
                        print("El costo actual es: " +str(costo)) #Muestra el costo actual
                    else:
                        # La puerta inteligente se encuentra abierta
                        print("La puerta Inteligente de la HABITACION 7 se encuentra abierta")
                        print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                elif (llave == 'no'):
                    print("No se encuentra dentro del rango establecido!")

                else:
                    print("Opción Inválida!!!")


            #HABITACION7
            if (ubicacion == 'HABITACION7'):
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion2 = input("Inserte el estado de la HABITACION 1")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion3 = input("Inserte el estado de la HABITACION 2")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion4 = input("Inserte el estado de la HABITACION 3")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion5 = input("Inserte el estado de la HABITACION 4")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion6 = input("Inserte el estado de la HABITACION 5")
                # el usuario indica la si la puerta inteligente se encuentra abierto o cerrado (0/1) en la ubicación indicada.
                ubicacion7 = input("Inserte el estado de la HABITACION 6")

                # Se muestran los resultados deseados.
                print("Objetivo Deseado:" + str(estadoObjetivo))
                # Se muestra la habitación en la que se encuentra la puerta Inteligente
                print("La Puerta Inteligente se encuentra en la HABITACION 7")

                if(estado == '1'):
                    # La puerta Inteligente de la HABITACION7 se encuentra cerrada
                    print("La puerta Inteligente se encuentra cerrada")
                    # La puerta Inteligente empezará abrirse
                    estadoObjetivo['HABITACION7'] = '0'
                    costo += 1  # El costo incrementará cada que la puerta Inteligente se abra
                    print("La puerta Inteligente esta abierta en la HABITACION 7")
                    # Muestra el costo actual.
                    print("El costo actual es: " + str(costo))
                    llave = input("La llave se encuentra dentro del rango (si o no): ")
                    


                    if (llave == 'si'):

                        if(ubicacion2 == '1'):
                            # Si la puerta inteligente de la HABITACION1 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 1 se encuentra cerrado")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION1'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 1")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 1 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    
                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion3 == '1'):
                            # Si la puerta inteligente de la HABITACION2 se encuentra cerrado.
                            print(
                                "La puerta Inteligente de la HABITACION 2 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION2'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print(
                                "La puerta inteligente se encuentra abierta en la HABITACION 2")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print(
                                "La puerta Inteligente de la HABITACION 2 se encuentra abierta")
                            print(
                                "No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input(
                        "La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion4 == '1'):
                            # Si la puerta inteligente de la HABITACION3 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 3 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION3'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 3")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 3 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion5 == '1'):
                            # Si la puerta inteligente de la HABITACION4 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 4 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION4'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 4")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 4 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion6 == '1'):
                            # Si la puerta inteligente de la HABITACION5 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 5 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION5'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 5")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 5 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion7 == '1'):
                            # Si la puerta inteligente de la HABITACION6 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 6 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION6'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 6")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 6 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " + str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                elif (estado == '0'):
                    # La puerta Inteligente se encuentra abierta
                    print("La puerta Inteligente de la HABITACION7 se encuentra abierta")
                    print("No se ejecuta ninguna acción. El costo actual es: " + str(costo))

                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):

                        if(ubicacion2 == '1'):
                            # Si la puerta inteligente de la HABITACION1 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 1 se encuentra cerrado")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1  # Incrementa el costo por moverse de locacion
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION1'] = '0'
                            costo += 1  # El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 1")
                            # Muestra el costo actual
                            print("El costo actual es: " + str(costo))
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 1 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))
                        
                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                        
                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion3 == '1'):
                            # Si la puerta inteligente de la HABITACION2 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 2 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1 #Incrementa el costo por moverse de locacion
                            print("El costo actual es: " +str(costo))#Muestra el costo actual
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION2'] = '0'
                            costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 2")
                            print("El costo actual es: " +str(costo)) #Muestra el costo actual
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 2 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")


                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion4 == '1'):
                            # Si la puerta inteligente de la HABITACION3 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 3 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1 #Incrementa el costo por moverse de locacion
                            print("El costo actual es: " +str(costo))#Muestra el costo actual
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION3'] = '0'
                            costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 3")
                            print("El costo actual es: " +str(costo)) #Muestra el costo actual
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 3 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")


                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion5 == '1'):
                            # Si la puerta inteligente de la HABITACION4 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 4 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1 #Incrementa el costo por moverse de locacion
                            print("El costo actual es: " +str(costo))#Muestra el costo actual
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION4'] = '0'
                            costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 4")
                            print("El costo actual es: " +str(costo)) #Muestra el costo actual
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 4 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                        
                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion6 == '1'):
                            # Si la puerta inteligente de la HABITACION5 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 5 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1 #Incrementa el costo por moverse de locacion
                            print("El costo actual es: " +str(costo))#Muestra el costo actual
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION5'] = '0'
                            costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 5")
                            print("El costo actual es: " +str(costo)) #Muestra el costo actual
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 5 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")

                        
                    llave = input("La llave se encuentra dentro del rango (si o no): ")

                    if (llave == 'si'):
                        if(ubicacion7 == '1'):
                            # Si la puerta inteligente de la HABITACION6 se encuentra cerrado.
                            print("La puerta Inteligente de la HABITACION 6 se encuenta cerrada")
                            print("El usuario se dirige a la siguiente HABITACION")
                            costo += 1 #Incrementa el costo por moverse de locacion
                            print("El costo actual es: " +str(costo))#Muestra el costo actual
                            # La puerta inteligente se abrirá
                            estadoObjetivo['HABITACION6'] = '0'
                            costo += 1 #El costo incrementará cada que la puerta inteligente se abra
                            print("La puerta inteligente se encuentra abierta en la HABITACION 6")
                            print("El costo actual es: " +str(costo)) #Muestra el costo actual
                        else:
                            # La puerta inteligente se encuentra abierta
                            print("La puerta Inteligente de la HABITACION 6 se encuentra abierta")
                            print("No se lleva a cabo ninguna acción. El costo actual es: " +str(costo))

                    elif (llave == 'no'):
                        print("No se encuentra dentro del rango establecido!")

                    else:
                        print("Opción Inválida!!!")
        # abierto
        print("Estado Objetivo: " + str(estadoObjetivo))
        print("Medición del desempeño " +str(costo))
        
    
    except Exception as e:  
        print(e)    

puerta_Inteligente()
   


