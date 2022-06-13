class puertaInteligente:
    """
    Esta clase representa a una puerta inteligente la cual tiene un estado, una ubicacion, una llave y un costo, a traves de los cuales se puede abrir o cerrar la puerta.
    
    Métodos
    ----------
    definirHabitacion(self,ubicacion, estado, costo, llave, estadoObjetivo)
        Este método define la ubicacion, el estado, el costo y la llave de la puerta inteligente, estos parametros serviran para realizar el análisis correspondiente para saber si se debe abrir o no la puerta.
    """
    
    def definirHabitacion(self,ubicacion, estado, costo, llave, estadoObjetivo):
        """_summary_

        Parametros
        -----------
            ubicacion (str): Indica la ubicacion de la puerta inteligente.
            estado (str): Indica el estado de la puerta inteligente.
            costo (int): Indica el costo de las acciones realizadas por la puerta inteligente.
            llave (str): Describe si la llave se encuentra dentro del rango de accion de la puerta inteligente.
            estadoObjetivo (diccionario): Proporciona el estado objetivo de las habitaciones evaluadas.

        Returns:
            costo: Retorna el costo total de las acciones realizadas por la puerta inteligente.
        """
        # Se inicia el control de excepciones
        try:
            # Se asigna el ubicación de la puerta inteligente.
            self.ubicacion = ubicacion
            # Se asigna el estado de la puerta inteligente.
            self.estado = estado
            # Se asigna el costo actual de las acciones realizadas por puerta inteligente.
            self.costo = costo
            # Se asigna el estado de la llave de la puerta inteligente.
            self.llave = llave
            
            # Si la llave esta dentro del rango de accion de la puerta inteligente.
            if llave == 'si' or llave == 'SI':
                # Imprime la ubicación de la puerta inteligente
                print("La Puerta Inteligente se encuentra en la ", ubicacion)
                # Si el estado de la puerta inteligente es cerrada.
                if(estado == '1'):
                    # Imprime el estado de la puerta inteligente.
                    print("La puerta de la ", ubicacion, " esta cerrada")
                    # Se asigna el nuevo estado a la puerta de la ubicación correspondiente.
                    estadoObjetivo[ubicacion] = '0'
                    # Se incrementa el costo en 1
                    costo += 1
                    # Se imprime el nuevo costo de la puerta inteligente.
                    print("El costo de abrir la puerta es de ", costo)
                    # Se imprime el nuevo estado de la puerta inteligente.
                    print("La puerta se encuentra abierta")
                    # Se retorna el costo actual de las acciones realizadas por la puerta inteligente.
                    return costo
                
                # Si el estado de la puerta inteligente es abierta.
                else:
                    # Imprime el estado de la puerta inteligente.
                    print("La puerta de la ", ubicacion, " esta abierta")
                    # Se muestra un mensaje informactivo de las acciones realizadas por la puerta inteligente.
                    print("No se realizo ninguna acción")
                    #Se imprime el costo actual de la puerta inteligente.
                    print("El costo de abrir la puerta es de ", costo)
                    # Se retorna el costo actual de las acciones realizadas por la puerta inteligente.
                    return costo
                
            # Si la llave no esta dentro del rango de accion de la puerta inteligente.
            else:
                # Imprime un mensaje indicando que la llave no esta dentro del rango de accion de la puerta inteligente.
                print("La llave no se encuentra dentro del rango de accion de la puerta inteligente")
                # Se retorna el costo actual de las acciones realizadas por la puerta inteligente.
                return costo
            
        # Se captura la excepcion.
        except Exception as e:  
            # Se imprime el mensaje de la excepcion.
            print(e)    

# Ejecucion del programa.
if __name__ == '__main__':
    # Se inicia el control de excepciones 
    try:
        # Se crea el diccionario de la ubicacion de la puerta inteligente.
        estadoObjetivo = {'HABITACION1': '0', 'HABITACION2': '0', 'HABITACION3': '0','HABITACION4': '0', 'HABITACION5': '0', 'HABITACION6': '0', 'HABITACION7': '0'}
        
        # Se crea una instancia de la clase puertaInteligente.
        puerta = puertaInteligente()

        # Se define un bucle para el ingreso de una ubicación valida.
        while True:
            # Se inicializa el costo
            costo = 0
            # Se imprime el menu de opciones.
            print("\n**************Bienvenido al sistema de control de puertas inteligentes************** \nUbicaciones disponibles: \n HABITACION1, HABITACION2, HABITACION3, HABITACION4, HABITACION5, HABITACION6, HABITACION7, \n Introduzca la palabra 'SALIR' para salir del sistema")
            # Se pide la ubicacion de la puerta inteligente.
            ubicacion = input("Por favor ingrese la ubicacion de la puerta que desea abrir, Porfavor Ingrese la ubicacion en Mayusculas\n")
            # Si la ubicacion ingresada se encuentra fuera del rango de las ubicaciones disponibles.
            if ubicacion != 'HABITACION1' and ubicacion != 'HABITACION2' and ubicacion != 'HABITACION3' and ubicacion != 'HABITACION4' and ubicacion != 'HABITACION5' and ubicacion != 'HABITACION6' and ubicacion != 'HABITACION7' and ubicacion != 'SALIR':
                print("La ubicación no es correcta, Por favor intente de nuevo\n")
                
            # Si la ubicacion ingresada es igual a la palabra 'SALIR'.
            elif ubicacion == 'SALIR':
                # Se imprime un mensaje de despedida.
                print("Gracias por usar el sistema")
                # Se termina el bucle para el ingreso de una ubicación valida.
                break
