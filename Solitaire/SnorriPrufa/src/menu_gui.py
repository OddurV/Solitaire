# -*- coding: cp1252 -*-
import pygame
import SolitaireGui
import Reglubok
from SolitaireGui import*

from pygame.locals import* 


FPS = 30
clock = pygame.time.Clock()

def Game_Run():
    game = Game()
    return game.start()

class Menu:
    selections = []
    selections_box_color = (0,0,0)
    box = []
    font_size = 40
    color_text =  (255, 128, 0)
    color_highlight = (255,255,204)
    font_path = 'data/fonts/menu_font.ttf'
    font = pygame.font.Font
    surface = pygame.Surface
    position = 0
    position_start = (0,0)
    menu_width = 0
    menu_height = 0

    class Box:
        text = ''
        box = pygame.Surface
        selections_box = pygame.Rect
        select_box = pygame.Rect
        
    def set_font(self, path):
        self.font_path = path
        
    def set_colors(self, text, selection):
        self.color_text =  text
        self.color_highlight = selection
        
    def get_position(self):
        return self.position
    
    def move_menu(self, top, left):
        self.position_start = (top,left) 
    
    def init(self, selections, surface):
        self.selections = selections
        self.surface = surface
        self.num_of_boxes = len(self.selections)
        self.create_structure()        
        
    def draw(self,move=0):
        if move:
            self.position += move 
            if self.position == -1:
                self.position = self.num_of_boxes - 1
            self.position %= self.num_of_boxes
        menu = pygame.Surface((self.menu_width, self.menu_height))
        menu.fill(self.selections_box_color)
        select_box = self.box[self.position].select_box
        pygame.draw.rect(menu,self.color_highlight,select_box)

        for i in xrange(self.num_of_boxes):
            menu.blit(self.box[i].box,self.box[i].selections_box)
        self.surface.blit(menu,self.position_start)
        return self.position

    def create_structure(self):
        self.menu_height = 0
        self.font = pygame.font.Font(self.font_path, self.font_size)
        for i in xrange(self.num_of_boxes):
            self.box.append(self.Box())
            self.box[i].text = self.selections[i]
            self.box[i].box = self.font.render(self.box[i].text, 1, self.color_text)
            self.box[i].selections_box = self.box[i].box.get_rect()
            space = int(self.font_size * 0.3)
            height = self.box[i].selections_box.height
            self.box[i].selections_box.left = space
            self.box[i].selections_box.top = space+(space*2+height)*i
            width = self.box[i].selections_box.width+space*2
            height = self.box[i].selections_box.height+space*2            
            left = self.box[i].selections_box.left-space
            top = self.box[i].selections_box.top-space
            self.box[i].select_box = (left,top ,width, height)
            if width > self.menu_width:
                    self.menu_width = width
            self.menu_height += height
        x = self.surface.get_rect().centerx - self.menu_width / 2
        y = self.surface.get_rect().centery - self.menu_height / 2 
        mx, my = self.position_start
        self.position_start = (x+mx, y+my)

if __name__ == "__main__":
    import sys
    if not pygame.display.get_init():
        pygame.display.init()

    if not pygame.font.get_init():
        pygame.font.init()
    
    surface = pygame.display.set_mode((720,480))
    surface.fill((0,0,0))
    
    '''
    screen = pygame.display.get_surface()
    background = 'data/images/background.jpg'
    background_surface = pygame.image.load(background)
    screen.blit(background_surface, (0,0)) 
    '''
    
    menu = Menu()
    menu.init(['Byrja','Topplisti', 'Reglur','Stoppa'], surface)
    menu.draw()
    pygame.key.set_repeat(200,50)
    pygame.display.set_caption('Klondike Solitaire')
    pygame.display.update()
    pygame.init() 
    pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=50)
    menu_music = pygame.mixer.Sound('data/music/menu_music.wav')
    key_up = pygame.mixer.Sound('data/music/up.wav')
    key_down = pygame.mixer.Sound('data/music/down.wav')
    key_quit = pygame.mixer.Sound('data/music/up.wav')
    key_down.set_volume(0.5)
    key_up.set_volume(0.5)
    icon = pygame.image.load('data/icon/icon.jpg')      
    pygame.display.set_icon(icon)
    menu_music.play(loops=-1)
    
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    key_up.play()
                    menu.draw(-1) 
                if event.key == K_DOWN:
                    key_down.play()
                    menu.draw(1)
                if event.key == K_RETURN:
                    if menu.get_position() == 0:
                        print('Byrja')
                        mygame = Game_Run()    
                        mygame.play(screen)
                    if menu.get_position() == 1:
                        print('Topplisti')
                    if menu.get_position() == 2:
                        print('Reglur')
                        mygame = Reglubok.display()
                        mygame.play(screen)
                    if menu.get_position() == 3:
                        pygame.display.quit()
                        sys.exit()                        
                if event.key == K_ESCAPE:
                    pygame.display.quit()
                    sys.exit()
                pygame.display.update()
            elif event.type == QUIT:
                pygame.display.quit()
                sys.exit()
