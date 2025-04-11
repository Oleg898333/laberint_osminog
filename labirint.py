# Разработай свою игру в этом файле!

from pygame import*
font.init()
font1 = font.SysFont('Arial',90)
win = font1.render ('YOU WIN', 1, (222,222,222) )
lol = font1.render ('Ho-Ho-Ho!', 1, (222,222,222) )
window = display.set_mode((800,500))
class GameSprite(sprite.Sprite):
    def __init__(self,picture,w,h,x,y):
        super().__init__()
        self.image = transform.scale(image.load(picture),(w,h))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class Enemu(GameSprite):
    def __init__(self,picture,w,h,x,y,x_speed):
        super().__init__(picture,w,h,x,y)
        self.x_speed = x_speed
       # self.y_speed = y_speed
        self.direction = 'left'
    def update (self):
        if self.rect.x <= 480:
            self.direction = 'rigt'
        if self.rect.x >= 700:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.x_speed
        else:
            self.rect.x += self.x_speed 
class Player(GameSprite):
    def __init__(self,picture,w,h,x,y,x_speed,y_speed):
        super().__init__(picture,w,h,x,y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        # self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, wallz, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left )
        if self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right )
        self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, wallz, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top )
        if self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom ) 
    def fire(self):
        bullet = Bullet('nosh.png', 20, 8, self.rect.right, self.rect.centery, 9)
        bullets.add(bullet)     

class Bullet(GameSprite):
    def __init__(self,picture,w,h,x,y,x_speed): 
        super().__init__(picture,w,h,x,y)
        self.speed = x_speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x >800:
            self.kill()




bullets = sprite.Group()

display.set_caption('laberint')
finish = False
run = True
tutol = Player('pac-8.png',70,70,50,410,0,0)
wall1 = GameSprite('platform_h.png',200,50,0,350)
wall2 = GameSprite('platform_h.png',30,300,450,230)
wall3 = GameSprite('platform_h.png',30,180,670,400)
wall4 = GameSprite('platform_h.png',30,100,450,0)
wall5 = GameSprite('platform_h.png',200,50,270,230)
wall6 = GameSprite('platform_h.png',50,150,270,100)
wall7 = GameSprite('platform_h.png',200,50,100,100)
wall8 = GameSprite('platform_h.png',200,50,100,230)
wall9 = GameSprite('platform_h.png',230,50,600,230)
wall10 = GameSprite('platform_h.png',260,50,450,400)
wall11 = GameSprite('platform_h.png',360,30,450,70)
pac8 = GameSprite ('pac-7.png',80,80,720,420)
Irik = Enemu ('pac-4 (1).png', 100,100,470,300,6)
povar = sprite.Group()
povar.add(Irik)
wallz = sprite.Group()
wallz.add(wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11)
# wallz.add(wall2)
#wallz.add(wall1)
#wallz.add(wall1)

while run:
    
    if finish == False:
        window.fill((231,142,225))
        tutol.update()
        tutol.reset()
        pac8.reset()
        povar.update()
        povar.draw(window)

        #wall1.reset()
        wallz.draw(window)
        bullets.update()
        bullets.draw(window)
        sprite.groupcollide(bullets, wallz, True, False)
        if len(sprite.groupcollide(bullets, povar, True, True)):
            Irik.rect.x = 804
        if sprite.collide_rect(pac8,tutol):
            finish = True   
            window.blit(win, (200,300))
        if sprite.collide_rect(tutol, Irik):
            finish = True   
            window.blit(lol, (200,300))

    time.delay(60)
    for eve in event.get():
        if eve.type == QUIT:
            run = False
        elif eve.type == KEYDOWN:
            if eve.key == K_w:
                    tutol.y_speed = -9
            if eve.key == K_s:
                    tutol.y_speed = 9
            if eve.key == K_a:
                    tutol.x_speed = -9
            if eve.key == K_d:
                    tutol.x_speed = 9
            if eve.key == K_SPACE:
                    tutol.fire()
            
        elif eve.type == KEYUP:
            if eve.key == K_w:
                    tutol.y_speed = 0
            if eve.key == K_s:
                    tutol.y_speed = 0
            if eve.key == K_a:
                    tutol.x_speed = 0
            if eve.key == K_d:
                    tutol.x_speed = 0
                

    display.update()


