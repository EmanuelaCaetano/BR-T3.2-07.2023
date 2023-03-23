import random
import pygame
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.apple import Apple

player_lives = 3

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(200, 300)
        self.apple_score = 0
    
    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200,300)
            power_up = random.choice([Shield(), Apple()])
            self.power_ups.append(power_up)
            
    def update(self, game):
        self.generate_power_up(game.score)
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            
            self.player = game.player
            if self.player.dino_rect.colliderect(power_up.rect):
                if isinstance(power_up, Shield):
                    self.player.shield = True
                    self.player.has_power_up = True
                    self.player.type = power_up.type #tipo de image que estaria utilizando
                    power_up.start_time = pygame.time.get_ticks()
                    self.player.power_up_time_up = power_up.start_time + (power_up.duration * 1000)
                    self.power_ups.remove(power_up)
                else:
                    if power_up.update(game.game_speed, self.power_ups):
                        self.apple_score += 1
                        player_lives += 1
                        # if self.apple_score % 10 == 0: ---> deveria ser 10 para juntar uma vida
                        #     player_lives += 1
                
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups.clear()
        self.when_appears = random.randint(200, 300)





