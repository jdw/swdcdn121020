import pygame

class Stuff(object):
    pass

STUFF = Stuff()

STUFF.SCREEN = None
STUFF.PADDLE1 = None
STUFF.PADDLE2 = None
STUFF.PADDLE1_X = 20
STUFF.PADDLE2_X = 600
STUFF.BALL = None
STUFF.BALL_DIR = -10
STUFF.BALL_POS = (320,240)
STUFF.RUNNING = 1

def draw():
    STUFF.SCREEN.fill((0, 0, 0))
    STUFF.SCREEN.blit(STUFF.BALL, STUFF.BALL_POS)
    STUFF.SCREEN.blit(STUFF.PADDLE1, (STUFF.PADDLE1_X,100))
    STUFF.SCREEN.blit(STUFF.PADDLE2, (STUFF.PADDLE2_X,100))
    pygame.display.flip()

def server_main():
    global STUFF

    while STUFF.RUNNING:
        pygame.time.delay(66)
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            STUFF.RUNNING = 0

        if not (STUFF.PADDLE1_X < STUFF.BALL_POS[0] and STUFF.BALL_POS[0] < STUFF.PADDLE2_X):
            STUFF.BALL_DIR *= -1

        pos = STUFF.BALL_POS
        STUFF.BALL_POS = (pos[0] + STUFF.BALL_DIR, pos[1])
        draw()

def client_main():
    pass


def setup():
    global STUFF

    STUFF.SCREEN = pygame.display.set_mode((640, 480))
    STUFF.PADDLE1 = pygame.image.load("assets/paddle.png")
    STUFF.PADDLE1.set_colorkey((255,0,255))
    STUFF.PADDLE2 = pygame.image.load("assets/paddle.png")
    STUFF.BALL = pygame.image.load("assets/ball.png")


if __name__ == "__main__":
    setup()

    if True:
        server_main()
    else:
        client_main()
