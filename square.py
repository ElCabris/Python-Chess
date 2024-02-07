import pygame

pygame.init()


class Square:
    def __init__(self, pos, size, color):
        """la variable size se le debe ingresar un entero self.size_square es una tupla
        type(pos) -> tuple(x,y)
        type(color) -> tuple (RGB)"""
        self.pos = pos  # posicion de la esquina izquierda superior de la casilla
        self.size_square = (size, size)  # tamaño de la casilla
        self.color = color  # color de la casilla
        # objeto de tipo pygame.Rect que representa la casilla
        self.square = pygame.Rect(self.pos[0], self.pos[1], self.size_square[0], self.size_square[1])

    def draw(self, screen_to_draw):
        """esta función dibuja en la pantalla la casilla seleccionada"""
        pygame.draw.rect(screen_to_draw, self.color, self.square)
        pygame.display.update()


def color_square(fil, column, color1=(255, 255, 255), color0=(0, 0, 0)):
    """esta funcion determina el color de la casilla
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
