import pygame

import sys

def __checkKeypress(game_settings, event, door1, door2, camera_system, power_system, assets):
    """Checks for key press events."""
    if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
    if game_settings.night_ongoing:
        if event.key == pygame.K_a:
            door1.toggleDoor(assets)
        elif event.key == pygame.K_d:
            door2.toggleDoor(assets)
        elif event.key == pygame.K_s:
            camera_system.toggleCamera(assets)
        elif event.key == pygame.K_1:
            camera_system.viewCamera("1a", assets)
        elif event.key == pygame.K_2:
            camera_system.viewCamera("1b", assets)
        elif event.key == pygame.K_3:
            camera_system.viewCamera("2a", assets)
        elif event.key == pygame.K_4:
            camera_system.viewCamera("2b", assets)
        elif event.key == pygame.K_5:
            camera_system.viewCamera("3", assets)
        elif event.key == pygame.K_6:
            camera_system.viewCamera("4a", assets)
        elif event.key == pygame.K_7:
            camera_system.viewCamera("4b", assets)
        elif event.key == pygame.K_8:
            camera_system.viewCamera("5", assets)
        elif event.key == pygame.K_RETURN:
            game_settings.night_ongoing == True
        
def checkEvents(game_settings, screen, assets, door1, door2, camera_system, power_system, enemies):
    """Makes it so that the game will respond to user input/keypresses"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            __checkKeypress(game_settings, event, door1, door2, camera_system, power_system, assets)
        if game_settings.night_ongoing:
            if event.type == game_settings.DRAIN_POWER_EVENT:
                power_system.drainPower()
            for enemy in enemies:
                if event.type == enemy.movement_event:
                    enemy.movementOpportunity(game_settings, screen, camera_system, assets)
            if event.type == game_settings.ONE_HOUR_EVENT:
                game_settings.hour_counter += 1
                for enemy in enemies:
                    enemy.difficultyUp()
            if power_system.current_power <= 0:
                game_settings.night_ongoing = False
                game_settings.blackout = True

    
    game_settings.current_time = pygame.time.get_ticks()

def checkBlitConditions(game_settings, screen, screen_rect, assets, door1, door2, camera_system, power_system, enemies=list()):
    if door1.is_open == False:
        screen.blit(assets.left_door_closed, screen_rect.topleft)
    if door1.is_open == True and enemies[0].getCurrentRoomIndex() == len(enemies[0].movement_Pattern) - 2:
        screen.blit(assets.left_door_enemy, screen_rect.topleft)
    if enemies[1].getCurrentRoomIndex() == len(enemies[0].movement_Pattern) - 2:
        screen.blit(assets.right_door_enemy, assets.right_door_enemy_rect)
    if door2.is_open == False:
        screen.blit(assets.right_door_closed, assets.right_door_closed_rect)
    if camera_system.camera_active == True:
        cameraBlitConditions(screen, screen_rect, assets, camera_system, enemies)

def cameraBlitConditions(screen, screen_rect, assets, camera_system, enemies=list()):
    for camera in camera_system.camera_list:
        if camera.isMonitored:
            camera_id = camera.camera_id
            if camera_id == "1a":
                if len(camera.enemies) == 1:
                    if camera.enemies[0] == enemies[0]:
                        screen.blit(assets.show_stage_camera[2], (0,0))
                    elif camera.enemies[0] == enemies[1]:
                        screen.blit(assets.show_stage_camera[1], (0,0))
                elif len(camera.enemies) == 2:
                    screen.blit(assets.show_stage_camera[0], (0,0))
                else:
                    screen.blit(assets.show_stage_camera[3], (0,0))
                screen.blit(assets.show_stage_label, assets.map_rect)
            if camera_id == "1b":
                if len(camera.enemies) == 1:
                    if camera.enemies[0] == enemies[0]:
                        screen.blit(assets.dining_area_camera[1], (0,0))
                    elif camera.enemies[0] == enemies[1]:
                        screen.blit(assets.dining_area_camera[2], (0,0))
                elif len(camera.enemies) == 2:
                    screen.blit(assets.dining_area_camera[3], (0,0))
                else:
                    screen.blit(assets.dining_area_camera[0], (0,0))
                screen.blit(assets.dining_area_label, assets.map_rect)
            if camera_id == "2a":
                if len(camera.enemies) == 1:
                    screen.blit(assets.west_hall_camera[1], (0,0))
                else:
                    screen.blit(assets.west_hall_camera[0], (0,0))
                screen.blit(assets.west_hall_label,  assets.map_rect)
            if camera_id == "2b":
                if len(camera.enemies) == 1:
                    screen.blit(assets.west_corner_camera[1], (0,0))
                else:
                    screen.blit(assets.west_corner_camera[0], (0,0))
                screen.blit(assets.west_corner_label, assets.map_rect)
            if camera_id == "3":
                if len(camera.enemies) == 1:
                    screen.blit(assets.backstage_camera[1], (0,0))
                else:
                    screen.blit(assets.backstage_camera[0], (0,0))    
                screen.blit(assets.backstage_label, assets.map_rect)        
            if camera_id == "4a":
                if len(camera.enemies) == 1:
                    screen.blit(assets.east_hall_camera[1], (0,0))
                else:
                    screen.blit(assets.east_hall_camera[0], (0,0))
                screen.blit(assets.east_hall_label, assets.map_rect)       
            if camera_id == "4b":
                if len(camera.enemies) == 1:
                    screen.blit(assets.east_corner_camera[1], (0,0))
                else:
                    screen.blit(assets.east_corner_camera[0], (0,0))
                screen.blit(assets.east_corner_label, assets.map_rect)
            if camera_id == "5":
                if len(camera.enemies) == 1:
                    screen.blit(assets.restroom_camera[1], (0,0))
                else:
                    screen.blit(assets.restroom_camera[0], (0,0))
                screen.blit(assets.restroom_label, assets.map_rect)
            screen.blit(assets.camera_recording, assets.camera_recording_rect)
            
def checkSurvival(game_settings):
    """Check if the player survived the night"""
    if game_settings.hour_counter >= game_settings.hours_win_condition:
        return True  # Change the game state to the win state
    return False