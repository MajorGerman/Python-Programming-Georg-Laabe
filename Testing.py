from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
   IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.SetMasterVolumeLevel(-12.0, None)
volume.SetMute(0, None)
import os
os.system('cats.mp3')
class People:
    name = ""
    age = 0
    country = ""
class Stupid(People):
    def data(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Country: ",self.country)
class Smart(People):
    def data(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Country: ",self.country)
anatoliy = Stupid()
anatoliy.name = "Anatoliy"
anatoliy.age = 16
anatoliy.country = "Russia"
georgiy = Smart()
georgiy.name = "Georgiy"
georgiy.age = 16
georgiy.country = "Estonia"