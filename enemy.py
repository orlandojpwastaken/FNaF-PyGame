import pygame
from random import randint

class Enemy:
    # Initializes the Enemies class 
    def __init__(self, enemyName, assigned_door, ai_Level= 0, ai_Increase = 1, jumpscare_animation=list() ,movement_Pattern=list(), movement_Interval=0):
        self.name = enemyName
        
        # Assigns a door to a enemy
        self.assigned_door = assigned_door
        
        # Initial AI difficulty level, increases as time goes on.
        self.ai_Level = ai_Level
        
        # Current AI level
        self.current_ai_Level = self.ai_Level
         
        # Increment value added to the AI level as time progresses.
        self.ai_Increase = ai_Increase
        
        # Jumpscare Animation
        self.jumpscare_animation = jumpscare_animation
        self.jumpscare_index = 0
        
        # List of rooms which the enemy traverses
        self.movement_Pattern = movement_Pattern
        
        # Interval between movement opportunities
        self.moveOpp_Interval = movement_Interval
        
        # Sets the starting position of the enemy
        self.startPos = "1a"
        
        # Tracks current position of the enemy
        self.currentPos = "1a"
        
        # Stores generated movement opportunity number
        self.opportunity_value = 0
        
        # Assigns a unique countdown timer for movement opportunity
        self.movement_event = pygame.USEREVENT + randint(1, 5) 
        pygame.time.set_timer(self.movement_event, self.moveOpp_Interval)

    # Function to be executed every movement opportunity
    def __generateMoveOpp(self):
        """Generates a random integer value which will be used as to determine whether enemies will move forward or not."""
        self.opportunity_value = randint(1, 20)
        print(f"{self.name} = {self.opportunity_value}")
        # print(self.opportunity_value)
        
    def movementOpportunity(self, game_settings, screen, camera_system, assets):
        """Commences the movement opportunity"""
        self.__generateMoveOpp() # Generates the movement opportunity value
        if  self.current_ai_Level >= self.opportunity_value:
            room_index = self.getCurrentRoomIndex()
            
            # If enemy is in anywhere before the second from last item of their movement pattern list
            if room_index < len(self.movement_Pattern) - 2: 
                self.__roomAdvance(room_index, assets)
                
            # If enemy is in the second from last item of their movement pattern list   
            elif room_index == len(self.movement_Pattern) - 2:
                # If the door is open, advance.
                if self.assigned_door.is_open:
                    self.__roomAdvance(room_index, assets)
                    assets.enemy_gasp.set_volume(0.5)
                    pygame.mixer.Channel(1).play(assets.enemy_gasp)
                # If the door is closed, go back to the enemy's starting position.
                else: 
                    self.__returnToStart(assets)
            
            # If enemy is in the last item of their movement pattern list
            elif room_index == len(self.movement_Pattern) - 1:
                self.__killsYou(game_settings, screen, assets)
            self.__updateCameraAssociation(camera_system)
    
    def getCurrentRoomIndex(self):
        """Gets the index of the room the enemy is in in order to move them forward up the list upon movement"""
        room_index = self.movement_Pattern.index(self.currentPos)
        return room_index
    
    def __roomAdvance(self, room_index, assets):
        """Moves the enemy to the next room in their movement pattern list"""
        self.currentPos = self.movement_Pattern[room_index +1]
        if self.currentPos == len(self.movement_Pattern) - 1:
            pygame.mixer.Channel(2).play(assets.windowscare, 0)
        else:
            pygame.mixer.Channel(2).play(assets.enemy_steps)
        
    def __killsYou(self, game_settings, screen, assets):
        """Placeholder method for when the animatronic kills"""
        assets.enemy_jumpscare.set_volume(0.1)
        pygame.mixer.Channel(3).play(assets.enemy_jumpscare)
        for _ in range(4):
            self.jumpscare_index = 0  # Reset jumpscare index for each repetition
            while self.jumpscare_index < len(self.jumpscare_animation):
                screen.blit(self.jumpscare_animation[self.jumpscare_index], (0, 0))
                pygame.display.flip()
                pygame.time.delay(30)
                self.jumpscare_index += 1

        game_settings.night_ongoing = False
        game_settings.game_over = True
        
    def __returnToStart(self, assets):
        """Sets the enemies's current position back to its starting position"""
        self.currentPos = self.movement_Pattern[0]
        pygame.mixer.Channel(2).play(assets.enemy_steps)
        
    def difficultyUp(self):
        """Increases the AI level of the Enemy by the AI Increase Level"""
        self.current_ai_Level += self.ai_Increase
        
    def __updateCameraAssociation(self, camera_system):
        """Update the association of the enemy with cameras based on current position."""
        camera_system.updateEnemyCameraAssociation(self)

            
