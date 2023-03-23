import random
import pygame
from dino_runner.utils.constants import APPLE, SHIELD_TYPE
from dino_runner.components.power_ups.power_up import PowerUp

class Apple(PowerUp):
    def __init__(self):
        super().__init__(APPLE, SHIELD_TYPE)

        