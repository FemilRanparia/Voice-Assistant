from main import voice_assistant

import keyboard

keyboard.add_hotkey('s', voice_assistant)

keyboard.wait('esc')