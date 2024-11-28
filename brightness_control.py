import keyboard
import screen_brightness_control 


def less():
    cb = screen_brightness_control.get_brightness()[0]
    new_cb = max(0, cb - 10)
    screen_brightness_control.set_brightness(new_cb)
    
def more():
    cb = screen_brightness_control.get_brightness()[0]
    
    if cb == 100:
        return
    
    new_cb = max(0, cb + 10)
    screen_brightness_control.set_brightness(new_cb)
    
keyboard.add_hotkey('ctrl+q', less)
keyboard.add_hotkey('ctrl+w', more)

keyboard.wait('esc')
 