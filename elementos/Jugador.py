import pygame

class Jugador(object):

    def __init__(self, ventana, posInicio, ancho, teclaArriba, teclaAbajo, color):
        """ Constructor de la raqueta del jugador """

        self.__ventana = ventana

        self.__altoVentana = self.__ventana.get_height()

        self.__posInicio = posInicio
        self.__posFinal = [posInicio[0], posInicio[1] + 200]

        self.__ancho = ancho

        # Asignamos la velocidad - Sube, + Baja
        self.__velocidad = 0

        self.__teclaAbajo = teclaAbajo
        self.__teclaArriba = teclaArriba

        self.__color = color


    #-----------------------------MÉTODOS GET-----------------------
    def getTeclaAbajo(self):
        return self.__teclaAbajo
    def getTeclaArriba(self):
        return self.__teclaArriba

    #------------------------------MÉTODOS SET-----------------------
    def setVelocidad(self, velocidad):
        self.__velocidad = velocidad

    def mover(self):
        """ Se encarga de detectar si una tecla fue presionada, y mueve el jugador """
        
        # La velocidad será 0, a menos que una tecla esté oprimida

        # Verificamos que la raqueta no se salga del mapa
        if self.__posInicio[1] <= 5 and self.__velocidad < 0:
            return
        elif self.__posFinal[1] >= self.__altoVentana - 5 and self.__velocidad > 0:
            return

        # Movemos el objeto
        self.__posInicio[1] += self.__velocidad
        self.__posFinal[1] += self.__velocidad


    def imprimir(self):
        """" Imprime la raqueta del jugador"""
        # En caso de que exista movimiento, lo movemos
        self.mover()

        pygame.draw.line(self.__ventana, self.__color, self.__posInicio, self.__posFinal, self.__ancho)