import square
import pygame
# input para determinar el tamaño de las casillas
size_squares = int(input("ingresa el tamaño de las casillas: "))
color_white = input("ingresa el color personalizado de las casillas blancas R G B: ")
color_white = [int(i) for i in color_white.split()]
color_white = tuple(color_white)
print(color_white)
color_black = input("ingrsea el color personalizado de las casillas negras R G B: ")
color_black = [int(i) for i in color_black.split()]
color_black = tuple(color_black)
print(color_black)
screen = pygame.display.set_mode((size_squares * 8, size_squares * 8))  # inicio del screen
squares = []  # arreglo donde van a ir cada una de las casillas

for fila in range(8):
    squares.append([])
    for col in range(8):
        util_color = square.color_square(fila, col, color_white, color_black)

        squares[fila].append(square.Square((size_squares * col, size_squares * fila), size_squares, util_color))
        squares[fila][col].draw(screen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()