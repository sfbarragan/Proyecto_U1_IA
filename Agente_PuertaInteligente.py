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

