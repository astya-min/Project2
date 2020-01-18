import pygame
import random

GREEN = (31, 222, 37)
WHITE = (255, 255, 255)
GREEN = (51, 92, 36)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 30


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class Mouse(pygame.sprite.Sprite):

    def __init__(self, x, y, img='mouse.png'):
        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
        self.walls = None

        self.cheeses = None
        self.collected_cheeses = 0

        self.cats = pygame.sprite.Group()
        self.wine = pygame.sprite.Group()

        self.alive = True

        self.win = False

    def update(self):

        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:

                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        cheeses_hit_list = pygame.sprite.spritecollide(self, self.cheeses, False)
        for cheeses in cheeses_hit_list:
            self.collected_cheeses += 1
            cheeses.kill()

        if pygame.sprite.spritecollideany(self, self.cats, False):
            self.alive = False
        if self.rect.x <= (wine.rect.x + 45) and self.rect.y <= (wine.rect.y + 45) and self.rect.x >= (
                wine.rect.x) and self.rect.y >= (wine.rect.y):
            self.win = True


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Cheeses(pygame.sprite.Sprite):
    def __init__(self, x, y, img='cheese.png'):
        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Wine(pygame.sprite.Sprite):
    def __init__(self, x, y, img='WINE.png'):
        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Cat(pygame.sprite.Sprite):
    def __init__(self, x, y, img='cat1.png'):
        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.start = x
        self.stop = x + random.randint(180, 240)
        self.direction = 1

    def update(self):

        if self.rect.x >= self.stop:
            self.rect.x = self.stop
            self.direction = -1

        if self.rect.x <= self.start:
            self.rect.x = self.start
            self.direction = 1

        self.rect.x += self.direction * 2


pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Мышка ищет винишко)')

all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

wall_coords = [
    [0, 0, 20, 700],
    [780, 0, 20, 700],
    [0, 0, 790, 20],
    [0, 580, 790, 590],
    [10, 100, 120, 20],
    [190, 10, 20, 425],
    [80, 180, 120, 20],
    [10, 250, 120, 20],
    [80, 350, 120, 20],
    [300, 100, 20, 500],
    [400, 300, 400, 20],
    [400, 300, 20, 200],
    [475, 400, 20, 200],
    [550, 300, 20, 200],
    [625, 400, 20, 200],
    [700, 300, 20, 200],
]
for coord in wall_coords:
    wall = Wall(coord[0], coord[1], coord[2], coord[3])
    wall_list.add(wall)
    all_sprite_list.add(wall)

cheeses_list = pygame.sprite.Group()
cheeses_coord = [[100, 140], [236, 50], [400, 234], [725, 25], [550, 530]]

for coord in cheeses_coord:
    cheeses = Cheeses(coord[0], coord[1])
    cheeses_list.add(cheeses)
    all_sprite_list.add(cheeses)

wine_list = pygame.sprite.Group()
wine_coord = [[725, 330]]
for coord in wine_coord:
    wine = Wine(coord[0], coord[1])
    wine_list.add(wine)
    all_sprite_list.add(wine)

cats_list = pygame.sprite.Group()
cats_coord = [[10, 450], [400, 50]]
for coord in cats_coord:
    cat = Cat(coord[0], coord[1])
    cats_list.add(cat)
    all_sprite_list.add(cat)

mouse = Mouse(50, 50)
mouse.walls = wall_list
all_sprite_list.add(mouse)

mouse.cheeses = cheeses_list

mouse.cats = cats_list

font = pygame.font.SysFont('Arial', 42, True)
text = font.render('ИГРА ОКОНЧЕНА', True, WHITE)
text_win = font.render('Лабиринт пройден', True, BLACK)
text_win2 = font.render('Вы выиграли!', True, BLACK)
BackGround = Background('fon.png', [0, 0])

clock = pygame.time.Clock()
well = False
done = False

while not well:
    BackGround1 = Background('wine-glass-and-bottle.png', [0, 0])
    screen.blit(BackGround1.image, BackGround1.rect)
    text_start = font.render('Нажмите F1, чтобы начать', True, WHITE)
    screen.blit(text_start, (200, 200))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            well = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                well = True
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mouse.change_x = -3
            elif event.key == pygame.K_RIGHT:
                mouse.change_x = 3
            elif event.key == pygame.K_UP:
                mouse.change_y = -3
            elif event.key == pygame.K_DOWN:
                mouse.change_y = 3

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                mouse.change_x = 0
            elif event.key == pygame.K_RIGHT:
                mouse.change_x = 0
            elif event.key == pygame.K_UP:
                mouse.change_y = 0
            elif event.key == pygame.K_DOWN:
                mouse.change_y = 0

    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)

    if not mouse.alive:
        BackGround1 = Background('wine-glass-and-bottle.png', [0, 0])
        screen.blit(BackGround1.image, BackGround1.rect)
        screen.blit(text, (200, 150))
        coll = font.render("Вы набрали: " + str(mouse.collected_cheeses), True, WHITE)
        screen.blit(coll, (200, 200))

    elif mouse.win:
        BackGround_win = Background('end-fon.png', [0, 0])
        screen.blit(BackGround_win.image, BackGround_win.rect)

        screen.blit(text_win, (200, 150))
        screen.blit(text_win2, (200, 200))
        coll = font.render("Вы набрали: " + str(mouse.collected_cheeses), True, BLACK)
        screen.blit(coll, (200, 250))
        pygame.display.flip()
    else:
        all_sprite_list.update()
        all_sprite_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
