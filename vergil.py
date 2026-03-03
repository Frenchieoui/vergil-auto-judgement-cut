import keyboard
import safeautogui
import sys
import time
import threading

enabled = False
# press [backspace] key to do auto judgement cut
# press [y] key to do multiple judgement cuts; YOU MUST set judgement cut keybind to [K]


def vergil_judgement_cut():
    safeautogui.keyDown("k")
    safeautogui.keyUp("k")
    time.sleep(0.7)
    t = 0.35
    safeautogui.keyDown("k")
    safeautogui.keyUp("k")
    time.sleep(t)
    safeautogui.keyDown("k")
    safeautogui.keyUp("k")
    time.sleep(t)
    safeautogui.keyDown("k")
    safeautogui.keyUp("k")


def auto_vergil_judgement_cut():
    while True:
        time.sleep(2.25)
        if enabled:
            vergil_judgement_cut()


def on_key_event(event):
    global enabled

    if event.name == "y" and event.event_type == keyboard.KEY_UP:
        threading.Thread(target=vergil_judgement_cut, daemon=True).start()

    if event.name == "backspace" and event.event_type == keyboard.KEY_UP:
        enabled = not enabled
        print("Enable auto" if enabled else "Disabled auto")

    if not enabled:
        return


threading.Thread(target=auto_vergil_judgement_cut, daemon=True).start()

keyboard.hook(on_key_event)


print("-------------------------------------------------------------------------------")
print("YOU MUST set judgement cut keybind to [K]")
print("Press [Y] key to do multiple judgement cuts")
print("Press [backspace] key to enable/disable auto judgement cut.")
print("Currently Disabled")
print("Press [DELETE] to exit script.")
print("-------------------------------------------------------------------------------")


keyboard.wait("delete")

print("Exiting...")
sys.exit(0)
