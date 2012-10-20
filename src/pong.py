import pygame

class Stuff(object):
    pass

STUFF = Stuff()

STUFF.SCREEN = None
STUFF.PADDLE1 = None
STUFF.PADDLE2 = None
STUFF.PADDLE1_X = 20
STUFF.PADDLE1_Y = 50
STUFF.PADDLE2_X = 600
STUFF.PADDLE2_Y = 50
STUFF.BALL = None
STUFF.BALL_DIR = -10
STUFF.BALL_POS = (320,240)
STUFF.RUNNING = 1

def draw():
    STUFF.SCREEN.fill((0, 0, 0))
    STUFF.SCREEN.blit(STUFF.BALL, STUFF.BALL_POS)
    STUFF.SCREEN.blit(STUFF.PADDLE1, (STUFF.PADDLE1_X,STUFF.PADDLE1_Y))
    STUFF.SCREEN.blit(STUFF.PADDLE2, (STUFF.PADDLE2_X,100))
    pygame.display.flip()

def input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            STUFF.RUNNING = 0
        if (event.type == pygame.KEYUP) or (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_UP: STUFF.PADDLE1_Y -= 10
            if event.key == pygame.K_DOWN: STUFF.PADDLE1_Y += 10
            if event.key == pygame.K_ESCAPE: STUFF.RUNNING = 0

def collides(one_pos, one_rect, two_pos, two_rect):
    rect_one = pygame.Rect(one_pos, (one_rect.get_width(), one_rect.get_height()))

def server_main():
    global STUFF


    while STUFF.RUNNING:
        pygame.time.delay(66)
        input()
        if collides((STUFF.PADDLE1_X, )STUFF.PADDLE1.get_rect(), STUFF.BALL.get_rect()):
            STUFF.BALL_DIR *= -1


        #elif STUFF.BALL_DIR > 0: # Moving right, towards clients paddle
        #    if not STUFF.BALL_POS[0] + STUFF.BALL.get_width() < STUFF.PADDLE2_X: STUFF.BALL_DIR *= -1


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
    pygame.display.set_caption('SWDCDN120120 pong FTW')

if __name__ == "__main__":
    setup()

    if True:
        server_main()
    else:
        client_main()
