import pygame


class Piece:
    def __init__(self, color, pos, size):
        """color acepta dos valores True para blancas, False para negras
        pos es la posicion (fila, columna) en la matriz squares
        size se utiliza para determinar el tamaño de la imagen de la pieza"""
        self.color = color
        self.pos = pos
        self.size = size


class King(Piece):
    def __init__(self, color, pos, size):
        super().__init__(color, pos, size)

        if self.color:
            self.picture = pygame.image.load("pictures/king.jpg")
        else:
            self.picture = pygame.image.load("pictures/DarkKing.jpg")

        self.picture = pygame.transform.scale(self.picture, (size, size))


class Queen(Piece):
    def __init__(self, color, pos, size):
        super().__init__(color, pos, size)

        if self.color:
            self.picture = pygame.image.load("pictures/queen.jpg")
        else:
            self.picture = pygame.image.load("pictures/DarkQueen.jpg")

        self.picture = pygame.transform.scale(self.picture, (size, size))


class Pawn(Piece):
    def __init__(self, color, pos, size):
        super().__init__(color, pos, size)

        if self.color:
            self.picture = pygame.image.load("pictures/pawn.png")
        else:
            self.picture = pygame.image.load("pictures/DarkPawn.jpg")

        self.picture = pygame.transform.scale(self.picture, (size, size))


class Rook(Piece):
    def __init__(self, color, pos, size):
        super().__init__(color, pos, size)

        if self.color:
            self.picture = pygame.image.load("pictures/Rook.jpg")
        else:
            self.picture = pygame.image.load("pictures/DarkRook.jpg")

        self.picture = pygame.transform.scale(self.picture, (size, size))


class Knight(Piece):
    def __init__(self, color, pos, size):
        super().__init__(color, pos, size)

        if self.color:
            self.picture = pygame.image.load("pictures/knight.jpg")
        else:
            self.picture = pygame.image.load("pictures/DarkKnight.jpg")

        self.picture = pygame.transform.scale(self.picture, (size, size))


class Bishop(Piece):
    def __init__(self, color, pos, size):
        super().__init__(color, pos, size)

        if self.color:
            self.picture = pygame.image.load("pictures/Bishop.jpg")
        else:
            self.picture = pygame.image.load("pictures/DarkBishop.jpg")

        self.picture = pygame.transform.scale(self.picture, (size, size))


# funcion para determinar la posición inicial de cada una de las piezas en el tablero deacuerdo
# a ma matriz squares de main
def init_pos(fil, col, size):
    """fila y columna son los indices en la matriz squares
    size es un parametro necesario para crear las piezas"""
    pos = (fil, col)
    if fil == 1:
        return Pawn(False, pos, size)
    elif fil == 6:
        return Pawn(True, pos, size)
    elif fil == 0:
        color = False
    elif fil == 7:
        color = True
    else:
        return None

    if col == 0 or col == 7:
        return Rook(color, pos, size)
    elif col == 1 or col == 6:
        return Knight(color, pos, size)
    elif col == 2 or col == 5:
        return Bishop(color, pos, size)
    elif col == 3:
        return Queen(color, pos, size)
    elif col == 4:
        return King(color, pos, size)
