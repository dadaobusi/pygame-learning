#!/usr/bin/env python
#-*- coding: cp936 -*-
# Filename: mymodule.py
# debug with python 2.7 win-xp
# --------------history end---------------------
import pygame
import sys
from pygame.locals import *

background_image_filename = 'background.jpg'
boy1_image_filename = 'boy1.png'
house_image_filename = 'house.png'
# init Pygame
pygame.init()

size = width, height = 600, 500

bg = (255, 255, 255) # RGB

screen = pygame.display.set_mode((640, 480), 0, 32)
#创建了一个窗口
pygame.display.set_caption("Hello, Xiao Ming!")
#设置窗口标题

background = pygame.image.load(background_image_filename)
#加载并转换图像
boy1 = pygame.image.load(boy1_image_filename).convert_alpha()
house = pygame.image.load(house_image_filename).convert_alpha()

while True:
#主循环
 
    for event in pygame.event.get():
        if event.type == QUIT:
            #接收到退出事件后退出程序
            exit()
 
    screen.blit(background, (0,0))
    #将背景图画上去
 
    # 把房子画上去
    x=100
    y=300
    screen.blit(house, (x, y))
    
    x, y = pygame.mouse.get_pos()
    #获得鼠标位置
    x-= boy1.get_width() / 2
    y-= boy1.get_height() / 2
    #计算光标的左上角位置
    screen.blit(boy1, (x, y))
    #把光标画上去
 
    pygame.display.update()
    #刷新一下画面
