import pygame
from sys import exit
from elementos.Jugador import Jugador

class Multijugador(object):

    def __init__(self):
        """ Constructor del juego en multijugador """

        pygame.init()

        tamano = (800, 600)

        # Declaramos los colores RGB
        self.__colorBlanco = (255, 255, 255)
        self.__colorNegro = (0, 0, 0)

        self.__ventana = pygame.display.set_mode(tamano)

        self.__jugador1 = Jugador(self.__ventana, [50, 100], 10, pygame.K_w, pygame.K_s, self.__colorBlanco)

        self.__reloj = pygame.time.Clock()
        self.__mainLoop()


    def __mainLoop(self):
        """" Método que se encarga de recargar en cada momento la pantalla del juego """

        while(True):    
            
            #Controlamos y vemos los eventos
            self.__controladorDeEventos()
            
            self.__ventana.fill(self.__colorNegro)

            # Pintamos elementos
            self.__jugador1.imprimir()

            #Actualizamos ventana 
            pygame.display.flip()

            self.__reloj.tick(60)


    def __controladorDeEventos(self):
        """ Se encarga de administrar todos los eventos del juego """

        
        for evento in pygame.event.get():
            #Si la ventana se cierra, terminamos el programa
            if(evento.type == pygame.QUIT):
                exit()
            
            #----EVENTOS DEL JUGADOR 1------------
            if evento.type == pygame.KEYUP:
                if evento.key == self.__jugador1.getTeclaArriba() or evento.key == self.__jugador1.getTeclaAbajo():
                    self.__jugador1.setVelocidad(0)
        
            if evento.type == pygame.KEYDOWN:
                if evento.key == self.__jugador1.getTeclaArriba():
                    self.__jugador1.setVelocidad(-5)
            
                if evento.key == self.__jugador1.getTeclaAbajo():
                    self.__jugador1.setVelocidad(5)

            #-----EVENTOS DEL JUGADOR 2------------

