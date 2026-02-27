import ctypes
import ctypes.wintypes
import time
from typing import Optional, Dict, Union

# this script stimulates~ windows and thinks its a real input so that it works in games...

user32 = ctypes.windll.user32

MAPVK_VK_TO_VSC = 0

INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_ABSOLUTE = 0x8000
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP = 0x0040
MOUSEEVENTF_WHEEL = 0x0800

KEYEVENTF_SCANCODE = 0x0008
KEYEVENTF_KEYUP = 0x0002

SendInput = ctypes.windll.user32.SendInput

PUL = ctypes.POINTER(ctypes.c_ulong)


class MouseInput(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", PUL),
    ]


class KeyboardInput(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", PUL),
    ]


class Input_I(ctypes.Union):
    _fields_ = [("mi", MouseInput), ("ki", KeyboardInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong), ("ii", Input_I)]


def screen_size():
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


def normalize_absolute_coords(x, y):
    screen_w, screen_h = screen_size()
    return int(x * 65535 / screen_w), int(y * 65535 / screen_h)


VK_CODE = {
    "left_mouse": 0x01,
    "right_mouse": 0x02,
    "cancel": 0x03,
    "middle_mouse": 0x04,
    "mouse_4": 0x05,
    "mouse_5": 0x06,
    "backspace": 0x08,
    "tab": 0x09,
    "clear": 0x0C,
    "enter": 0x0D,
    "shift": 0x10,
    "ctrl": 0x11,
    "alt": 0x12,
    "pause": 0x13,
    "capslock": 0x14,
    "kana": 0x15,
    "hangul": 0x15,
    "junja": 0x17,
    "final": 0x18,
    "hanja": 0x19,
    "kanji": 0x19,
    "esc": 0x1B,
    "convert": 0x1C,
    "nonconvert": 0x1D,
    "accept": 0x1E,
    "modechange": 0x1F,
    "space": 0x20,
    "pageup": 0x21,
    "pagedown": 0x22,
    "end": 0x23,
    "home": 0x24,
    "left": 0x25,
    "up": 0x26,
    "right": 0x27,
    "down": 0x28,
    "select": 0x29,
    "print": 0x2A,
    "execute": 0x2B,
    "printscreen": 0x2C,
    "insert": 0x2D,
    "delete": 0x2E,
    "help": 0x2F,
    "0": 0x30,
    "1": 0x31,
    "2": 0x32,
    "3": 0x33,
    "4": 0x34,
    "5": 0x35,
    "6": 0x36,
    "7": 0x37,
    "8": 0x38,
    "9": 0x39,
    "a": 0x41,
    "b": 0x42,
    "c": 0x43,
    "d": 0x44,
    "e": 0x45,
    "f": 0x46,
    "g": 0x47,
    "h": 0x48,
    "i": 0x49,
    "j": 0x4A,
    "k": 0x4B,
    "l": 0x4C,
    "m": 0x4D,
    "n": 0x4E,
    "o": 0x4F,
    "p": 0x50,
    "q": 0x51,
    "r": 0x52,
    "s": 0x53,
    "t": 0x54,
    "u": 0x55,
    "v": 0x56,
    "w": 0x57,
    "x": 0x58,
    "y": 0x59,
    "z": 0x5A,
    "left_win": 0x5B,
    "right_win": 0x5C,
    "apps": 0x5D,
    "sleep": 0x5F,
    "num0": 0x60,
    "num1": 0x61,
    "num2": 0x62,
    "num3": 0x63,
    "num4": 0x64,
    "num5": 0x65,
    "num6": 0x66,
    "num7": 0x67,
    "num8": 0x68,
    "num9": 0x69,
    "multiply": 0x6A,
    "add": 0x6B,
    "separator": 0x6C,
    "subtract": 0x6D,
    "decimal": 0x6E,
    "divide": 0x6F,
    "f1": 0x70,
    "f2": 0x71,
    "f3": 0x72,
    "f4": 0x73,
    "f5": 0x74,
    "f6": 0x75,
    "f7": 0x76,
    "f8": 0x77,
    "f9": 0x78,
    "f10": 0x79,
    "f11": 0x7A,
    "f12": 0x7B,
    "f13": 0x7C,
    "f14": 0x7D,
    "f15": 0x7E,
    "f16": 0x7F,
    "f17": 0x80,
    "f18": 0x81,
    "f19": 0x82,
    "f20": 0x83,
    "f21": 0x84,
    "f22": 0x85,
    "f23": 0x86,
    "f24": 0x87,
    "numlock": 0x90,
    "scrolllock": 0x91,
    "left_shift": 0xA0,
    "right_shift": 0xA1,
    "left_ctrl": 0xA2,
    "right_ctrl": 0xA3,
    "left_alt": 0xA4,
    "right_alt": 0xA5,
    "browser_back": 0xA6,
    "browser_forward": 0xA7,
    "browser_refresh": 0xA8,
    "browser_stop": 0xA9,
    "browser_search": 0xAA,
    "browser_favorites": 0xAB,
    "browser_home": 0xAC,
    "volume_mute": 0xAD,
    "volume_down": 0xAE,
    "volume_up": 0xAF,
    "next_track": 0xB0,
    "previous_track": 0xB1,
    "stop_media": 0xB2,
    "play_pause": 0xB3,
    "launch_mail": 0xB4,
    "launch_media_select": 0xB5,
    "launch_app1": 0xB6,
    "launch_app2": 0xB7,
    "semicolon": 0xBA,
    "plus": 0xBB,
    "comma": 0xBC,
    "minus": 0xBD,
    "period": 0xBE,
    "slash": 0xBF,
    "grave": 0xC0,
    "left_bracket": 0xDB,
    "backslash": 0xDC,
    "right_bracket": 0xDD,
    "apostrophe": 0xDE,
}


def keyname_to_scancode(name: str) -> int:
    key = name.lower()

    if key in VK_CODE:
        vk = VK_CODE[key]
    elif len(key) == 1:
        vk = user32.VkKeyScanW(ord(key)) & 0xFF
    else:
        raise ValueError(f"Unknown key name: '{name}'")

    scancode = user32.MapVirtualKeyW(vk, MAPVK_VK_TO_VSC)
    if scancode == 0:
        raise ValueError(f"Could not convert VK {vk} to scan code.")

    return scancode


# api below


def moveRel(dx, dy):
    ii_ = Input_I()
    ii_.mi = MouseInput(dx, dy, 0, MOUSEEVENTF_MOVE, 0, None)
    SendInput(1, ctypes.byref(Input(INPUT_MOUSE, ii_)), ctypes.sizeof(Input))


_last_mouse_pos: Dict[str, Optional[int]] = {"x": None, "y": None}


def get_actual_mouse_pos():
    pt = ctypes.wintypes.POINT()
    user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y


def moveTo(x, y, sensitivity=1.0):
    global _last_mouse_pos
    screen_w, screen_h = screen_size()

    x = max(0, min(int(x), screen_w - 1))
    y = max(0, min(int(y), screen_h - 1))

    if _last_mouse_pos["x"] is None or _last_mouse_pos["y"] is None:
        real_x, real_y = get_actual_mouse_pos()
        _last_mouse_pos["x"] = real_x
        _last_mouse_pos["y"] = real_y

    dx = int((x - _last_mouse_pos["x"]) * sensitivity)
    dy = int((y - _last_mouse_pos["y"]) * sensitivity)

    if dx != 0 or dy != 0:
        moveRel(dx, dy)

    _last_mouse_pos["x"] = x
    _last_mouse_pos["y"] = y


def mouseDown(button="left"):
    syncMouseTracker()

    flags = {
        "left": MOUSEEVENTF_LEFTDOWN,
        "right": MOUSEEVENTF_RIGHTDOWN,
        "middle": MOUSEEVENTF_MIDDLEDOWN,
    }
    if button not in flags:
        raise ValueError("Invalid button")
    _send_mouse_event(flags[button])


def mouseUp(button="left"):
    syncMouseTracker()

    flags = {
        "left": MOUSEEVENTF_LEFTUP,
        "right": MOUSEEVENTF_RIGHTUP,
        "middle": MOUSEEVENTF_MIDDLEUP,
    }
    if button not in flags:
        raise ValueError("Invalid button")
    _send_mouse_event(flags[button])


def _send_mouse_event(flag):
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, 0, flag, 0, None)
    SendInput(1, ctypes.byref(Input(INPUT_MOUSE, ii_)), ctypes.sizeof(Input))


def scroll(amount):
    ii_ = Input_I()
    ii_.mi = MouseInput(0, 0, int(amount * 120), MOUSEEVENTF_WHEEL, 0, None)
    SendInput(1, ctypes.byref(Input(INPUT_MOUSE, ii_)), ctypes.sizeof(Input))


def keyDown(key):
    sc = keyname_to_scancode(key)
    if sc is None:
        raise ValueError(f"Unknown key: {key}")
    ii_ = Input_I()
    ii_.ki = KeyboardInput(0, sc, KEYEVENTF_SCANCODE, 0, None)
    SendInput(1, ctypes.byref(Input(INPUT_KEYBOARD, ii_)), ctypes.sizeof(Input))


def keyUp(key):
    sc = keyname_to_scancode(key)
    if sc is None:
        raise ValueError(f"Unknown key: {key}")
    ii_ = Input_I()
    ii_.ki = KeyboardInput(0, sc, KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP, 0, None)
    SendInput(1, ctypes.byref(Input(INPUT_KEYBOARD, ii_)), ctypes.sizeof(Input))


def is_cursor_hidden():
    user32.ShowCursor(True)
    user32.ShowCursor(False)
    return False if user32.ShowCursor(False) >= 0 else True


def resetMouseTracker():
    global _last_mouse_pos
    _last_mouse_pos = {"x": None, "y": None}


def syncMouseTracker():
    global _last_mouse_pos
    real_x, real_y = get_actual_mouse_pos()
    _last_mouse_pos["x"] = real_x
    _last_mouse_pos["y"] = real_y


def unstuck_keys():
    for key in VK_CODE:
        try:
            keyUp(key)
        except Exception as e:
            print(f"Failed to release {key}: {e}")


def hotkey(*keys, delay=0.01):
    if not keys:
        return

    for key in keys:
        keyDown(key)
        time.sleep(delay)

    for key in reversed(keys):
        keyUp(key)
        time.sleep(delay)


def hotkey_vk(*keys, delay=0.01):
    inputs = []

    for key in keys:
        vk = VK_CODE[key]
        ki = KeyboardInput(vk, 0, 0, 0, None)
        inputs.append(Input(INPUT_KEYBOARD, Input_I(ki=ki)))
        time.sleep(delay)

    for key in reversed(keys):
        vk = VK_CODE[key]
        ki = KeyboardInput(vk, 0, KEYEVENTF_KEYUP, 0, None)
        inputs.append(Input(INPUT_KEYBOARD, Input_I(ki=ki)))
        time.sleep(delay)

    SendInput(len(inputs), (Input * len(inputs))(*inputs), ctypes.sizeof(Input))
