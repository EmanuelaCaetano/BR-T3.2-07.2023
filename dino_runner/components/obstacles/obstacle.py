from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Obstacle:
    def __init__(self, images, type):
        self.image = images[type]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.set_y_pos(SCREEN_HEIGHT)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def set_y_pos(self, y):
        self.rect.y = y


        