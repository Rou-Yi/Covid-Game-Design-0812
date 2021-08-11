import pygame
import os
import math, random
from settings import PATH_P
from all_image import *


class Cats:
    # [圖像. 名字. 血量. 攻擊力. 攻擊範圍. 移動步伐. 招喚消耗]
    def __init__(self, image, name, health, damage, attack_range, stride, cost):
        self.type = name
        self.path = PATH_P(random.choice([360, 370, 380, 390, 400, 410, 420]))
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
        self.cost = cost  # 招喚消耗
        self.cd_count = 0
        self.cd_max_count = 30

    def check_moving(self, enemy_group):
        """
        Check whether cat reaches the virus or cat is at the last point.
        :param enemy_group: EnemyGroup()
        :return: boolean
        """
        # Control the move
        moving = True
        for virus in enemy_group.get():
            # calculate the distance between cat and virus
            dist = abs(virus.rect.x - self.rect.x)
            if dist <= self.attack_range:
                moving = False  # stop moving
                break
        if self.path_index == len(self.path) - 1:
            moving = False
        return moving

    def move(self):
        """
        Cat moves until reaching the last point.
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

    def attack(self, enemy_group):
        """
        Cat attack action.
        :param enemy_group: EnemyGroup
        :return cd time: int
        """
        # 當CD滿足時，執行攻擊
        if self.cd_count < self.cd_max_count:
            self.cd_count += 1
        else:
            # attack virus
            for en in enemy_group.get():
                dist_en = abs(self.rect.x - en.rect.x)
                # if in range, go on an attack, and cause damage
                if dist_en <= self.attack_range:
                    en.health -= self.damage
                    self.cd_count = 0
                    return
            # attack tower
            dist_tw = abs(self.rect.x - enemy_group.tower.rect.left)
            if dist_tw <= self.attack_range:
                enemy_group.tower.health -= self.damage
                self.cd_count = 0
                return
            # if no attack, keep CD count
            self.cd_count = 61

    @property
    def get_cost(self):
        return self.cost

    # 用繼承寫出貓咪種類
    @classmethod
    def Normal_Cat(cls):  # 第一種普通貓
        normal_cat = cls(NORMAL_CAT_IMAGE, 'normal',
                         health=50, damage=15, attack_range=100, stride=1.2, cost=10)
        return normal_cat

    @classmethod
    def Mask_Cat(cls):  # 第二種口罩貓
        mask_cat = cls(MASK_CAT_IMAGE, 'mask',
                       health=200, damage=20, attack_range=120, stride=1.3, cost=15)
        return mask_cat

    @classmethod
    def Sanitizer(cls):
        sanitizer = cls(SANI_CAT_IMAGE, 'sanitizer',
                        health=180, damage=25, attack_range=120, stride=0.8, cost=30)
        return sanitizer

    """
    @classmethod
    def Alcohol(cls):
        alcohol = cls(MASK_CAT_IMAGE, 'alcohol',
                        health=180, damage=10, attack_range=120, stride=0.8, cost=10)
        return alcohol

    @classmethod
    def Vaccine(cls):
        vaccine = cls(MASK_CAT_IMAGE, 'vaccine',
                        health=180, damage=10, attack_range=120, stride=0.8, cost=10)
        return vaccine
    """