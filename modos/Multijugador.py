import pygame
from sys import exit
from pygame import Vector2
from elementos.Jugador import Jugador
from elementos.Pelota import Pelota

class Multijugador(object): 
    """ MODO MULTIJUGADOR DE PYPONG """
    def __init__(self):
        """ Constructor del juego en multijugador """

        pygame.init()

        tamano = (800, 600)

        # Declaramos los colores RGB
        self.__colorBlanco = (255, 255, 255)
        self.__colorNegro = (0, 0, 0)

        self.__ventana = pygame.display.set_mode(tamano)



        jugador1 = Jugador(self.__ventana, Vector2(50, 100), Vector2(0, 0), 10, pygame.K_w, pygame.K_s, self.__colorBlanco)
        jugador2 = Jugador(self.__ventana, Vector2(750, 100), Vector2(0, 0), 10, pygame.K_i, pygame.K_k, self.__colorBlanco)

        posPelota = Vector2([self.__ventana.get_width() / 2, self.__ventana.get_height() / 2])
        pelota = Pelota(self.__ventana, posPelota, Vector2(5, 5), 10, self.__colorBlanco)

        # Creamos una lista de jugadores
        self.__listaJugadores = [jugador1, jugador2]

        # Creamos una lista polimorfica de objetos, que incluye la pelota y losjugadores
        self.__listaObjetos = [jugador for jugador in self.__listaJugadores]
        self.__listaObjetos.append(pelota)

        self.__reloj = pygame.time.Clock()
        self.__mainLoop()
        

    def __mainLoop(self):
        """" Método que se encarga de recargar en cada momento la pantalla del juego """

        while(True):    
            
            #Controlamos y vemos los eventos
            self.__controladorDeEventos()
            
            self.__ventana.fill(self.__colorNegro)

            # Pintamos elementos y jugadores
            for objeto in self.__listaObjetos:
                objeto.imprimir()

            #Actualizamos ventana 
            pygame.display.flip()

            self.__reloj.tick(60)


    def __controladorDeEventos(self):
        """ Se encarga de administrar todos los eventos del juego """
        
        for evento in pygame.event.get():
            #Si la ventana se cierra, terminamos el programa
            if(evento.type == pygame.QUIT):
                exit()
            
            for jugador in self.__listaJugadores:
                #----EVENTOS DEL JUGADOR------------
                if evento.type == pygame.KEYUP:
                    if evento.key == jugador.getTeclaArriba() or evento.key == jugador.getTeclaAbajo():
                        jugador.setVelocidad(Vector2(0, 0))
            
                if evento.type == pygame.KEYDOWN:
                    if evento.key == jugador.getTeclaArriba():
                        jugador.setVelocidad(Vector2(0, -5))
                
                    if evento.key == jugador.getTeclaAbajo():
                        jugador.setVelocidad(Vector2(0, 5))

            #-----EVENTOS DEL JUGADOR 2------------

