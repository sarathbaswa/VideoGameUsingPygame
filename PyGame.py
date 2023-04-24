import pygame, sys, random

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1200
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# colors
bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

# Game variables
player_speed = 0
opponent_speed = 7
ball_speed_x = -7
ball_speed_y = -7

# Text variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 24)

# Game rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.key == pygame.KEY_UP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

# Ball animation
ball.x += ball_speed_x
ball.y += ball_speed_y

if ball.top <= 0 or ball.bottom >= screen_height:
    ball_speed_y *= -1
if ball.left <= 0:
    # Reset ball
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_x = 7 * random.choice((1, -1))
    ball_speed_y = 7 * random.choice((1, -1))
    player_score += 1
    # NOTE: update player scoreboard font
if ball.right >= screen_width:
    # Reset ball
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_x = 7 * random.choice((1, -1))
    ball_speed_y = 7 * random.choice((1, -1))
    opponent_score += 1
    # NOTE: update opponent scoreboard font

if ball.colliderect(player) and ball_speed_x > 0:
    ball_speed_x *= -1
if ball.colliderect(opponent) and ball_speed_x < 0:
    ball_speed_x *= -1

# Player Animation
player.y += player_speed
if player.top <= 0:
    player.top = 0
if player.bottom >= screen_height:
    player.bottom = screen_height

# Opponent 'A1'
if opponent.top < ball.y:
    opponent.top += opponent_speed
if opponent.bottom > ball.y:
    opponent.top -= opponent_speed
if opponent.top <= 0:
    opponent.top = 0
if opponent.bottom >= screen_height:
    opponent.bottom = screen_height

# Visuals
screen.fill(bg_color)
pygame.draw.rect(screen, light_gray, ball)
pygame.draw.rect(screen, light_gray, player)
pygame.draw.rect(screen, light_gray, opponent)
pygame.draw.aaline(
    screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height)
)

# Fontstuffs
player_text = game_font.render(f"(player_score)", false, light_grey)
screen.blit(player_text, (610, 350))

opponent_text = game_font.render(f"(opponent_score)", false, light_grey)
screen.bilt(opponent_text, (580, 350))

# Updating the window
pygame.display.flip()  # updates the entire screen, alternative is .display.update() to optimize flip
clock.tick(60)
