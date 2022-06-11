import unittest

from SistemaMetro import Grafo


class TestGrafo(unittest.TestCase):

    def test_grafo(self):
        """
        Este método testea el grafo.
        """

        # Se crea el diccionario con las estaciones del tren

        estaciones = {0: "Valdecarro", 1: "Cuatro caminos", 2: "Alto Moncloa", 3: "Pinar de Chamartin", 4: "Casa de campo", 5: "Circular", 6: "Hospital Henares Pitis", 7: "Aeropuerto", 8: "Paco de Lucía", 9: "Hospital infante Sofia", 10: "Plaza Eliptica la fortuna", 11: "Metro sur", 12: "Opera", 13: "Las tablas", 14: "Aravaca", 15: "Puerta de Boadilla", 16: "San Ferrin-Oicasur", 17: "Estación de arte", 18: "Valdezarza", 19: "Lucero "}
        # Se instancia la clase Grafo
        g = Grafo(20, estaciones)  

        # Se agrega los bordes del grafo con valor peso correspondiente
        g.llenar_grafo(g)
        g.imprimir_grafo()

        # Se agrega las estaciones sobre las cuales se realizará el recorrido del metro a ser evaluado
        self.assertEqual(g.dfs(2, 7, ruta = [], visitado = set()), ['Alto Moncloa', 'Circular', 'Cuatro caminos', 'Hospital Henares Pitis', 'Hospital infante Sofia', 'Casa de campo', 'Paco de Lucía', 'Pinar de Chamartin', 'Aeropuerto'])
        # Se agrega las estaciones sobre las cuales se realizará el recorrido del metro a ser evaluado
        self.assertEqual(g.dfs(0, 5, ruta = [], visitado = set()), ['Valdecarro', 'Alto Moncloa', 'Circular'])
        # Se agrega las estaciones sobre las cuales se realizará el recorrido del metro a ser evaluado
        self.assertEqual(g.dfs(5, 10, ruta = [], visitado = set()), ['Circular', 'Plaza Eliptica la fortuna'])


if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)
    