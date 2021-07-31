import pygame
from pygame import *

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 10, 20)

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Three in a row"
        self.startx, self.starty = self.mid_w, self.mid_h
        self.start2x, self.start2y = self.mid_w, self.mid_h + 30
        self.exitx, self.exity = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.start2x - 120, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2 , self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text("Three in a row", 15, self.startx, self.starty)
            self.game.draw_text("Multiplicity", 15, self.start2x, self.start2y)
            self.game.draw_text("Exit", 15, self.exitx, self.exity)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Three in a row':
                self.cursor_rect.midtop = (self.start2x - 110, self.start2y)
                self.state = 'Multiplicity'
            elif self.state == 'Multiplicity':
                self.cursor_rect.midtop = (self.exitx - 50, self.exity)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx - 120, self.starty)
                self.state = 'Three in a row'
        elif self.game.UP_KEY:
            if self.state == 'Three in a row':
                self.cursor_rect.midtop = (self.exitx - 50, self.exity)
                self.state = 'Exit'
            elif self.state == 'Multiplicity':
                self.cursor_rect.midtop = (self.startx - 120, self.starty)
                self.state = 'Three in a row'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.start2x - 110, self.start2y)
                self.state = 'Multiplicity'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Three in a row':
                self.game.playing = True
            elif self.state == 'Multiplicity':
                self.game.curr_menu = self.game.options
            elif self.state == 'Exit':
                self.game.curr_menu = self.game.exit
            self.run_display = False

# class OptionsMenu(Menu):
#     def __init__(self, game):
#         Menu.__init__(self, game)
#         self.volx, self.voly = self.mid_w, self.mid_h + 20
#
#     def display_menu(self):
#         self.run_display = True
#         while self.run_display:
#             self.game.check_events()
#             self.check_input()
#             self.game.display.fill((0, 0, 0))
#             self.game.draw_text('Multiplicity', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
#             self.draw_cursor()
#             self.blit_screen()
#
#     def check_input(self):
#         if self.game.BACK_KEY:
#             self.game.curr_menu = self.game.main_menu
#             self.run_display = False

class ExitMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Exit', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Are you sure?', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.game.draw_text('Press Enter to exit', 10, self.game.DISPLAY_W * 3 / 4, self.game.DISPLAY_H * 5 / 6)
            self.blit_screen()