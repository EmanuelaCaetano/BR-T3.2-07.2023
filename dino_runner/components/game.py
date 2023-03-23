import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, HEART, APPLE
from dino_runner.utils.constants import FONT_STYLE, DEFAULT_TYPE, GAME_OVER, BOOM, FIRST, TRY_AGAIN
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.power_ups import power_up_manager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = -35
        self.score = 0

        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
    
    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        
        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()
    
    def reset_game(self):
        self.player = Dinosaur()
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
         
        self.game_speed = 20
        self.score = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)       
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.update_score()
        
    def update_score(self):
        self.score+=1
        if self.score%100 == 0:
            self.game_speed+=5

        self.new_score = self.score
        self.hank = self.score

        if self.new_score >= self.score:
             self.hank = self.score
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
    
        self.player.draw(self.screen)
        self.draw_score()
        self.draw_best_score()
        self.draw_power_up_time()
        self.draw_score_life()
        self.draw_score_life()
        
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        
        pygame.display.flip()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks())/1000, 2)
            
            if time_to_show >=0:
                font = pygame.font.Font(FONT_STYLE, 22)
                text = font.render(f"Power Up: {time_to_show}", True, (255,0,0))
                text_rect = text.get_rect()
                text_rect.x = 425
                text_rect.y = 100
                self.screen.blit(text, text_rect)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def draw_score_life(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"lifes: {power_up_manager.player_lives}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (100, 50)
        self.screen.blit(text, text_rect)
        
        self.x = 160
        
        for i in range(power_up_manager.player_lives):
            self.screen.blit(HEART, (self.x + (30 * i), 35))

        self.screen.blit(APPLE, (80,70))

        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"{self.power_up_manager.apple_score}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (270, 50)
        self.screen.blit(text, text_rect) 
                
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def draw_best_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Best Score: {self.hank}", True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 100)
        self.screen.blit(text, text_rect)
    
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
    def show_menu(self):
        self.screen.fill((255,255,255))
        
        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2
        
        if  power_up_manager.player_lives == 3:
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Press (S) to start playing", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height + 250)
            self.screen.blit(text, text_rect)
            self.screen.blit(FIRST, (half_screen_width-270, half_screen_height-300 ))
        elif power_up_manager.player_lives == 0:
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Press (r) to restart playing", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height + 260)
            self.screen.blit(text, text_rect)
            self.screen.blit(BOOM, (half_screen_width-270, half_screen_height-300 ))
            self.screen.blit(GAME_OVER, (350, half_screen_height + 200))
        else:
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Press (C) to continue playing", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (850, 500)
            self.screen.blit(text, text_rect)
            self.screen.blit(TRY_AGAIN, (half_screen_height, half_screen_height - 100))
            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render("Press (r) to restart play", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (250, 500)
            self.screen.blit(text, text_rect)

            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render(f"Best Score: {self.hank}", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (350, 150)
            self.screen.blit(text, text_rect)

            font = pygame.font.Font(FONT_STYLE, 22)
            text = font.render(f"Acctualy Score: {self.hank}", True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (670, 150)
            self.screen.blit(text, text_rect)
        
        pygame.display.update()
        
        self.handle_events_on_menu()
    
    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_s] and power_up_manager.player_lives == 3:
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_c] and power_up_manager.player_lives != 3:  #arrumar
                    self.obstacle_manager.obstacles.clear()
                    self.power_up_manager.apple_score = 0 #voce perde suas maças ao continuar o jogo
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_r]:
                    power_up_manager.player_lives = 3
                    self.run()

