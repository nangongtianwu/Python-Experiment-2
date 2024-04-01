# @Version  : 1.0
# @Author   : 彭翔
# @File     : button.py
# @TIME     : 2024/4/1 14:38
import pygame.font


class Button:
    """为游戏创建按钮的类"""

    def __init__(self, ai_game, msg):
        # 初始化按钮的属性
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 256, 64
        self.button_color = (50, 130, 246)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('Microsoft YaHei UI', 48)

        # 创建按钮的rect对象,并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self,msg):
        # 将msg渲染为图像,并使其在按钮上居中
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个用颜色填充的按钮,再绘制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def set_msg(self, msg):
        # 设置按钮牛的文本
        self._prep_msg(msg)
