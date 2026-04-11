from pygame import *
from ball import*
init()

WINDOW_SIZE = (1200, 800)
FPS = 60

screen = display.set_mode(WINDOW_SIZE)
display.set_caption(Arkanoid)
clk = time.Clock()

running = True
lose = False


while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

   
    screen.fill((180, 180, 180))
    screen.blit(g_block, g_block_rect)
    draw.rect(screen, (255, 0, 0), player)

    display.update()
    clk.tick(FPS)