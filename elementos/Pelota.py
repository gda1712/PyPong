import pygame
from elementos.Objeto import Objeto
from pygame import Vector2

class Pelota(Objeto):
    """ Objeto que representa a la pelota del juego en el PONG """


    def __init__(self, ventana:pygame.surface, posicion:Vector2, velocidad:Vector2, radio:int, color:tuple):
        # Asignamos como valo inicial el centro de la cancha
        Objeto.__init__(self, ventana, posicion, velocidad, color)
        #[ventana.width / 2, ventana.height / 2]
        # radio de la pelota
        self.__radio = radio


    def mover(self):
        """ Se encarga de mover la pelota """

        # Verificamos que la pelota no se salga del mapa
        if self.getPosicion().y <= 10 and self.getVelocidad().y != 0:
            self.getVelocidad().y *= -1
        elif self.getPosicion().y >= self.getVentana().get_height() - 10 and self.getVelocidad().y != 0:
            self.getVelocidad().y *= -1

        # Movemos la pelota
        for i in range(2):
            self.getPosicion()[i] = self.getPosicion()[i] + self.getVelocidad()[i]
    

    def imprimir(self):
        self.mover()

        pygame.draw.circle(self.getVentana(), self.getColor(), self.getPosicion(), self.__radio)

        