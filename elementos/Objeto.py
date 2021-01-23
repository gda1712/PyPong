import pygame
from abc import ABC, abstractmethod
from pygame import Vector2

class Objeto(object):

    def __init__(self, ventana:pygame.surface, posicion:Vector2, velocidad:Vector2, color:tuple):
        self.__ventana = ventana
        self.__posicion = posicion
        self.__velocidad = velocidad
        self.__color = color

    #------------------------------MÉTODOS SET-----------------------
    def setVelocidad(self, velocidad:Vector2):
        self.__velocidad = velocidad

    def setPosicion(self, posicion:Vector2):
        self.__posicion = posicion

    #-------------------------------MÉTODOS GET-----------------------
    def getVelocidad(self):
        return self.__velocidad

    def getPosicion(self):
        return self.__posicion
    
    def getVentana(self):
        return self.__ventana

    def getColor(self):
        return self.__color


    @abstractmethod
    def mover(self):
        pass
    
    @abstractmethod
    def imprimir(self):
        pass