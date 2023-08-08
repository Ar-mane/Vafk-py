import keyboard
import time

AFK_MESSAGES = [
    'This is AFK Bot, download it from https://t.ly/joyboy',
    "Sorry guys, emergency! Be right back.",
    "Just a quick AFK, back in a sec.",
    "Emergency situation, brb ASAP.",
]

def type_message(msg):
    keyboard.press_and_release('enter')
    time.sleep(1)
    keyboard.write(msg) 
    time.sleep(1)
    keyboard.press_and_release('enter')
    time.sleep(1)


def type_empty_messages():
    for i in range(2):
        type_message(' ')
        time.sleep(2)
        


def press_enter_periodically():     
    message_index = 0
    while True:        
        type_message(AFK_MESSAGES[message_index])   
        message_index = (message_index + 1) % len(AFK_MESSAGES)
        type_empty_messages()


if __name__ == "__main__":
    print("Starting anti-AFK script. Press Ctrl+C to stop.")
    time.sleep(5)
    try:
        press_enter_periodically()
    except KeyboardInterrupt:
        print("Script stopped.")
