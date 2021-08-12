from all_image import *
from button import Button

level_setting = {
    'level_1': {
        'cats_name': ['normal', 'mask'],
        'cats_but': [Button(NORMAL_CAT_BUTTON, "normal", 475, 600),
                     Button(MASK_CAT_BUTTON, "mask", 725, 600)],
        'mana_value': 40,
        'next level': 'level_2'
    },
    'level_2': {
        'cats_name': ['normal', 'mask', 'sanitizer'],
        'cats_but': [Button(NORMAL_CAT_BUTTON, "normal", 400, 600),
                     Button(MASK_CAT_BUTTON, "mask", 600, 600),
                     Button(SANI_CAT_BUTTON, "sanitizer", 800, 600)],
        'mana_value': 80,
        'next level': 'level'  # 目前沒有第三關
    }
}





