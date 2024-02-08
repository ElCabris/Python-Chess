import pygame
import square
import piece

# input para determinar el tamaño de las casillas
size_squares = int(input("ingresa el tamaño de las casillas: "))
color_white = input("ingresa el color personalizado de las casillas blancas R G B: ")
color_white = [int(i) for i in color_white.split()]
color_white = tuple(color_white)
color_black = input("ingrsea el color personalizado de las casillas negras R G B: ")
color_black = [int(i) for i in color_black.split()]
color_black = tuple(color_black)

screen = pygame.display.set_mode((size_squares * 8, size_squares * 8))  # inicio del screen
squares = []  # arreglo donde van a ir cada una de las casillas
pieces = {}  # mapa donde vana a ir las piezas con sus posiciones respectivas en squares
for fila in range(8):
    squares.append([])
    for col in range(8):
        util_color = square.color_square(fila, col, color_white, color_black)
        if not (1 < fila < 6):
            pieces[(fila, col)] = piece.init_pos(fila, col, size_squares)
            squares[fila].append(square.Square((size_squares * col, size_squares * fila), size_squares,
                                               util_color, pieces[(fila, col)].picture))
        else:
            squares[fila].append(square.Square((size_squares * col, size_squares * fila), size_squares,
                                               util_color))
        squares[fila][col].draw(screen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # las blancas inician su turno
    # format imput (inicial de la pieza) coordenadas en el sistema algebraico (columna(letra), columna(numero))
    # - (casilla final en el sistema algebraico)
    turn_withe = input()
    piece_move = piece.piece_class(turn_withe[0])
    coo_origin = square.algebraic_to_sqscreen([turn_withe[1], int(turn_withe[2])])
    coo_fin = square.algebraic_to_sqscreen([turn_withe[4], int(turn_withe[5])])

    if piece.is_a_piece(pieces, coo_origin, piece_move):
        pieces[coo_fin] = pieces[coo_origin]
        del pieces[coo_origin]
    
        squares[coo_fin[0]][coo_fin[1]].piece = pieces[coo_fin].picture
        squares[coo_origin[0]][coo_origin[1]].piece = None
        squares[coo_origin[0]][coo_origin[1]].draw(screen)
        squares[coo_fin[0]][coo_fin[1]].draw(screen)

    else:
        print("syntax error")

pygame.quit()
