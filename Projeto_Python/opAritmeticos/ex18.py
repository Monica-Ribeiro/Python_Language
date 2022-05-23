# Tocando um MP3:

from pygame import mixer
mixer.init()
mixer.music.load('ex18.mp3')
mixer.music.play()
input('CURTE O SOM!\nPs: TENHA DETERMINAÇÃO!!!')