
class MultimediaDevice:
    def __init__(self, name):
        self.name = name
        self.powered_on = False
        self.volume = 50

    def power_on(self):
        self.powered_on = True

    def power_off(self):
        self.powered_on = False

    def increase_volume(self):
        if self.powered_on:
            self.volume += 10
            if self.volume > 100:
                self.volume = 100

    def decrease_volume(self):
        if self.powered_on:
            self.volume -= 10
            if self.volume < 0:
                self.volume = 0


class TV(MultimediaDevice):
    def __init__(self, name, screen_size):
        super().__init__(name)
        self.screen_size = screen_size
        self.channels = []

    def add_channel(self, channel_name):
        self.channels.append(channel_name)

    def change_channel(self, channel_name):
        if self.powered_on and channel_name in self.channels:
            print(f"Changing channel to {channel_name}")
        else:
            print("TV is either off or the channel doesn't exist.")


class SoundSystem(MultimediaDevice):
    def __init__(self, name):
        super().__init__(name)
        self.equalizer = "Default"

    def set_equalizer(self, equalizer):
        self.equalizer = equalizer

    def play_music(self, song):
        if self.powered_on:
            print(f"Playing {song} with {self.equalizer} equalizer")


tv = TV("Living Room TV", "55-inch")
tv.add_channel("News")
tv.add_channel("Movies")
tv.power_on()
tv.change_channel("Movies")

sound_system = SoundSystem("Living Room Sound System")
sound_system.set_equalizer("Rock")
sound_system.power_on()
sound_system.play_music("Bohemian Rhapsody")
