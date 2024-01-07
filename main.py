import pygame

from pygame import mixer

import sys

import os

from game_classes import *

from enemy import Enemy

from settings import Settings

import eventHandler as eh

from assets import Assets

import gameStateManager as states

from ui import HUD

def run_game():
    pygame.init()
    mixer.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    screen_rect = screen.get_rect()
    pygame.display.set_caption("Just One Night at Freddy Fazbear's")
    
    clock = pygame.time.Clock()
    
    # Loads related assets
    assets = Assets(game_settings, screen_rect)
    hud_manager = HUD(game_settings)
    
    # Create instances of the classes
    power_system = PowerSystem()
    door1 = Door("Left Door", power_system)
    door2 = Door("Right Door", power_system)
    camera_system = CameraSystem(power_system)
    bonnie = Enemy("Bonnie", door1, 10, 1, assets.bonnie_jumpscare_animation, ["1a", "1b", "3", "2a", "2b", "left", "office"], 5000)
    chica = Enemy("Chica", door2, 10, 1, assets.chica_jumpscare_animation, ["1a", "1b", "5", "4a", "4b", "right", "office"], 4000)
    enemies = [bonnie, chica]
    camera_system.setupCameras()
    
    camera_system.camera_list[0].addEnemy(bonnie)
    camera_system.camera_list[0].addEnemy(chica)

    running = True
    while running:

        eh.checkEvents(game_settings, screen, assets, door1, door2, camera_system, power_system, enemies)
        
        states.handleGameStates(game_settings, screen, screen_rect, hud_manager, assets, door1, door2, camera_system, power_system, enemies)
        
        pygame.display.flip()
        
        clock.tick(60)

if __name__ == '__main__':
    run_game()