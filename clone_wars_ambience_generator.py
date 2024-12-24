from cmu_graphics import *
from pydub import AudioSegment
import simpleaudio as sa
import os
import random
import threading

def load_sounds(directory):
    return [AudioSegment.from_wav(os.path.join(directory, filename)) for filename in os.listdir(directory) if filename.endswith(".wav")]

DC15 = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\DC15")
E5 = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\E5")
DC17 = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\DC17")
DC17M = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\DC17M\Fire")
DC17M_alt = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\DC17M\Alt Fire")
T21 = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\T21")
Valken38X = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\Valken-38X")
Z6 = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Clones\Z6 Rotary Blaster")
app.Z6Steps = 1
app.Z6 = False

B2 = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\B2 Arm Blaster")
Droideka = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\Droideka Twin Blaster")
E5 = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\E5")
E5BX = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\E5BX")
E5C = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\E5C")
E5S = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\E5S")
RG4D = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Blasters\Droids\RG4D")

clone_voice_lines = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Clone Trooper Voice Lines")

AA_cannon = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Cannons\AA Cannon")

# ATRT_walk = load_sounds(r)
ATRT_cannon = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Cannons\AT-RT Light Blaster Cannon")
app.ATRTSteps = 1

# ATTE_walk = AudioSegment.from_wav(r)
ATTE_cannon_quad = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Cannons\AT-TE\Quad Cannon")
ATTE_cannon_linked = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Cannons\AT-TE\Linked")
app.ATTESteps = 1

BARC_speeder = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Vehicles\BARC Speeder")

LAAT = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Vehicles\LAAT")
# LAAT_cannon = load_sounds(r)
LAAT_distant = AudioSegment.from_wav(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Vehicles\LAAT\Distant\LAAT Engine Distant.wav")

# LAATC_flyby = load_sounds(r)
# LAATC_land = load_sounds(r)
# LAATC_drop = load_sounds(r)
# LAATC_takeoff = load_sounds(r)

HMP = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Vehicles\HMP")
# HMP_cannon = load_sounds(r)

AAT_passby = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Vehicles\AAT")
AAT_twin_cannon = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Cannons\AAT\AAT Twin Blaster Cannon")
AAT_anti_vehicle = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Cannons\AAT\AAT Anti Vehicle")
AAT_blaster_cannon = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Cannons\AAT\AAT Blaster Cannon")
AAT_twin_cannon_linked = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Cannons\AAT\AAT Twin Blaster Cannon Linked")
AATCannons = ["linked", "twin", "anti_vehicle", "blaster"]
app.AATSteps = 1
app.AAT = False
app.AATCannon = ""

MTT_passby = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Vehicles\MTT")
MTT_cannon = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Cannons\MTT Blaster Cannon")
app.MTTSteps = 1
app.MTT = False

# Octupurra_cannon = load_sounds(r)

# Hailfire_cannon = load_sounds(r)

NRN99 = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Vehicles\NR-N99")
app.NRN99Steps = 1
app.NRN99 = False

STAP = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Vehicles\STAP")

TX130_passby = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Vehicles\TX-130")
TX130_cannon = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Cannons\TX-130")
app.TX130Steps = 1
app.TX130 = False

explosions_distant = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Explosions\Distant")
explosions_far = load_sounds(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Explosions\Far")

venator_charge = AudioSegment.from_wav(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Cannons\Venator Laser Beam\VenatorLaserBeam Charge 1.wav")
venator_fire = AudioSegment.from_wav(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Cannons\Venator Laser Beam\VenatorLaserBeam Fire Close 1.wav")
app.venatorSteps = 64

def play_sound(sound):
    playback = sa.play_buffer(sound.raw_data, num_channels=sound.channels, bytes_per_sample=sound.sample_width, sample_rate=sound.frame_rate)

def play_random_sound(sound_list):
    if sound_list:
        sound = random.choice(sound_list)
        threading.Thread(target=play_sound, args=(sound,), daemon=True).start()

play_sound(AudioSegment.from_wav(r"C:\Users\Austin\Documents\Python\Clone Wars Ambience Generator\Sound\Deep Wind.wav"))

app.stepsPerSecond = 16
app.steps = 0
def onStep():
    app.steps += 1
    app.venatorSteps += 1
    app.TX130Steps += 1
    app.AATSteps += 1
    app.MTTSteps += 1
    app.Z6Steps += 1
    app.ATRTSteps += 1
    app.ATTESteps += 1



    if random.randint(0, 3) == 0:
        play_random_sound(DC15)
    if random.randint(0, 8) == 0:
        play_random_sound(DC17)
    if random.randint(0, 16) == 0:
        play_random_sound(T21)
    if random.randint(0, 32) == 0:
        play_random_sound(Valken38X)

    if random.randint(0, 3) == 0:
        play_random_sound(E5)
    if random.randint(0, 5) == 0:
        play_random_sound(E5C)
    if random.randint(0, 16) == 0:
        play_random_sound(RG4D)
    if random.randint(0, 32) == 0:
        play_random_sound(E5S)
    if random.randint(0, 5) == 0:
        play_random_sound(B2)

    if random.randint(0, 6) == 0:
        play_random_sound(clone_voice_lines)

    if random.randint(0, 250) == 0:
        play_random_sound(LAAT)
    if random.randint(0, 300) == 0:    
        play_random_sound(HMP)

    if random.randint(0, 200) == 0:
        play_random_sound(explosions_distant)
    if random.randint(0, 200) == 0:
        play_random_sound(explosions_far)

    if app.venatorSteps == 0:
        play_sound(venator_charge)
    elif app.venatorSteps == 48:
        play_sound(venator_fire)
    elif app.venatorSteps > 960 and random.randint(0, 250) == 0:
        app.venatorSteps = -1
    
    if app.TX130Steps == 0:
        play_random_sound(TX130_passby)
    if app.TX130 and app.TX130Steps % 12 == 0:
        play_random_sound(TX130_cannon)
        if random.randint(0, 4) == 0:
            app.TX130 = False
    elif app.TX130 == False and app.TX130Steps > 480 and random.randint(0,250) == 0:
        app.TX130 = True
        app.TX130Steps = -1
    
    if app.AATSteps == 0:
        play_random_sound(AAT_passby)
        app.AATCannon = random.choice(AATCannons)
    if app.AAT and app.AATSteps % 8 == 0:
        if app.AATCannon == "linked":
            play_random_sound(AAT_twin_cannon_linked)
        elif app.AATCannon == "twin":
            play_random_sound(AAT_twin_cannon)
        elif app.AATCannon == "anti_vehicle":
            play_random_sound(AAT_anti_vehicle)
        elif app.AATCannon == "blaster":
            play_random_sound(AAT_blaster_cannon)
        if random.randint(0, 6) == 0:
            app.AAT = False
    elif app.AAT == False and app.AATSteps > 480 and random.randint(0,250) == 0:
        app.AAT = True
        app.AATSteps = -1

    if app.MTTSteps == 0:
        play_random_sound(MTT_passby)
    if app.MTT and app.MTTSteps % 8 == 0:
        play_random_sound(MTT_cannon)
        if random.randint(0, 4) == 0:
            app.MTT = False
    elif app.MTT == False and app.MTTSteps > 480 and random.randint(0,250) == 0:
        app.MTT = True
        app.MTTSteps = -1

    if app.NRN99Steps == 0:
        play_random_sound(NRN99)
    elif app.NRN99 == False and app.NRN99Steps > 480 and random.randint(0,250) == 0:
        app.NRN99 = True
        app.NRN99Steps = -1

    if app.Z6 and app.Z6Steps % 4 == 0:
        play_random_sound(Z6)
        if random.randint(0, 20) == 0:
            app.Z6 = False
    elif app.Z6 == False and app.Z6Steps > 960 and random.randint(0,250) == 0:
        app.Z6 = True
        app.Z6Steps = -1

    if random.randint(0, 100) == 0:
        play_random_sound(AA_cannon)

    if random.randint(0, 250) == 0:
        play_random_sound(BARC_speeder)
        print("BARC")
    if random.randint(0, 320) == 0:
        play_random_sound(STAP)
    
cmu_graphics.run() # type: ignore