from importlib.machinery import WindowsRegistryFinder
from turtle import color, pos
import pygame
import random
import math
import time


clock = pygame.time.Clock()
clock.tick(60)

speed = 20
scale = 20
window_width = 1280 
window_height = 720

rect_size = 150
gap = 20

player = 1
cells = [0,0,0,0,0,0,0,0,0]


pygame.init()
pygame.display.set_caption("Tic Tac Toe")
window = pygame.display.set_mode((window_width, window_height))

font = pygame.font.SysFont("Arial", 18)
refreshrate = pygame.time.Clock()


def game_loop():
    global player
    while True:
        paint_hud()
        pos=detect_mouseclick()
        if pos != None:
            clickedRect=click_in_rect(pos)
            if clickedRect != None:
                cells[clickedRect] = player + 1
                window.fill(pygame.Color(0,0,0))
                paint_pieces()
                if player == 1:
                    player = 2
                else:
                    player = 1
        playername()
        game_Over()
        winner = game_Over()
        render = font.render(f"Winner: {winner} ", True, pygame.Color(255,255,255))
        window.blit(render, [100,200])
        pygame.display.flip()
        if cells[0] != 0 and cells[1]!= 0 and cells[2] != 0 and cells[3] != 0 and cells[4] != 0 and cells[5] != 0 and cells[6] != 0 and cells[7] != 0 and cells[8] != 0 and winner != 1 and winner != 2:
            winner = 123
            paint_hud()
            game_over_message_draw()

        if winner == 1 or winner == 2:
            paint_hud()
            game_over_message()


        pygame.display.update()



        
def playername():   
    global player
    render = font.render(f"Player: {player} ", True, pygame.Color(255,255,255))
    window.blit(render, [100,100])
    pygame.display.flip()

def paint_hud():
    for i in range(0,3):
        y = 120 + i*(rect_size + gap)
        for j in range(0,3):
            x = 350 + j*(rect_size + gap)
            rect = pygame.draw.rect(window, pygame.Color(100,100,100), [x,y,rect_size,rect_size], 1)
            pygame.display.flip()


def detect_mouseclick():
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            return pos
    return None

def click_in_rect(pos):
    for i in range(0,3):
        y = 120 + i*(rect_size + gap)
        if pos[1] >= y and pos[1] <= y + rect_size:
            for j in range(0,3):
                x = 350 + j*(rect_size + gap)
                if pos[0] >= x and pos[0] <= x + rect_size:
                    return(i*3+j)

    return None

def game_Over():
	win_cond = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
	for each in win_cond:
		try:
			if cells[each[0]] == cells[each[1]] and cells[each[1]] == cells[each[2]]:
				return cells[each[0]]
		except:
			pass
	return 0

    # global render
    # #Zeilencheck
    # for i in range(0,3):
    #     winner = cells[i]
    #     for j in range(1,3):
    #         if cells[j*3+i] != winner:
    #             winner = 0
    #         else:
    #             print(winner)
    #             render = font.render(f"Winner: {winner} ", True, pygame.Color(255,255,255))
    #             window.blit(render, [100,200])
    #             pygame.display.flip()
    # #Spaltencheck
    # for i in range(0,3):
    #     winner = cells[i]
    #     for j in range(1,3):
    #         if cells[i*3+j] != winner:
    #             winner = 0
    #         else:
    #             print(winner)
    #             window.blit(render, [100,240])
    #             pygame.display.flip()
    
    # #Diagonal
    # winner = cells[0]
    # if cells[0] == winner and cells[4] == winner and cells[8] == winner:
    #     window.blit(render, [100,240])


                    
def paint_pieces():
    for c in range (0, len(cells)): 
        if cells[c] > 1:
            i = c//3
            j = c%3
            y = 120 + i*(rect_size + gap)
            x = 350 + j*(rect_size + gap)
            if cells[c] == 2 :
                pygame.draw.ellipse(window, pygame.Color(100,100,100), [x,y,150,150], 1)
            else:
                pygame.draw.line(window, pygame.Color(100,100,100), [x, y], [x+rect_size,y+rect_size])
                pygame.draw.line(window, pygame.Color(100,100,100), [x+rect_size, y], [x,y+rect_size])

def game_over_message():
    winner = game_Over()
    font = pygame.font.SysFont("Arial", scale*4)
    render = font.render(f"Winner: {winner} ", True, pygame.Color(255,255,255))
    rect = render.get_rect()
    rect.midtop = (window_width / 2, window_height / 2 - 45)
    window.blit(render, rect)
    pygame.display.flip()
    time.sleep(4)
    exit(0)

def game_over_message_draw():
    global winner
    font = pygame.font.SysFont("Arial", scale*4)
    render = font.render(f"DRAW", True, pygame.Color(255,255,255))
    rect = render.get_rect()
    rect.midtop = (window_width / 2 - 40, window_height / 2 - 45)
    window.blit(render, rect)
    pygame.display.flip()
    time.sleep(4)
    exit(0)


if __name__ == "__main__":
    game_loop()