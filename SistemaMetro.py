from queue import Queue


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

    __init__(self, num_de_nodos, dirigido=True)
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

    def __init__(self, numero_nodos, dirigido=True):
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
        m_lista_adyacencia : diccionario
            Diccionario que almacena el valor de los nodos
        """
        try:
             # Se asigna el valor del numero de nodos a través del parametro recibido
            self.m_numero_nodos = numero_nodos
            # Se genera el rango de nodos en base a m_numero_nodos
            self.m_nodos = range(self.m_numero_nodos)
            # se define el tipo de grafo
            self.m_dirigido = dirigido
            
            # Se crea el diccionario de la lista de adyacencia
            self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}
        except Exception as e:  
            print(e)
