import pygame

pygame.init()


class Square:
    def __init__(self, pos, size, color, piece=None):
        """la variable size se le debe ingresar un entero self.size_square es una tupla
        type(pos) -> tuple(x,y)
        type(color) -> tuple (RGB)
        pice debe ser una instancia de pygame.Surface"""
        self.pos = pos  # posicion de la esquina izquierda superior de la casilla
        self.size_square = (size, size)  # tamaño de la casilla
        self.color = color  # color de la casilla
        # objeto de tipo pygame.Rect que representa la casilla
        self.square = pygame.Rect(self.pos[0], self.pos[1], self.size_square[0], self.size_square[1])
        # objeto de tipo Surface
        self.__piece = piece

    @property
    def piece(self):
        return self.__piece

    @piece.setter
    def piece(self, piece):
        self.__piece = piece


    def draw(self, screen_to_draw):
        """esta función dibuja en la pantalla la casilla seleccionada"""
        pygame.draw.rect(screen_to_draw, self.color, self.square)
        if self.__piece is not None:
            self.__piece = pygame.transform.scale(self.__piece, self.size_square)
            screen_to_draw.blit(self.__piece, self.pos)
        pygame.display.update()


def color_square(fil, column, color1=(255, 255, 255), color0=(0, 0, 0)):
    """esta S determina el color de la casilla
    según la columna y la fila. La fila 0 es la fila superior,
    la columna 0 es la primera columna de la izquierda
    color1 es el equivalente al blanco
    color0 es el equivalnete al negro"""
    if fil % 2 == 0:
        if column % 2 == 0:
            return color1
        else:
            return color0
    else:
        if column % 2 == 0:
            return color0
        else:
            return color1
