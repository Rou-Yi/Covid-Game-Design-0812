import pygame
import os
import math, random
from settings import PATH_E
from all_image import *


class Virus:
    # [圖像. 名字. 血量. 攻擊力. 攻擊範圍. 移動步伐]
    def __init__(self, image, name, health, damage, attack_range, stride):
        self.type = name
        self.path = PATH_E(random.choice([360, 370, 380, 390, 400, 410, 420]))
        self.path_index = 0
        self.move_count = 0
        self.stride = stride  # 移動步伐
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]

        self.health = health
        self.max_health = health  # 血量
        self.damage = damage  # 攻擊力
        self.attack_range = attack_range  # 攻擊範圍
        self.cd_count = 0
        self.cd_max_count = 60

    def check_moving(self, ally_group):
        """
        Check whether virus reaches the cat or virus is at the last point.
        :param ally_group: AllyGroup()
        :return: boolean
        """
        # Control the move
        moving = True
        for cat in ally_group.get():
            # calculate the distance between cat and virus
            dist = abs(cat.rect.x - self.rect.x)
            if dist <= self.attack_range:
                moving = False  # stop moving
                break
        if self.path_index == len(self.path) - 1:
            moving = False
        return moving

    def move(self):
        """
        Virus move until reaching the last point.
        :return: none
        """
        x1, y1 = self.path[self.path_index]
        x2, y2 = self.path[self.path_index + 1]
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        max_count = int(distance / self.stride)
        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance
        # compute the movement
        delta_x = unit_vector_x * self.stride * self.move_count
        delta_y = unit_vector_y * self.stride * self.move_count
        # update the position and counter
        if self.move_count < max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_count += 1
        else:
            self.move_count = 0
            self.path_index += 1
            self.rect.center = self.path[self.path_index]

    def attack(self, ally_group):
        """
        Virus attack action.
        :param ally_group: AllyGroup()
        :return cd time: int
        """
        if self.cd_count < self.cd_max_count:
            self.cd_count += 1
        else:
            # attack cat
            for cat in ally_group.get():
                dist_cat = abs(self.rect.x - cat.rect.x)
                # if in range, go on an attack, and cause damage
                if dist_cat <= self.attack_range:
                    cat.health -= self.damage
                    self.cd_count = 0
                    return
            # attack tower
            dist_tw = abs(self.rect.x - ally_group.tower.rect.right)
            if dist_tw <= self.attack_range:
                ally_group.tower.health -= self.damage
                self.cd_count = 0
                return
            # if no attack, keep CD count
            self.cd_count = 61

    # 用繼承寫出病毒種類
    @classmethod
    def Normal_Virus(cls):  # 第一種普通貓
        normal_virus = cls(NORMAL_VIRUS_IMAGE, 'normal_virus',
                           health=100, damage=15, attack_range=110, stride=1)
        return normal_virus

