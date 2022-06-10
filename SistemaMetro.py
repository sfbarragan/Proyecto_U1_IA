from queue import Queue

from sklearn import tree
from sqlalchemy import true


class Grafo:
    """
    Clase Grafo, esta clase representara a un grafo junto a sus atributos y funcionalidades,

     Atributos
    ----------
        m_numero_nodos : int
            Cantidad de nodos que tendra el grafo.
        m_nodos : int
            Rango de nodos sobre los que trabajara el grafo.
        m_dirigido : boolean
            Tipo de nodo dirigido o no dirigido.
        m_lista_adyacencia : diccionario
            Diccionario que almacena el valor de los nodos


     Métodos
    ----------

    __init__(self, num_de_nodos, estaciones, dirigido=True)
        Este metodo funcionara como el constuctor de la clase `Grafo()`, recibe el Numero de nodos (m_num_nodos),
        crea el rango de nodos (numero_nodos), determina el tipo de grafo si es dirigido o no dirigido (m_dirigido) y
        creara el diccionario de la lista de adyacencia.

    agregar_borde(self, nodo1, nodo2, peso=1)
        Genera los bordes de la lista de adyacencia agregando el nodo 2 a la lista de adyacencia del nodo 1.

    Imprimir_lista_adyacencia(self)
        Imprime el grafo generado en base a la lista de adyacencia.

    dfs(self, inicio, objetivo, ruta = [], visitado = set())
        Método que imprime el recorrido BFS de un vértice fuente dado.
    """

    def __init__(self, numero_nodos, estaciones, dirigido=True):
        """
        Este metodo funcionara como el constuctor de la clase Grafo(), recibe el Numero de nodos (m_num_nodos),
        crea el rango de nodos (numero_nodos), determina el tipo de grafo si es dirigido o no dirigido (m_dirigido) y
        creara el diccionario de la lista de adyacencia.


        Parametros
        ----------
        m_numero_nodos : int
            Cantidad de nodos que tendra el grafo.
        m_nodos : int
            Rango de nodos sobre los que trabajara el grafo.
        m_dirigido : boolean
            Tipo de nodo dirigido o no dirigido.
        m_lista_adyacencia : {}
            Diccionario que almacena el valor de los nodos
        m_estaciones : {}
            Diccionario que almacena de las estaciones
        """
        try:
             # Se asigna el valor del numero de nodos a través del parametro recibido
            self.m_numero_nodos = numero_nodos
            # Se genera el rango de nodos en base a m_numero_nodos
            self.m_nodos = range(self.m_numero_nodos)
            # se define el tipo de grafo
            self.m_dirigido = dirigido
            # se crea el diccionario con los nodos
            self.m_estaciones = estaciones
            
            # Se crea el diccionario de la lista de adyacencia
            self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}
        except Exception as e:  
            print(e)
    

    def crear_grafo(self, nodo1, nodo2, peso=1):
        """
        Este método define el borde de la lista de adyacencia.
        Recibe como parametros el nodo1, el nodo2 y el peso cuyo valor por defecto es de 1.
        Posteriormente se agregan a la lista de adyacencia del nodo al que corresponde.

        Parametros
        ----------
        nodo1 : int
        nodo2 : int
        peso: int

        Retorno
        -------
        Nada 
        """

        try:
            # Agrega el nodo 2 a la lista de adyacencia del nodo 1.
            self.m_lista_adyacencia[nodo1].add((nodo2, peso))
            if not self.m_dirigido:
                # Agrega el nodo 1 a la lista de adyacencia del nodo 2.
                self.m_lista_adyacencia[nodo2].add((nodo1, peso))
        except Exception as e:
            print(e)


    def imprimir_grafo(self):
        """
        Este método imprime el grafo generado a través de la lista de adyacencia.

        Parametros
        ----------
        Nada

        Retorno
        -------
        Nada 
        """

        try:
            # recorre la lista de adyacencia
            for llave in self.m_lista_adyacencia.keys():
                # imprime el cada nodo almacenado en la lista de adyacencia.
                print("nodo", llave, ": ", self.m_lista_adyacencia[llave])

        except Exception as e:
            print(e)


    def dfs(self, inicio, objetivo, ruta = [], visitado = set()):
        """
        Este método imprime el recorrido dfs generado a través de un nodo inicial y un nodo objetivo.
        Genera una lista de los nodos visitados y muestra el recorrido realizado hasta llegar al objetivo. 

        Parametros
        ----------
        ruta : lista
        visitado : diccionario

        Retorno
        -------
        ruta / resultado / None 
        """
        try:
            # Se agrega el nodo inicial a la lista de visitados
            visitado.add(inicio)
            # Se agrega el nodo inicial a la lista de ruta
            ruta.append(self.m_estaciones[inicio])
        except Exception as e:
            print(e)
        
        try:
            # Si el nodo inicial es el objetivo se imprime el recorrido
            if inicio == objetivo:
                return ruta

            # Se recorre la lista de adyacencia del nodo inicial
            for(vecino, peso) in self.m_lista_adyacencia[inicio]:
                # Si el nodo vecino no ha sido visitado se llama al metodo dfs con el nodo vecino como inicio
                if vecino not in visitado:
                    #se asigna a la variable resultado el nodo vecino, el objetivo, la ruta y la lista de nodos visitados
                    resultado = self.dfs(vecino, objetivo, ruta, visitado) 
                    # Si el resultado no es nulo se retorna el resultado
                    if resultado is not None:
                        #Retorna resultado
                        return resultado 
        except Exception as e:
            print(e)

        try:
            # Si el resultado es nulo se retorna None        
            ruta.pop() 
            return None
        except Exception as e:
            print(e)



if __name__ == "__main__":
    """
    Dentro de la clase main se instancia a la clase Grafo para acceder a sus metodos.
    """

    try:
        #Se crea el diccionario con las estaciones del tren
        estaciones = {0:"Valdecarro",1:"Cuatro caminos",2:"Alto Moncloa",3:"Pinar de Chamartin",4:"Casa de campo",5:"Circular",6:"Hospital Henares Pitis",7:"Aeropuerto", 8:"Paco de Lucía", 9:"Hospital infante Sofia", 10:"Plaza Eliptica la fortuna", 11:"Metro sur", 12:"Opera", 13:"Las tablas", 14:"Aravaca", 15:"Puerta de Boadilla", 16:"San Ferrin-Oicasur", 17:"Estación de arte", 18:"Valdezarza", 19:"Lucero "}
        
        g = Grafo(20, estaciones)#Se instancia la clase Grafo

        # Se agrega los bordes del grafo con valor peso correspondiente
        g.crear_grafo(0, 1, 10)
        g.crear_grafo(0, 2, 10) 
        g.crear_grafo(0, 3, 25) 

        g.crear_grafo(1, 3, 3)
        g.crear_grafo(1, 2, 7)
        g.crear_grafo(1, 6, 1)
        g.crear_grafo(1, 8, 15)
        g.crear_grafo(1, 4, 18)
        g.crear_grafo(1, 5, 16)

        g.crear_grafo(2, 3, 0.5)
        g.crear_grafo(2, 1, 6)
        g.crear_grafo(2, 9, 4)
        g.crear_grafo(2, 0, 6)
        g.crear_grafo(2, 4, 7)
        g.crear_grafo(2, 5, 8)

        g.crear_grafo(3, 1, 1)
        g.crear_grafo(3, 0, 2.5) 
        g.crear_grafo(3, 9, 3) 
        g.crear_grafo(3, 6, 15) 
        g.crear_grafo(3, 7, 19) 
        
        g.crear_grafo(4, 5, 5)
        g.crear_grafo(4, 2, 8) 
        g.crear_grafo(4, 9, 16)
        g.crear_grafo(4, 8, 17) 
        g.crear_grafo(4, 3, 18) 
        g.crear_grafo(4, 1, 19) 
        g.crear_grafo(4, 6, 20) 
        
        g.crear_grafo(5, 3, 0.5)
        g.crear_grafo(5, 2, 0.9) 
        g.crear_grafo(5, 1, 5) 
        g.crear_grafo(5, 7, 6) 
        g.crear_grafo(5, 6, 7) 
        g.crear_grafo(5, 8, 7) 
        g.crear_grafo(5, 4, 8) 
        g.crear_grafo(5, 0, 15) 
        g.crear_grafo(5, 10, 17) 
        g.crear_grafo(5, 9, 30) 

        g.crear_grafo(6, 5, 10)
        g.crear_grafo(6, 1, 11) 
        g.crear_grafo(6, 9, 12) 
        g.crear_grafo(6, 8, 13) 
        g.crear_grafo(6, 3, 13) 
        g.crear_grafo(6, 4, 18)

        g.crear_grafo(7, 3, 9)
        g.crear_grafo(7, 8, 15)
        g.crear_grafo(7, 5, 19)

        g.crear_grafo(8, 0, 6)
        g.crear_grafo(8, 7, 7)
        g.crear_grafo(8, 6, 14)
        g.crear_grafo(8, 3, 14)
        g.crear_grafo(8, 4, 15)
        g.crear_grafo(8, 1, 16)
        g.crear_grafo(8, 5, 17.5)

        g.crear_grafo(9, 14, 10)
        g.crear_grafo(9, 4, 11)
        g.crear_grafo(9, 5, 13)
        g.crear_grafo(9, 2, 13.5)
        g.crear_grafo(9, 0, 15)
        g.crear_grafo(9, 4, 16)
        g.crear_grafo(9, 6, 17)
        g.crear_grafo(9, 7, 18)
        g.crear_grafo(9, 13, 25)

        g.crear_grafo(10, 5, 10)

        g.crear_grafo(11, 9, 7)

        g.crear_grafo(12, 9, 1)
        g.crear_grafo(12, 4, 4)

        g.crear_grafo(13, 9, 1)
        g.crear_grafo(13, 0, 10)

        g.crear_grafo(14, 2, 10)

        g.crear_grafo(15, 1, 15)

        g.crear_grafo(16, 2, 1)
        
        g.crear_grafo(17, 0, 1)

        g.crear_grafo(18, 6, 5)

        g.crear_grafo(19, 5, 2)


        while(True):
            op = int(input("1. Mostrar Estaciones \n 2. Mostrar Grafo \n 3. Buscar Ruta \n 4. Salir"))

            if op == 1:
                print(estaciones)

            elif(op == 2):
                g.imprimir_grafo() #Imprime la lista de adyacencia
        
            elif(op == 3):
                ruta_transversal = [] # Se inicializa la variable ruta_transversal

                while true:
                    #Se pide al usuario la estación inicial
                    estacion_inicial = int(input("Ingrese la estación inicial")) 
                    #Se pide al usuario que ingrese la estación objetivo
                    estacion_objetivo = int(input("Ingrese la estación objetivo"))    
                    if(estacion_inicial >= 0 and estacion_inicial <= 19 and estacion_objetivo >= 0 and estacion_objetivo <= 19):
                        ruta_transversal = g.dfs(estacion_inicial, estacion_objetivo) # Se almacena el recorrido dfs en la variable ruta_transversal
                        print(f"La ruta para llegar al destino es:  {ruta_transversal}") #Imprime el recorriodo dfs
                        break
                    else:
                        print("Se ingreso una estación no válida")
        

            elif op == 4:
                break

            else:
                print("Opción invalida, intente de nuevo")
            
    except Exception as e:
        print(e)