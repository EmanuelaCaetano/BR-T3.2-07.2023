import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5

class Dinosaur:
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False #criação da variavel duck
        self.step_index = 0
        self.jump_vel = JUMP_VEL
    
    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1] #ternary operator 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index+=1        
        
        if self.step_index >= 10:
            self.step_index = 0
    
    def jump(self):
        self.image = JUMPING
        
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel*4
            self.jump_vel -=0.8
        
        if self.jump_vel < -JUMP_VEL:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_vel = JUMP_VEL
    
    def duck(self): #abaixando
        self.image = DUCKING[0]                #partindo do 0
        self.dino_rect = self.image.get_rect() #pegando a imagem certa
        self.dino_rect.x = X_POS               #plano cartesiano 
        self.dino_rect.y = Y_POS + 30
        self.dino_duck = False                 #deixando a ação no off

    
    def update(self, user_input):         #alteraçãol para agora aceitar o duck
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True

            
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck: #adicionando mais um estado para o dino
            self.duck()                
            
    
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x,self.dino_rect.y))
    