import pygame
import os
from all_image import *
from button import Button
from level_setting import level_setting


class Button_menu:
    """
    Set on the button of the game screen. Let player choose the cat to fight virus.
    """
    def __init__(self, level):
        self.__buttons = level_setting[level]['cats_but']

    def get_buttons(self):
        return self.__buttons




