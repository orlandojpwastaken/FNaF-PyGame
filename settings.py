import pygame

class Settings():
    """A class storing all the settings for the game"""
    
    def __init__(self):
        """Initialize the game's settings"""
        # Game states:
        self.night_ongoing = True
        self.night_win = False
        self.dead = False
        self.blackout = False
        self.game_over = False
           
        # Screen-related settings
        self.screen_width = 1600      
        self.screen_height = 720
        self.background_color = (255, 0, 0)
        
        # Timers
        # The duration for one in-game hour (in milliseconds)
        self.HOUR_DURATION = 60 * 1000
        
        # How much time has passed
        self.hour_counter = 0
        
        # Win Condition
        self.hours_win_condition = 6

        # Sets a hour one event to update the timer as well as increase the AI level
        self.ONE_HOUR_EVENT = pygame.USEREVENT + 7
        pygame.time.set_timer(self.ONE_HOUR_EVENT, self.HOUR_DURATION)

        # The duration between each tick of power drain (5 seconds in milliseconds)
        self.POWER_DRAIN_INTERVAL = 7000
    
        # Drains power every 5 seconds
        self.DRAIN_POWER_EVENT = pygame.USEREVENT + 8
        pygame.time.set_timer(self.DRAIN_POWER_EVENT, self.POWER_DRAIN_INTERVAL)
        
        # Added property because audio won't stop looping.
        self.audio_played = False
        
        # Font size
        self.font_size = 18
        
        # Asset Margin
        self.ASSETS_MARGIN = 20
        