import pygame
from elementos.Objeto import Objeto
from pygame import Vector2

class Jugador(Objeto):
    """ Objeto que representa a un jugador del videojuego PONG"""

    def __init__(self, ventana:pygame.surface, posicion:Vector2, velocidad:Vector2, ancho:int, teclaArriba:int, teclaAbajo:int, color:tuple):
        """ Constructor de la raqueta del jugador """

        Objeto.__init__(self, ventana, posicion, velocidad, color)
        
        self.__posFinal =  Vector2([self.getPosicion()[0], self.getPosicion()[1] + 200])

        self.__ancho = ancho

        # Asignamos la velocidad - Sube, + Baja

        self.__teclaAbajo = teclaAbajo
        self.__teclaArriba = teclaArriba



    #-----------------------------MÉTODOS GET-----------------------
    def getTeclaAbajo(self):
        return self.__teclaAbajo
    def getTeclaArriba(self):
        return self.__teclaArriba


    def mover(self):
        """ Se encarga de detectar si una tecla fue presionada, y mueve el jugador """
        
        # La velocidad será 0, a menos que una tecla esté oprimida

        # Verificamos que la raqueta no se salga del mapa
        if self.getPosicion().y <= 5 and self.getVelocidad().y < 0:
            return
        elif self.__posFinal.y >= self.getVentana().get_height() - 5 and self.getVelocidad().y > 0:
            return

        self.getPosicion().y = self.getPosicion().y + self.getVelocidad().y

        # Movemos el objeto
        self.__posFinal.y += self.getVelocidad().y


    def imprimir(self):
        """" Imprime la raqueta del jugador"""
        # En caso de que exista movimiento, lo movemos
        
        self.mover()

        pygame.draw.line(self.getVentana(), self.getColor(), self.getPosicion(), self.__posFinal, self.__ancho)