import pygame
import os

class HUD:
    def __init__(self, game_settings):
        font_size = game_settings.font_size
        font_path = os.path.abspath(os.path.join("assets", "font", "fnaf.ttf"))

        # Use a built-in font for simplicity
        self.font = pygame.font.Font(font_path, font_size)

    def displayTime(self, game_settings, screen, screen_rect):

        hours = game_settings.hour_counter
        
        if hours == 0:
            hours = 12

        time_text = f"{hours} AM"
        text_surface = self.font.render(time_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(topright=screen_rect.topright)
        text_rect.x -= game_settings.ASSETS_MARGIN * 2
        text_rect.y += game_settings.ASSETS_MARGIN * 2

        screen.blit(text_surface, text_rect)
            
    def displayPower(self, game_settings, screen, screen_rect, assets, power_system):
        
        usage_text = f"Power Usage: "
        usage_surface = self.font.render(usage_text, True, (255, 255, 255))
        usage_rect = usage_surface.get_rect(bottomleft=screen_rect.bottomleft)
        usage_rect.x += game_settings.ASSETS_MARGIN * 2
        usage_rect.y -= game_settings.ASSETS_MARGIN * 2
        
        
        power_usage_rect = assets.power_usage_levels[0].get_rect(bottomleft = usage_rect.bottomright)
        
        if power_system.power_consumption == 1:
            screen.blit(assets.power_usage_levels[0], power_usage_rect)
        elif power_system.power_consumption == 2:
            screen.blit(assets.power_usage_levels[1], power_usage_rect)
        elif power_system.power_consumption == 3:
            screen.blit(assets.power_usage_levels[2], power_usage_rect)
        elif power_system.power_consumption == 4:
            screen.blit(assets.power_usage_levels[3], power_usage_rect)
        
        power_text = f"Power Left: {power_system.current_power}%"
        power_surface = self.font.render(power_text, True, (255, 255, 255))
        power_rect = power_surface.get_rect(bottomleft=usage_rect.topleft)
        power_rect.y -= game_settings.ASSETS_MARGIN
                
        screen.blit(power_surface, power_rect)
        screen.blit(usage_surface, usage_rect)
        
    def displayHUD(self, game_settings, screen, screen_rect, assets, power_system):
        self.displayTime(game_settings, screen, screen_rect)
        self.displayPower(game_settings, screen, screen_rect, assets, power_system)