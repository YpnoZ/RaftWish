import pygame

class GameConfig:
  WINDOW_H=900
  WINDOW_W=1600
  PLAYER_W=20
  PLAYER_H=24
  BAT_W=20
  BAT_H=25
  VAGUE_W=325
  VAGUE_H=100
  DT=0.5
  FORCE_LEFT=-20
  FORCE_RIGHT=-FORCE_LEFT
  FORCE_UP=-20
  FORCE_DOWN=-FORCE_UP
  GRID=[]
  NB_FRAMES_PER_SPRITE_PLAYER=1
  TICKS_BETWEEN_BATONS=100
  TICKS_BETWEEN_CORDES=200
  TICKS_BETWEEN_TISSUS=300
  TICKS_BETWEEN_VAGUES=500
  BATON_MIN_SPEED=5
  BATON_MAX_SPEED=15
  VAGUE_MAX_SPEED=10
  VAGUE_MIN_SPEED=5
  INVENTORY={"lance":"","canneApeche":"","baton":0,"corde":0,"tissu":0,"silex":0,"radeau":100,"voile":10,"pique":10,"filet":50,"torche":10}
  QUANTITY_COORDS=[(525,850),(584,849),(643,850),(702,849),(761,850),(820,849),(879,850),(938,849),(997,850),(1056,849),(1115,850)]
  SELECTOR_COORDS=[(478,823),(534,825),(596,823),(652,825),(714,823),(770,825),(832,823),(888,825),(950,823),(1006,825),(1068,823)]
  HOTBAR_ICONS_COORDS=[(481,827),(537.5,828.5),(600,828),(656,829),(718,828),(774,829),(836,829),(893,830),(954,829),(1011,830),(1072,829)]
  HELP_COORDS=[[(418,616),(418,590),(418,568),(418,568),(418,619)],[(474,616),(474,591),(474,591),(474,591),(474,621)],(535,700),(592,700),(653,700),(709,690),(795,741),(827,657),(889,657),(945,682),(1007,682)]
  INDICE_OBJET=4
  TKINTER_INSTALLED=False
  IS_FULLSCREEN=False
  SOUND_ON=True
  CONTROLLER=False
  IMAGE = 1
  CURSOR = 0
  END = False
  TIME_ACCELERATION=1.0
  NB_VOILES=0

  #STATISTIQUES
  RADEAUX=0
  VOILES=0
  PIQUES=0
  FILETS=0
  TORCHES=0
  REQUINS_TUES=0
  RADEAUX_DETRUITS=0

  time=1
  SHARK_MAX_X=500
  SHARK_MAX_Y=800
  TICKS_BETWEEN_SHARKS = 200

  ROD_RANGES = [50, 100, 150, 200, 250]

  # Import des ressources
  def reset():
    GameConfig.INVENTORY={"lance":"","canneApeche":"","baton":0,"corde":0,"tissu":0,"silex":0,"radeau":100,"voile":10,"pique":10,"filet":50,"torche":10}
    GameConfig.INDICE_OBJET=4
    GameConfig.TIME_ACCELERATION=1.0
    GameConfig.NB_VOILES=0
    GameConfig.time=1
    GameConfig.END=False
    GameConfig.GRID=[]
    for i in range(18):
      GameConfig.GRID.append([])
      for j in range(32):
        GameConfig.GRID[i].append(0)
    GameConfig.GRID[8][15]={"type":"radeau","vie":100}
    GameConfig.GRID[8][16]={"type":"radeau","vie":100}
    GameConfig.GRID[9][15]={"type":"radeau","vie":100}
    GameConfig.GRID[9][16]={"type":"radeau","vie":100}
    GameConfig.RADEAUX=0
    GameConfig.VOILES=0
    GameConfig.PIQUES=0
    GameConfig.FILETS=0
    GameConfig.TORCHES=0
    GameConfig.REQUINS_TUES=0
    GameConfig.RADEAUX_DETRUITS=0
    
  def init():
    GameConfig.CONTROLLER_A_BUTTON_IMG=pygame.image.load('Ressources/Controller_A.png').convert_alpha()    
    GameConfig.CONTROLLER_B_BUTTON_IMG=pygame.image.load('Ressources/Controller_B.png').convert_alpha()    
    GameConfig.CONTROLLER_DISCONNECTED_IMG=pygame.image.load('Ressources/Controller_disconnected.png').convert_alpha()
    GameConfig.CONTROLLER_CONNECTED_IMG=pygame.image.load('Ressources/Controller_connected.png').convert_alpha()
    GameConfig.INV_CONTROLLER_IMG=pygame.image.load('Ressources/hotbar_controller.png').convert_alpha()
    
    GameConfig.aileD=pygame.image.load('Ressources/aileD.png').convert_alpha()
    GameConfig.aileD=pygame.transform.scale(GameConfig.aileD,(60,60))
    GameConfig.aileD_MASK=pygame.mask.from_surface(GameConfig.aileD)

    GameConfig.aileG=pygame.image.load('Ressources/aileG.png').convert_alpha()
    GameConfig.aileG=pygame.transform.scale(GameConfig.aileG,(60,60))
    GameConfig.aileG_MASK=pygame.mask.from_surface(GameConfig.aileG)

    #----------------------------------------------------------------------------
    #nouveaux sprites requin

    GameConfig.requinR1=pygame.image.load('Ressources/requinLR_1.png').convert_alpha()
    GameConfig.requinR1=pygame.transform.scale(GameConfig.requinR1,(60,30))
    GameConfig.requinR1_MASK=pygame.mask.from_surface(GameConfig.requinR1)

    GameConfig.requinR2=pygame.image.load('Ressources/requinLR_2.png').convert_alpha()
    GameConfig.requinR2=pygame.transform.scale(GameConfig.requinR2,(60,30))
    GameConfig.requinR2_MASK=pygame.mask.from_surface(GameConfig.requinR2)

    GameConfig.requinR3=pygame.image.load('Ressources/requinLR_3.png').convert_alpha()
    GameConfig.requinR3=pygame.transform.scale(GameConfig.requinR3,(60,30))
    GameConfig.requinR3_MASK=pygame.mask.from_surface(GameConfig.requinR3)

    GameConfig.requinR4=pygame.image.load('Ressources/requinLR_4.png').convert_alpha()
    GameConfig.requinR4=pygame.transform.scale(GameConfig.requinR4,(60,30))
    GameConfig.requinR4_MASK=pygame.mask.from_surface(GameConfig.requinR4)
    

    GameConfig.requinL1=pygame.image.load('Ressources/requinRL_1.png').convert_alpha()
    GameConfig.requinL1=pygame.transform.scale(GameConfig.requinL1,(60,30))
    GameConfig.requinL1_MASK=pygame.mask.from_surface(GameConfig.requinL1)

    GameConfig.requinL2=pygame.image.load('Ressources/requinRL_2.png').convert_alpha()
    GameConfig.requinL2=pygame.transform.scale(GameConfig.requinL2,(60,30))
    GameConfig.requinL2_MASK=pygame.mask.from_surface(GameConfig.requinL2)

    GameConfig.requinL3=pygame.image.load('Ressources/requinRL_3.png').convert_alpha()
    GameConfig.requinL3=pygame.transform.scale(GameConfig.requinL3,(60,30))
    GameConfig.requinL3_MASK=pygame.mask.from_surface(GameConfig.requinL1)

    GameConfig.requinL4=pygame.image.load('Ressources/requinRL_4.png').convert_alpha()
    GameConfig.requinL4=pygame.transform.scale(GameConfig.requinL4,(60,30))
    GameConfig.requinL4_MASK=pygame.mask.from_surface(GameConfig.requinL4)

    #----------------------------------------------------------------------------
    
    GameConfig.MAIN_MENU_IMG=pygame.image.load('Ressources/main_menu.png').convert_alpha()
    GameConfig.HELP_MENU_BUTTON_IMG=pygame.image.load('Ressources/help_menu_button.png').convert_alpha()
    GameConfig.HELP_MENU_BUTTON_RECT = GameConfig.HELP_MENU_BUTTON_IMG.get_rect(topleft=(654, 507))
    GameConfig.SETTINGS_MENU_BUTTON_IMG=pygame.image.load('Ressources/settings_menu_button.png').convert_alpha()
    GameConfig.SETTINGS_MENU_BUTTON_RECT = GameConfig.SETTINGS_MENU_BUTTON_IMG.get_rect(topleft=(654,627))

    GameConfig.END_IMG=pygame.image.load('Ressources/ending_menu.png').convert_alpha()
    GameConfig.MORT_IMG=pygame.image.load('Ressources/end_mort_menu.png').convert_alpha()
    
    GameConfig.SETTINGS_MENU_IMG=pygame.image.load('Ressources/settings_menu.png').convert_alpha()
    GameConfig.IMPORT_BUTTON_IMG=pygame.image.load('Ressources/upload_button.png').convert_alpha()
    GameConfig.IMPORT_BUTTON_2_IMG=pygame.image.load('Ressources/upload_button_2.png').convert_alpha()
    GameConfig.IMPORT_BUTTON_RECT = GameConfig.IMPORT_BUTTON_IMG.get_rect(topleft=(1071,604))
    GameConfig.BUTTON_ON_IMG=pygame.image.load('Ressources/button_on.png').convert_alpha()
    GameConfig.BUTTON_ON_FULLSCREEN_RECT = GameConfig.BUTTON_ON_IMG.get_rect(topleft=(150,442))
    GameConfig.BUTTON_ON_SOUND_RECT = GameConfig.BUTTON_ON_IMG.get_rect(topleft=(150,600))
    GameConfig.BUTTON_OFF_IMG=pygame.image.load('Ressources/button_off.png').convert_alpha()
    GameConfig.BUTTON_OFF_FULLSCREEN_RECT = GameConfig.BUTTON_OFF_IMG.get_rect(topleft=(150,442))
    GameConfig.BUTTON_OFF_SOUND_RECT = GameConfig.BUTTON_OFF_IMG.get_rect(topleft=(150,600))
    
    GameConfig.BACKGROUND_IMG=pygame.image.load('Ressources/background.png').convert_alpha()
    GameConfig.RADEAU_IMG=pygame.image.load('Ressources/radeau.png').convert_alpha()
    GameConfig.RADEAU_DAMAGED_IMG=pygame.image.load('Ressources/radeau_damaged.png').convert_alpha()
    GameConfig.RADEAU_FILET_IMG=pygame.image.load('Ressources/radeau_filet.png').convert_alpha()
    GameConfig.RADEAU_FILET_DAMAGED_IMG=pygame.image.load('Ressources/radeau_filet_damaged.png').convert_alpha()
    GameConfig.RADEAU_PIQUES_IMG=pygame.image.load('Ressources/radeau_piques.png').convert_alpha()
    GameConfig.RADEAU_PIQUES_DAMAGED_IMG=pygame.image.load('Ressources/radeau_piques_damaged.png').convert_alpha()
    GameConfig.RADEAU_VOILE_IMG=pygame.image.load('Ressources/sail.png').convert_alpha()
    GameConfig.TIMER_IMG=pygame.image.load('Ressources/timer.png').convert_alpha()
    GameConfig.INV_IMG=pygame.image.load('Ressources/hotbar.png').convert_alpha()
    GameConfig.SELECT_IMG=[pygame.image.load('Ressources/selector1.png').convert_alpha(),pygame.image.load('Ressources/selector2.png').convert_alpha()]
    GameConfig.HOTBAR_ICONS_IMG=[pygame.image.load('Ressources/hammer_OK.png').convert_alpha(),pygame.image.load('Ressources/hammer_NOK.png').convert_alpha(),pygame.image.load('Ressources/upgrade_OK.png').convert_alpha(),pygame.image.load('Ressources/upgrade_NOK.png').convert_alpha(),pygame.image.load('Ressources/help.png').convert_alpha()]
    GameConfig.STANDING_IMGS=[
      pygame.image.load('Ressources/standing.png').convert_alpha()
    ]
    GameConfig.WALKING_LEFT_IMGS=[
      pygame.image.load('Ressources/left01.png').convert_alpha()
    ]
    GameConfig.WALKING_RIGHT_IMGS=[
      pygame.image.load('Ressources/right01.png').convert_alpha()
    ]
    GameConfig.WALKING_TOP_IMGS=[
      pygame.image.load('Ressources/top01.png').convert_alpha()
    ]
    GameConfig.HELP_IMGS=[[pygame.image.load('Ressources/help_lance1.png').convert_alpha(),pygame.image.load('Ressources/help_lance2.png').convert_alpha(),pygame.image.load('Ressources/help_lance3.png').convert_alpha(),pygame.image.load('Ressources/help_lance4.png').convert_alpha(),pygame.image.load('Ressources/help_lance5.png').convert_alpha()],[pygame.image.load('Ressources/help_rod1.png').convert_alpha(),pygame.image.load('Ressources/help_rod2.png').convert_alpha(),pygame.image.load('Ressources/help_rod3.png').convert_alpha(),pygame.image.load('Ressources/help_rod4.png').convert_alpha(),pygame.image.load('Ressources/help_rod5.png').convert_alpha()],pygame.image.load('Ressources/help_baton.png').convert_alpha(),pygame.image.load('Ressources/help_corde.png').convert_alpha(),pygame.image.load('Ressources/help_tissu.png').convert_alpha(),pygame.image.load('Ressources/help_dent.png').convert_alpha(),pygame.image.load('Ressources/help_radeau.png').convert_alpha(),pygame.image.load('Ressources/help_voile.png').convert_alpha(),pygame.image.load('Ressources/help_pique.png').convert_alpha(),pygame.image.load('Ressources/help_filet.png').convert_alpha(),pygame.image.load('Ressources/help_torche.png').convert_alpha()]
    GameConfig.WALKING_LEFT_MASKS=[]
    GameConfig.WALKING_RIGHT_MASKS=[]
    GameConfig.STANDING_MASKS=[]
    GameConfig.TOP_MASKS=[]
    for im in GameConfig.STANDING_IMGS:
      GameConfig.STANDING_MASKS.append(pygame.mask.from_surface(im))
    for im in GameConfig.WALKING_LEFT_IMGS:
      GameConfig.WALKING_LEFT_MASKS.append(pygame.mask.from_surface(im))
    for im in GameConfig.WALKING_RIGHT_IMGS:
      GameConfig.WALKING_RIGHT_MASKS.append(pygame.mask.from_surface(im))
    for im in GameConfig.WALKING_TOP_IMGS:
      GameConfig.TOP_MASKS.append(pygame.mask.from_surface(im))
    GameConfig.STATS_IMG=pygame.image.load('Ressources/stats_frame.png').convert_alpha()
    
    GameConfig.BATON_IMG=pygame.image.load('Ressources/baton.png').convert_alpha()
    GameConfig.BATON_HALO=pygame.image.load('Ressources/baton_halo.png').convert_alpha()
    GameConfig.CORDE_IMG=pygame.image.load('Ressources/corde.png').convert_alpha()
    GameConfig.CORDE_HALO=pygame.image.load('Ressources/corde_halo.png').convert_alpha()
    GameConfig.SILEX_IMG=pygame.image.load('Ressources/silex.png').convert_alpha()
    GameConfig.SILEX_HALO=pygame.image.load('Ressources/silex_halo.png').convert_alpha()
    GameConfig.TISSU_IMG=pygame.image.load('Ressources/tissu.png').convert_alpha()
    GameConfig.TISSU_HALO=pygame.image.load('Ressources/tissu_halo.png').convert_alpha()

    GameConfig.VAGUE_IMG1=pygame.image.load('Ressources/vague1.png').convert_alpha()
    GameConfig.VAGUE_IMG2=pygame.image.load('Ressources/vague2.png').convert_alpha()
    GameConfig.VAGUE_IMG3=pygame.image.load('Ressources/vague3.png').convert_alpha()
    GameConfig.VAGUE_IMG4=pygame.image.load('Ressources/vague4.png').convert_alpha()
    GameConfig.VAGUE_IMG5=pygame.image.load('Ressources/vague5.png').convert_alpha()
    
    GameConfig.TORCHE_IMG=pygame.image.load('Ressources/torch.png').convert_alpha()
    GameConfig.LIGHT_IMG=pygame.image.load('Ressources/light.png').convert_alpha()

    for i in range(18):
      GameConfig.GRID.append([])
      for j in range(32):
        GameConfig.GRID[i].append(0)
    GameConfig.GRID[8][15]={"type":"radeau","vie":100}
    GameConfig.GRID[8][16]={"type":"radeau","vie":100}
    GameConfig.GRID[9][15]={"type":"radeau","vie":100}
    GameConfig.GRID[9][16]={"type":"radeau","vie":100}
    
    GameConfig.FONT60=pygame.font.Font('Ressources/timerFont.ttf',60)
    GameConfig.FONT18=pygame.font.Font('Ressources/timerFont.ttf',18)
    GameConfig.FONT22=pygame.font.Font('Ressources/font.ttf',22)

    GameConfig.CRAFT_RECTs=[]
    for i in range(11):
      GameConfig.CRAFT_RECTs.append(pygame.Rect(GameConfig.HOTBAR_ICONS_COORDS[i][0]-3,GameConfig.HOTBAR_ICONS_COORDS[i][1]-2,17,14))
      
    joystick_count = pygame.joystick.get_count()
    if joystick_count != 0:
      GameConfig.CONTROLLER=pygame.joystick.Joystick(0)
      
    #sounds
    GameConfig.SELECTED_SOUND=pygame.mixer.Sound('Ressources/selection.wav')
    GameConfig.PICK_UP_SOUND=[pygame.mixer.Sound('Ressources/item_pickup_1.wav'),pygame.mixer.Sound('Ressources/item_pickup_2.wav'),pygame.mixer.Sound('Ressources/item_pickup_3.wav'),pygame.mixer.Sound('Ressources/item_pickup_4.wav')]
    # GameConfig.HIT_SOUND=[pygame.mixer.Sound('Ressources/shark_hit_1.wav'),pygame.mixer.Sound('Ressources/shark_hit_2.wav'),pygame.mixer.Sound('Ressources/shark_hit_3.wav')]
    # GameConfig.DEATH_SOUND=[pygame.mixer.Sound('Ressources/shark_death_1.wav'),pygame.mixer.Sound('Ressources/shark_death_2.wav'),pygame.mixer.Sound('Ressources/shark_death_3.wav')]