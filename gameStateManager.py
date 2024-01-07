import pygame

import sys

import eventHandler as eh

import ui

import random

def handleGameStates(game_settings, screen, screen_rect, hud_manager, assets, door1, door2, camera_system, power_system, enemies):
    if game_settings.night_ongoing == True:
        screen.blit(assets.office, (0,0))
        assets.office_ambience.set_volume(0.05)
        assets.office_ambience.play()

        # Checks whether the player has survived the entire night duration.
        if eh.checkSurvival(game_settings):
            game_settings.night_win = True
            game_settings.night_ongoing = False

        eh.checkBlitConditions(game_settings, screen, screen_rect, assets, door1, door2, camera_system, power_system, enemies)
        
        hud_manager.displayHUD(game_settings, screen, screen_rect, assets, power_system)
        
        pygame.display.flip()
        
    elif game_settings.night_win == True:
        assets.office_ambience.stop()
        screen.blit(assets.black_screen, (0, 0))
        screen.blit(assets.paycheck, assets.paycheck_rect)
            
        if not game_settings.audio_played:
            assets.night_end.play(0)
            assets.happy.set_volume(0.5)
            assets.happy.play(0)
            game_settings.audio_played = True
                
    elif game_settings.game_over == True:
        assets.office_ambience.stop()
        screen.blit(assets.black_screen, (0, 0))
        screen.blit(assets.game_over_screen, assets.game_over_screen_rect)
        screen.blit(assets.game_over_text, assets.game_over_text_rect)
            
        
    elif game_settings.blackout == True:
        assets.office_ambience.stop()
        screen.blit(assets.blackout_office[0], (0, 0))
        pygame.display.flip()
        
        flicker_start_time = pygame.time.get_ticks()
        flicker_duration = 14000
        flicker_interval = 40
        flicker_timer = flicker_start_time

        if not game_settings.audio_played:
            assets.power_out.set_volume(0.4)
            assets.power_out.play()
            pygame.time.delay(4000)
            assets.power_out.stop()
            game_settings.audio_played = True
            game_settings.dead = False

        while not game_settings.dead and flicker_timer - flicker_start_time < flicker_duration:
            current_time = pygame.time.get_ticks()
            assets.music_box.set_volume(0.1)
            assets.music_box.play(0)

            if current_time - flicker_start_time >= 4000:
                if current_time - flicker_timer >= flicker_interval:
                    flicker_timer = current_time
                    screen.blit(random.choice(assets.blackout_office), (0, 0))
                    pygame.display.flip()
                    
            if current_time - flicker_start_time >= flicker_duration:
                assets.music_box.stop()
                screen.blit(assets.black_screen, (0,0))
                pygame.display.flip()
                assets.lights_out.play()
                pygame.time.delay(250)
                assets.lights_out.stop()
                pygame.time.delay(random.randint(2500, 8000))

                screen.blit(assets.blackout_office_pre_jumpscare, (0, 0))

                assets.enemy_jumpscare.set_volume(0.1)
                assets.enemy_jumpscare.play(0)
                
                # For the jumpscare thing
                jumpscare_index = 0  # Variable to keep track of the current jumpscare frame
                jumpscare_delay = 30  # Delay between jumpscare frames

                while jumpscare_index < len(assets.blackout_jumpscare_animation):
                    screen.blit(assets.blackout_jumpscare_animation[jumpscare_index], assets.newspaper_rect)
                    pygame.display.flip()
                    pygame.time.delay(jumpscare_delay)
                    jumpscare_index += 1
                else:
                    game_settings.dead = True
                    game_settings.game_over = True