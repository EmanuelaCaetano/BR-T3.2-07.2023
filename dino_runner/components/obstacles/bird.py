import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self,images):
        super().__init__(images, random.randint(0,1))
        self.images = images
        self.flying_index = 0
        
        self.touched_ground = False
        #this will decide if the bird would be in zig-zig or not
        self.moving = random.randint(1,2) % 2 == 0 and True or False

    
    def update(self,game_speed, obstacles):
        #changing the images
        self.image = self.images[self.flying_index //5] 
        
        self.flying_index += 1
                
        if self.moving:
            if not self.touched_ground:
                self.rect.y +=10
                if self.rect.y > 350:
                    self.touched_ground = True
            else:
                self.rect.y -=10
                if self.rect.y < 200:
                    self.touched_ground = False
        
        if self.flying_index >=10:
            self.flying_index = 0
        
        super().update(game_speed, obstacles)

# import pygame
# import random

# from dino_runner.components.obstacles.obstacle import Obstacle


# class Bird(Obstacle):
#     def __init__(self, images):
#         self.type = 0
#         super().__init__(images, self.type)
        
#         self.rect.y = 270

# class Bird_02(Obstacle):
#     def __init__(self, images):
#         self.type = 1
#         super().__init__(images, self.type)
        
#         self.rect.y = 270


# import random

# from dino_runner.components.obstacles.obstacle import Obstacle


# from dino_runner.utils.constants import SCREEN_WIDTH

# class Bird(Obstacle):
#     def __init__(self, image, obstacle_type):
#         super().__init__(image, obstacle_type)
#         self.rect.x = SCREEN_WIDTH + self.rect.width
#         self.rect.y = 300
#         self.index = 0
#         self.counter = 0
#         self.score_counted = False


#     def update(self, speed, obstacles):
#         self.rect.x -= speed
#         self.animate()

#     def animate(self):
#         self.timer += pygame.time.get_ticks()
#         if self.timer > self.animation_time:
#             self.timer = 0
#             self.current_image = random.choice(self.images)

#     def draw(self, screen):
#         screen.blit(self.current_image, self.rect)

# import pygame
# import random

# from dino_runner.components.obstacles.obstacle import Obstacle
# from dino_runner.utils.constants import BIRD

# import pygame

# class Bird:
#     def __init__(self, img_path):
#         self.image = pygame.image.load(img_path).convert_alpha()
#         self.width = self.image.get_width()
#         self.height = self.image.get_height()
#         self.rect = self.image.get_rect()
#         self.rect.x = 800
#         self.rect.y = 250
#         self.fly_frames = [self.image, pygame.transform.flip(self.image, True, False)]
#         self.fly_index = 0
#         self.animation_time = pygame.time.get_ticks()
        
#     def update(self, game_speed, obstacles):
#         self.rect.x -= game_speed
#         self.animate()
        
#         if self.rect.right < 0:
#             obstacles.remove(self)
            
#     def draw(self, screen):
#         screen.blit(self.image, self.rect)
        
#     def animate(self):
#         if pygame.time.get_ticks() - self.animation_time > 200:
#             self.animation_time = pygame.time.get_ticks()
#             self.fly_index = (self.fly_index + 1) % len(self.fly_frames)
#             self.image = self.fly_frames[self.fly_index]
#             self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))


# class Bird(Obstacle):
#     def __init__(self, image):
#         self.step_index = 0
#         super().__init__(image, 0)
        
#     def update(self, game_speed, obstacles):
#         self.step_index += 1
#         if self.step_index < 5:
#             self.image = self.image[0]
#         elif self.step_index < 10:
#             self.image = self.image[1]
#         else:
#             self.image = self.image[0]
#             self.step_index = 0
        
#         self.rect.x -= game_speed
        
#         if self.rect.x < -self.rect.width:
#             obstacles.pop(0)



# import pygame
# import random

# from dino_runner.components.obstacles.obstacle import Obstacle

# class Bird(Obstacle):
#     def __init__(self, images):
#         self.type = 0
#         super().__init__(images[0], self.type)
#         self.images = images
#         self.image_index = 0
#         self.rect.y = 270
#         self.timer = pygame.time.get_ticks()

#     def update(self):
#         current_time = pygame.time.get_ticks()
#         if current_time - self.timer > 2000:  
#             self.image_index = (self.image_index + 1) % len(self.images)
#             self.image = self.images[self.image_index]
#             self.timer = current_time
#         super().update()



# import random

# from dino_runner.components.obstacles.obstacle import Obstacle



# class Bird(Obstacle):
#     def __init__(self, images):
#         self.type = 0
#         super().__init__(images, self.type)
        
#         self.rect.y = 270

        


# class Bird(Obstacle):
#     def __init__(self, images):
#         self.type = 0
#         self.update_counter = 0
#         super().__init__(images, self.type)
#         self.rect.y = 300

#     def update(self):
#         self.update_counter += 1
#         if self.update_counter % 5 == 0:
#             self.type = (self.type + 1) % 2
#             self.image = self.images[self.type]



# import random

# from dino_runner.components.obstacles.obstacle import Obstacle

# class Bird(Obstacle):
#     def __init__(self, images):
#         self.type = random.randint(0,2)
#         super().__init__(images, self.type)
        
#         self.rect.y = 300

#
# import random

# from dino_runner.components.obstacles.obstacle import Obstacle

# class Bird(Obstacle):
#     def __init__(self, images):
    
#         self.step = 0
        
#         while True:
#             if self.step % 5 == 0 :
#                 self.type = self.type[0]
#             else:
#                 self.type = self.type[1]
#             self.step += 1
#             if self.step > 100:
#                 break
#         super().__init__(images, self.type)
#         self.rect.y = 270



        
        


# from dino_runner.components.obstacles.obstacle import Obstacle

# class Bird(Obstacle):
#     def __init__(self, images):
#         super().__init__(self, images)  # inicia com o tipo 0
#         self.step_index = 0
#         self.rect.y = 325  # define a posição vertical do retângulo


#     def update(self):
            
#         if self.step_index % 5 == 0:
#             self.image = self.images[0]
#         else:
#             self.image = self.images[1]
#         self.step_index += 1
            



        # self.step_index += 1
        # self.image = self.type[0] [self.step_index // 5 % 2]  # alterna entre as duas imagens a cada 5 frames

        
        #self.image = self.type[0] if self.step_index < 5 else self.type[1]
#         


# import random

# from dino_runner.components.obstacles.obstacle import Obstacle

# class Bird(Obstacle):
#     def __init__(self, images):
#         self.step_index = 0
#         self.image = self.type[0] if self.step_index < 5 else self.type[1]
#         #self.type = random.randint(0,2)
#         #super().__init__(images, self.type)
#         self.step_index+=1        
        
#         if self.step_index >= 10:
#             self.step_index = 0
        
#         self.rect.y = 325

# import random
# from dino_runner.components.obstacles.obstacle import Obstacle

# class Bird(Obstacle):
#     def __init__(self, images):
#         super().__init__(images)  # inicia com o tipo 0
#         self.step_index = 0
#         self.rect.y = 325  # define a posição vertical do retângulo

#     def update(self):
#         self.image = self.type[self.step_index // 5]  # atualiza a imagem do obstáculo a cada 5 frames
#         self.step_index = (self.step_index + 1) % 10  # incrementa o índice e reseta para 0 quando chegar a 10


# import random

# from dino_runner.components.obstacles.obstacle import Obstacle

# class Bird(Obstacle):
#     def __init__(self, images):
#         self.step_index = 0
#         self.image = self.type[0] if self.step_index < 5 else self.type[1]
#         self.step_index+=1        
        
#         if self.step_index >= 10:
#             self.step_index = 0
        
#         self.rect.y = 325