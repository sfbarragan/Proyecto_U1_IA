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
