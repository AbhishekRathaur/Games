import  sys, pygame
import random
import time

from pygame.locals import *
pygame.init()

size = width, height = 400, 400
speed = [2, 2]
black = 0, 0, 0
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
initial_x = 195
initial_y = 195

class Point:
    def __init__(self , x , y ):
        self.x = x
        self.y = y


snake_body = []
snake_body.append(Point(initial_x,initial_y))

DISPLAY=pygame.display.set_mode(size,0,32)

initial_direction = 0
unit_size = 10


count = 0
size = 1
isfood = False

def check_food_eat(p1 , p2):
    x1 = p1.x - unit_size/2
    x2 = p1.x + unit_size/2
    x3 = p2.x - unit_size / 2
    x4 = p2.x + unit_size / 2
    y1 = p1.y - unit_size / 2
    y2 = p1.y + unit_size / 2
    y3 = p2.y - unit_size / 2
    y4 = p2.y + unit_size / 2
    if (( (x3 >= x1 and x3 <= x2) or (x4 >= x1 and x4 <= x2) or (x1 >= x3 and x1 <= x4) or (x2 >= x3 and x2 <= x4) )
        and
        ((y3 >= y1 and y3 <= y2) or (y4 >= y1 and y4 <= y2) or (y1 >= y3 and y1 <= y4) or (y2 >= y3 and y2 <= y4)) ):
        return True
    return False


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            initial_direction = 1
        elif event.key == pygame.K_RIGHT:
            initial_direction = 0
        elif event.key == pygame.K_UP:
            initial_direction = 2
        elif event.key == pygame.K_DOWN:
            initial_direction = 3

    count+=1

    tail = snake_body.pop()
    if len(snake_body) ==0 :
        head = tail
    else :
        head = snake_body[0]
    new_head_x = head.x
    new_head_y = head.y

    if initial_direction == 1:
        new_head_x -= unit_size
    elif initial_direction == 0:
        new_head_x += unit_size
    elif initial_direction == 2:
        new_head_y -= unit_size
    elif initial_direction == 3:
        new_head_y += unit_size
    if new_head_x <=0 :
        new_head_x = width - unit_size/2
    if new_head_x >=400 :
        new_head_x = unit_size/2
    if new_head_y <= 0:
        new_head_y = height - unit_size/2
    if new_head_y >= 400:
        new_head_y = unit_size/2

    snake_body.insert(0, Point(new_head_x, new_head_y))

    if count % 5 == 0 and isfood == False:
        food_x = int(random.uniform(unit_size, width - unit_size))
        food_y = int(random.uniform(unit_size, height - unit_size))
        isfood = True

    pygame.draw.rect(DISPLAY, blue, (new_head_x, new_head_y, unit_size, unit_size))
    if isfood:
        if not check_food_eat(snake_body[0], Point(food_x, food_y)):
            pygame.draw.circle(DISPLAY, red, (food_x, food_y), int(unit_size / 2), int(unit_size / 2))
            pygame.draw.rect(DISPLAY, black, (tail.x, tail.y, unit_size, unit_size))
        else:
            isfood = False
            pygame.draw.circle(DISPLAY, black, (food_x, food_y), int(unit_size / 2), int(unit_size / 2))
            pygame.draw.rect(DISPLAY, blue, (tail.x, tail.y, unit_size, unit_size))
            snake_body.append(tail)
            size+=1
    else:
        pygame.draw.rect(DISPLAY, black, (tail.x, tail.y, unit_size, unit_size))

    pygame.display.update()
    time.sleep(0.1)




