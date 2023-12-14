from pynput.keyboard import Key, Listener, Controller
import time
from pydub import AudioSegment
from pydub.playback import play
import threading  # Import the threading module

YOURFILENAME = "audio.mp3"

import os

keyboard = Controller()
locked = False
sheepMode = False
typed_characters = []

# Create a function for audio playback
def play_audio():
    input_file = AudioSegment.from_file(os.path.dirname(os.path.abspath(__file__)) + "/" + YOURFILENAME)
    play(input_file)

def backspace():
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)

def printWord(word):
    for x in word:
        if x == "·":
            keyboard.type("\u00B7")  # ·
        else:
            keyboard.press(x)
            keyboard.release(x)

def on_press(key):
    global typed_characters, locked, sheepMode
    try:
        char = key.char
        if char is not None:
            if not locked:
                typed_characters.append(char)
                typed_characters = typed_characters[-100:]

                typed_text = (''.join(typed_characters)).lower()
            else:
                if key != Key.backspace:
                    typed_characters.append(char)
                    typed_characters = typed_characters[-100:]
                    typed_text = (''.join(typed_characters)).lower()
                    backspace()
                    if sheepMode:
                        # Play audio in a separate thread
                        audio_thread = threading.Thread(target=play_audio)
                        audio_thread.start()

            if 'password' in typed_text:
                locked = False
                sheepMode = False
                typed_characters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']

            if 'pqow' in typed_text:
                locked = True
                typed_characters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
                backspace()
                time.sleep(0.1)
                backspace()
                time.sleep(0.1)
                backspace()
                time.sleep(0.1)
                backspace()

            if 'locksheep' in typed_text:
                locked = True
                sheepMode = True
                typed_characters = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
                backspace()
                time.sleep(0.1)
                backspace()
                time.sleep(0.1)
                backspace()
                time.sleep(0.1)
                backspace()
                time.sleep(0.1)
                backspace()
                time.sleep(0.1)
                backspace()
                time.sleep(0.1)
                backspace()
                time.sleep(0.1)
                backspace()
                time.sleep(0.1)
                backspace()
                
    except AttributeError:
        if key == Key.backspace and not locked:
            if typed_characters:
                typed_characters.pop()

def on_release(key):
    pass

with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
