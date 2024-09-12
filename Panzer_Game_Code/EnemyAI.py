import pygame 
import math 
from os.path import join 
from objects_class import *
from maps import map

class Enemy(Panzern):
    def __init__(self, left, top, img):
        super().__init__(left, top)
        self.img = pygame.image.load(r"D:\Projects\Python\Panzer_Game_Git\Panzer_Game\Panzer_Game_Code\Textures\silvertank_front.png")
        self.img = pygame.transform.scale(self.img, (STEP, STEP))

    def update(self, user):
        dx = user.rect.x - self.rect.x #deltaX
        dy = user.recct.y - self.rect.y
        dist = math.hypot(dx, dy)

        if dist > 0:
            dx, dy = dx / dist, dy / dist
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed
            
            self.angle = math.degrees(math.atan2(-dy, dx)) - 90

    def rotation_to_obj(self, screen):       
        rotated_img = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_img.get_rect(center = self.rect.center)
        screen.blit(rotated_img, new_rect.topleft)

