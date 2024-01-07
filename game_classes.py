import pygame

class Door:
    def __init__(self, name, power_system):
        # Connects the doors system to the power system
        self.power_sys = power_system
        
        self.name = name
        self.is_open = True
        
    def openDoor(self):
        """Opens the door and decreases power level consumption."""
        self.is_open = True
        self.power_sys.drainLevelDown()
        
    def closeDoor(self):
        """Closes the door and increases power level consumption."""
        self.is_open = False
        self.power_sys.drainLevelUp()
    
    def toggleDoor(self, assets):
        """Toggles the state of the door between opened and closed."""
        pygame.mixer.Channel(4).play(assets.door_toggle)
        if self.is_open == True:
            self.closeDoor()
        else:
            self.openDoor()

class PowerSystem:
    def __init__(self):
        # The default state of the electricity/power in the building
        self.is_power_on = True
        
        # The amount of power the player starts with.
        self.total_power = 100
        
        # The current power of the building, starts at 100.
        self.current_power = self.total_power
        
        # Default level of power consumption 
        # Level increases by 1 for every utility used/removed
        self.power_consumption = 1 
    
    def drainPower(self):
        """Subtracts the power of the building based on level of power consumption"""
        self.current_power -= self.power_consumption
    
    def drainLevelUp(self):
        """Increases the amount of power drained"""
        self.power_consumption += 1
        
    def drainLevelDown(self):
        """Decreases the amount of power drained"""
        self.power_consumption -= 1
          

class Camera:
    def __init__(self, camera_id):
        self.camera_id = camera_id
        self.isMonitored = False
        self.enemies = []
        
    def addEnemy(self, enemy):
        """Adds an enemy to the camera's list."""
        self.enemies.append(enemy) 
        
    def removeEnemy(self, enemy):
        """Remove an enemy from the camera's list."""
        if enemy in self.enemies:
            self.enemies.remove(enemy)

    def __str__(self):
        return f"Camera {self.camera_id} - Monitored: {self.isMonitored}"

class CameraSystem:
    def __init__(self, power_system, cameras=None, enemies=None):
        # State which determines whether the user is using the camera or not
        self.camera_active = False
        
        # Connects the camera system to the power system
        self.power_sys = power_system
        
        #List of accesible cameras
        self.camera_list = cameras if cameras else []
        
        # Keeps track of last viewed camera
        self.last_viewed_camera = None

        # Tracks Currently Monitored camera
        self.current_cam = None
        
        # Assign the list of enemies to each camera
        for camera in self.camera_list:
            camera.enemies = enemies if enemies else []
        
    # Function which is used when user uses the camera
    def cameraOn(self, assets):
        """Activates the cameras"""
        self.camera_active = True
        self.power_sys.drainLevelUp()
        pygame.mixer.Channel(5).play(assets.camera_on)
    
    # Function for when users put the camera
    def cameraOff(self, assets):
        """Deactivates the cameras"""
        self.camera_active = False
        self.power_sys.drainLevelDown()
        pygame.mixer.Channel(5).stop()
        pygame.mixer.Channel(5).play(assets.camera_off)

    def toggleCamera(self, assets):
        if not self.camera_active:
            self.cameraOn(assets)

            # If the camera system is opened for the first time, view the first camera in the list
            if self.last_viewed_camera is None and self.camera_list:
                first_camera = self.camera_list[0]
                first_camera.isMonitored = True
                self.last_viewed_camera = first_camera
            
            else:
                current_cam = self.last_viewed_camera
                current_cam.isMonitored = True

        else:
            # When turning off the camera system, set all cameras' monitored state to False
            for camera in self.camera_list:
                camera.isMonitored = False

            self.cameraOff(assets)
            
    def addCamera(self, camera_id):
        new_camera = Camera(camera_id)
        self.camera_list.append(new_camera)
        
    def viewCamera(self, camera_id, assets):
        if not self.camera_active:
            return

        for camera in self.camera_list:
            if camera.camera_id == camera_id:
                camera.isMonitored = True
                self.current_cam = camera
                pygame.mixer.Channel(6).play(assets.camera_switch)
                
            else:
                camera.isMonitored = False

        if self.current_cam:
            self.last_viewed_camera = self.current_cam
            
    def setupCameras(self):
        self.addCamera("1a")
        self.addCamera("1b")
        self.addCamera("2a")
        self.addCamera("2b")
        self.addCamera("3")
        self.addCamera("4a")
        self.addCamera("4b")
        self.addCamera("5")

    def updateEnemyCameraAssociation(self, enemy):
        """Update the association of an enemy with cameras based on its currentPos."""
        for camera in self.camera_list:
            if enemy.currentPos == camera.camera_id:
                camera.addEnemy(enemy)
            else:
                camera.removeEnemy(enemy)