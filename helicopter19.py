import pygame
import time
from random import randint, randrange
from PIL import Image

black = (0, 0, 0)
white = (255, 255, 255)

sunset = (253, 72, 47)

red = (255, 0, 0)
greenYellow = (184, 255, 0)
brightBlue = (47, 228, 253)
orange = (255, 113, 0)
yellow = (255, 236, 0)
purple = (252, 67, 255)

colorChoices = [greenYellow, brightBlue, orange, yellow, purple, sunset]

pygame.init()

surfaceWidth = 900
surfaceHeight = 600
size=(surfaceWidth,surfaceHeight)
screen=pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("Helicopter Game")
with Image.open('Helicopter.png') as image:
    imageWidth, imageHeight = image.size

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption('Helicopter')
clock = pygame.time.Clock()
bg=pygame.image.load("cloud.png").convert()
bg = pygame.transform.scale(bg, (size))

#screen.blit(bg,(0,0))

img = pygame.image.load('Helicopter.png')

def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                     intro =False
                if event.key == pygame.K_q:
                     pygame.quit()
                     quit()

        size = width,height = 900,600
        bg1 = pygame.image.load("helicoptermain.jpg")
        bg1 = pygame.transform.scale(bg1,(size))
        pygame.display.set_mode(size)
        screen=pygame.display.set_mode(size)

        screen.blit(bg1,(0,0))
        #message_to_screen("Press p to play and q to quit , black,20")
        basicfont = pygame.font.SysFont(None,48)
        text = basicfont.render("PRESS p TO START THE GAME",True,(255,0,0),(255,255,255))
        textrect=text.get_rect()
        textrect.centerx=screen.get_rect().centerx
        textrect.centery=screen.get_rect().centery
        screen.blit(text,textrect)
        pygame.display.update()
        clock.tick(15)


def score(count):
    font = pygame.font.SysFont('freesansbold.ttf', 40)
    text = font.render('Score: ' + str(count), True, white)
    surface.blit(text, [0, 0])


def blocks(xBlock, yBlock, blockWidth, blockHeight, gap, blockColor):
    pygame.draw.rect(surface, blockColor, [xBlock, yBlock, blockWidth, blockHeight])
    pygame.draw.rect(surface, blockColor, [xBlock, yBlock + blockHeight + gap, blockWidth, surfaceHeight])


def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            return event.key

    return None


def make_text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def message_surface(message):
    smallText = pygame.font.SysFont('freesansbold.ttf', 20)
    largeText = pygame.font.SysFont('freesansbold.ttf', 150)

    titleTextSurface, titleTextRectangle = make_text_objects(message, largeText)
    titleTextRectangle.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurface, titleTextRectangle)

    typTextSurface, typTextRectangle = make_text_objects('Press any key to continue', smallText)
    typTextRectangle.center = surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(typTextSurface, typTextRectangle)

    pygame.display.update()
    time.sleep(3)

    while replay_or_quit() == None:
        clock.tick()

    main()


def game_over():
    message_surface('Crashed!')


def helicopter(x, y, image):
    surface.blit(img, (x, y))



def main():
    x = 150
    y = 200
    y_move = 0

    xBlock = surfaceWidth
    yBlock = 0
    blockWidth = 70
    blockHeight = randint(0, surfaceHeight / 2)
    gap = imageHeight * 3
    blockMove = 4

    currentScore = 0

    blockColor = colorChoices[randrange(0, len(colorChoices))]

    gameOver = False

    while not gameOver:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 3
        y += y_move
        screen.blit(bg,(0,0))

        	   
        helicopter(x, y, img)
        blocks(xBlock, yBlock, blockWidth, blockHeight, gap, blockColor)
        score(currentScore)
        xBlock -= blockMove

        if y > surfaceHeight - imageHeight or y < 0:
            game_over()

        if xBlock < (-1 * blockWidth):
            xBlock = surfaceWidth
            blockHeight = randint(0, surfaceHeight / 2)
            blockColor = colorChoices[randrange(0, len(colorChoices))]
            currentScore += 1

        #Check for collision with upper block
        if x + imageWidth > xBlock:
            if x < xBlock + blockWidth:
                if y < blockHeight:
                    if x - imageWidth < blockWidth + xBlock:
                        game_over()

        #Check for collision with lower block
        if x + imageWidth > xBlock:
            if y + imageHeight > blockHeight + gap:
                if x < blockWidth + xBlock:
                    game_over()

        if 3 <= currentScore < 5:
            blockMove = 5
            gap = imageHeight * 2.8
        if 5 <= currentScore < 8:
            blockMove = 6
            gap = imageHeight * 2.6
	   
    

	   
        pygame.display.update()
        clock.tick(60)

game_intro()
main()
pygame.quit()
quit()
