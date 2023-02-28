import pygame
from random import randrange

RES = 800
SIZE = 50
SIZE1 = SIZE // 2
x, y = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
length = 1
snake = [(x, y)]
dirx, diry = 0, 0
fps = 60
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
score = 0
speed_count = 0
snake_speed = 10
pygame.init()
screen = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_end = pygame.font.SysFont('Arial', 66, bold=True)
img = pygame.image.load('трава.jpg').convert()
pygame.display.set_caption('Змейка. Счёт:' + str(score))
running = True


def apple_generation():
    global apple, score, length
    apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
    for sn in range(len(snake)):
        if apple[0] == snake[sn][0] and apple[1] == snake[sn][1]:
            apple_generation()
        else:
            apple = randrange(SIZE, RES - SIZE, SIZE), randrange(SIZE, RES - SIZE, SIZE)
            break
    score += 1
    length += 1


def new_window():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


while True:
    pygame.display.set_caption('Змейка. Счёт:' + str(score))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.blit(img, (0, 0))
    [pygame.draw.rect(screen, pygame.Color('green'), (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
    pygame.draw.circle(screen, pygame.Color('red'), (apple[0] + SIZE1, apple[1] + SIZE1), SIZE1)
    speed_count += 1
    if not speed_count % snake_speed:
        x += dirx * SIZE
        y += diry * SIZE
        snake.append((x, y))
        snake = snake[-length:]
    if snake[-1] == apple:
        apple_generation()
        snake_speed -= 1
        snake_speed = max(snake_speed, 4)
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while running:
            render_end = font_end.render('Игра окончена', 1, pygame.Color('black'))
            count_end = font_end.render('Счёт:' + str(score), 1, pygame.Color('white'))
            screen.blit(render_end, (RES // 2 - 250, RES // 3))
            screen.blit(count_end, (RES // 2 - 110, RES // 3 + 100))
            pygame.display.flip()
            new_window()
            quit()
    pygame.display.flip()
    clock.tick(fps)
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        if dirs['W']:
            dirx, diry = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
    elif key[pygame.K_s]:
        if dirs['S']:
            dirx, diry = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
    elif key[pygame.K_a]:
        if dirs['A']:
            dirx, diry = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
    elif key[pygame.K_d]:
        if dirs['D']:
            dirx, diry = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True, }
