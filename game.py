import pygame
from game_config import *
from pygame.locals import *
from game_state import *
from move import *

try:
  # Vérifie si tkinter est installé
  from tkinter import filedialog
  GameConfig.TKINTER_INSTALLED=True
except ImportError:
  GameConfig.TKINTER_INSTALLED=False

# Fonctions utiles pour la gestion du jeu
# (affichage de message, rejouer etc.)

#Boucle de jeu
def game_loop(window):
  quitting=False
  game_state=GameState()
  GameConfig.reset()
  while not quitting and not game_state.ENDED:
    game_state.controller_state(window)
    next_move=get_next_move()
    game_state.advance_state(next_move,window)
    if not next_move.quit:
      game_state.draw(window)
    else:
      return pygame.quit()
    if next_move.escape:
      print('Menu pause')
      reprendre=False
      #ajout d'un filtre à l'écran
      filter_surface = pygame.Surface((GameConfig.WINDOW_W, GameConfig.WINDOW_H),pygame.SRCALPHA)
      pygame.draw.rect(filter_surface, (128, 128, 128, 51), filter_surface.get_rect())
      window.blit(filter_surface, (0, 0), special_flags=BLEND_RGBA_MULT)
      GameState.display_message(window,"PAUSE",60,GameConfig.WINDOW_W/2,GameConfig.WINDOW_H/2,"center",(255,255,255))
      GameState.display_message(window,"Appuyez sur ECHAP pour reprendre",60,GameConfig.WINDOW_W/2,GameConfig.WINDOW_H/2+70,"center",(255,255,255))
      pygame.display.update()
      while True:
        for event in pygame.event.get():
          if event.type==WINDOWEXPOSED:
            pygame.display.update()
          if GameConfig.CONTROLLER:
            if event.type==JOYBUTTONDOWN and event.button==7:
              print('Jeu repris')
              reprendre=True
          if event.type == KEYDOWN and event.key == K_ESCAPE:
            print('Jeu repris')
            reprendre=True
          if event.type==QUIT:
            return pygame.quit()
        if reprendre:
          break
    pygame.display.update()
    pygame.time.delay(35)
  if game_state.ENDED:
      return end_menu(window,game_state.MORT, game_state.TEMPS_ECOULE)


# Détection des input du joueur
def get_next_move():
  next_move=Move()
  keys=pygame.key.get_pressed()
  next_move.pos = pygame.mouse.get_pos()
  if keys[K_q]:
    next_move.left = True
  if keys[K_d]:
    next_move.right = True
  if keys[K_z]:
    next_move.up = True
  if keys[K_s]:
    next_move.down = True
  if keys[K_e]:
    next_move.e_pressed = True
  for event in pygame.event.get():
    if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:  # Left click
          next_move.left_click = True
        elif event.button == 3:  # Right click
          next_move.right_click = True
    if event.type == MOUSEWHEEL:
        if event.y<0:
          next_move.scroll_up = True
        elif event.y>0:
          next_move.scroll_down = True      
    if event.type == KEYDOWN and event.key == K_ESCAPE:
      next_move.escape = True
    if event.type == QUIT:
        next_move.quit = True
    
    if event.type==WINDOWMINIMIZED: #Si fenêtre minimisée, menu pause
      next_move.escape = True
      
    if GameConfig.CONTROLLER:
      if event.type==JOYBUTTONDOWN:
        print(event.button)
        if event.button==7:
          next_move.escape = True
        elif event.button==0:
          next_move.left_click=True
        elif event.button==1:
          next_move.right_click=True
        elif event.button==2:
          next_move.e_pressed=True
        elif event.button==4:
          next_move.scroll_down=True
        elif event.button==5:
          next_move.scroll_up=True
  if GameConfig.CONTROLLER:
    if GameConfig.CONTROLLER.get_axis(0) > 0.5:
      next_move.right=True
    if  GameConfig.CONTROLLER.get_axis(0) < -0.5:
      next_move.left=True
    if GameConfig.CONTROLLER.get_axis(1) > 0.5:
      next_move.down=True
    if GameConfig.CONTROLLER.get_axis(1) < -0.5:
      next_move.up=True
  return next_move

# Gestion du menus

def end_menu(window, mort, temps_ecoule):
  game_state = GameState()
  while True:
    next_move=get_next_move()  
    menu_rect=pygame.Rect(1168,641,284,101)
    if temps_ecoule:
        window.blit(GameConfig.END_IMG,(0,0))
        stats_rect=pygame.Rect(841,641,284,101)
        if stats_rect.collidepoint(pygame.mouse.get_pos()):
          window.blit(GameConfig.STATS_IMG,(93,227))
          GameState.display_message(window,"x"+str(GameConfig.RADEAUX),22,182,493,"center",(0,0,0))
          GameState.display_message(window,"x"+str(GameConfig.VOILES),22,287,493,"center",(0,0,0))
          GameState.display_message(window,"x"+str(GameConfig.PIQUES),22,398,493,"center",(0,0,0))
          GameState.display_message(window,"x"+str(GameConfig.FILETS),22,512,493,"center",(0,0,0))
          GameState.display_message(window,"x"+str(GameConfig.TORCHES),22,618.5,493,"center",(0,0,0))
          GameState.display_message(window,"x"+str(GameConfig.REQUINS_TUES),22,245.5,701,"center",(0,0,0))
          GameState.display_message(window,"x"+str(GameConfig.RADEAUX_DETRUITS),22,555.5,701,"center",(0,0,0))
    elif mort:
      window.blit(GameConfig.MORT_IMG,(0,0))
      stats_rect=pygame.Rect(841,641,284,101)
      if stats_rect.collidepoint(pygame.mouse.get_pos()):
        window.blit(GameConfig.STATS_IMG,(93,227))
        GameState.display_message(window,"x"+str(GameConfig.RADEAUX),22,182,493,"center",(0,0,0))
        GameState.display_message(window,"x"+str(GameConfig.VOILES),22,287,493,"center",(0,0,0))
        GameState.display_message(window,"x"+str(GameConfig.PIQUES),22,398,493,"center",(0,0,0))
        GameState.display_message(window,"x"+str(GameConfig.FILETS),22,512,493,"center",(0,0,0))
        GameState.display_message(window,"x"+str(GameConfig.TORCHES),22,618.5,493,"center",(0,0,0))
        GameState.display_message(window,"x"+str(GameConfig.REQUINS_TUES),22,245.5,701,"center",(0,0,0))
        GameState.display_message(window,"x"+str(GameConfig.RADEAUX_DETRUITS),22,555.5,701,"center",(0,0,0))
    pygame.display.update()
    if menu_rect.collidepoint(next_move.pos):
      game_state.change_cursor(1)
      if next_move.left_click:
        GameConfig.END = True
        return main_menu(window)
    else:
      game_state.change_cursor(0)
    if next_move.quit:
      return pygame.quit()

def main_menu(window):
  while True:
    game_state=GameState()
    game_state.controller_state(window)
    window.blit(GameConfig.MAIN_MENU_IMG,(0,0))
    window.blit(GameConfig.HELP_MENU_BUTTON_IMG,(654,507))
    window.blit(GameConfig.SETTINGS_MENU_BUTTON_IMG,(654,627))
    GameState.display_message(window,"JOUER",60,GameConfig.WINDOW_W/2,806,"center",(255,255,255))
    if GameConfig.CONTROLLER:
      window.blit(GameConfig.CONTROLLER_A_BUTTON_IMG,(867,806))
    pygame.display.update()
    pos = pygame.mouse.get_pos()
    if GameConfig.HELP_MENU_BUTTON_RECT.collidepoint(pos) or GameConfig.SETTINGS_MENU_BUTTON_RECT.collidepoint(pos) or (GameConfig.WINDOW_W/2)-107 <= pos[0] <= (GameConfig.WINDOW_W/2)+107 and 762 <= pos[1] <= 844:
      game_state.change_cursor(1)
    else:
      game_state.change_cursor(0)
    for event in pygame.event.get([KEYDOWN, QUIT, MOUSEBUTTONDOWN, JOYBUTTONDOWN]):
      if event.type == QUIT:
        return pygame.quit()
      if event.type == MOUSEBUTTONDOWN:
        if GameConfig.HELP_MENU_BUTTON_RECT.collidepoint(pos):
          game_state.play_sound(GameConfig.SELECTED_SOUND)
          print("help_menu opened")
          return help_menu(window)
        elif GameConfig.SETTINGS_MENU_BUTTON_RECT.collidepoint(pos):
          game_state.play_sound(GameConfig.SELECTED_SOUND)
          print("settings_menu opened")
          return settings_menu(window)
        elif (GameConfig.WINDOW_W/2)-107 <= pos[0] <= (GameConfig.WINDOW_W/2)+107 and 762 <= pos[1] <= 844:
          game_state.play_sound(GameConfig.SELECTED_SOUND)
          return game_loop(window)
      if event.type == JOYBUTTONDOWN and GameConfig.CONTROLLER:
        if event.button==0:
          game_state.play_sound(GameConfig.SELECTED_SOUND)
          return game_loop(window)

# Gestion du menu d'aide
def help_menu(window):
  while True:
    window.blit(GameConfig.MAIN_MENU_IMG,(0,0))
    pygame.display.update()
    for event in pygame.event.get([KEYDOWN,QUIT]):
      if event.type==QUIT:
        return pygame.quit()
      if event.type==KEYDOWN:
        if event.key==K_ESCAPE:
          return main_menu(window)

# Gestions du menu des paramètres
def settings_menu(window):
  while True:
    game_state=GameState()
    window.blit(GameConfig.SETTINGS_MENU_IMG,(0,0))
    if GameConfig.IS_FULLSCREEN:
      window.blit(GameConfig.BUTTON_ON_IMG,(150,442))
    else:
      window.blit(GameConfig.BUTTON_OFF_IMG,(150,442))
    if GameConfig.SOUND_ON:
      window.blit(GameConfig.BUTTON_ON_IMG,(150,600))
    else:
      window.blit(GameConfig.BUTTON_OFF_IMG,(150,600))
    if GameConfig.TKINTER_INSTALLED:
      window.blit(GameConfig.IMPORT_BUTTON_IMG,(1071,604))
    else:
      window.blit(GameConfig.IMPORT_BUTTON_2_IMG,(1071,604))
    pygame.display.update()
    pos = pygame.mouse.get_pos()
    return_rect = pygame.Rect(13,13,110,110)
    if GameConfig.BUTTON_ON_FULLSCREEN_RECT.collidepoint(pos) or GameConfig.BUTTON_OFF_FULLSCREEN_RECT.collidepoint(pos) or GameConfig.BUTTON_ON_SOUND_RECT.collidepoint(pos) or GameConfig.BUTTON_OFF_SOUND_RECT.collidepoint(pos) or GameConfig.IMPORT_BUTTON_RECT.collidepoint(pos) or return_rect.collidepoint(pos):
      game_state.change_cursor(1)
    else:
      game_state.change_cursor(0)
    for event in pygame.event.get([KEYDOWN,QUIT,DROPFILE,MOUSEBUTTONDOWN]):
      if event.type==QUIT:
        return pygame.quit()

      if event.type==DROPFILE:
        game_state.load_img(event.file)
        
      if event.type==KEYDOWN:
        if event.key==K_ESCAPE:
          return main_menu(window)
        
      if event.type == MOUSEBUTTONDOWN:
        if GameConfig.BUTTON_ON_FULLSCREEN_RECT.collidepoint(pos) or GameConfig.BUTTON_OFF_FULLSCREEN_RECT.collidepoint(pos):
          GameConfig.IS_FULLSCREEN=not GameConfig.IS_FULLSCREEN
          if GameConfig.IS_FULLSCREEN:
            window = pygame.display.set_mode((GameConfig.WINDOW_W, GameConfig.WINDOW_H), FULLSCREEN)
          else:
            window = pygame.display.set_mode((GameConfig.WINDOW_W, GameConfig.WINDOW_H))
        
        if GameConfig.BUTTON_ON_SOUND_RECT.collidepoint(pos) or GameConfig.BUTTON_OFF_SOUND_RECT.collidepoint(pos):
          GameConfig.SOUND_ON=not GameConfig.SOUND_ON
        
        if return_rect.collidepoint(pos):
          return main_menu(window)
        
        #Utilisation de tkinter pour l'importation des textures si installé
        if GameConfig.TKINTER_INSTALLED:
          if GameConfig.IMPORT_BUTTON_RECT.collidepoint(pos):
            game_state.play_sound(GameConfig.SELECTED_SOUND)
            file_paths = filedialog.askopenfilenames(title='Selectionner le/les fichiers',filetypes=(('PNG files', '*.png'), ('Tous les fichiers', '*.*')))
            for file_path in file_paths:
              game_state.load_img(file_path)
      
#Lancement du jeu
if __name__ == '__main__':
  pygame.init()
  window = pygame.display.set_mode((GameConfig.WINDOW_W, GameConfig.WINDOW_H))
  pygame.joystick.init()
  pygame.mixer.init()
  GameConfig.init()
  Player.init_sprites()
  Baton.init_sprites()
  Corde.init_sprites()
  Tissu.init_sprites()
  Vague.init_sprites()
  Torche.init_sprites()
  pygame.display.set_caption('RaftWish')
  pygame.display.set_icon(GameConfig.STANDING_IMGS[0])
  main_menu(window)
  pygame.quit()
  quit()