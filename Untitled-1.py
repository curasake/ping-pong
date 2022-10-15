from pygame import *


window = display.set_mode((700, 500))
display.set_caption("Ping-Pong")
background = transform.scale(image.load("dota-2-carl-invoker-mag-plasch.jpg"),(700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_size1, player_size2):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_size1, player_size2))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_d] and self.rect.x < 650:
            self.rect.x += self.speed

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_s] and self.rect.y < 650:
            self.rect.x += self.speed

game = True
clock = time.Clock()
FPS = 60
finish = False
while game:
    for  e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0,0))











    display.update()
time.delay(50)



