import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus 
from dino_runner.components.obstacles.cactusLarge import CactusLarge
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.bird import Bird_02

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.opcoes = ["small_cactus", "large_cactus", "bird"]  # lista com opções para sorteio
        self.animation_counter = 0
        self.step_index = 0
        self.is_bird_02_active = False
        
    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_type = random.choice(self.opcoes)
            if obstacle_type == "small_cactus":
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif obstacle_type == "large_cactus":
                self.obstacles.append(CactusLarge(LARGE_CACTUS))
            elif obstacle_type == "bird":
                self.obstacles.clear() 
                self.step_index = 1 # inicializa o contador de animação
                while self.step_index < 10:
                    self.obstacles.clear()
                    if self.is_bird_02_active:
                        self.obstacles.append(Bird_02(BIRD))
                    else:
                        self.obstacles.append(Bird(BIRD))
                    self.step_index += 1
                    self.is_bird_02_active = not self.is_bird_02_active
                    for i, obstacle in enumerate(self.obstacles):
                        obstacle.update(game.game_speed, self.obstacles)
                        if game.player.dino_rect.colliderect(obstacle.rect):
                            pygame.time.delay(500)
                            game.playing = False
                            break
                
        for i, obstacle in enumerate(self.obstacles):
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break                
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)


# import pygame
# import random

# from dino_runner.components.obstacles.cactus import Cactus 
# from dino_runner.components.obstacles.cactusLarge import CactusLarge
# from dino_runner.components.obstacles.bird import Bird
# from dino_runner.components.obstacles.bird import Bird_02

# from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

# class ObstacleManager:
#     def __init__(self):
#         self.obstacles = []
#         self.opcoes = ["small_cactus", "large_cactus", "bird"]  # lista com opções para sorteio
#         self.animation_counter = 0
#         self.step_index = 0
        
#     def update(self, game):
#         if len(self.obstacles) == 0:
#             obstacle_type = random.choice(self.opcoes)
#             if obstacle_type == "small_cactus":
#                 self.obstacles.append(Cactus(SMALL_CACTUS))
#             elif obstacle_type == "large_cactus":
#                 self.obstacles.append(CactusLarge(LARGE_CACTUS))
#             elif obstacle_type == "bird":
#                 self.obstacles.clear() 
#                 self.step_index = 1 # inicializa o contador de animação
#                 while self.step_index < 10:
#                     self.obstacles.clear()
#                     if self.step_index % 2 == 0:
#                         self.obstacles.append(Bird_02(BIRD))
#                         self.step_index +=1
#                         for i, obstacle in enumerate(self.obstacles):
#                             obstacle.update(game.game_speed, self.obstacles)
#                     else:
#                     #self.obstacles.clear()
#                         pygame.time.delay(10)
#                         self.obstacles.append(Bird(BIRD))
#                         self.step_index +=1
#                         for i, obstacle in enumerate(self.obstacles):
#                             obstacle.update(game.game_speed, self.obstacles)
                              
                
#         for i, obstacle in enumerate(self.obstacles):
#             obstacle.update(game.game_speed, self.obstacles)
#             if game.player.dino_rect.colliderect(obstacle.rect):
#                 pygame.time.delay(500)
#                 game.playing = False
#                 break                
    
#     def draw(self, screen):
#         for obstacle in self.obstacles:
#             obstacle.draw(screen)

# import pygame
# import random

# from dino_runner.components.obstacles.cactus import Cactus 
# from dino_runner.components.obstacles.cactusLarge import CactusLarge
# from dino_runner.components.obstacles.bird import Bird
# from dino_runner.components.obstacles.bird import Bird_02

# from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

# class ObstacleManager:
#     def __init__(self):
#         self.obstacles = []
#         self.opcoes = ["small_cactus", "large_cactus", "bird"]  # lista com opções para sorteio
#         self.animation_counter = 0
#         self.step_index = 0
        
#     def update(self, game):
#         if len(self.obstacles) == 0:
#             obstacle_type = random.choice(self.opcoes)
#             if obstacle_type == "small_cactus":
#                 self.obstacles.append(Cactus(SMALL_CACTUS))
#             elif obstacle_type == "large_cactus":
#                 self.obstacles.append(CactusLarge(LARGE_CACTUS))
#             elif obstacle_type == "bird":
#                 self.obstacles.clear() 
#                 self.step_index = 0 # inicializa o contador de animação
#                 while self.step_index < 10:
#                     self.obstacles.clear()
#                     self.obstacles.append(Bird_02(BIRD))
#                     for i, obstacle in enumerate(self.obstacles):
#                         obstacle.update(game.game_speed, self.obstacles)
                        
#                     #self.obstacles.clear()
#                     pygame.time.delay(10)
#                     self.obstacles.append(Bird(BIRD))
#                     self.step_index +=1
#                     for i, obstacle in enumerate(self.obstacles):
#                         obstacle.update(game.game_speed, self.obstacles)
                              
                
#         for i, obstacle in enumerate(self.obstacles):
#             obstacle.update(game.game_speed, self.obstacles)
#             if game.player.dino_rect.colliderect(obstacle.rect):
#                 pygame.time.delay(500)
#                 game.playing = False
#                 break                
    
#     def draw(self, screen):
#         for obstacle in self.obstacles:
#             obstacle.draw(screen)


# import pygame
# import random

# from dino_runner.components.obstacles.cactus import Cactus 
# from dino_runner.components.obstacles.cactusLarge import CactusLarge
# from dino_runner.components.obstacles.bird import Bird
# from dino_runner.components.obstacles.bird import Bird_02

# from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

# class ObstacleManager:
#     def __init__(self):
#         self.obstacles = []
#         self.opcoes = ["small_cactus", "large_cactus", "bird"]  # lista com opções para sorteio
#         self.animation_counter = 0
        
#     def update(self, game):
#         if len(self.obstacles) == 0:
#             obstacle_type = random.choice(self.opcoes)
#             if obstacle_type == "small_cactus":
#                 self.obstacles.append(Cactus(SMALL_CACTUS))
#             elif obstacle_type == "large_cactus":
#                 self.obstacles.append(CactusLarge(LARGE_CACTUS))
#             elif obstacle_type == "bird":
#                 self.obstacles.clear()
#                 self.obstacles.append(Bird(BIRD))
#                 self.obstacles.append(Bird_02(BIRD))

                
#         for obstacle in self.obstacles:
#             obstacle.update(game.game_speed, self.obstacles)
            

            
#             if game.player.dino_rect.colliderect(obstacle.rect):
#                 pygame.time.delay(500)
#                 game.playing = False
#                 break                
    
#     def draw(self, screen):
#         for obstacle in self.obstacles:
#             obstacle.draw(screen)


# import pygame
# import random

# from dino_runner.components.obstacles.cactus import Cactus 
# from dino_runner.components.obstacles.cactusLarge import CactusLarge
# from dino_runner.components.obstacles.bird import Bird
# from dino_runner.components.obstacles.bird import Bird_02

# from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

# class ObstacleManager:
#     def __init__(self):
#         self.obstacles = []
#         self.opcoes = ["small_cactus", "large_cactus", "bird"]  # lista com opções para sorteio
#         self.animation_counter = 0
        
#     def update(self, game):
#         if len(self.obstacles) == 0:
#             obstacle_type = random.choice(self.opcoes)
#             if obstacle_type == "small_cactus":
#                 self.obstacles.append(Cactus(SMALL_CACTUS))
#             elif obstacle_type == "large_cactus":
#                 self.obstacles.append(CactusLarge(LARGE_CACTUS))
#             elif obstacle_type == "bird":
#                 self.obstacles.clear()
#                 self.obstacles.append(Bird(BIRD))
#                 self.obstacles.append(Bird_02(BIRD))

#             if obstacle_type == "bird":
#                 self.step_index = 0
#                 self.images = obstacle.images
#                 self.image = self.obstacles[0] if self.step_index < 5 else self.obstacles[1] #ternary operator 
#                 self.step_index += 1        
#                 if self.step_index >= 10:
#                     self.step_index = 0

                
#         for obstacle in self.obstacles:
#             obstacle.update(game.game_speed, self.obstacles)
            
            
            
#             if game.player.dino_rect.colliderect(obstacle.rect):
#                 pygame.time.delay(500)
#                 game.playing = False
#                 break                
    
#     def draw(self, screen):
#         for obstacle in self.obstacles:
#             obstacle.draw(screen)

# class ObstacleManager:
#     def __init__(self):
#         self.obstacles = []
#         self.opcoes = ["small_cactus", "large_cactus", "bird"] # lista com opções para sorteio
#         self.frame_count = 0 # variável de contagem de frames
#         self.bird_type = Bird # tipo de pássaro atual
        
#     def update(self, game):
#         if len(self.obstacles) == 0:
#             if self.frame_count == 0: # escolhe um novo tipo de obstáculo a cada 5 frames
#                 obstacle_type = random.choice(self.opcoes)
#                 if obstacle_type == "small_cactus":
#                     self.obstacles.append(Cactus(SMALL_CACTUS))
#                 elif obstacle_type == "large_cactus":
#                     self.obstacles.append(CactusLarge(LARGE_CACTUS))
#                 elif obstacle_type == "bird":
#                     self.obstacles.append(self.bird_type(BIRD))
#                     self.frame_count = 0
                    
#                     if self.bird_type == Bird:
#                         self.bird_type = Bird_02
#                     else:
#                         self.bird_type = Bird
                        
#                 self.frame_count = 1
            
#             else:
#                 self.frame_count += 1
        
#         for obstacle in self.obstacles:
#             obstacle.update(game.game_speed, self.obstacles)
            
#             if game.player.dino_rect.colliderect(obstacle.rect):
#                 pygame.time.delay(500)
#                 game.playing = False
#                 break                
    
#     def draw(self, screen):
#         for obstacle in self.obstacles:
#             obstacle.draw(screen)


# import pygame
# import random

# from dino_runner.components.obstacles.cactus import Cactus 
# from dino_runner.components.obstacles.cactusLarge import CactusLarge
# from dino_runner.components.obstacles.bird import Bird
# from dino_runner.components.obstacles.bird import Bird_02

# from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

# class ObstacleManager:
#     def __init__(self):
#         self.obstacles = []
#         self.opcoes = ["small_cactus", "large_cactus", "bird"] #lista com opções para sorteio
    
#     def update(self, game):
#         if len(self.obstacles) == 0:
#             obstacle_type = random.choice(self.opcoes)
#             if obstacle_type == "small_cactus":
#                 self.obstacles.append(Cactus(SMALL_CACTUS))
#             elif obstacle_type == "large_cactus":
#                 self.obstacles.append(CactusLarge(LARGE_CACTUS))
#             elif obstacle_type == "bird":
#                 self.obstacles.append(Bird(BIRD))
#                 self.obstacles.append(Bird_02(BIRD))
    
        
#         for obstacle in self.obstacles:
#             obstacle.update(game.game_speed, self.obstacles)
        
#             if obstacle_type == "bird":
#                 self.step_index = 0
#                 self.image = obstacles[0] if self.step_index < 5 else obstacles[1] #ternary operator 
#                 self.step_index+=1        
#                 if self.step_index >= 10:
#                         self.step_index = 0
            
#             if game.player.dino_rect.colliderect(obstacle.rect):
#                 pygame.time.delay(500)
#                 game.playing = False
#                 break                
    
#     def draw(self, screen):
#         for obstacle in self.obstacles:
#             obstacle.draw(screen)

# import pygame
# import random

# from dino_runner.components.obstacles.cactus import Cactus 
# from dino_runner.components.obstacles.cactusLarge import CactusLarge
# from dino_runner.components.obstacles.bird import Bird
# from dino_runner.components.obstacles.bird import Bird_02

# from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

# class ObstacleManager:
#     def __init__(self):
#         self.obstacles = []
#         self.opcoes = ["small_cactus", "large_cactus", "bird"] #lista com opções para sorteio
#         self.frame_count = 0 # variável de contagem de frames
#         self.bird_type = Bird # tipo de pássaro atual
        
#     def update(self, game):
#         if len(self.obstacles) == 0:
#             if self.frame_count == 0: # escolhe um novo tipo de obstáculo a cada 5 frames
#                 obstacle_type = random.choice(self.opcoes)
#                 if obstacle_type == "small_cactus":
#                     self.obstacles.append(Cactus(SMALL_CACTUS))
#                 elif obstacle_type == "large_cactus":
#                     self.obstacles.append(CactusLarge(LARGE_CACTUS))
#                 elif obstacle_type == "bird":
#                     self.frame_count = 0
#                     while self.frame_count < 10:
#                         if self.bird_type == Bird:
#                             self.obstacles.append(Bird(BIRD))
#                             self.bird_type = Bird_02
#                         else:
#                             self.obstacles.append(Bird_02(BIRD))
#                             self.bird_type = Bird
#                         self.frame_count += 1
#                         pygame.time.delay(120)
                        
#         for obstacle in self.obstacles:
#             obstacle.update(game.game_speed, self.obstacles)
            
#             if game.player.dino_rect.colliderect(obstacle.rect):
#                 pygame.time.delay(500)
#                 game.playing = False
#                 break                
    
#     def draw(self, screen):
#         for obstacle in self.obstacles:
#             obstacle.draw(screen)


# import pygame
# import random

# from dino_runner.components.obstacles.cactus import Cactus 
# from dino_runner.components.obstacles.cactusLarge import CactusLarge
# from dino_runner.components.obstacles.bird import Bird
# from dino_runner.components.obstacles.bird import Bird_02

# from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

# class ObstacleManager:
#     def __init__(self):
#         self.obstacles = []
#         self.opcoes = ["small_cactus", "large_cactus", "bird"] #lista com opções para sorteio
#         self.frame_count = 0 # variável de contagem de frames
#         self.bird_type = Bird # tipo de pássaro atual
        
#     def update(self, game):
#         if len(self.obstacles) == 0:
#             if self.frame_count == 0: # escolhe um novo tipo de obstáculo a cada 5 frames
#                 obstacle_type = random.choice(self.opcoes)
#                 if obstacle_type == "small_cactus":
#                     self.obstacles.append(Cactus(SMALL_CACTUS))
#                 elif obstacle_type == "large_cactus":
#                     self.obstacles.append(CactusLarge(LARGE_CACTUS))
#                 elif obstacle_type == "bird":
#                     self.frame_count = 0
#                     while (self.frame_count < 10):
#                             self.obstacles.append(Bird(BIRD)) # alterna entre Bird e Bird_02
#                             self.frame_count += 1
#                             pygame.time.delay(120)
#                             self.obstacles.pop(Bird(BIRD))
#                             self.obstacles.append(Bird_02(BIRD))
#                             pygame.time.delay(120)
#                             self.frame_count += 1
#                             self.obstacles.pop(Bird_02(BIRD))

                        
                        
                
#         for obstacle in self.obstacles:
#             obstacle.update(game.game_speed, self.obstacles)
            
#             if game.player.dino_rect.colliderect(obstacle.rect):
#                 pygame.time.delay(500)
#                 game.playing = False
#                 break                
    
#     def draw(self, screen):
#         for obstacle in self.obstacles:
#             obstacle.draw(screen)

# import pygame
# import random


# from dino_runner.components.obstacles.cactus import Cactus 
# from dino_runner.components.obstacles.cactusLarge import CactusLarge
# from dino_runner.components.obstacles.bird import Bird
# from dino_runner.components.obstacles.bird import Bird_02

# from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

# class ObstacleManager:
#     def __init__(self):
#         self.obstacles = []
#         self.opcoes = [SMALL_CACTUS, LARGE_CACTUS, BIRD] #lista com opções para sorteio
#         self.step_index = 0
#         self.bird_timer = 0
#         self.bird_switch_time = 2  # tempo em segundos para alternar entre as opções de Bird
        
#     def update(self, game):
#         if len(self.obstacles) == 0:
#             obstacle_type = random.choice(self.opcoes)
#             if obstacle_type == SMALL_CACTUS:
#                 self.obstacles.append(Cactus(SMALL_CACTUS))
#             elif obstacle_type == LARGE_CACTUS:
#                 self.obstacles.append(CactusLarge(LARGE_CACTUS))
#             elif obstacle_type == BIRD:
#                 self.obstacles.append(Bird(BIRD))
#                 self.obstacles.append(Bird_02(BIRD))
        
#         # Verifica se já se passaram 2 segundos desde a última mudança de opção de Bird
#         self.bird_timer += game.dt
#         if self.bird_timer >= self.bird_switch_time:
#             self.bird_timer = 0
#             if self.obstacles[-1].type == BIRD:
#                 self.obstacles.pop()  # remove a última opção de Bird
#                 self.obstacles.append(Bird_02(BIRD))  # adiciona a outra opção de Bird
#             else:
#                 self.obstacles.pop()  # remove a última opção de Bird
#                 self.obstacles.append(Bird(BIRD))  # adiciona a outra opção de Bird
        
#         for obstacle in self.obstacles:
#             obstacle.update(game.game_speed, self.obstacles)
            
#             if game.player.dino_rect.colliderect(obstacle.rect):
#                 pygame.time.delay(500)
#                 game.playing = False
#                 break                
    
#     def draw(self, screen):
#         for obstacle in self.obstacles:
#             obstacle.draw(screen)


# import pygame
# import random

# from dino_runner.components.obstacles.cactus import Cactus 
# from dino_runner.components.obstacles.cactusLarge import CactusLarge
# from dino_runner.components.obstacles.bird import Bird
# from dino_runner.components.obstacles.bird import Bird_02

# from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

# class ObstacleManager:
#     def __init__(self):
#         self.obstacles = []
#         self.opcoes = [SMALL_CACTUS, LARGE_CACTUS, BIRD] #lista com opções para sorteio
#         self.step_index = 0
    
#     def update(self, game):
#         if len(self.obstacles) == 0:
#             obstacle_type = random.choice(self.opcoes)
#             if obstacle_type == SMALL_CACTUS:
#                 self.obstacles.append(Cactus(SMALL_CACTUS))
#             elif obstacle_type == LARGE_CACTUS:
#                 self.obstacles.append(CactusLarge(LARGE_CACTUS))
#             elif obstacle_type == BIRD:
#                 self.obstacles.append(Bird(BIRD))
#                 self.obstacles.append(Bird_02(BIRD))
        
#         for obstacle in self.obstacles:
#             obstacle.update(game.game_speed, self.obstacles)
            
            
#             if game.player.dino_rect.colliderect(obstacle.rect):
#                 pygame.time.delay(500)
#                 game.playing = False
#                 break                
    
#     def draw(self, screen):
#         for obstacle in self.obstacles:
#             obstacle.draw(screen)


# import pygame
# import random

# from dino_runner.components.obstacles.cactus import Cactus 
# from dino_runner.components.obstacles.cactusLarge import CactusLarge
# from dino_runner.components.obstacles.bird import Bird
# from dino_runner.components.obstacles.bird import Bird_02

# from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

# class ObstacleManager:
#     def __init__(self):
#         self.obstacles = []
#         self.opcoes = [SMALL_CACTUS, LARGE_CACTUS, BIRD] #lista com opções para sorteio
#         self.step_index = 0
    
#     def update(self, game):
#         if len(self.obstacles) == 0:
#             obstacle_type = random.choice(self.opcoes)
#             if obstacle_type == SMALL_CACTUS:
#                 self.obstacles.append(Cactus(SMALL_CACTUS))
#             elif obstacle_type == LARGE_CACTUS:
#                 self.obstacles.append(CactusLarge(LARGE_CACTUS))
#             elif obstacle_type == BIRD:
#                 self.obstacles.append(Bird(BIRD))
#                 self.obstacles.append(Bird_02(BIRD))
        
#         for obstacle in self.obstacles:
#             obstacle.update(game.game_speed, self.obstacles)
        
#             if obstacle_type == BIRD:
#                 obstacle = self.obstacles[0] 
#                 if self.step_index % 5 == 0 :
#                     self.obstacles[1]
#                 # obstacle = self.obstacles[self.step_index // 5] #corrigindo animação do Bird
#                 self.step_index += 1
#                 if self.step_index >= 10:
#                     self.step_index = 0
#                 obstacle.update(game.game_speed, self.obstacles)
            
#             if game.player.dino_rect.colliderect(obstacle.rect):
#                 pygame.time.delay(500)
#                 game.playing = False
#                 break                
    
#     def draw(self, screen):
#         for obstacle in self.obstacles:
#             obstacle.draw(screen)


# import pygame
# import random

# from dino_runner.components.obstacles.cactus import Cactus 
# from dino_runner.components.obstacles.cactusLarge import CactusLarge
# from dino_runner.components.obstacles.bird import Bird
# from dino_runner.components.obstacles.bird import Bird_02

# from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

# class ObstacleManager:
#     def __init__(self):
#         self.obstacles = []
#         self.opcoes = ["small_cactus", "large_cactus", "bird"] #lista com opções para sorteio
#         self.time_since_last_obstacle = 0 # variável de contagem de tempo desde o último obstáculo
#         self.bird_type = Bird # tipo de pássaro atual
        
#     def update(self, game, delta_time):
#         if len(self.obstacles) == 0:
#             self.time_since_last_obstacle += delta_time # atualiza o tempo desde o último obstáculo
#             if self.time_since_last_obstacle >= 5: # escolhe um novo tipo de obstáculo a cada 5 segundos
#                 obstacle_type = random.choice(self.opcoes)
#                 if obstacle_type == "small_cactus":
#                     self.obstacles.append(Cactus(SMALL_CACTUS))
#                 elif obstacle_type == "large_cactus":
#                     self.obstacles.append(CactusLarge(LARGE_CACTUS))
#                 elif obstacle_type == "bird":
#                     self.bird_type = random.choice([Bird, Bird_02]) # alterna entre Bird e Bird_02
#                     self.obstacles.append(self.bird_type(BIRD))
#                 self.time_since_last_obstacle = 0 # reinicia a contagem de tempo após escolher um novo obstáculo
                    
#         for obstacle in self.obstacles:
#             obstacle.update(game.game_speed, self.obstacles)
            
#             if game.player.dino_rect.colliderect(obstacle.rect):
#                 pygame.time.delay(500)
#                 game.playing = False
#                 break                
    
#     def draw(self, screen):
#         for obstacle in self.obstacles:
#             obstacle.draw(screen)



# import pygame
# import random

# from dino_runner.components.obstacles.cactus import Cactus 
# from dino_runner.components.obstacles.cactusLarge import CactusLarge
# from dino_runner.components.obstacles.bird import Bird
# from dino_runner.components.obstacles.bird import Bird_02

# from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

# class ObstacleManager:
#     def __init__(self):
#         self.obstacles = []
#         self.opcoes = ["small_cactus", "large_cactus", "bird"] #lista com opções para sorteio
#         self.frame_count = 0 # variável de contagem de frames
#         self.bird_type = Bird # tipo de pássaro atual
        
#     def update(self, game):
#         if len(self.obstacles) == 0:
#             if self.frame_count == 0: # escolhe um novo tipo de obstáculo a cada 5 frames
#                 obstacle_type = random.choice(self.opcoes)
#                 if obstacle_type == "small_cactus":
#                     self.obstacles.append(Cactus(SMALL_CACTUS))
#                 elif obstacle_type == "large_cactus":
#                     self.obstacles.append(CactusLarge(LARGE_CACTUS))
#                 elif obstacle_type == "bird":
#                     self.bird_type = random.choice([Bird, Bird_02]) # alterna entre Bird e Bird_02
#                     self.obstacles.append(self.bird_type(BIRD))
                    
#             self.frame_count += 1
#             if self.frame_count == 5:
#                 self.frame_count = 0
                
#         for obstacle in self.obstacles:
#             obstacle.update(game.game_speed, self.obstacles)
            
#             if game.player.dino_rect.colliderect(obstacle.rect):
#                 pygame.time.delay(500)
#                 game.playing = False
#                 break                
    
#     def draw(self, screen):
#         for obstacle in self.obstacles:
#             obstacle.draw(screen)



# import pygame
# import random

# from dino_runner.components.obstacles.cactus import Cactus 
# from dino_runner.components.obstacles.cactusLarge import CactusLarge
# from dino_runner.components.obstacles.bird import Bird
# from dino_runner.components.obstacles.bird import Bird_02

# from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

# class ObstacleManager:
#     def __init__(self):
#         self.obstacles = []
#         self.opcoes = ["small_cactus", "large_cactus", "bird"] #lista com opções para sorteio
    
#     def update(self, game):
#         if len(self.obstacles) == 0:
#             obstacle_type = random.choice(self.opcoes)
#             if obstacle_type == "small_cactus":
#                 self.obstacles.append(Cactus(SMALL_CACTUS))
#             elif obstacle_type == "large_cactus":
#                 self.obstacles.append(CactusLarge(LARGE_CACTUS))
#             elif obstacle_type == "bird":
#                 self.obstacles.append(Bird(BIRD))
#                 self.obstacles.append(Bird_02(BIRD))
    
        
#         for obstacle in self.obstacles:
#             obstacle.update(game.game_speed, self.obstacles)
        
#             if obstacle_type == "bird":
#                 self.step_index = 0
#                 self.image = obstacles[0] if self.step_index < 5 else obstacles[1] #ternary operator 
#                 self.step_index+=1        
#                 if self.step_index >= 10:
#                         self.step_index = 0
            
#             if game.player.dino_rect.colliderect(obstacle.rect):
#                 pygame.time.delay(500)
#                 game.playing = False
#                 break                
    
#     def draw(self, screen):
#         for obstacle in self.obstacles:
#             obstacle.draw(screen)

# class ObstacleManager:
#     def __init__(self):
#         self.obstacles = []
#         self.opcoes = ["small_cactus", "large_cactus", "bird"] #lista com opções para sorteio
    
#     def update(self, game):
#         if len(self.obstacles) == 0:
#             obstacle_type = random.choice(self.opcoes)
#             if obstacle_type == "small_cactus":
#                 self.obstacles.append(Cactus(SMALL_CACTUS))
#             elif obstacle_type == "large_cactus":
#                 self.obstacles.append(CactusLarge(LARGE_CACTUS))
#             elif obstacle_type == "bird":
#                 self.obstacles.append(Bird(BIRD))
#                 self.obstacles.append(Bird_02(BIRD))
                
        
#         for obstacle in self.obstacles:
#             obstacle.update(game.game_speed, self.obstacles)
            
#             if game.player.dino_rect.colliderect(obstacle.rect):
#                 pygame.time.delay(500)
#                 game.playing = False
#                 break                
    
#     def draw(self, screen):
#         for obstacle in self.obstacles:
#             obstacle.draw(screen)
