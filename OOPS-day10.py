class Device:
    def __init__(self, brand):
        self.brand=brand

class VoiceControl(Device):
    def __init__(self,brand):
        super().__init__(brand)
    def voice_activate(self):
        return "voice"

class AppControl(Device):
    def __init__(self,brand):
        super().__init__(brand)
    def app_activate(self):
        return "app"

class SmartSpeaker(VoiceControl, AppControl):
    def __init__(self,brand):
        super().__init__(brand)
    def control_methods(self):
        return f"{self.brand} can be controlled via {self.voice_activate()} and {self.app_activate()}."

s1 = SmartSpeaker("Echo")
print( s1.control_methods())