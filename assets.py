import pygame

class Assets:
    """Class for imported assets"""
    def __init__(self, game_settings, screen_rect):
        Assets.images(self, game_settings, screen_rect)
        
        Assets.audio(self)
        
        print("Assets loaded!")
    
    def images(self, game_settings, screen_rect):
        """Imports images from the assets folder"""
                
        # Black screen
        self.black_screen = pygame.Surface((game_settings.screen_width, game_settings.screen_height))
        self.black_screen.fill((0, 0, 0))
        
        # Office Room
        # Office
        self.office = pygame.image.load("assets/images/office/office.png").convert()
        
        # Blackout office
        self.blackout_office = []
        
        for i in range(2):
            self.blackout_office.append(
                pygame.image.load(f"assets/images/office/blackout/{i+1}.png").convert()
                )
            
        # Blackout office - Pre-jumpscare
        self.blackout_office_pre_jumpscare = pygame.image.load(f"assets/images/office/blackout/3.png").convert()
        
        #Right door closed
        self.right_door_closed = pygame.image.load(f"assets/images/office/right_door/1.png").convert_alpha()
        self.right_door_closed_rect = self.right_door_closed.get_rect(topright=screen_rect.topright)
        
        #Left door closed
        self.left_door_closed = pygame.image.load(f"assets/images/office/left_door/1.png").convert_alpha()

        # Right door enemy
        self.right_door_enemy = pygame.image.load(f"assets/images/office/right_door/2.png").convert_alpha()
        self.right_door_enemy_rect = self.right_door_enemy.get_rect(topright=self.right_door_closed_rect.topleft)
        
        # Left door enemy
        self.left_door_enemy = pygame.image.load(f"assets/images/office/left_door/2.png").convert_alpha()
                
        # Cameras
        self.camera_recording = pygame.image.load("assets/images/cameras/utils/1.png").convert_alpha()
        self.camera_recording_rect = self.camera_recording.get_rect(topleft=screen_rect.topleft)
        
        self.camera_recording_rect.x += game_settings.ASSETS_MARGIN * 3
        self.camera_recording_rect.y += game_settings.ASSETS_MARGIN * 3
        
        # Camera For Rooms
        # # Main Stage
        self.show_stage_camera = []
        
        for i in range(4):
            self.show_stage_camera.append(
                pygame.image.load(f"assets/images/cameras/locations/MainStage/{i}.png").convert()
                )
            
        self.show_stage_label = pygame.image.load(f"assets/images/cameras/locations/MainStage/label.png").convert_alpha()
        self.map_rect = self.show_stage_label.get_rect(bottomright=screen_rect.bottomright)
        
        self.map_rect.x -= game_settings.ASSETS_MARGIN * 5
        self.map_rect.y -= game_settings.ASSETS_MARGIN * 2
    
        # Dining Area
        self.dining_area_camera = []
        
        for i in range(4):
            self.dining_area_camera.append(
                pygame.image.load(f"assets/images/cameras/locations/DiningArea/{i}.png").convert()
                )
            
        self.dining_area_label = pygame.image.load(f"assets/images/cameras/locations/DiningArea/label.png").convert_alpha()
        
        # West Hall
        self.west_hall_camera = []
        
        for i in range(2):
            self.west_hall_camera.append(
                pygame.image.load(f"assets/images/cameras/locations/WestHall/{i}.png").convert()
                )
            
            self.west_hall_label = pygame.image.load(f"assets/images/cameras/locations/WestHall/label.png").convert_alpha()
            
        # West Corner
        self.west_corner_camera = []
        for i in range(2):
            self.west_corner_camera.append(
                pygame.image.load(f"assets/images/cameras/locations/WestCorner/{i}.png").convert()
            )
            
        self.west_corner_label = pygame.image.load(f"assets/images/cameras/locations/WestCorner/label.png").convert_alpha()
        
        # Backstage
        self.backstage_camera = []
            
        for i in range(2):
            self.backstage_camera.append(
                pygame.image.load(f"assets/images/cameras/locations/Backstage/{i}.png").convert()
            )
            
        self.backstage_label = pygame.image.load(f"assets/images/cameras/locations/Backstage/label.png").convert_alpha()
        
        # East Hall
        self.east_hall_camera = []
        
        for i in range(2):
            self.east_hall_camera.append(
                pygame.image.load(f"assets/images/cameras/locations/EastHall/{i}.png").convert()
            )
        
        self.east_hall_label = pygame.image.load(f"assets/images/cameras/locations/EastHall/label.png").convert_alpha()
        
        # East Corner
        self.east_corner_camera = []
        
        for i in range(2):
            self.east_corner_camera.append(
                pygame.image.load(f"assets/images/cameras/locations/EastCorner/{i}.png").convert()
            )
            
        self.east_corner_label = pygame.image.load(f"assets/images/cameras/locations/EastCorner/label.png").convert_alpha()
        
        # Restroom
        self.restroom_camera = []
        
        for i in range(2):
            self.restroom_camera.append(
                pygame.image.load(f"assets/images/cameras/locations/Restroom/{i}.png").convert()
            )
            
        self.restroom_label = pygame.image.load(f"assets/images/cameras/locations/Restroom/label.png").convert_alpha()
        
        # Interface
        # Power Usage
        self.power_usage_levels = []
        
        for i in range(4):
            self.power_usage_levels.append(
                pygame.image.load(f"assets/images/power/usage_bar/{i}.png").convert_alpha()
            )
                    
        # Jumpscares
        # Bonnie Jumpscare Animation
        self.bonnie_jumpscare_animation = []
        
        for i in range(11):
            self.bonnie_jumpscare_animation.append(
                pygame.image.load(f"assets/images/jumpscares/bonnie/{i+1}.png").convert_alpha()
            )
            
        # Chica Jumpscare Animation
        self.chica_jumpscare_animation = []
        
        for i in range(16):
            self.chica_jumpscare_animation.append(
                pygame.image.load(f"assets/images/jumpscares/chica/{i+1}.png").convert_alpha()
            )
        
        # Freddy Blackout Jumpscare Animation
        self.blackout_jumpscare_animation = []
        
        for i in range(20):
            self.blackout_jumpscare_animation.append(
                pygame.image.load(f"assets/images/jumpscares/blackout/{i+1}.png").convert_alpha()
            )
        
        # Menus
        self.paycheck = pygame.image.load("assets/images/menu/screens/2.png").convert()
        self.paycheck_rect = self.paycheck.get_rect(center=screen_rect.center)
        

        # Game Over
        self.game_over_screen = pygame.image.load(f"assets/images/menu/nights/2.png").convert()
        self.game_over_screen_rect = self.game_over_screen.get_rect(center= screen_rect.center)
        self.game_over_text = pygame.image.load(f"assets/images/menu/nights/3.png").convert_alpha()
        self.game_over_text_rect = self.game_over_text.get_rect(bottomleft=self.game_over_screen_rect.bottomleft)
        self.game_over_text_rect.x += game_settings.ASSETS_MARGIN * 2
        self.game_over_text_rect.y -= game_settings.ASSETS_MARGIN * 2
    
    def audio(self):
        # Office Ambience
        self.office_ambience = pygame.mixer.Sound("assets/audio/buzzing_ambience.wav")
        
        # Camera sounds
        self.camera_switch = pygame.mixer.Sound("assets/audio/camera_switch.wav")
        self.camera_on =  pygame.mixer.Sound("assets/audio/camera_on.wav")
        self.camera_off =  pygame.mixer.Sound("assets/audio/camera_off.wav")
        
        # Door sounds
        self.door_toggle = pygame.mixer.Sound("assets/audio/door_toggle.wav")
        
        # Enemy sounds
        self.enemy_steps = pygame.mixer.Sound("assets/audio/enemy_steps.wav")
        self.windowscare = pygame.mixer.Sound("assets/audio/windowscare.wav")
        self.enemy_jumpscare = pygame.mixer.Sound("assets/audio/jumpscare.wav")
        self.enemy_gasp = pygame.mixer.Sound("assets/audio/enemy_gasp.wav")
        
        # Game state sounds
        self.night_end = pygame.mixer.Sound("assets/audio/6AM_chimes.wav")
        self.happy = pygame.mixer.Sound("assets/audio/yay.wav")
        self.power_out = pygame.mixer.Sound("assets/audio/powerdown.wav")
        self.lights_out = pygame.mixer.Sound("assets/audio/lights_out.wav")
        self.music_box = pygame.mixer.Sound("assets/audio/blackout_music.wav")
