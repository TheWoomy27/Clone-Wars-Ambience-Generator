from cmu_graphics import *
from pydub import AudioSegment
from pydub.playback import play
import os
import random
import time
# import concurrent.futures


#mixer.init()



DC15 = [AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\DC15", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\DC15") if filename.endswith(".wav")]
DC17 = [AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\DC17", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\DC17") if filename.endswith(".wav")]
DC17M = [AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\DC17M", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\DC17M") if filename.endswith(".wav")]
T21 = [AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\T21", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\T21") if filename.endswith(".wav")]
Valken38X = [AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\Valken-38X", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\Valken-38X") if filename.endswith(".wav")]
Z6 = [AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\Z6 Rotary Blaster", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\Z6 Rotary Blaster") if filename.endswith(".wav")]

B2 = [AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\B2 Arm Blaster", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\B2 Arm Blaster") if filename.endswith(".wav")]
Droideka = [AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\Droideka Twin Blaster", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\Droideka Twin Blaster") if filename.endswith(".wav")]
E5 = [AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\E5", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\E5") if filename.endswith(".wav")]
E5BX = [AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\E5BX", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\E5BX") if filename.endswith(".wav")]
E5C = [AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\E5C", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\E5C") if filename.endswith(".wav")]
E5S = [AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\E5S", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\E5S") if filename.endswith(".wav")]
RG4D = [AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\RG4D", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\RG4D") if filename.endswith(".wav")]

LAAT = [AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Vehicles\LAAT", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Vehicles\LAAT") if filename.endswith(".wav")]

Explosions_Distant = [AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Explosions\Distant", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Explosions\Distant") if filename.endswith(".wav")]
Explosions_Far = [AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Explosions\Far", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Explosions\Far") if filename.endswith(".wav")]

AAT_passby = [AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Vehicles\AAT", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Vehicles\AAT") if filename.endswith(".wav")]

AAT_twin_cannon =[AudioSegment.from_wav(os.path.join(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Cannons\AAT\AAT Twin Blaster Cannon", filename)) for filename in os.listdir(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Cannons\AAT\AAT Twin Blaster Cannon") if filename.endswith(".wav")]
AAT = False
AATsteps = 0

play(AudioSegment.from_wav(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Deep Wind.wav"))

# Main loop
app.steps = 0
app.stepsPerSecond = 1
app.AAT = False
app.AATsteps = 0

def onStep():
    app.steps += 1
    print(app.steps)

    if (random.randint(0,1) == 0) or True:
        play(random.choice(E5))
    if (random.randint(0,1) == 0) or True:
        play(random.choice(DC15))

def onMousePress(x, y):
    app.stepsPerSecond += 1


    # steps += 1
    # AATsteps += 1

    # # Check and reset steps as per your logic
    # if steps == 32:
    #     steps = 0
    #     AATsteps = 0

    # # Control AAT passby and cannon sounds
    # if steps % (app.stepsPerSecond * random.randint(1, 4)) == 0:
    #     AAT = True

    # if AAT and AATsteps % 16 == 0:
    #     executor.submit(play_random_sound, AAT_twin_cannon)
    #     print("AAT")
    #     print(AATsteps)

    # Randomly play other sounds in parallel
    # if random.randint(0, 2) == 0:
    #     executor.submit(play_random_sound, E5)
    # if random.randint(0, 2) == 0:
    #     executor.submit(play_random_sound, DC15)
    # if random.randint(0, 2) == 0:
    #     executor.submit(play_random_sound, DC17)
    # if random.randint(0, 4) == 0:
    #     executor.submit(play_random_sound, T21)
    # if random.randint(0, 8) == 0:
    #     executor.submit(play_random_sound, Valken38X)
    # if random.randint(0, 2) == 0:
    #     executor.submit(play_random_sound, E5C)
    # if random.randint(0, 8) == 0:
    #     executor.submit(play_random_sound, E5S)
    # if random.randint(0, 3) == 0:
    #     executor.submit(play_random_sound, B2)
    # if random.randint(0, 4) == 0:
    #     executor.submit(play_random_sound, RG4D)
    # if random.randint(0, 15) == 0:
    #     executor.submit(play_random_sound, LAAT)
    # if random.randint(0, 8) == 0:
    #     executor.submit(play_random_sound, Explosions_Distant)
    # if random.randint(0, 8) == 0:
    #     executor.submit(play_random_sound, Explosions_Far)
# steps = 0
# stepsPerSecond = 30
# while True:
#     time.sleep(0.05)
#     steps += 1
#     AATsteps += 1
#     if steps == 32:
#         steps = 0
#         AATsteps = 0

#     if steps % (stepsPerSecond * random.randint(1, 4)) == 0:
#         #AAT_passby[random.randint(0, len(AAT_passby)-1)].play()
#         AAT=True

    
#     if AAT and AATsteps % 16 == 0: # (random.randint(0,1) == 0 or 0 == 0) 
#         AAT_twin_cannon[random.randint(0, len(AAT_twin_cannon)-1)].play()
#         print("AAT")
#         print(AATsteps)

#     if (random.randint(0,2) == 0):
#         E5[random.randint(0, len(E5)-1)].play()
#     if (random.randint(0,2) == 0):
#         DC15[random.randint(0, len(DC15)-1)].play()
#     if (random.randint(0,2) == 0):
#         DC17[random.randint(0, len(DC17)-1)].play()
#     if (random.randint(0,4) == 0):
#         T21[random.randint(0, len(T21)-1)].play()
#     if (random.randint(0,8) == 0):
#         Valken38X[random.randint(0, len(Valken38X)-1)].play()
#     if (random.randint(0,2) == 0):
#         E5C[random.randint(0, len(E5C)-1)].play()
#     if (random.randint(0,8) == 0):
#         E5S[random.randint(0, len(E5S)-1)].play()
#     if (random.randint(0,3) == 0):
#         B2[random.randint(0, len(B2)-1)].play()
#     if (random.randint(0,4) == 0):
#         RG4D[random.randint(0, len(RG4D)-1)].play()

#     if (random.randint(0,15) == 0):
#         LAAT[random.randint(0, len(LAAT)-1)].play()

#     if (random.randint(0,8) == 0):
#         Explosions_Distant[random.randint(0, len(Explosions_Distant)-1)].play()
#     if (random.randint(0,8) == 0):
#         Explosions_Far[random.randint(0, len(Explosions_Far)-1)].play()
    

cmu_graphics.run() # type: ignore
