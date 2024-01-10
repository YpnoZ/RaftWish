import pygame
from game_config import *
import math

class Shark():

    def __init__(self,x,y,vx,vy):

        self.rect=pygame.Rect(x,y,vx,vy)
        
        self.health=10
        self.vx=vx
        self.vy=vy

        self.aileD=GameConfig.aileD
        self.maskD=GameConfig.aileD_MASK

        self.aileG=GameConfig.aileG
        self.maskG=GameConfig.aileG_MASK

        self.image=self.aileD

        self.sur_radeau=False
        self.radeau_casse=False

        self.dead=False


    def draw(self,window):
        #window.blit(self.aileD,self.rect.topleft)
        window.blit(self.image,self.rect)
    
    def perdre_vie(self):
        self.health-=1

    def is_dead(self):
        return self.health<=0 or self.dead==True

    def advance_state(self,player_x,player_y):
        #dans une première partie, on calcule le déplacement du requin
        #ensuite on teste si il est sur un radeau
        #       si oui on enleve de la vie au radeau et on ne bouge plus le requin
        #       sinon on bouge le requin avec le déplacement calculé
        #       si le requin a déjà été en contact avec un radeau, mais ne l'est plus, cela veut dire que le radeau a été cassé. On fait alors disparaitre le requin.
        vitesse=4
        #---------------------------------------------------------------------
        amplitude = 7   # Amplitude de l'ondulation
        frequency = 0.1  # Fréquence de l'ondulation

        # Calcul de la différence entre la position actuelle et la position du joueur
        diff_x = player_x - self.rect.centerx
        diff_y = player_y - self.rect.centery

        # Calcul de l'angle entre la position actuelle et le centre de la fenêtre
        angle = math.atan2(diff_y, diff_x)
        
        # Calcul des déplacements en fonction de l'angle
        move_x = vitesse * math.cos(angle)
        move_y = vitesse * math.sin(angle)

        # Ajout d'une ondulation à la trajectoire en fonction du temps
        wave_y = amplitude * math.sin(frequency * GameConfig.time)
        move_y += wave_y  # Ajoute l'ondulation à l'axe vertical

        wave_x = (amplitude//2) * math.sin(frequency * GameConfig.time)
        move_x += wave_x  # Ajoute l'ondulation à l'axe horizontal

        #-------------------------Test si sur un radeau-------------------------------------

        top_left_x = math.floor(self.rect.left/50)     #coin en haut à gauche
        top_left_y = math.floor(self.rect.top/50)

        top_right_x=math.ceil(self.rect.right/50)     #coin en haut à droite
        top_right_y=math.floor(self.rect.top/50)

        bottom_right_x = math.ceil(self.rect.right/50)     #coin en bas à droite
        bottom_right_y = math.ceil(self.rect.bottom/50)

        bottom_left_x = math.floor(self.rect.left/50)     #coin en bas à gauche
        bottom_left_y = math.ceil(self.rect.bottom/50)

        maxx=len(GameConfig.GRID[1])
        maxy=len(GameConfig.GRID)

        if self.radeau_casse:
            self.dead=True

        if (maxy>top_left_y and maxx>bottom_right_x and maxy>bottom_right_y and maxx>top_left_x and maxy>top_right_y and maxx>bottom_left_x and maxy>bottom_left_y and maxx>top_right_x):
            if GameConfig.GRID[top_left_y][top_left_x]!=0 :
                pos_x_radeau=top_left_x
                pos_y_radeau=top_left_y

                self.sur_radeau=True                                      #on indique que le requin est sur une case

                if GameConfig.GRID[pos_y_radeau][pos_x_radeau].get("vie")>0:            # si le radeau a une vie > 0     
                     GameConfig.GRID[pos_y_radeau][pos_x_radeau]["vie"]-=0.5         # alors on baisse la vie
                
                GameConfig.time+=1
                self.image=self.aileG
                
            elif GameConfig.GRID[bottom_right_y][bottom_right_x]!=0 :
                pos_x_radeau=bottom_right_x
                pos_y_radeau=bottom_right_y

                self.sur_radeau=True                                      #on indique que le requin est sur une case

                if GameConfig.GRID[pos_y_radeau][pos_x_radeau].get("vie")>0:            # si le radeau a une vie > 0     
                     GameConfig.GRID[pos_y_radeau][pos_x_radeau]["vie"]-=0.5         # alors on baisse la vie

                GameConfig.time+=1
                self.image=self.aileD

            elif GameConfig.GRID[top_right_y][top_right_x]!=0 :
                pos_x_radeau=top_right_x
                pos_y_radeau=top_right_y

                self.sur_radeau=True                                      #on indique que le requin est sur une case
        
                if GameConfig.GRID[pos_y_radeau][pos_x_radeau].get("vie")>0:            # si le radeau a une vie > 0     
                     GameConfig.GRID[pos_y_radeau][pos_x_radeau]["vie"]-=0.5         # alors on baisse la vie

                GameConfig.time+=1
                self.image=self.aileD
            
            elif GameConfig.GRID[bottom_left_y][bottom_left_x]!=0 :
                pos_x_radeau=bottom_left_x
                pos_y_radeau=bottom_left_y

                self.sur_radeau=True                                      #on indique que le requin est sur une case

                if GameConfig.GRID[pos_y_radeau][pos_x_radeau].get("vie")>0:            # si le radeau a une vie > 0     
                     GameConfig.GRID[pos_y_radeau][pos_x_radeau]["vie"]-=0.5         # alors on baisse la vie

                GameConfig.time+=1
                self.image=self.aileG

            else:                                            #si le requin n'est en contact avec aucun radeau
                if self.sur_radeau:                    #et qu'il en a déjà trouvé un 
                    self.dead=True                           #alors cela veut dire qu'il en a déjà cassé un et on le fait disparaître
                    self.radeau_casse=True

        #-----------------------------déplacement si pas sur radeau-------------------------------------
        if not self.sur_radeau:
            if int(move_x)>=0:
                self.image=self.aileD
            else:
                self.image=self.aileG
            GameConfig.time+=1
            self.rect=self.rect.move(int(move_x), int(move_y))