import pygame
import os

pygame.init()
# Initialize pygame sounds and audio module
pygame.mixer.init()

class SoundManager:
    def __init__(self):
        self.sounds = {}
        self.sounds_enabled = True
    
    def play(self, name):
        """Play the sounds by its name if sounds are enabled"""
        if name in self.sounds and self.sounds_enabled:
            self.sounds[name].play()

    def load_sound(self, name, file_path):
        """Load sound file and store it with a name"""
        try:
            self.sounds[name] = pygame.mixer.Sound(file_path)
            return True
        except pygame.error as e:
            print(f"Error loading sounds from: {file_path}. Error: {e}")
            return False

    def set_volume(self, name, volume):
        """Set volume from 0.0 to 1.0"""
        if name in self.sounds:
            self.sounds[name].set_volume(volume)

    def toggle_sound(self):
        """Toggle sounds on / off"""
        self.sounds_enabled = not self.sounds_enabled
        return "Sound: On" if self.sounds_enabled else "Sound: Off"

    def stop_all(self):
        """Stop of all sounds"""
        pygame.mixer.stop()

# create instance to import
sound_manager = SoundManager()

# Define Sounds
"""get the parent directory name and ensure it reaches the parent directory"""
PARENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
print(f"Parent project: {PARENT_DIR}")
BUTTON_SOUND_DIR = os.path.join(PARENT_DIR, "Sounds", "Clicking")
#GAME_OBJECTS_SOUND_DIR


def load_game_sounds():
    sounds = {
        "button_click": os.path.join(BUTTON_SOUND_DIR, "button_click.wav"),
        "button_hover": os.path.join(BUTTON_SOUND_DIR, "button_hover.wav"),
        "back_button_click": os.path.join(BUTTON_SOUND_DIR, "back_button_click.wav")
    }

    for name, path in sounds.items():
        print(f"Loading sounds: {path}")
        if os.path.exists(path):
            print(f"{path} exists")
            if sound_manager.load_sound(name, path):
                print(f"Sounds {name} loaded: True")
            else:
                print(f"Sounds {name} loaded: False")
        else:
            print(f"{path} does not exist")
        



