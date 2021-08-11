import os
from settings import *

# background image
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "background.jpg")), (WIN_WIDTH, WIN_HEIGHT))
MENU_BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("images", "menu background.jpeg")), (WIN_WIDTH, WIN_HEIGHT))
# LOGO image
LOGO_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "LOGO1.png")), (726, 280))
LOGO_IMAGE_small = pygame.transform.scale(pygame.image.load(os.path.join("images", "LOGO_small.png")), (183, 69))

# button for main menu
LEVEL_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "level_button.png")), (300, 135))
INTRO_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "introduction_button.png")), (300, 135))

# button for introduction menu
RETURN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "arrow.png")), (100, 50))
WAIT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "wait.png")), (400, 350))

# button for level menu (open / close)
LV1_OP_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv1.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))
LV2_OP_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv2.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))
LV3_OP_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv3.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))
LV4_OP_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv4.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))
LV5_OP_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv5.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))

LV2_CL_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv2_CL.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))
LV3_CL_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv3_CL.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))
LV4_CL_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv4_CL.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))
LV5_CL_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "Lv5_CL.png")), (LV_BTN_WIDTH, LV_BTN_HEIGHT))

# game over image
WIN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "win.png")), (768, 317))
LOSE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "lose.png")), (812, 312))
BTN_W, BTN_H = 364, 135
NEXT_BTN = pygame.transform.scale(pygame.image.load(os.path.join("images", "next_level.png")), (BTN_W, BTN_H))
BACK_BTN = pygame.transform.scale(pygame.image.load(os.path.join("images", "back_to_menu.png")), (BTN_W, BTN_H))

# cat image
NORMAL_CAT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "cat.png")), (50, 55))
MASK_CAT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "mask_cat.png")), (50, 55))
SANI_CAT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "sanitizer_cat.png")), (70, 70))
VACCINE_CAT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "vaccine_cat.png")), (70, 75))

# cat button image
NORMAL_CAT_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("images", "cat_button.png")), (150, 150))
MASK_CAT_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("images", "mask_cat_button.png")), (150, 150))
SANI_CAT_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("images", "sanitizer_cat_button.png")), (150, 150))
VACCINE_CAT_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("images", "vaccine_cat_button.png")), (150, 150))

# virus image
NORMAL_VIRUS_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "virus.png")), (50, 50))

# tower image
TOWER_IMG_PL = pygame.transform.scale(pygame.image.load(os.path.join("images", "tower.png")), (TOWER_WIDTH, TOWER_HEIGHT))
TOWER_IMG_CP = pygame.transform.scale(pygame.image.load(os.path.join("images", "tower 2.png")), (TOWER_WIDTH, TOWER_HEIGHT))

# introduce page
INTRODUCE01 = pygame.transform.scale(pygame.image.load(os.path.join("images", "introduce01.jpg")), (WIN_WIDTH, WIN_HEIGHT))
INTRODUCE02 = pygame.transform.scale(pygame.image.load(os.path.join("images", "introduce02.jpg")), (WIN_WIDTH, WIN_HEIGHT))

