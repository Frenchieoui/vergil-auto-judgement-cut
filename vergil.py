import keyboard
import safeautogui
import sys
import time
from pynput import mouse
import threading
import tkinter as tk

enabled = True


def vergil_judgement_cut():
    safeautogui.keyDown("k")
    safeautogui.keyUp("k")
    time.sleep(0.65)
    t = 0.35
    safeautogui.keyDown("k")
    safeautogui.keyUp("k")
    time.sleep(t)
    safeautogui.keyDown("k")
    safeautogui.keyUp("k")
    time.sleep(t)
    safeautogui.keyDown("k")
    safeautogui.keyUp("k")


def on_key_event(event):
    global enabled

    if event.name == "`" and event.event_type == keyboard.KEY_UP:
        enabled = not enabled
        print("Enabled" if enabled else "Disabled")

    if not enabled:
        return

    if event.name == "y" and event.event_type == keyboard.KEY_UP:
        threading.Thread(target=vergil_judgement_cut, daemon=True).start()


keyboard.hook(on_key_event)


print("-------------------------------------------------------------------------------")
print("Press [`] (back tick) key to enable/disable.")
print("Press [DELETE] to exit.")
print("-------------------------------------------------------------------------------")


keyboard.wait("delete")

print("Exiting...")
sys.exit(0)
