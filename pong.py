import pygame
import sys
import random

def ballAnimation():
    global ball_speed_x, ball_speed_y # need to make it global so the variable can be used in the function
    ball.x += ball_speed_x # moves the ball left and right
    ball.y += ball_speed_y # moves the ball up and down

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1 # reverses direction if hits top or bottom
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x += .25
        ball_speed_y += .25
        ballRestart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1 # reverses direction if hits player
        

def playerAnimation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0 # stops from leaving top of screen
    if player.bottom >= screen_height:
        player.bottom = screen_height # stops from leaving bottom of screen

def opponentAnimation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0 # stops from leaving top of screen
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height # stops from leaving bottom of screen

def ballRestart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    if (ball.right >= screen_width):
        ball_speed_x = (-1 * abs(ball_speed_x)) # If hits opp side, goes left
    if (ball.left <= 0):
        ball_speed_x = abs(ball_speed_x) # If hits player side, goes right

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Window
screen_width = 1250
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width-10, screen_height/2 - 70,10,140)
opponent = pygame.Rect(0, screen_height/2 - 70, 10, 140)
score = pygame.Rect(screen_width/2 - 150, 10, 300, 100)

# Colors
bg_color = (35,35,35)
gold = (212,175,55)

# Speed
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 5.5 * random.choice((1,-1))
player_speed = 0
opponent_speed = 10

# Score
opponentScore = 0
playerScore = 0
font = pygame.font.Font("freesansbold.ttf", 32)


while True:
    # Handling input
    # "event" is what pygame calls anything that the user does
    # "pygame.event.get()" is the queue of events that the user inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #closes the game safely
            pygame.quit()
            sys.exit()
        # were to change player speed, if (q down): player speed = var # not 7
        # key down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        # key up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ballAnimation() # runs better if code is initiated before hand
    playerAnimation()
    opponentAnimation()

    # Visuals
    screen.fill(bg_color) # code is run top to bottom, so bg has to be first
    pygame.draw.rect(screen, gold, player)
    pygame.draw.rect(screen, gold, opponent)
    pygame.draw.ellipse(screen, gold, ball)
    pygame.draw.aaline(screen, gold, (screen_width/2,0), (screen_width/2,screen_height))
    #pygame.draw.rect(screen, gold, score)
    #pygame.draw.aaline(screen, bg_color, (screen_width/2,10), (screen_width/2, 110))

    # Window Update
    pygame.display.flip() #updates whole screen
    clock.tick(60) #60fps
