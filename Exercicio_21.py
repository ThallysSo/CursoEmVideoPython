from pygame import mixer
mixer.init()
mixer.music.load("song.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()

print("<P> PAUSE")
print("<R> DESPAUSAR")
print('<E> STOP')
while True:
    query = input(" ").lower()
    if query == 'p':
        mixer.music.pause()
    elif query == 'r':
        mixer.music.unpause()
    elif query == 'e':
        mixer.music.stop()
        break

