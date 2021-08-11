import pygame
from ally.cat import Cats
from level_setting import level_setting

"""This module is import in model.py"""

"""
Here we demonstrate how does the Observer Pattern work
Once the subject updates, if will notify all the observer who has register the subject
"""


class RequestSubject:
    def __init__(self, model):
        self.__observers = []
        self.model = model

    def register(self, observer):
        self.__observers.append(observer)

    def notify(self, user_request):
        for o in self.__observers:
            o.update(user_request, self.model)


class CatsGenerator:
    def __init__(self, subject, level):
        subject.register(self)
        self.cats_name = level_setting[level]['cats_name']

    def update(self, user_request: str, model):
        """add new cat"""
        for name in self.cats_name:
            if user_request == name:
                cats_dict = {'normal': Cats.Normal_Cat(), 'mask': Cats.Mask_Cat(), 'sanitizer': Cats.Sanitizer()}
                new_cats = cats_dict[user_request]

                if model.mana_value >= new_cats.get_cost:
                    model.mana_value -= new_cats.get_cost
                    model.mana.mana_update(model.mana_value)
                    model.allies.get().append(new_cats)
                    # The last step also means 'campaign cats'


