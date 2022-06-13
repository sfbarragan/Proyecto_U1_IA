# Se importa la libreria unittest
import unittest

# Se importa la clase puertaInteligente de Agente_PuertaInteligente.py
from Agente_PuertaInteligente import puertaInteligente

class TestPuertaInteligente(unittest.TestCase):
    """
    Esta clase ejecuta las pruebas automáticas.
    
    Métodos:
        test_puerta(): Este método testea la puerta inteligente.
    """

    def test_puerta_valoresCorrectos(self):
        """
        Este método testea la puerta inteligente con valores correctos.
        """

        # Se crea el diccionario de la ubicacion de la puerta inteligente.
        estadoObjetivo = {'HABITACION1': '0', 'HABITACION2': '0', 'HABITACION3': '0','HABITACION4': '0', 'HABITACION5': '0', 'HABITACION6': '0', 'HABITACION7': '0'}
        
        # Se crea una instancia de la clase puertaInteligente.
        puerta = puertaInteligente() 

        # Se agrega el estado la ubicación, estado, costo, estado de la llave y ubicaciones de la puerta inteligente.
        self.assertEqual(puerta.definirHabitacion('HABITACION1', '1', 0, 'SI', estadoObjetivo), 1)
        # Se agrega el estado la ubicación, estado, costo, estado de la llave y ubicaciones de la puerta inteligente.
        self.assertEqual(puerta.definirHabitacion('HABITACION3', '0', 0, 'SI', estadoObjetivo), 0)
        # Se agrega el estado la ubicación, estado, costo, estado de la llave y ubicaciones de la puerta inteligente.
        self.assertEqual(puerta.definirHabitacion('HABITACION7', '1', 0, 'NO', estadoObjetivo), 0)
        
    def test_puerta_valoresErroneos(self):
        """
        Este método testea la puerta inteligente con valores erroneos.
        """

        # Se crea el diccionario de la ubicacion de la puerta inteligente.
        estadoObjetivo = {'HABITACION1': '0', 'HABITACION2': '0', 'HABITACION3': '0','HABITACION4': '0', 'HABITACION5': '0', 'HABITACION6': '0', 'HABITACION7': '0'}
        
        # Se crea una instancia de la clase puertaInteligente.
        puerta = puertaInteligente() 

        # Se agrega el estado la ubicación, estado, costo, estado de la llave y ubicaciones de la puerta inteligente.
        self.assertFalse(puerta.definirHabitacion('HABITACION1', '1', 0, 'A', estadoObjetivo), 1)
        # Se agrega el estado la ubicación, estado, costo, estado de la llave y ubicaciones de la puerta inteligente.
        self.assertFalse(puerta.definirHabitacion('HABITACION3', '6', 0, 'SI', estadoObjetivo), 0)
        # Se agrega el estado la ubicación, estado, costo, estado de la llave y ubicaciones de la puerta inteligente.
        self.assertFalse(puerta.definirHabitacion('HABITACION7', '1', 0, 'NO', estadoObjetivo), 6)
        
        

# Ejecucion de las pruebas. 
if __name__ == '__main__':
    #Se ejecuta el test
    unittest.main(argv=['ignored', '-v'], exit=False)