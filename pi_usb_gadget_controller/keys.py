NULL_BYTE = 0x0
NULL_CHAR = bytes((0,))
CONSUMER_CONTROL_RELEASE = NULL_CHAR*2
KEYBOARD_RELEASE = NULL_CHAR*8

KEYBOARD_MODIFIER_KEYS = {
    'KEY_LEFTCTRL':1,
    'KEY_LEFTSHIFT': 2,
    'KEY_LEFTALT': 4,
    'KEY_LEFTMETA': 8,
    'KEY_RIGHTCTRL':16,
    'KEY_RIGHTSHIFT' : 32,
    'KEY_RIGHTALT' : 64,
    'KEY_RIGHTMETA' : 128,
}


keys_keyboard = {
    "KEY_ESC": bytes((0x29, )),
    "KEY_1": bytes((0x1E, )),
    "KEY_2": bytes((0x1F, )),
    "KEY_3": bytes((0x20, )),
    "KEY_4": bytes((0x21, )),
    "KEY_5": bytes((0x22, )),
    "KEY_6": bytes((0x23, )),
    "KEY_7": bytes((0x24, )),
    "KEY_8": bytes((0x25, )),
    "KEY_9": bytes((0x26, )),
    "KEY_0": bytes((0x27, )),
    "KEY_MINUS": bytes((0x2D, )),
    "KEY_EQUAL": bytes((0x2E, )),
    "KEY_BACKSPACE": bytes((0x2A, )),
    "KEY_TAB": bytes((0x2B, )),
    "KEY_Q": bytes((0x14, )),
    "KEY_W": bytes((0x1A, )),
    "KEY_E": bytes((0x08, )),
    "KEY_R": bytes((0x15, )),
    "KEY_T": bytes((0x17, )),
    "KEY_Y": bytes((0x1C, )),
    "KEY_U": bytes((0x18, )),
    "KEY_I": bytes((0x0C, )),
    "KEY_O": bytes((0x12, )),
    "KEY_P": bytes((0x13, )),
    "KEY_LEFTBRACE": bytes((0x2F, )),
    "KEY_RIGHTBRACE": bytes((0x30, )),
    "KEY_ENTER": bytes((0x28, )),
    "KEY_A": bytes((0x04, )),
    "KEY_S": bytes((0x16, )),
    "KEY_D": bytes((0x07, )),
    "KEY_F": bytes((0x09, )),
    "KEY_G": bytes((0x0A, )),
    "KEY_H": bytes((0x0B, )),
    "KEY_J": bytes((0x0D, )),
    "KEY_K": bytes((0x0E, )),
    "KEY_L": bytes((0x0F, )),
    "KEY_SEMICOLON": bytes((0x33, )),
    "KEY_APOSTROPHE": bytes((0x34, )),
    "KEY_GRAVE": bytes((0x35, )),
    "KEY_BACKSLASH": bytes((0x31, )),
    "KEY_Z": bytes((0x1D, )),
    "KEY_X": bytes((0x1B, )),
    "KEY_C": bytes((0x06, )),
    "KEY_V": bytes((0x19, )),
    "KEY_B": bytes((0x05, )),
    "KEY_N": bytes((0x11, )),
    "KEY_M": bytes((0x10, )),
    "KEY_COMMA": bytes((0x36, )),
    "KEY_DOT": bytes((0x37, )),
    "KEY_SLASH": bytes((0x38, )),
    "KEY_KPASTERISK": bytes((0x55, )),
    "KEY_SPACE": bytes((0x2C, )),
    "KEY_CAPSLOCK": bytes((0x39, )),
    "KEY_F1": bytes((0x3A, )),
    "KEY_F2": bytes((0x3B, )),
    "KEY_F3": bytes((0x3C, )),
    "KEY_F4": bytes((0x3D, )),
    "KEY_F5": bytes((0x3E, )),
    "KEY_F6": bytes((0x3F, )),
    "KEY_F7": bytes((0x40, )),
    "KEY_F8": bytes((0x41, )),
    "KEY_F9": bytes((0x42, )),
    "KEY_F10": bytes((0x43, )),
    "KEY_NUMLOCK": bytes((0x53, )),
    "KEY_SCROLLLOCK": bytes((0x47, )),
    "KEY_KP7": "",
    "KEY_KP8": "",
    "KEY_KP9": "",
    "KEY_KPMINUS": bytes((0x56, )),
    "KEY_KP4": "",
    "KEY_KP5": "",
    "KEY_KP6": "",
    "KEY_KPPLUS": bytes((0x57, )),
    "KEY_KP1": "",
    "KEY_KP2": "",
    "KEY_KP3": "",
    "KEY_KP0": "",
    "KEY_KPDOT": bytes((0x63, )),
    "KEY_ZENKAKUHANKAKU": "",
    "KEY_102ND": "",
    "KEY_F11": bytes((0x44, )),
    "KEY_F12": bytes((0x45, )),
    "KEY_RO": "",
    "KEY_KATAKANA": "",
    "KEY_HIRAGANA": "",
    "KEY_HENKAN": "",
    "KEY_KATAKANAHIRAGANA": "",
    "KEY_MUHENKAN": "",
    "KEY_KPJPCOMMA": "",
    "KEY_KPENTER": bytes((0x58, )),
    "KEY_KPSLASH": "",
    "KEY_SYSRQ": "",
    "KEY_HOME": bytes((0x4A, )),
    "KEY_UP": bytes((0x52, )),
    "KEY_PAGEUP": bytes((0x4B, )),
    "KEY_LEFT": bytes((0x50, )),
    "KEY_RIGHT": bytes((0x4F, )),
    "KEY_END": bytes((0x4D, )),
    "KEY_DOWN": bytes((0x51, )),
    "KEY_PAGEDOWN": bytes((0x4E, )),
    "KEY_INSERT": bytes((0x49, )),
    "KEY_DELETE": "",
#    "KEY_MUTE": bytes((0x7F, )),
#    "KEY_VOLUMEDOWN": bytes((0x81, )),
#    "KEY_VOLUMEUP": bytes((0x80, )),
    "KEY_POWER": "",
    "KEY_KPEQUAL": bytes((0x67, )),
    "KEY_PAUSE": "",
    "KEY_KPCOMMA": "",
    "KEY_HANGUEL": "",
    "KEY_HANJA": "",
    "KEY_YEN": "",
    "KEY_COMPOSE": bytes((0x65, )),
    "KEY_STOP": "",
    "KEY_AGAIN": "",
    "KEY_PROPS": "",
    "KEY_UNDO": "",
    "KEY_FRONT": "",
    "KEY_COPY": "",
    "KEY_OPEN": "",
    "KEY_PASTE": "",
    "KEY_FIND": "",
    "KEY_CUT": "",
    "KEY_HELP": "",
    "KEY_CALC": "",
    "KEY_SLEEP": "",
    "KEY_WWW": "",
    "KEY_SCREENLOCK": "",
    "KEY_BACK": "",
    "KEY_FORWARD": "",
    "KEY_EJECTCD": "",
    "KEY_NEXTSONG": "",
    "KEY_PLAYPAUSE": "",
    "KEY_PREVIOUSSONG": "",
    "KEY_STOPCD": "",
    "KEY_REFRESH": "",
    "KEY_EDIT": "",
    "KEY_SCROLLUP": "",
    "KEY_SCROLLDOWN": "",
    "KEY_KPLEFTPAREN": "",
    "KEY_KPRIGHTPAREN": "",
    "KEY_F13": bytes((0x68, )),
    "KEY_F14": bytes((0x69, )),
    "KEY_F15": bytes((0x6A, )),
    "KEY_F16": bytes((0x6B, )),
    "KEY_F17": bytes((0x6C, )),
    "KEY_F18": bytes((0x6D, )),
    "KEY_F19": bytes((0x6E, )),
    "KEY_F20": bytes((0x6F, )),
    "KEY_F21": bytes((0x70, )),
    "KEY_F22": bytes((0x71, )),
    "KEY_F23": bytes((0x72, )),
    "KEY_F24": bytes((0x73, )),
    "KEY_UNKNOWN": "",
}

keys_consumer_control = {
    "KEY_ESC": "",
    "KEY_ENTER": bytes((0x41, NULL_BYTE)), # bytes((65,))+NULL_CHAR,
    "KEY_KPMINUS": "",
    "KEY_KPPLUS": "",
    "KEY_UP": bytes((0x42, NULL_BYTE)), # bytes((66,)) + NULL_CHAR,
    "KEY_LEFT": bytes((0x44, NULL_BYTE)), # bytes((68,))+NULL_CHAR,
    "KEY_RIGHT": bytes((0x45, NULL_BYTE)), # bytes((69,))+NULL_CHAR,
    "KEY_DOWN": bytes((0x43, NULL_BYTE)), # bytes((67,))+NULL_CHAR,
    "KEY_INSERT": "",
    "KEY_DELETE": "",
    "KEY_MUTE": bytes((0xE2, NULL_BYTE)), # bytes((226,))+NULL_CHAR
    "KEY_VOLUMEDOWN": bytes((0xEA, NULL_BYTE)),
    "KEY_VOLUMEUP": bytes((0xE9, NULL_BYTE)),
    "KEY_POWER": bytes((0x30, NULL_BYTE)),
    "KEY_PAUSE": "",
    "KEY_SCALE": "",
    "KEY_STOP": "",
    "KEY_PROPS": "",
    "KEY_UNDO": "",
    "KEY_COPY": "",
    "KEY_OPEN": "",
    "KEY_PASTE": "",
    "KEY_FIND": "",
    "KEY_CUT": "",
    "KEY_HELP": bytes((0x95, NULL_BYTE)),
    "KEY_MENU": bytes((0x40, NULL_BYTE)),
    "KEY_CALC": "",
    "KEY_SLEEP": bytes((0x34, NULL_BYTE)),
    "KEY_FILE": "",
    "KEY_WWW": bytes((0x8A, NULL_BYTE)),
    "KEY_SCREENLOCK": "",
    "KEY_MAIL": bytes((0x8A, 0x01)),
    "KEY_BOOKMARKS": "",
    "KEY_BACK":  bytes((0x24, 0x02)), # bytes((36,))+bytes((2,)),
    "KEY_FORWARD": "",
    "KEY_EJECTCD": "",
    "KEY_NEXTSONG": bytes((0xB5, NULL_BYTE)),
    "KEY_PLAYPAUSE": bytes((0xCD, NULL_BYTE)), # bytes((205,))+NULL_CHAR,
    "KEY_PREVIOUSSONG": bytes((0xB6, NULL_BYTE)),
    "KEY_STOPCD": "",
    "KEY_RECORD": bytes((0xB2, NULL_BYTE)),
    "KEY_REWIND": bytes((0xB4, NULL_BYTE)),
    "KEY_PHONE": "",
    "KEY_CONFIG": bytes((0x83, 0x01)),
    "KEY_HOMEPAGE": bytes((0x23, 0x02)), #bytes((35,))+bytes((2,)),
    "KEY_REFRESH": "",
    "KEY_EXIT": "",
    "KEY_EDIT": "",
    "KEY_SCROLLUP": "",
    "KEY_SCROLLDOWN": "",
    "KEY_NEW": "",
    "KEY_REDO": "",
    "KEY_CLOSE": "",
    "KEY_PLAY": "",
    "KEY_FASTFORWARD": bytes((0xB3, NULL_BYTE)),
    "KEY_BASSBOOST": "",
    "KEY_PRINT": "",
    "KEY_CAMERA": "",
    "KEY_CHAT": "",
    "KEY_SEARCH": bytes((0x21, 0x02)),
    "KEY_FINANCE": "",
    "KEY_CANCEL": "",
    "KEY_BRIGHTNESSDOWN": "",
    "KEY_BRIGHTNESSUP": "",
    "KEY_KBDILLUMTOGGLE": "",
    "KEY_KBDILLUMDOWN": "",
    "KEY_KBDILLUMUP": "",
    "KEY_SEND": "",
    "KEY_REPLY": "",
    "KEY_FORWARDMAIL": "",
    "KEY_SAVE": "",
    "KEY_DOCUMENTS": "",
    "KEY_UNKNOWN": "",
    "KEY_VIDEO_NEXT": "",
    "KEY_BRIGHTNESS_ZERO": "",
    "BTN_0": "",
    "KEY_SELECT": "",
    "KEY_GOTO": "",
    "KEY_INFO": "",
    "KEY_PROGRAM": "",
    "KEY_PVR": bytes((0x9A, NULL_BYTE)),
    "KEY_SUBTITLE": "",
    "KEY_ZOOM": "",
    "KEY_KEYBOARD": "",
    "KEY_SCREEN": "",
    "KEY_PC": "",
    "KEY_TV": "",
    "KEY_TV2": "",
    "KEY_VCR": "",
    "KEY_VCR2": "",
    "KEY_SAT": "",
    "KEY_CD": "",
    "KEY_TAPE": "",
    "KEY_TUNER": "",
    "KEY_PLAYER": "",
    "KEY_DVD": "",
    "KEY_AUDIO": "",
    "KEY_VIDEO": "",
    "KEY_MEMO": "",
    "KEY_CALENDAR": "",
    "KEY_RED": "",
    "KEY_GREEN": "",
    "KEY_YELLOW": "",
    "KEY_BLUE": "",
    "KEY_CHANNELUP": bytes((0x9C, NULL_BYTE)),
    "KEY_CHANNELDOWN": bytes((0x9D, NULL_BYTE)),
    "KEY_LAST": "",
    "KEY_NEXT": "",
    "KEY_RESTART": "",
    "KEY_SLOW": "",
    "KEY_SHUFFLE": "",
    "KEY_PREVIOUS": "",
    "KEY_VIDEOPHONE": "",
    "KEY_GAMES": "",
    "KEY_ZOOMIN": bytes((0x2D, 0x2)),
    "KEY_ZOOMOUT": bytes((0x2E, 0x2)),
    "KEY_ZOOMRESET": "",
    "KEY_WORDPROCESSOR": "",
    "KEY_EDITOR": "",
    "KEY_SPREADSHEET": "",
    "KEY_GRAPHICSEDITOR": "",
    "KEY_PRESENTATION": "",
    "KEY_DATABASE": "",
    "KEY_NEWS": "",
    "KEY_VOICEMAIL": "",
    "KEY_ADDRESSBOOK": "",
    "KEY_MESSENGER": "",
    "KEY_DISPLAYTOGGLE": "",
    "KEY_SPELLCHECK": "",
    "KEY_LOGOFF": "",
    "KEY_MEDIA_REPEAT": "",
    "KEY_IMAGES": "",
    "KEY_BUTTONCONFIG": "",
    "KEY_TASKMANAGER": "",
    "KEY_JOURNAL": "",
    "KEY_CONTROLPANEL": "",
    "KEY_APPSELECT": "",
    "KEY_SCREENSAVER": "",
    "KEY_VOICECOMMAND": bytes((0xCF, NULL_BYTE)), # bytes((207,))+NULL_CHAR
    "KEY_ASSISTANT": "",
    "?": "",
    "?": "",
    "KEY_BRIGHTNESS_MIN": "",
    "KEY_BRIGHTNESS_MAX": "",
    "KEY_KBDINPUTASSIST_PREV": "",
    "KEY_KBDINPUTASSIST_NEXT": "",
    "KEY_KBDINPUTASSIST_PREVGROUP": "",
    "KEY_KBDINPUTASSIST_NEXTGROUP": "",
    "KEY_KBDINPUTASSIST_ACCEPT": "",
    "KEY_KBDINPUTASSIST_CANCEL": "",
}

MOUSE_BUTTONS = {
    'BTN_LEFT': 1,
    'BTN_RIGHT': 2,
}


def is_consumer_control_scancode(scancode):
    return scancode.startswith('c')


def is_keyboard_scancode(scancode):
    return scancode.startswith('7')


def scan_code_to_bytes(scancode):
    # c01f4
    # Remove the page info at the front.
    # 01f4
    code = scancode[1:]
    # Split into pairs:
    # 01 f4
    # Reverse them:
    # f4 01
    # Into Bytes:
    # bytes((0xF4, 0x01))
    return code

'''
Record/List top left
Event: time 1654408498.010322, type 4 (EV_MSC), code 4 (MSC_SCAN), value c01f4
Event: time 1654408498.010322, type 1 (EV_KEY), code 240 (KEY_UNKNOWN), value 0
Event: time 1654408498.010322, -------------- SYN_REPORT ------------

Apps
Event: time 1654408539.689560, type 4 (EV_MSC), code 4 (MSC_SCAN), value c02ff
Event: time 1654408539.689560, type 1 (EV_KEY), code 240 (KEY_UNKNOWN), value 1
Event: time 1654408539.689560, -------------- SYN_REPORT ------------

Prime Video
Event: time 1654408556.218658, type 4 (EV_MSC), code 4 (MSC_SCAN), value c01fc
Event: time 1654408556.218658, type 1 (EV_KEY), code 240 (KEY_UNKNOWN), value 1
Event: time 1654408556.218658, -------------- SYN_REPORT ------------

Kids
Event: time 1654408573.859846, type 4 (EV_MSC), code 4 (MSC_SCAN), value c02fd
Event: time 1654408573.859846, type 1 (EV_KEY), code 240 (KEY_UNKNOWN), value 1
Event: time 1654408573.859846, -------------- SYN_REPORT ------------

Live TV/Exit
Event: time 1654408589.701873, type 4 (EV_MSC), code 4 (MSC_SCAN), value c02fe
Event: time 1654408589.701873, type 1 (EV_KEY), code 240 (KEY_UNKNOWN), value 1
Event: time 1654408589.701873, -------------- SYN_REPORT ------------

Top Picks
Event: time 1654408610.316754, type 4 (EV_MSC), code 4 (MSC_SCAN), value c02fc
Event: time 1654408610.316754, type 1 (EV_KEY), code 240 (KEY_UNKNOWN), value 1
Event: time 1654408610.316754, -------------- SYN_REPORT ------------

Magnifying Glass
Event: time 1654408631.256593, type 4 (EV_MSC), code 4 (MSC_SCAN), value c01c6
Event: time 1654408631.256593, type 1 (EV_KEY), code 240 (KEY_UNKNOWN), value 1
Event: time 1654408631.256593, -------------- SYN_REPORT ------------

Guide
Event: time 1654408647.310463, type 4 (EV_MSC), code 4 (MSC_SCAN), value c01f3
Event: time 1654408647.310463, type 1 (EV_KEY), code 240 (KEY_UNKNOWN), value 1
Event: time 1654408647.310463, -------------- SYN_REPORT ------------

Info:
Event: time 1654408682.630193, type 4 (EV_MSC), code 4 (MSC_SCAN), value c01c2
Event: time 1654408682.630193, type 1 (EV_KEY), code 240 (KEY_UNKNOWN), value 1
Event: time 1654408682.630193, -------------- SYN_REPORT ------------

Red:
Event: time 1654408699.009541, type 4 (EV_MSC), code 4 (MSC_SCAN), value c02f3
Event: time 1654408699.009541, type 1 (EV_KEY), code 240 (KEY_UNKNOWN), value 1
Event: time 1654408699.009541, -------------- SYN_REPORT ------------

Green:
Event: time 1654408708.304831, type 4 (EV_MSC), code 4 (MSC_SCAN), value c02f4
Event: time 1654408708.304831, type 1 (EV_KEY), code 240 (KEY_UNKNOWN), value 1
Event: time 1654408708.304831, -------------- SYN_REPORT ------------

Yellow
Event: time 1654408720.098940, type 4 (EV_MSC), code 4 (MSC_SCAN), value c02f5
Event: time 1654408720.098940, type 1 (EV_KEY), code 240 (KEY_UNKNOWN), value 1
Event: time 1654408720.098940, -------------- SYN_REPORT ------------

Blue:
Event: time 1654408736.877999, type 4 (EV_MSC), code 4 (MSC_SCAN), value c02f2
Event: time 1654408736.877999, type 1 (EV_KEY), code 240 (KEY_UNKNOWN), value 1
Event: time 1654408736.877999, -------------- SYN_REPORT ------------

S/AD:
Event: time 1654408751.220642, type 4 (EV_MSC), code 4 (MSC_SCAN), value c02f8
Event: time 1654408751.220642, type 1 (EV_KEY), code 240 (KEY_UNKNOWN), value 1
Event: time 1654408751.220642, -------------- SYN_REPORT ------------



'''

keys_system_control = {
    "KEY_POWER": bytes((0x81, NULL_BYTE)),
    "KEY_SLEEP": bytes((0x82, NULL_BYTE)),
    "KEY_WAKEUP": bytes((0x83, NULL_BYTE)),
}

# Until we implement mouse we will just make these look like key presses
keys_mouse = {
    "BTN_LEFT": keys_consumer_control['KEY_ENTER'],
    "BTN_RIGHT": keys_consumer_control['KEY_BACK'],
}



keys = {
    "UP": keys_consumer_control['KEY_UP'],
    "DOWN": keys_consumer_control['KEY_DOWN'],
    "LEFT": keys_consumer_control['KEY_LEFT'],
    "RIGHT": keys_consumer_control['KEY_RIGHT'],
    "SELECT": keys_consumer_control['KEY_ENTER'],
    "HOME": keys_consumer_control['KEY_HOMEPAGE'],
    "BACK": keys_consumer_control['KEY_BACK'],
    "PLAY": keys_consumer_control['KEY_PLAYPAUSE'],
    "MUTE": keys_consumer_control['KEY_MUTE'],
    "MIC": keys_consumer_control['KEY_VOICECOMMAND'],
}

