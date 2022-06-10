from SistemaMetro import Grafo
import unittest


class TestGrafo(unittest.TestCase):


    def test_grafo(self):

        """
        Este método testea el grafo.
        """

        #Se crea el diccionario con las estaciones del tren

        estaciones = {0: "Valdecarro",1: "Cuatro caminos",2:"Alto Moncloa",3:"Pinar de Chamartin",4:"Casa de campo",5:"Circular",6:"Hospital Henares Pitis",7:"Aeropuerto", 8:"Paco de Lucía", 9:"Hospital infante Sofia", 10:"Plaza Eliptica la fortuna", 11:"Metro sur", 12:"Opera", 13:"Las tablas", 14:"Aravaca", 15:"Puerta de Boadilla", 16:"San Ferrin-Oicasur", 17:"Estación de arte", 18:"Valdezarza", 19:"Lucero "}

        g = Grafo(20, estaciones)# Se instancia la clase Grafo

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

        g.imprimir_grafo()

        #Esta funciono
        #self.assertEqual(g.dfs(2, 7), ['Alto Moncloa', 'Circular', 'Cuatro caminos', 'Hospital Henares Pitis', 'Hospital infante Sofia', 'Casa de campo', 'Paco de Lucía', 'Pinar de Chamartin', 'Aeropuerto'])
        
        
        #self.assertEqual(g.dfs(0, 5), ['Valdecarro', 'Alto Moncloa', 'Circular'])
        
        self.assertEqual(g.dfs(5, 10), ['Circular', 'Plaza Eliptica la fortuna'])

if __name__ == '__main__':
    unittest.main(argv=['ignored', '-v'], exit=False)