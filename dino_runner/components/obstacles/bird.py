
import random

from dino_runner.components.obstacles.obstacle import Obstacle



class Bird(Obstacle):
    def __init__(self, images):
        self.type = 0
        super().__init__(images, self.type)
        
        self.rect.y = 270

class Bird_02(Obstacle):
    def __init__(self, images):
        self.type = 1
        super().__init__(images, self.type)
        
        self.rect.y = 270

        


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