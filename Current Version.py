import pygame, time, random, json, math

py72 = input('Run Game: ')

initiate = True
if initiate == True:
  file1 = 'save files\World 1\world.txt'
  file2 = 'save files\World 1\location.txt'
  file3 = 'save files\World 2\world.txt'
  file4 = 'save files\World 2\location.txt'
  file5 = 'save files\World 3\world.txt'
  file6 = 'save files\World 3\location.txt'
  file7 = 'save files\World 4\world.txt'
  file8 = 'save files\World 4\location.txt'
  files = [[file1, file2], [file3, file4], [file5, file6], [file7, file8]]

  w = 'in a way working'
  k = 'kinda working'
  b = 'bug'
  n = 'no bug here'

  pygame.init()
  Tree = pygame.image.load('images - Current Version/Tree.png')
  Tree = pygame.transform.scale(Tree, (59, 59))
  Options = pygame.image.load('images - Current Version/Options.png')
  Options = pygame.transform.scale(Options, (59, 59))

  key_up = False
  key_down = False
  key_left = False
  key_right = False
  Main_game = False
  Home_page = True
  Save = False
  Load = False
  ready = True

class camera:
  def __init__(self):
    self.x = 0
    self.y = 0
  
  def up(self):
    self.y += 120
  def down(self):
    self.y -= 120
  def left(self):
    self.x += 120
  def right(self):
    self.x -= 120

class map_tiles:
  def __init__(self):
    self.Iron_Ore = pygame.image.load('images - Current Version/iron Ore.png')
    self.Iron_Ore = pygame.transform.scale(self.Iron_Ore, (59, 59))
    self.Copper_Ore = pygame.image.load('images - Current Version/Copper Ore.png')
    self.Copper_Ore = pygame.transform.scale(self.Copper_Ore, (59, 59))
    self.Coal = pygame.image.load('images - Current Version/Coal Ore.png')
    self.Coal = pygame.transform.scale(self.Coal, (59, 59))
    self.Oil = pygame.image.load('images - Current Version/Oil.png')
    self.Oil = pygame.transform.scale(self.Oil, (59, 59))
    self.Uranium_Ore = pygame.image.load('images - Current Version/Uranium Ore.png')
    self.Uranium_Ore = pygame.transform.scale(self.Uranium_Ore, (59, 59))
    self.click = 0
    self.done_pt2 = False
    self.done_pt1 = False
    self.turn = 0
    self.river_length = []
    self.rivers = []
    self.direction = []
    self.numbers = []
    self.image = 100,100,59,59
    self.colour = 'blue'
    self.save_blue = []
    self.tile_heights = []
    self.next_river_tile = []
    self.animation = [101, 101]
    self.animation_turn = 0
    self.animation_x = 0
    self.oresx = []
    self.oresy = []
    self.ores = 161
    for i in range(30):
      self.next_river_tile.append([1000,1000])
      self.save_blue.append([])
      self.numbers.append([0,0])
      self.river_length.append(0)
      self.rivers.append(True)
      self.direction.append(0)
      i += 1
    x = -100
    while x < 100:
      y = -100
      self.tile_heights.append([])
      while y < 100:
        self.tile_heights[x + 100].append(0)
        y += 1
      x += 1
    self.x_distance_cam = 0
    self.y_distance_cam = 0
    self.islandx = []
    self.islandy = []
    for i in range(30):
      self.islandy.append(random.randint(-100, 100))
      self.islandx.append(random.randint(-100, 100))
    self.riverx = []
    self.rivery = []
    for i in range(30):
      self.rivery.append(random.randint(-100, 100))
      self.riverx.append(random.randint(-100, 100))
    self.colours = []
    for i in range(201):
      self.colours.append([])
      z = 0
      while z < 201:
        self.colours[i].append('blue')
        z += 1
    for i in range(161):
      self.oresy.append(random.randint(-100, 100))
      self.oresx.append(random.randint(-100, 100))
    i = 0
    
  def main_game(self):
    self.turn += 1
    self.number = 0
    x = -100
    while x < 99:
        y = -100
        while y < 99:
          if turn < 30 or [x + 100, y + 100] in self.next_river_tile or [x, y] == [-100, -100] or turn > 295:
            for i in range(30):
              if x == self.islandx[i] and y == self.islandy[i]:
                self.tile_heights[x + 100][y + 100] = random.randint(1,6)
            self.colour = 'black'
            if self.turn < 21:
              self.colours[x + 100][y + 100] = 'blue'
              number = 6
              while number > 0:
                if (self.tile_heights[x + 101][y + 100] == number or self.tile_heights[x + 99][y + 100] == number or self.tile_heights[x + 100][y + 101] == number or self.tile_heights[x + 100][y + 99] == number) and self.tile_heights[x + 100][y + 100] < 6:
                  heights_chance = [0]
                  for i in range(7 - number):
                    heights_chance.append(1)
                    i += 1
                  self.tile_heights[x + 100][y + 100] = number - random.choice(heights_chance)
                number -= 1
              if self.tile_heights[x + 100][y + 100] > 2:
                self.colour = 'green'
                self.colours[x + 100][y + 100] = 'green'
              if self.tile_heights[x + 101][y + 100] > 2 and self.tile_heights[x + 99][y + 100] > 2 and self.tile_heights[x + 100][y + 101] > 2 and self.tile_heights[x + 100][y + 99] > 2:
                self.colour = 'green'
                self.colours[x + 100][y + 100] = 'green'
            if turn < 21:
              if self.colours[x + 100][y + 100] == 'green':
                tree_random = random.randint(1,10)
                if self.colours[x + 101][y + 100] == 'Tree' or self.colours[x + 99][y + 100] == 'Tree' or self.colours[x + 100][y + 101] == 'Tree' or self.colours[x + 100][y + 99] == 'Tree':
                  if tree_random > 5:
                    self.colours[x + 100][y + 100] = 'Tree'
                else:
                  if tree_random > 9:
                    self.colours[x + 100][y + 100] = 'Tree'
            if self.turn > 20:
              i = 0
              while i < 30:
                if self.river_length[i] == 0:
                  if (turn == 21 and x == self.riverx[i] and y == self.rivery[i]) or x == self.next_river_tile[i][0] and y == self.next_river_tile[i][1]:
                    self.tile_heights[x + 100][y + 100] = 1
                    self.curve_type = random.randint(1,6)
                    self.river_length[i] = random.randint(6,30)
                    self.direction[i] = random.randint(0,3)
                    if self.curve_type == 1:
                      self.numbers[i] = [3,4]
                    elif self.curve_type == 2:
                      self.numbers[i] = [2,3]
                    elif self.curve_type == 3:
                      self.numbers[i] = [3,3,4]
                    elif self.curve_type == 4:
                      self.numbers[i] = [2,3,3]
                    elif self.curve_type == 5:
                      self.numbers[i] = [3,3,3,4]
                    elif self.curve_type == 6:
                      self.numbers[i] = [2,3,3,3]
                    self.number = random.choice(self.numbers[i]) - 1
                    self.directional_number = self.number
                    for z in range(self.direction[i]):
                      self.directional_number += 1
                      if self.directional_number > 3:
                        self.directional_number = 0
                    self.directions = [[x + 100, y + 99], [x + 101, y + 100], [x + 100, y + 101], [x + 99, y + 100]]
                    self.next_river_tile[i] = self.directions[self.directional_number]
                    self.colour = 'blue'
                    self.colours[x + 100][y + 100] = 'blue'
                i += 1
            if True in self.rivers:
              i = 0
              while i < 30:
                if x + 100 == self.next_river_tile[i][0] and y + 100 == self.next_river_tile[i][1] and self.rivers[i] == True and self.numbers[i] != [0,0] and turn > 20:
                  self.random_numbers = self.numbers[i]
                  if len(self.random_numbers) > 1:
                    self.number = random.choice(self.random_numbers) - 1
                  self.directional_number = self.number
                  for b in range(self.direction[i]):
                    self.directional_number += 1
                    if self.directional_number > 3:
                      self.directional_number = 0
                  self.directions = [[x + 100, y + 99], [x + 101, y + 100], [x + 100, y + 101], [x + 99, y + 100]]
                  if self.colours[x + 100][y + 100] == 'blue':
                    self.rivers[i] = False
                  else:
                    self.next_river_tile[i] = self.directions[self.directional_number]
                  if self.next_river_tile[i][0] < 1 or self.next_river_tile[i][0] > 200 or self.next_river_tile[i][1] < 1 or self.next_river_tile[i][1] > 200:
                    self.rivers[i] = False
                  self.colour = 'blue'
                  self.colours[x + 100][y + 100] = 'blue'
                i += 1
            river_start = 0
            for i in range(len(self.riverx)):
              if self.colours[x + 100][y + 100] == 'blue' and turn > 290 and not(x + 100 == self.riverx[i] and y + 100 == self.rivery[i]):
                river_start += 1
                if river_start == len(self.riverx):
                  surrounding = 0
                  if self.colours[x + 101][y + 100] == 'green' or self.colours[x + 101][y + 100] == 'Tree':
                    surrounding += 1
                  if self.colours[x + 99][y + 100] == 'green' or self.colours[x + 99][y + 100] == 'Tree':
                    surrounding += 1
                  if self.colours[x + 100][y + 101] == 'green' or self.colours[x + 100][y + 101] == 'Tree':
                    surrounding += 1
                  if self.colours[x + 100][y + 99] == 'green' or self.colours[x + 100][y + 99] == 'Tree':
                    surrounding += 1
                  if surrounding > 2:
                    self.colours[x + 100][y + 100] = 'green'
            if self.turn > 300:
              self.done_pt1 = True
              self.rivers = [False]
            if True not in self.rivers:
              self.done_pt1 = True
            if self.done_pt1 == True:
              for i in range(161):
                if x == self.oresx[i] and y == self.oresy[i]:
                  if self.colours[x + 100][y + 100] == 'green' or self.colours[x + 100][y + 100] == 'Tree':
                    if i < 1:
                      self.colours[x + 100][y + 100] = 'Uranium'
                    elif i < 6:
                      self.colours[x + 100][y + 100] = 'Oil'
                    elif i < 21:
                      self.colours[x + 100][y + 100] = 'Coal'
                    elif i < 61 :
                      self.colours[x + 100][y + 100] = 'Copper'
                    else:
                      self.colours[x + 100][y + 100] = 'Iron'
                    self.ores -= 1
                  else:
                    self.oresx[i] = random.randint(-100, 100)
                    self.oresy[i] = random.randint(-100, 100)
            if self.ores == 0:
              self.done_pt2 = True
          y += 1
        x += 1
  
  def running(self,Tree):
    x = max(-round(game_cam.x/60) - 1, -80)
    self.x = game_cam.x
    self.y = game_cam.y
    while x < -round(game_cam.x/60) + 20 and x < 80:
      y = max(-round(game_cam.y/60) - 1, -80)
      while y < -round(game_cam.y/60) + 20 and y < 80:
        if self.animation == [x, y]:
          if self.animation_turn > 9:
            self.animation_x += 3
          elif self.animation_turn > 3:
            self.animation_x -= 3
          elif self.animation_turn > 0:
            self.animation_x += 3
          else:
            if self.colours[x + 100][y + 100] == 'Tree':
              self.colours[x + 100][y + 100] = 'Tree1'
            elif self.colours[x + 100][y + 100] == 'Tree1':
              self.colours[x + 100][y + 100] = 'Tree2'
            elif self.colours[x + 100][y + 100] == 'Tree2':
              self.colours[x + 100][y + 100] = 'green'
              inv.items[0] += random.randint(2,5)
            self.animation = [101, 101]
          self.animation_turn -= 1
          pygame.draw.rect(screen, 'green', (x * 60 + self.x,y * 60 + self.y, 59, 59))
          screen.blit(Tree, (x * 60 + self.x + self.animation_x,y * 60 + self.y))
        else:
          if self.colours[x + 100][y + 100] == 'blue' or self.colours[x + 100][y + 100] == 'green':
            pygame.draw.rect(screen, self.colours[x + 100][y + 100], (x * 60 + self.x,y * 60 + self.y, 59, 59))
          elif self.colours[x + 100][y + 100] == 'Tree' or self.colours[x + 100][y + 100] == 'Tree1' or self.colours[x + 100][y + 100] == 'Tree2':
            pygame.draw.rect(screen, 'green', (x * 60 + self.x,y * 60 + self.y, 59, 59))
            screen.blit(Tree, (x * 60 + self.x,y * 60 + self.y))
          elif self.colours[x + 100][y + 100] == 'Iron':
            pygame.draw.rect(screen, 'green', (x * 60 + self.x,y * 60 + self.y, 59, 59))
            screen.blit(self.Iron_Ore, (x * 60 + self.x,y * 60 + self.y))
          elif self.colours[x + 100][y + 100] == 'Copper':
            pygame.draw.rect(screen, 'green', (x * 60 + self.x,y * 60 + self.y, 59, 59))
            screen.blit(self.Copper_Ore, (x * 60 + self.x,y * 60 + self.y))
          elif self.colours[x + 100][y + 100] == 'Coal':
            pygame.draw.rect(screen, 'green', (x * 60 + self.x,y * 60 + self.y, 59, 59))
            screen.blit(self.Coal, (x * 60 + self.x,y * 60 + self.y))
          elif self.colours[x + 100][y + 100] == 'Oil':
            pygame.draw.rect(screen, 'green', (x * 60 + self.x,y * 60 + self.y, 59, 59))
            screen.blit(self.Oil, (x * 60 + self.x,y * 60 + self.y))
          elif self.colours[x + 100][y + 100] == 'Uranium':
            pygame.draw.rect(screen, 'green', (x * 60 + self.x,y * 60 + self.y, 59, 59))
            screen.blit(self.Uranium_Ore, (x * 60 + self.x,y * 60 + self.y))
          for i in range(len(Ui.Building_Images)):
            if self.colours[x + 100][y + 100][0] == Ui.all_buildings[i]:
              pygame.draw.rect(screen, 'green', (x * 60 + self.x,y * 60 + self.y, 59, 59))
              if isinstance(Ui.Building_Images[i][self.colours[x + 100][y + 100][1]], list):
                screen.blit(Ui.Building_Images[i][self.colours[x + 100][y + 100][1]][self.colours[x + 100][y + 100][2]], (x * 60 + self.x,y * 60 + self.y))
              else:
                screen.blit(Ui.Building_Images[i][self.colours[x + 100][y + 100][1]], (x * 60 + self.x,y * 60 + self.y))
          mouse = pygame.mouse.get_pos()
          if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse[0] > x * 60 + self.x and mouse[0] < x * 60 + self.x + 60 and mouse[1] > y * 60 + self.y and mouse[1] < y * 60 + self.y + 60 and Buildings.i == -1:
              if (self.colours[x + 100][y + 100] == 'Tree' or self.colours[x + 100][y + 100] == 'Tree1' or self.colours[x + 100][y + 100] == 'Tree2') and not (Ui.options_hitbox.colliderect(x * 60 + self.x,  y * 60 + self.y, 60, 60) or Ui.build_hitbox.colliderect(x * 60 + self.x,  y * 60 + self.y, 60, 60) or (Ui.build_hitbox.colliderect(x * 60 + self.x,  y * 60 + self.y, 60, 60) and Buildings.i != -1) or (y * 60 + self.y > 600 and Ui.build_menu == True)):
                self.animation_turn = 12
                self.animation = [x, y]
                self.animation_x = 0
              if (self.colours[x + 100][y + 100] == 'Iron' or self.colours[x + 100][y + 100] == 'Copper' or self.colours[x + 100][y + 100] == 'Coal') and self.click > 4:
                self.click = 0
                if self.colours[x + 100][y + 100] == 'Iron':
                  inv.items[1] += 1
                if self.colours[x + 100][y + 100] == 'Copper':
                  inv.items[2] += 1
                if self.colours[x + 100][y + 100] == 'Coal':
                  inv.items[3] += 1
              for i in range(len(Ui.all_buildings)):
                if self.colours[x + 100][y + 100][0] == Ui.all_buildings[i] and not (Ui.options_hitbox.colliderect(x * 60 + self.x,  y * 60 + self.y, 60, 60) or Ui.build_hitbox.colliderect(x * 60 + self.x,  y * 60 + self.y, 60, 60) or (Ui.build_hitbox.colliderect(x * 60 + self.x,  y * 60 + self.y, 60, 60) and Buildings.i != -1) or (y * 60 + self.y > 600 and Ui.build_menu == True)):
                  Buildings.i = Buildings.buildings.index([x + 100, y + 100])
              
        y += 1
      x += 1
    screen.blit(Tree, (self.animation[0] * 60 + self.x + self.animation_x,self.animation[1] * 60 + self.y))

class loading_page:
  def __init__(self):
    self.create_new_game = pygame.draw.rect(screen, 'sky blue', (40,70, 590, 80))
    self.load_game = pygame.draw.rect(screen, 'sky blue', (40,290, 400, 80))
    self.quit = pygame.draw.rect(screen, 'sky blue', (40,510, 170, 80))

  def loading(self, turn, done):
    pygame.draw.rect(screen, 'white', (275,375, 300 * 0.82, 30))
    pygame.draw.rect(screen, 'black', (280,380, 285 * 0.82, 20))
    pygame.draw.rect(screen, 'white', (280,375, turn * 0.79, 30))
    text_font = pygame.font.SysFont("Ariel", 100)
    img = text_font.render('loading', True, 'white')
    screen.blit(img, (275,300))
    
  def main_page(self):
    self.create_new_game = pygame.draw.rect(screen, (109, 209, 209), (0,130, 400, 120))
    self.load_game = pygame.draw.rect(screen, (109, 209, 209), (0,250, 350, 70))
    self.quit = pygame.draw.rect(screen, (109, 209, 209), (0,320, 400, 80))
    screen.blit(pygame.image.load('images - Current Version/Beta 1.7 Home page.png'), (0,0))

class ui:
  def __init__(self):
    self.build_wood = pygame.transform.scale(inv.Pngs[0], (20, 20))
    self.build_Iron_Rod = pygame.transform.scale(inv.Pngs[5], (20, 20))
    self.build_Iron_Plate = pygame.transform.scale(inv.Pngs[6], (20, 20))
    self.build_copper_sheet = pygame.transform.scale(inv.Pngs[9], (20, 20))
    self.options_hitbox = pygame.draw.rect(screen, 'black', (712,22, 55, 55), 0)
    self.build_hitbox = pygame.draw.rect(screen, 'black', (712,652, 55, 55), 0)
    self.close_hitbox = pygame.draw.rect(screen, 'black', (650, 100, 50, 50))
    self.return_hitbox = pygame.draw.rect(screen, 'black', (650, 100, 50, 50))
    self.menu_bar = pygame.draw.rect(screen, 'white', (0,600, 800, 200))
    self.Build = pygame.image.load('images - Current Version/Build.png')
    self.Build = pygame.transform.scale(self.Build, (59, 59))    
    self.Exit = pygame.image.load('images - Current Version/Exit.png')
    self.Return = pygame.image.load('images - Current Version/Return.png')
    self.Resume_game = pygame.draw.rect(screen, 'sky blue', (40,70, 500, 80))
    self.Save_game = pygame.draw.rect(screen, 'sky blue', (40,200, 400, 80))
    self.Load_game = pygame.draw.rect(screen, 'sky blue', (40,330, 400, 80))
    self.Main_Menu = pygame.draw.rect(screen, 'sky blue', (40,460, 390, 80))
    self.Quit = pygame.draw.rect(screen, 'sky blue', (40,590, 170, 80))
    self.Save_1 = pygame.draw.rect(screen, 'sky blue', (40,70, 500, 80))
    self.Save_2 = pygame.draw.rect(screen, 'sky blue', (40,200, 400, 80))
    self.Save_3 = pygame.draw.rect(screen, 'sky blue', (40,330, 400, 80))
    self.Save_4 = pygame.draw.rect(screen, 'sky blue', (40,460, 170, 80))
    self.research_center = [False, False, True]
    self.Research_Center = [0,0,0,0]
    self.Research_Center[0] = pygame.image.load('images - Current Version/Research Center.png')
    self.Research_Center[0] = pygame.transform.scale(self.Research_Center[0], (59, 59))
    self.Research_Center[1] = pygame.transform.rotate(self.Research_Center[0], 90)
    self.Research_Center[2] = pygame.transform.rotate(self.Research_Center[0], 180)
    self.Research_Center[3] = pygame.transform.rotate(self.Research_Center[0], 270)
    self.construction = [False, False, True]
    self.Construction_Bench = [0,0,0,0]
    self.construction_bench_num = 0
    self.Construction_Bench[0] = pygame.image.load('images - Current Version/Construction Bench.png')
    self.Construction_Bench[0] = pygame.transform.scale(self.Construction_Bench[0], (59, 59))
    self.Construction_Bench[1] = pygame.transform.rotate(self.Construction_Bench[0], 90)
    self.Construction_Bench[2] = pygame.transform.rotate(self.Construction_Bench[0], 180)
    self.Construction_Bench[3] = pygame.transform.rotate(self.Construction_Bench[0], 270)
    self.molder = [False, False, False]
    self.Molder = [0,0,0,0]
    self.molder_num = 0
    self.Molder[0] = pygame.image.load('images - Current Version/Molder.png')
    self.Molder[0] = pygame.transform.scale(self.Molder[0], (59, 59))
    self.Molder[1] = pygame.transform.rotate(self.Molder[0], 90)
    self.Molder[2] = pygame.transform.rotate(self.Molder[0], 180)
    self.Molder[3] = pygame.transform.rotate(self.Molder[0], 270)
    self.smelter = [False, False, False]
    self.Smelter = [0,0,0,0]
    self.smelter_num = 0
    self.Smelter[0] = pygame.image.load('images - Current Version/Smelter.png')
    self.Smelter[0] = pygame.transform.scale(self.Smelter[0], (59, 59))
    self.Smelter[1] = pygame.transform.rotate(self.Smelter[0], 90)
    self.Smelter[2] = pygame.transform.rotate(self.Smelter[0], 180)
    self.Smelter[3] = pygame.transform.rotate(self.Smelter[0], 270)
    self.pipe = [False, False, False]
    self.Pipe = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    self.pipe_num = 0
    self.Pipe[0][0] = pygame.image.load('images - Current Version/Pipe.png')
    self.Pipe[0][0] = pygame.transform.scale(self.Pipe[0][0], (59, 59))
    self.Pipe[0][1] = pygame.transform.rotate(self.Pipe[0][0], 90)
    self.Pipe[0][2] = pygame.transform.rotate(self.Pipe[0][0], 180)
    self.Pipe[0][3] = pygame.transform.rotate(self.Pipe[0][0], 270)
    self.Pipe[1][0] = pygame.image.load('images - Current Version/pipe curve.png')
    self.Pipe[1][0] = pygame.transform.scale(self.Pipe[1][0], (59, 59))
    self.Pipe[1][1] = pygame.transform.rotate(self.Pipe[1][0], 90)
    self.Pipe[1][2] = pygame.transform.rotate(self.Pipe[1][0], 180)
    self.Pipe[1][3] = pygame.transform.rotate(self.Pipe[1][0], 270)
    self.Pipe[2][0] = pygame.image.load('images - Current Version/3 way pipe junc.png')
    self.Pipe[2][0] = pygame.transform.scale(self.Pipe[2][0], (59, 59))
    self.Pipe[2][1] = pygame.transform.rotate(self.Pipe[2][0], 90)
    self.Pipe[2][2] = pygame.transform.rotate(self.Pipe[2][0], 180)
    self.Pipe[2][3] = pygame.transform.rotate(self.Pipe[2][0], 270)
    self.Pipe[3][0] = pygame.image.load('images - Current Version/4 way pipe junc.png')
    self.Pipe[3][0] = pygame.transform.scale(self.Pipe[3][0], (59, 59))
    self.Pipe[3][1] = pygame.transform.scale(self.Pipe[3][0], (59, 59))
    self.Pipe[3][2] = pygame.transform.scale(self.Pipe[3][0], (59, 59))
    self.Pipe[3][3] = pygame.transform.scale(self.Pipe[3][0], (59, 59))
    self.buildings = ['research center', 'construction bench']
    self.all_buildings = ['research center', 'construction bench']
    self.build_stats = [self.molder, self.construction, self.research_center, self.smelter, self.pipe]
    self.Building_Images = [self.Research_Center, self.Construction_Bench]
    self.selection = False
    self.build_menu = False
    self.selections = False
    self.build_hitbox_y = 720
    self.Save = 0
    self.space = False
    self.Turn = 0
    self.research_center[2] = True
    self.Miner_Mrk1 = False
    self.BeltMrk1 = False
    self.mouse_button = 4
    self.r_key = False
    self.e_key = False
    self.direction = 0
    self.type = 0
    self.new_turn = False
  
  def in_game_hitboxes(self):
    self.options_hitbox = pygame.draw.rect(screen, 'black', (712,22, 55, 55), 0)
    self.build_hitbox = pygame.draw.rect(screen, 'black', (712,self.build_hitbox_y, 55, 55), 0)
    self.close_hitbox = pygame.draw.rect(screen, 'black', (660, 110, 30, 30))
    self.return_hitbox = pygame.draw.rect(screen, 'black', (110, 110, 30, 30))
  
  def in_game_buttons(self, Options):
    screen.blit(Options, (710, 20))
    screen.blit(self.Build, (712, self.build_hitbox_y))
 
  def options_screen(self):
    self.Resume_game = pygame.draw.rect(screen, 'sky blue', (40,70, 500, 80))
    self.Save_game = pygame.draw.rect(screen, 'sky blue', (40,200, 400, 80))
    self.Load_game = pygame.draw.rect(screen, 'sky blue', (40,330, 400, 80))
    self.Main_Menu = pygame.draw.rect(screen, 'sky blue', (40,460, 390, 80))
    self.Quit = pygame.draw.rect(screen, 'sky blue', (40,590, 170, 80))
    text_font = pygame.font.SysFont("Ariel", 100)
    img = text_font.render('Resume Game', True, 'white')
    screen.blit(img, (40,80))
    img = text_font.render('Save Game', True, 'white')
    screen.blit(img, (40,210))
    img = text_font.render('Load Game', True, 'white')
    screen.blit(img, (40,340))
    img = text_font.render('Main Menu', True, 'white')
    screen.blit(img, (40,470))
    img = text_font.render('Quit', True, 'white')
    screen.blit(img, (40,590))

  def save_game(self, files):
    if self.selections == True:
      with open(files[self.Save][0], 'w') as w:
        w.write(str(tiles.colours))
      with open(files[self.Save][1], 'w') as l:
        l.write(str([[Buildings.i, Buildings.buildings, Buildings.type, Buildings.pipe_locs, self.buildings, self.all_buildings, self.build_stats], [game_cam.x, game_cam.y], [inv.rescoures_found, inv.items], [Buildings.researches, Buildings.research_costs, Buildings.construction_bench_recipes, Buildings.machines_recipe, Buildings.machines_recipes, Buildings.rescources]]))
      print('Saved values')
      return True
    else:
      self.Save_1 = pygame.draw.rect(screen, 'sky blue', (40,70, 250, 80))
      self.Save_2 = pygame.draw.rect(screen, 'sky blue', (40,200, 250, 80))
      self.Save_3 = pygame.draw.rect(screen, 'sky blue', (40,330, 250, 80))
      self.Save_4 = pygame.draw.rect(screen, 'sky blue', (40,460, 250, 80))
      text_font = pygame.font.SysFont("Ariel", 100)
      img = text_font.render('Save_1', True, 'white')
      screen.blit(img, (40,80))
      img = text_font.render('Save_2', True, 'white')
      screen.blit(img, (40,210))
      img = text_font.render('Save_3', True, 'white')
      screen.blit(img, (40,340))
      img = text_font.render('Save_4', True, 'white')
      screen.blit(img, (40,470))
      return(False)
  
  def load_game(self, files):
    if self.selection == True:
      with open(files[self.Save][0], 'r') as w:
        world = w.read()
      with open(files[self.Save][1], 'r') as l:
        location = l.read()
      game_cam_loc = eval(location)
      game_cam.x = int(game_cam_loc[1][0])
      game_cam.y = int(game_cam_loc[1][1])
      Buildings.i = game_cam_loc[0][0]
      Buildings.buildings = game_cam_loc[0][1]
      Buildings.type = game_cam_loc[0][2]
      Buildings.pipe_locs = game_cam_loc[0][3]
      self.buildings = game_cam_loc[0][4]
      self.all_buildings = game_cam_loc[0][5]
      self.build_stats = game_cam_loc[0][6]
      [self.molder, self.construction, self.research_center, self.smelter, self.pipe] = game_cam_loc[0][6]
      inv.rescoures_found = game_cam_loc[2][0]
      inv.items = game_cam_loc[2][1] 
      Buildings.researches = game_cam_loc[3][0]
      Buildings.research_costs = game_cam_loc[3][1]
      Buildings.construction_bench_recipes = game_cam_loc[3][2]
      Buildings.machines_recipe = game_cam_loc[3][3]
      Buildings.machines_recipes = game_cam_loc[3][4]
      Buildings.rescources = game_cam_loc[3][5]
      if 'molder' in self.all_buildings:
        self.Building_Images.append(self.Molder)
      if 'smelter' in self.all_buildings:
        self.Building_Images.append(self.Smelter)
      if 'pipe' in self.all_buildings:
        self.Building_Images.append(self.Pipe)
      print('Loaded values:')  
      try:
        tiles.colours = eval(world)
      except:
        print('creating a new file...')   
      return True
    else:
      self.Save_1 = pygame.draw.rect(screen, 'sky blue', (40,70, 250, 80))
      self.Save_2 = pygame.draw.rect(screen, 'sky blue', (40,200, 250, 80))
      self.Save_3 = pygame.draw.rect(screen, 'sky blue', (40,330, 250, 80))
      self.Save_4 = pygame.draw.rect(screen, 'sky blue', (40,460, 250, 80))
      text_font = pygame.font.SysFont("Ariel", 100)
      img = text_font.render('Save_1', True, 'white')
      screen.blit(img, (40,80))
      img = text_font.render('Save_2', True, 'white')
      screen.blit(img, (40,210))
      img = text_font.render('Save_3', True, 'white')
      screen.blit(img, (40,340))
      img = text_font.render('Save_4', True, 'white')
      screen.blit(img, (40,470))
      return(False)
  
  def Placement_system(self, imp):
    text_font = pygame.font.SysFont("Ariel", 30)
    if imp[3][0][2] == True and self.new_turn == True:
      self.menu_bar = pygame.draw.rect(screen, 'white', (0,600, 800, 200))
      self.new_turn = False
    if imp[3][0][2] == True:
      self.num = self.buildings.index(imp[2])
      self.Hitbox = pygame.draw.rect(screen, 'white', (20 + 80 * self.num,620, 55, 55), 0)
      self.hitbox_num = self.num
      if isinstance(imp[3][1][0], list):
        screen.blit(imp[3][1][0][0], (20 + 80 * self.num, 620))
      else:
        screen.blit(imp[3][1][0], (20 + 80 * self.num, 620))
      for i in range(len(imp[1])):
        img = text_font.render(imp[1][i][0], True, 'black')
        screen.blit(img, (30 + 80 * self.num,680 + 30 * i))
        screen.blit(pygame.transform.scale(pygame.image.load(imp[1][i][1]), (20, 20)), (60 + 80 * self.num,680 + 30 * i))
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_button == 4:
      self.mouse_button = 1
    elif event.type == pygame.MOUSEBUTTONDOWN and self.mouse_button == 2 and imp[3][0][2] == True and imp[3][0][0] == True:
      x, y = pygame.mouse.get_pos()
      if self.mouse_button == 2 and y < 600:
        self.snap_mouse_location = [(x - 30 - game_cam.x) / 60,(y - 30 - game_cam.y) / 60]
        self.Cost_check = 0
        for i in range(len(imp[4][1])):
          if imp[4][1][i][0] >= imp[4][1][i][1]:
            self.Cost_check += 1
        if tiles.colours[round(self.snap_mouse_location[0]) + 100][round(self.snap_mouse_location[1]) + 100] == 'green' and self.Cost_check == len(imp[4][1]):
          if isinstance(imp[3][1][0], list):
            tiles.colours[round(self.snap_mouse_location[0]) + 100][round(self.snap_mouse_location[1]) + 100] = [imp[2], self.type, self.direction]
            if imp[2] == 'pipe':
              Buildings.pipe_locs[0].append([round(self.snap_mouse_location[0]) + 100, round(self.snap_mouse_location[1]) + 100])
              pipe_loc = []
              for i in range(len(Buildings.types[0][self.type])):
                pipe_loc.append(Buildings.types[0][3].index(Buildings.types[0][self.type][i]) + self.direction)
                if pipe_loc[i] < 3:
                  pipe_loc[i] -= 4
                pipe_loc[i] = Buildings.types[0][3][pipe_loc[i]]
              Buildings.pipe_locs[1].append(pipe_loc)
              Buildings.pipe_locs[2].append(0)
              Buildings.pipe_locs[3].append('')
          else:
            tiles.colours[round(self.snap_mouse_location[0]) + 100][round(self.snap_mouse_location[1]) + 100] = [imp[2], self.direction]
            Buildings.pipe_locs[0].append([round(self.snap_mouse_location[0]) + 100, round(self.snap_mouse_location[1]) + 100])
            pipe_loc = []
            for i in range(len(Buildings.types[1][Buildings.building.index(imp[2])])):
              pipe_loc.append(Buildings.types[0][3].index(Buildings.types[1][Buildings.building.index(imp[2])][i]) + self.direction)
              if pipe_loc[i] > 3:
                pipe_loc[i] -= 4
              pipe_loc[i] = Buildings.types[0][3][pipe_loc[i]]
            Buildings.pipe_locs[1].append(pipe_loc)
            Buildings.pipe_locs[2].append(0)
            Buildings.pipe_locs[3].append('')
          Buildings.buildings.append([round(self.snap_mouse_location[0]) + 100, round(self.snap_mouse_location[1]) + 100])
          Buildings.machines_recipe.append(0)
          Buildings.rescources.append([[[0,0,0,0]], [0,0,0], [round(self.snap_mouse_location[0]) + 100, round(self.snap_mouse_location[1]) + 100]])
          if imp[4][0] == True:  
            imp[3][0][2] = False
            self.buildings.remove(imp[2])
          for i in range(len(imp[4][1])):
            imp[4][1][i][0] -= imp[4][1][i][1]
      self.mouse_button = 3
    elif event.type == pygame.MOUSEBUTTONUP and self.mouse_button == 1 and imp[3][0][2] == True and self.Hitbox.collidepoint(x,y) and self.num == self.hitbox_num:
      for i in range(len(self.build_stats)):
        self.build_stats[i][0] = False
      self.mouse_button = 2
      imp[3][0][0] = True
    elif event.type == pygame.MOUSEBUTTONUP and self.mouse_button == 3:
      self.mouse_button = 4
    if self.mouse_button == 2 and imp[3][0][2] == True:
      x, y = pygame.mouse.get_pos()
      self.snap_mouse_location = [(x - game_cam.x - 30) / 60,(y - game_cam.y - 30) / 60]
      if imp[3][0][0] == True and tiles.colours[round(self.snap_mouse_location[0]) + 100][round(self.snap_mouse_location[1]) + 100] == 'green':
        self.snap_mouse_location = [(x - 30) / 60,(y - 30) / 60]
        if isinstance(imp[3][1][0], list) and round(self.snap_mouse_location[1]) * 60 < 540:
          screen.blit(imp[3][1][self.type][self.direction], (round(self.snap_mouse_location[0]) * 60, round(self.snap_mouse_location[1]) * 60))
        elif round(self.snap_mouse_location[1]) * 60 < 540:
          screen.blit(imp[3][1][self.direction], (round(self.snap_mouse_location[0]) * 60, round(self.snap_mouse_location[1]) * 60))
    if self.r_key == True and self.r_key_check == True:
      self.r_key_check = False
      self.direction += 1
      if self.direction == 4:
        self.direction = 0
    if self.r_key == False:
      self.r_key_check = True
    if self.e_key == True and self.e_key_check == True:
      self.e_key_check = False
      self.type += 1
      if self.type == 4:
        self.type = 0
    if self.e_key == False:
      self.e_key_check = True
    out = []
    for i in range(len(imp[4][1])):
      out.append(imp[4][1][i][0])
    self.build_stats[imp[0]] = imp[3][0]
    [self.molder, self.construction, self.research_center, self.smelter, self.pipe] = self.build_stats
    return(out)
  
  def tutorial(self):
    if self.Turn == 0:
      text_font = pygame.font.SysFont("Ariel", 60)
      screen.blit(pygame.image.load('images - Current Version/Beta 1.5 Main page.png'), (0,0))
      pygame.draw.rect(screen, 'White', (0,0, 800, 80))
      img = text_font.render('Press enter to proceed throughout', True, 'black')
      screen.blit(img, (10, 10))
      img = text_font.render('the tutorial', True, 'black')
      screen.blit(img, (10, 40))
    if self.Turn == 1:
      text_font = pygame.font.SysFont("Ariel", 60)
      screen.blit(pygame.image.load('images - Current Version/Beta 1.5 Main page.png'), (0,0))
      pygame.draw.rect(screen, 'White', (0,0, 800, 80))
      img = text_font.render('This is the main menu', True, 'black')
      screen.blit(img, (10, 10))
      img = text_font.render('They are very self-explanatory', True, 'black')
      screen.blit(img, (10, 40))
    if self.Turn == 2:
      text_font = pygame.font.SysFont("Ariel", 60)
      screen.blit(pygame.image.load('images - Current Version/Tutorial 1.png'), (0,0))
      pygame.draw.rect(screen, 'White', (0,0, 800, 80))
      img = text_font.render('Collect wood by shaking a tree', True, 'black')
      screen.blit(img, (10, 10))
      img = text_font.render('three times(clicking)', True, 'black')
      screen.blit(img, (10, 40))
    if self.Turn == 3:
      text_font = pygame.font.SysFont("Ariel", 60)
      screen.blit(pygame.image.load('images - Current Version/Tutorial 2.png'), (0,0))
      pygame.draw.rect(screen, 'White', (0,0, 800, 80))
      img = text_font.render('You can view your inventory by', True, 'black')
      screen.blit(img, (10, 10))
      img = text_font.render('pressing tab', True, 'black')
      screen.blit(img, (10, 40))
    if self.Turn == 3:
      text_font = pygame.font.SysFont("Ariel", 60)
      screen.blit(pygame.image.load('images - Current Version/Tutorial 3.png'), (0,0))
      pygame.draw.rect(screen, 'White', (0,0, 800, 80))
      img = text_font.render('Open the build menu in the bottom', True, 'black')
      screen.blit(img, (10, 10))
      img = text_font.render('right when you have 5 wood', True, 'black')
      screen.blit(img, (10, 40))
    if self.Turn == 4:
      text_font = pygame.font.SysFont("Ariel", 60)
      screen.blit(pygame.image.load('images - Current Version/Tutorial 4.png'), (0,0))
      pygame.draw.rect(screen, 'White', (0,0, 800, 80))
      img = text_font.render('Select the construction bench and', True, 'black')
      screen.blit(img, (10, 10))
      img = text_font.render('place it over the map', True, 'black')
      screen.blit(img, (10, 40))
    if self.Turn == 5:
      text_font = pygame.font.SysFont("Ariel", 60)
      screen.blit(pygame.image.load('images - Current Version/Tutorial 5.png'), (0,0))
      pygame.draw.rect(screen, 'White', (0,0, 800, 80))
      img = text_font.render('Collect recsources from across the', True, 'black')
      screen.blit(img, (10, 10))
      img = text_font.render('map', True, 'black')
      screen.blit(img, (10, 40))
    if self.Turn == 6:
      text_font = pygame.font.SysFont("Ariel", 60)
      screen.blit(pygame.image.load('images - Current Version/Tutorial 5.png'), (0,0))
      pygame.draw.rect(screen, 'White', (0,0, 800, 80))
      img = text_font.render('Continue to craft, make more buildings', True, 'black')
      screen.blit(img, (10, 10))
      img = text_font.render('and complete researches', True, 'black')
      screen.blit(img, (10, 40))
    if self.Turn == 7:
      pygame.quit()
    if self.space == True and self.space2 == False:
      self.space2 = True
      self.Turn += 1
    if self.space == False:
      self.space2 = False

class inventory:
  def __init__(self):
    self.Pngs = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    self.Pngs[0] = pygame.image.load('images - Current Version/Wood.png')
    self.Pngs[0] = pygame.transform.scale(self.Pngs[0], (40, 40))
    self.Pngs[1] = pygame.transform.scale(tiles.Iron_Ore, (30, 30))
    self.Pngs[2] = pygame.transform.scale(tiles.Copper_Ore, (30, 30))
    self.Pngs[3] = pygame.transform.scale(tiles.Coal, (30, 30))
    self.Pngs[4] = pygame.image.load('images - Current Version/iron Ingot.png')
    self.Pngs[5] = pygame.image.load('images - Current Version/iron Rod.png')
    self.Pngs[6] = pygame.image.load('images - Current Version/iron Plate.png')
    self.Pngs[7] = pygame.image.load('images - Current Version/Copper Ingot.png')
    self.Pngs[8] = pygame.image.load('images - Current Version/Wire.png')
    self.Pngs[9] = pygame.image.load('images - Current Version/Copper Sheet.png')
    self.Pngs[10] = pygame.image.load('images - Current Version/Rotor.png')
    self.Pngs[11] = pygame.image.load('images - Current Version/iron Crate.png')
    self.Pngs[12] = pygame.image.load('images - Current Version/Hammer.png')
    self.items = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    self.num = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    self.Tab = False
    self.rescoures_found = []

  def UI(self, name, i):
    if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB and tiles.click > 2:
      tiles.click = 0
      if self.Tab == False:
        self.Tab = True
      else:
        self.Tab = False
    if name in self.rescoures_found:
      if self.Tab == True:
        self.num[i] = self.rescoures_found.index(name) + 1
        if 40 + 80 * self.num[i] < 660:
          text_font = pygame.font.SysFont("Ariel", 15)
          pygame.draw.rect(screen, 'White', ( 40 + 80 * self.num[i], 100, 70, 70))
          img = text_font.render(name, True, 'black')
          screen.blit(img, (40 + 80 * self.num[i], 100))
          screen.blit(self.Pngs[i], (40 + 80 * self.num[i], 120))
          text_font = pygame.font.SysFont("Ariel", 20)
          img = text_font.render(str(self.items[i]), True, 'black')
          screen.blit(img, ( 42 + 80 * self.num[i], 158))
        else:
          self.y_dif = round((self.num[i]/ 8) - 0.5)
          text_font = pygame.font.SysFont("Ariel", 15)
          pygame.draw.rect(screen, 'White', ( 40 + 80 * (self.num[i] - self.y_dif * 8), 100 + 80 * self.y_dif, 70, 70))
          img = text_font.render(name, True, 'black')
          screen.blit(img, (40 + 80 * (self.num[i] - self.y_dif * 8), 100 + 80 * self.y_dif))
          screen.blit(self.Pngs[i], (40 + 80 * (self.num[i] - self.y_dif * 8), 120 + 80 * self.y_dif))
          text_font = pygame.font.SysFont("Ariel", 20)
          img = text_font.render(str(self.items[i]), True, 'black')
          screen.blit(img, ( 42 + 80 * (self.num[i] - self.y_dif * 8), 158 + 80 * self.y_dif))
    else:
      if self.items[i] > 0:
        self.rescoures_found.append(name)
        self.num[i] = len(self.rescoures_found)

class buildings:
  def __init__(self):
    self.iron_ore_iron_ingot_recipe = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.iron_ingot_iron_rod_recipe = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.iron_ingot_iron_plate_recipe = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.copper_ore_copper_ingot_recipe = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.copper_ingot_wire_recipe = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.copper_ingot_copper_sheet_recipe = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.rotor = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.iron_Crate = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.hammer = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.recipes = [self.iron_Crate, self.rotor, self.copper_ingot_copper_sheet_recipe, self.copper_ingot_wire_recipe, self.copper_ore_copper_ingot_recipe, self.iron_ingot_iron_plate_recipe, self.iron_ingot_iron_rod_recipe, self.iron_ore_iron_ingot_recipe]
    if py72 == 'Hammer':
      self.recipes.append(self.hammer)
    self.iron_basics = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.copper_basics = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.molders = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.manufacturing = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.pipes = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.smelters = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.research = [self.iron_basics, self.copper_basics, self.molders, self.manufacturing, self.pipes, self.smelters]
    self.iron_liquid = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.copper_liquid = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.iron_ingot = pygame.draw.rect(screen, 'sky blue', (100, 150, 600, 40))
    self.machines_rec = [[self.iron_liquid, 'smelter'], [self.copper_liquid, 'smelter'], [self.iron_ingot, 'molder']]
    self.ui = pygame.draw.rect(screen, 'white', (100, 100, 600, 600))
    self.buildings = []
    self.building = ['research center', 'construction bench', 'molder', 'smelter']
    self.rescources = []
    self.type = []
    self.input = [pygame.draw.rect(screen, 'orange', (30, 30, 30, 30)),pygame.draw.rect(screen, 'orange', (30, 30, 30, 30)),pygame.draw.rect(screen, 'orange', (30, 30, 30, 30)),pygame.draw.rect(screen, 'orange', (30, 30, 30, 30)),-1,'']
    self.pipe_locs = [[], [], [], []]
    self.types = [[[[-1, 0], [1, 0]], [[-1, 0], [0, 1]], [[-1, 0], [0, 1], [1, 0]], [[-1, 0], [0, 1], [1, 0], [0, -1]]], [[], [], [[-1, 0]], [[1, 0]]]]
    self.time = 0
    self.liquids = [['', 'iron liquid', 'copper liquid'], ['white', 'grey', 'orange']]
    self.mouse_button = False
    self.i = -1
    self.x1 = 0
    self.y1 = 0
    self.y = 0
    self.z_offset = 0
    self.layers = 0
    self.space = False
    self.space1 = False
    self.machines = ['smelter', 'molder']
    self.machines_recipe = []
    self.construction_bench_recipes = [[[['1','images - Current Version\Inv Iron Ore.png']], ['1',  'images - Current Version\Iron Ingot.png']]]
    if py72 == 'Hammer':
      self.construction_bench_recipes.append([[['1', 'images - Current Version\Inv Wood.png'], ['1', 'images - Current Version\Iron Rod.png']], ['1', 'images - Current Version\Hammer.png']])
    self.researches = ['iron basics']
    self.research_costs = [[['20',  'images - Current Version\Iron Ingot.png']]]
    self.machines_recipes = [[[[['1','images - Current Version\Inv Iron Ore.png', True]], ['1',  'images - Current Version\Iron Liquid.png', False]], [[['1', 'images - Current Version\Inv Copper Ore.png', True]], ['1', 'images - Current Version\Copper Liquid.png', False]]], [[[['1', 'images - Current Version\Iron Liquid.png', False]], ['1',  'images - Current Version\Iron Ingot.png', True]], [[['1', 'images - Current Version\Copper Liquid.png', False]], ['1',  'images - Current Version\Copper Ingot.png', True]]]]

  def Constuction_table(self, i, recipe, imp, out, back):
    if recipe in self.construction_bench_recipes:
      z = self.construction_bench_recipes.index(recipe)
      if len(self.type) > i:
        self.type[i] = tiles.colours[self.buildings[i][0]][self.buildings[i][1]][0]
        if self.type[i] == 'construction bench':
          if back == True:
            self.ui = pygame.draw.rect(screen, 'white', (100, 100, 600, 600))
            self.z_offset = 0
          self.z_offsetting = z + self.z_offset
          text_font = pygame.font.SysFont("Ariel", 60)
          img = text_font.render('Construction Bench', True, 'black')
          screen.blit(img, (200,100))
          self.total_lengths = 0
          self.offset_reset = 0
          for length in range(len(self.construction_bench_recipes[z][0])):
            img = text_font.render((str(imp[length][0]) + '|' + str(self.construction_bench_recipes[z][0][length][0])), True, 'black')
            [x, y] = img.get_size()
            if x + self.total_lengths > 580:
              self.total_lengths = 0
              self.z_offsetting += 1
              self.z_offset += 1
              self.offset_reset += 1
            self.total_lengths += x + 30
            img = pygame.image.load(self.construction_bench_recipes[z][0][length][1])
            if 40 + self.total_lengths > 580:
              self.total_lengths = 0
              self.z_offsetting += 1
              self.z_offset += 1
              self.offset_reset += 1
            self.total_lengths += 70
          img = text_font.render('>', True, 'black')
          if 40 + self.total_lengths > 580:
            self.total_lengths = 0
            self.z_offsetting += 1
            self.z_offset += 1
            self.offset_reset += 1
          self.total_lengths += 70
          img = text_font.render((str(out[0]) + '|' + str(self.construction_bench_recipes[z][0][length][0])), True, 'black')
          [x, y] = img.get_size()
          if x + self.total_lengths > 580:
            self.total_lengths = 0
            self.z_offsetting += 1
            self.z_offset += 1
            self.offset_reset += 1
          self.total_lengths += x + 30
          img = pygame.image.load(self.construction_bench_recipes[z][1][1])
          self.total_lengths = 0
          self.z_offsetting -= self.offset_reset
          self.z_offset -= self.offset_reset
          self.recipes[z] = pygame.draw.rect(screen, 'sky blue', (100, 150 + 50 * self.z_offsetting , 600, 40 + self.offset_reset * 50))
          for length in range(len(self.construction_bench_recipes[z][0])):
            img = text_font.render((str(imp[length][0]) + '|' + str(self.construction_bench_recipes[z][0][length][0])), True, 'black')
            [x, y] = img.get_size()
            if x + self.total_lengths > 580:
              self.total_lengths = 0
              self.z_offsetting += 1
              self.z_offset += 1
            screen.blit(img, (110 + self.total_lengths,150 + 50 * self.z_offsetting))
            self.total_lengths += x + 30
            img = pygame.image.load(self.construction_bench_recipes[z][0][length][1])
            if 40 + self.total_lengths > 580:
              self.total_lengths = 0
              self.z_offsetting += 1
              self.z_offset += 1
            screen.blit(img, (110 + self.total_lengths,155 + 50 * self.z_offsetting))
            self.total_lengths += 70
          img = text_font.render('>', True, 'black')
          if 40 + self.total_lengths > 580:
            self.total_lengths = 0
            self.z_offsetting += 1
            self.z_offset += 1
          screen.blit(img, (110 + self.total_lengths,145 + 50 * self.z_offsetting))
          self.total_lengths += 70
          img = text_font.render((str(out[0]) + '|' + str(self.construction_bench_recipes[z][0][length][0])), True, 'black')
          [x, y] = img.get_size()
          if x + self.total_lengths > 580:
            self.total_lengths = 0
            self.z_offsetting += 1
            self.z_offset += 1
          screen.blit(img, (110 + self.total_lengths,150 + 50 * self.z_offsetting))
          self.total_lengths += x + 30
          img = pygame.image.load(self.construction_bench_recipes[z][1][1])
          screen.blit(img, (110 + self.total_lengths,155 + 50 * self.z_offsetting))
      else:  
        self.type.append(tiles.colours[self.buildings[i][0]][self.buildings[i][1]][0])
      x, y = pygame.mouse.get_pos()
      if [self.x1, self.y1] != [x, y] and self.space == True:
        self.space = False
      self.x1 = x
      self.y1 = y
      self.g_check = 0
      if self.recipes[z].collidepoint(x, y) and self.type[i] == 'construction bench' and tiles.click > 4 and (self.mouse_button == True or self.space == True):
        for g in range(len(imp)):
          if imp[g][0] > imp[g][1] - 1:
            self.g_check += 1
        if self.g_check == g + 1:
          tiles.click = 0
          for g in range(len(imp)):
            imp[g][0] -= imp[g][1]
          out[0] += out[1]
    screen.blit(Ui.Exit, (660, 110))
    return_line = []
    for i in range(len(imp)):
      return_line.append(imp[i][0])
    return_line.append(out[0])
    return(return_line)
  
  def Research_center(self, i, recipe, imp, out):
    if recipe in self.researches:
      z = self.researches.index(recipe)
      if len(self.type) > i:
        if self.type[i] == 'research center':
          if z == 0:
            self.ui = pygame.draw.rect(screen, 'white', (100, 100, 600, 600))
            self.layers = 0
            self.y = 0
          f = z + self.y
          text_font = pygame.font.SysFont("Ariel", 60)
          img = text_font.render('Research Center', True, 'black')
          screen.blit(img, (200,100))
          if recipe in self.researches:
            self.research[z] = pygame.draw.rect(screen, 'sky blue', (100, 150 + f * 50, 600, 50 * math.ceil(len(self.research_costs[z]) / 3) - 10))
          img = text_font.render(self.researches[z], True, 'black')
          screen.blit(img, (100,150 + 50 * f))
          for d in range(len(self.research_costs[z])):
            h = d
            img = text_font.render(self.research_costs[z][d][0], True, 'black')
            if 400 + 100 * d > 699:
              h = 0
              f += 1
              self.y += 1
            screen.blit(img, (410 + 100 * h, 155 + 50 * f))
            screen.blit(pygame.image.load(self.research_costs[z][d][1]), (460 + 100 * h,155 + 50 * f))
      else:
        self.type.append(tiles.colours[self.buildings[i][0]][self.buildings[i][1]][0])
      x, y = pygame.mouse.get_pos()
      if [self.x1, self.y1] != [x, y] and self.space == True:
        self.space = False
      self.x1 = x
      self.y1 = y
      if self.research[z].collidepoint(x, y) and recipe in self.researches and self.type[i] == 'research center' and imp[0][0] > imp[1][0] - 1 and tiles.click > 8 and event.type == pygame.MOUSEBUTTONDOWN:
        tiles.click = 0
        self.reset = False
        self.research.remove(self.research[z])
        for d in range(len(imp[0])):
          imp[0][d] -= imp[1][d]
        self.research_costs.remove(self.research_costs[z])
        self.researches.remove(recipe)
        for d in range(len(out[0])):
          self.construction_bench_recipes.append(out[0][d])
        for d in range(len(out[1])):
          self.researches.append(out[1][d])
        for d in range(len(out[2])):
          self.research_costs.append(out[2][d])
        for d in range(len(out[3])):
          Ui.buildings.append(out[3][d])
          Ui.all_buildings.append(out[3][d])
          if out[3][d] == 'molder':
            Ui.Building_Images.append(Ui.Molder)
            Ui.molder[2] = True 
          if out[3][d] == 'pipe':
            Ui.Building_Images.append(Ui.Pipe)
            Ui.pipe[2] = True
          if out[3][d] == 'smelter':
            Ui.Building_Images.append(Ui.Smelter)
            Ui.smelter[2] = True
    return_line = []
    for i in range(len(imp[0])):
      return_line.append(imp[0][i])
    screen.blit(Ui.Exit, (660, 110))
    return(return_line)
  
  def automated_machines(self, i, type, recipe, imp, out, back):
    self.t = self.machines.index(type)
    text_font = pygame.font.SysFont("Ariel", 60)
    z = self.machines_recipes[self.t].index(recipe)
    if len(self.type) > i:
      self.type[i] = tiles.colours[self.buildings[i][0]][self.buildings[i][1]][0]
      if self.type[i] == type and self.machines_recipe[i] == 0:
        self.imp = imp
        self.out = out
        self.rescources[i][1][0] = self.pipe_locs[2][self.pipe_locs[0].index(self.rescources[i][2])]
        if back == True:
          self.ui = pygame.draw.rect(screen, 'white', (100, 100, 600, 600))
          self.z_offset = 0
        self.z_offsetting = z + self.z_offset
        img = text_font.render(self.type[i], True, 'black')
        screen.blit(img, (300,100))
        self.total_lengths = 0
        self.offset_reset = 0
        for length in range(len(self.machines_recipes[self.t][z][0])):
          img = text_font.render((str(imp[length][0]) + '|' + str(self.machines_recipes[self.t][z][0][length][0])), True, 'black')
          [x, y] = img.get_size()
          if x + self.total_lengths > 580:
            self.total_lengths = 0
            self.z_offsetting += 1
            self.z_offset += 1
            self.offset_reset += 1
          self.total_lengths += x + 30
          img = pygame.image.load(self.machines_recipes[self.t][z][0][length][1])
          if 40 + self.total_lengths > 580:
            self.total_lengths = 0
            self.z_offsetting += 1
            self.z_offset += 1
            self.offset_reset += 1
          self.total_lengths += 70
        img = text_font.render('>', True, 'black')
        if 40 + self.total_lengths > 580:
          self.total_lengths = 0
          self.z_offsetting += 1
          self.z_offset += 1
          self.offset_reset += 1
        self.total_lengths += 70
        img = text_font.render((str(out[0]) + '|' + str(self.machines_recipes[self.t][z][0][length][0])), True, 'black')
        [x, y] = img.get_size()
        if x + self.total_lengths > 580:
          self.total_lengths = 0
          self.z_offsetting += 1
          self.z_offset += 1
          self.offset_reset += 1
        self.total_lengths += x + 30
        img = pygame.image.load(self.machines_recipes[self.t][z][1][1])
        self.total_lengths = 0
        self.z_offsetting -= self.offset_reset
        self.z_offset -= self.offset_reset
        self.machines_rec[z][0] = pygame.draw.rect(screen, 'sky blue', (100, 150 + 50 * self.z_offsetting , 600, 40 + self.offset_reset * 50))
        self.machines_rec[z][1] = type
        for length in range(len(self.machines_recipes[self.t][z][0])):
          if imp[length][0] not in self.liquids[0]:
            img = text_font.render((str(inv.items[imp[length][0]]) + '|' + str(self.machines_recipes[self.t][z][0][length][0])), True, 'black')
          else:
            img = text_font.render((str(self.machines_recipes[self.t][z][0][length][0]) + 'L'), True, 'black')
          [x, y] = img.get_size()
          if x + self.total_lengths > 580:
            self.total_lengths = 0
            self.z_offsetting += 1
            self.z_offset += 1
          screen.blit(img, (110 + self.total_lengths,150 + 50 * self.z_offsetting))
          self.total_lengths += x + 30
          img = pygame.image.load(self.machines_recipes[self.t][z][0][length][1])
          if 40 + self.total_lengths > 580:
            self.total_lengths = 0
            self.z_offsetting += 1
            self.z_offset += 1
          screen.blit(img, (110 + self.total_lengths,155 + 50 * self.z_offsetting))
          self.total_lengths += 70
        img = text_font.render('>', True, 'black')
        if 40 + self.total_lengths > 580:
          self.total_lengths = 0
          self.z_offsetting += 1
          self.z_offset += 1
        screen.blit(img, (110 + self.total_lengths,145 + 50 * self.z_offsetting))
        self.total_lengths += 70
        if out[0] in self.liquids[0]:
          img = text_font.render((str(self.machines_recipes[self.t][z][0][length][0]) + 'L'), True, 'black')
        else:
          img = text_font.render((str(inv.items[out[0]]) + '|' + str(self.machines_recipes[self.t][z][0][length][0])), True, 'black')
        [x, y] = img.get_size()
        if x + self.total_lengths > 580:
          self.total_lengths = 0
          self.z_offsetting += 1
          self.z_offset += 1
        screen.blit(img, (110 + self.total_lengths,150 + 50 * self.z_offsetting))
        self.total_lengths += x + 30
        img = pygame.image.load(self.machines_recipes[self.t][z][1][1])
        screen.blit(img, (110 + self.total_lengths,155 + 50 * self.z_offsetting))
    else:
      self.type.append(tiles.colours[self.buildings[i][0]][self.buildings[i][1]][0])
    x, y = pygame.mouse.get_pos()
    if [self.x1, self.y1] != [x, y] and self.space == True:
        self.space = False
    self.x1 = x
    self.y1 = y
    if self.machines_rec[z][0].collidepoint(x, y) and self.mouse_button == True and self.machines_recipe[i] == 0  and self.type[i] == self.machines_rec[z][1] and self.type[i] == type:
      self.machines_recipe[i] = recipe
      self.rescources[i][0][0][1] = imp[0][0]
      self.rescources[i][1][1] = out[0]
      self.rescources[i][0][0][2] = imp[0][1]
      self.rescources[i][1][2] = out[1]
      self.rescources[i][0][0][3] = out[2]
    if self.machines_recipe[i] == recipe and self.type[i] == type:
      self.ui = pygame.draw.rect(screen, 'white', (100, 100, 600, 600))
      screen.blit(Ui.Return, (110, 110))
      x, y = pygame.mouse.get_pos()
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
            self.machines_recipe[i] = 0
      if Ui.return_hitbox.collidepoint(x, y) and self.mouse_button == True:
        self.machines_recipe[i] = 0
        if isinstance(self.rescources[i][1][1], int):
          inv.items[self.rescources[i][1][1]] += self.rescources[i][1][0]
        if isinstance(self.rescources[i][0][0][1], int):
          inv.items[self.rescources[i][0][0][1]] += self.rescources[i][0][0][0]
        self.rescources[i][1][0] = 0
        self.rescources[i][0][0][0] = 0
      text_font = pygame.font.SysFont("Ariel", 120)
      img = text_font.render(self.type[i], True, 'black')
      screen.blit(img, (300,100))
      for length in range(len(self.machines_recipes[self.t][z][0])):
        if imp[0][0] not in self.liquids[0]:
          img = text_font.render(str(self.machines_recipes[self.t][z][0][length][0]), True, 'black')
          screen.blit(img, (200 - img.get_size()[0], (385 - (length + 1) * 15) + (length + 1) * 30))
          img = text_font.render(str(self.rescources[i][0][length][0]), True, 'black')
          screen.blit(img, (200, (485 - (length + 1) * 15) + (length + 1) * 30))
        else:
          img = text_font.render(str(self.machines_recipes[self.t][z][0][length][0]) + 'L', True, 'black')
          screen.blit(img, (200 - img.get_size()[0], (385 - (length + 1) * 15) + (length + 1) * 30))
          img = text_font.render(str(round(self.rescources[i][0][length][0], 2)) + 'L', True, 'black')
          screen.blit(img, (200, (485 - (length + 1) * 15) + (length + 1) * 30))
        screen.blit(pygame.transform.scale(pygame.image.load(self.machines_recipes[self.t][z][0][length][1]), (80, 80)), (200, (385 - (length + 1) * 15) + (length + 1) * 30))
        if self.machines_recipes[self.t][z][0][length][2] == True:
          text_font = pygame.font.SysFont("Ariel", 60)
          img = text_font.render('+', True, 'black')
          self.input[0] = pygame.draw.rect(screen, 'orange', (300, (385 - (length + 1) * 15) + (length + 1) * 30, 30, 30))
          screen.blit(img, (302, (385 - (length + 1) * 15) + (length + 1) * 30 - 10))
          img = text_font.render('-', True, 'black')
          self.input[1] = pygame.draw.rect(screen, 'orange', (300, (425 - (length + 1) * 15) + (length + 1) * 30, 30, 30))
          screen.blit(img, (307, (425 - (length + 1) * 15) + (length + 1) * 30 - 7))
      text_font = pygame.font.SysFont("Ariel", 120)
      if out[0] in self.liquids[0]:
        img = text_font.render(str(self.machines_recipes[self.t][z][1][0]) + 'L', True, 'black')
        screen.blit(img, (550 - img.get_size()[0], 400))
        img = text_font.render(str(round(self.rescources[i][1][0], 2)) + 'l', True, 'black')
        screen.blit(img, (520, 500))
      else:
        img = text_font.render(str(self.machines_recipes[self.t][z][1][0]), True, 'black')
        screen.blit(img, (550 - img.get_size()[0], 400))
        img = text_font.render(str(self.rescources[i][1][0]), True, 'black')
        screen.blit(img, (520, 500))
      screen.blit(pygame.transform.scale(pygame.image.load(self.machines_recipes[self.t][z][1][1]), (80, 80)), (550, 400))
      if self.machines_recipes[self.t][z][1][2] == True:
        text_font = pygame.font.SysFont("Ariel", 69)
        img = text_font.render('+', True, 'black')
        self.input[2] = pygame.draw.rect(screen, 'orange', (650, 400, 30, 30))
        screen.blit(img, (652, 390))
        img = text_font.render('-', True, 'black')
        self.input[3] = pygame.draw.rect(screen, 'orange', (650, 440, 30, 30))
        screen.blit(img, (657, 432))
      x,y = pygame.mouse.get_pos()
      if self.input[0].collidepoint(x, y) and self.mouse_button == True:
        self.input[4] = 0
      if self.input[1].collidepoint(x, y) and self.mouse_button == True:
        self.input[4] = 1
      if self.input[2].collidepoint(x, y) and self.mouse_button == True:
        self.input[4] = 2
      if self.input[3].collidepoint(x, y) and self.mouse_button == True:
        self.input[4] = 3
      if self.input[4] != -1:
        text_font = pygame.font.SysFont("Ariel", 50)
        pygame.draw.rect(screen, 'black', (340, 400, (len(self.input[5]) + len(self.machines_recipes[self.t][z][0][0][0])) * 20 + 30, 60), 2)
        img = text_font.render(self.input[5] + '|' + self.machines_recipes[self.t][z][0][0][0], True, 'black')
        screen.blit(img, (350, 410))
    screen.blit(Ui.Exit, (660, 110))

  def pipe(self, i):
    text_font = pygame.font.SysFont("Ariel", 110)
    small_font = pygame.font.SysFont("Ariel", 80)
    self.max_capacity = 600
    if len(self.type) > i:
      if self.type[i] == 'pipe':
        self.amount = self.pipe_locs[2][self.pipe_locs[0].index([self.buildings[i][0], self.buildings[i][1]])]
        self.ui = pygame.draw.rect(screen, 'white', (100, 100, 600, 600))
        img = text_font.render('pipe', True, 'black')
        screen.blit(img, (300, 110))
        img = small_font.render('Flush', True, 'black')
        screen.blit(img, (320, 580))
        pygame.draw.circle(screen, self.liquids[1][self.liquids[0].index(self.pipe_locs[3][self.pipe_locs[0].index([self.buildings[i][0], self.buildings[i][1]])])], (550, 400), 100)
        self.flush = pygame.draw.circle(screen, 'black', (550, 600), 40)
        pygame.draw.rect(screen, 'white', (450, 300 , 200, 200 - (self.amount/self.max_capacity) * 200))
        pygame.draw.circle(screen, 'black', (550, 400), 110, 10)
        img = text_font.render(str(round(self.amount, 2)) + 'L', True, 'black')
        screen.blit(img, (150, 300))
        pygame.draw.line(screen, 'black', (150, 385), (430, 385), 20)
        img = text_font.render(str(self.max_capacity) + 'L', True, 'black')
        screen.blit(img, (150, 400))
        x, y = pygame.mouse.get_pos()
        if self.flush.collidepoint(x, y) and self.mouse_button == True:
          while round(self.pipe_locs[2][self.pipe_locs[0].index([self.buildings[i][0], self.buildings[i][1]])], 3) != 0:
            if self.pipe_locs[2][self.pipe_locs[0].index([self.buildings[i][0], self.buildings[i][1]])] < 1:
              self.pipe_locs[2][self.pipe_locs[0].index([self.buildings[i][0], self.buildings[i][1]])] -= 0.001
            elif self.pipe_locs[2][self.pipe_locs[0].index([self.buildings[i][0], self.buildings[i][1]])] < 5:
              self.pipe_locs[2][self.pipe_locs[0].index([self.buildings[i][0], self.buildings[i][1]])] -= 0.01
            elif self.pipe_locs[2][self.pipe_locs[0].index([self.buildings[i][0], self.buildings[i][1]])] < 20:
              self.pipe_locs[2][self.pipe_locs[0].index([self.buildings[i][0], self.buildings[i][1]])] -= 0.1
            elif self.pipe_locs[2][self.pipe_locs[0].index([self.buildings[i][0], self.buildings[i][1]])] < 80:
              self.pipe_locs[2][self.pipe_locs[0].index([self.buildings[i][0], self.buildings[i][1]])] -= 1
            else:
              self.pipe_locs[2][self.pipe_locs[0].index([self.buildings[i][0], self.buildings[i][1]])] -= 10
            for h in range(len(self.pipe_locs[1])):
              for b in range(len(self.pipe_locs[1][h])):
                self.new_pipe_loc = [self.pipe_locs[0][h][0] + self.pipe_locs[1][h][b][0], self.pipe_locs[0][h][1] + self.pipe_locs[1][h][b][1]]
                if self.new_pipe_loc in self.pipe_locs[0]:
                  self.new_pipe = self.pipe_locs[0].index(self.new_pipe_loc)
                  if [0 - self.pipe_locs[1][h][b][0], 0 - self.pipe_locs[1][h][b][1]] in self.pipe_locs[1][self.new_pipe]:
                    if self.pipe_locs[2][self.new_pipe] > self.pipe_locs[2][h] and (self.pipe_locs[3][self.new_pipe] == self.pipe_locs[3][h] or self.pipe_locs[3][h] == ''):
                      self.transfer = 0.05 * (self.pipe_locs[2][self.new_pipe] - self.pipe_locs[2][h])
                      self.pipe_locs[2][self.new_pipe] -= self.transfer
                      self.pipe_locs[2][h] += self.transfer
                    if self.pipe_locs[3][h] == '':
                      self.pipe_locs[3][h] = self.pipe_locs[3][self.new_pipe]
            self.amount = self.pipe_locs[2][self.pipe_locs[0].index([self.buildings[i][0], self.buildings[i][1]])]
            self.ui = pygame.draw.rect(screen, 'white', (100, 100, 600, 600))
            img = text_font.render('pipe', True, 'black')
            screen.blit(img, (300, 110))
            img = small_font.render('Flush', True, 'black')
            screen.blit(img, (320, 580))
            pygame.draw.circle(screen, self.liquids[1][self.liquids[0].index(self.pipe_locs[3][self.pipe_locs[0].index([self.buildings[i][0], self.buildings[i][1]])])], (550, 400), 100)
            self.flush = pygame.draw.circle(screen, 'black', (550, 600), 40)
            pygame.draw.rect(screen, 'white', (450, 300 , 200, 200 - (self.amount/self.max_capacity) * 200))
            pygame.draw.circle(screen, 'black', (550, 400), 110, 10)
            img = text_font.render(str(round(self.amount, 2)) + 'L', True, 'black')
            screen.blit(img, (150, 300))
            pygame.draw.line(screen, 'black', (150, 385), (430, 385), 20)
            img = text_font.render(str(self.max_capacity) + 'L', True, 'black')
            screen.blit(img, (150, 400))
            screen.blit(Ui.Exit, (660, 110))
            pygame.display.update()
          self.pipe_locs[3][self.pipe_locs[0].index([self.buildings[i][0], self.buildings[i][1]])] = ''
      for h in range(len(self.pipe_locs[1])):
        for b in range(len(self.pipe_locs[1][h])):
          self.new_pipe_loc = [self.pipe_locs[0][h][0] + self.pipe_locs[1][h][b][0], self.pipe_locs[0][h][1] + self.pipe_locs[1][h][b][1]]
          if self.new_pipe_loc in self.pipe_locs[0]:
            self.new_pipe = self.pipe_locs[0].index(self.new_pipe_loc)
            if [0 - self.pipe_locs[1][h][b][0], 0 - self.pipe_locs[1][h][b][1]] in self.pipe_locs[1][self.new_pipe]:
              if self.pipe_locs[2][self.new_pipe] > self.pipe_locs[2][h] and (self.pipe_locs[3][self.new_pipe] == self.pipe_locs[3][h] or self.pipe_locs[3][h] == ''):
                self.transfer = 0.05 * (self.pipe_locs[2][self.new_pipe] - self.pipe_locs[2][h])
                self.pipe_locs[2][self.new_pipe] -= self.transfer
                self.pipe_locs[2][h] += self.transfer
              if self.pipe_locs[3][h] == '':
                self.pipe_locs[3][h] = self.pipe_locs[3][self.new_pipe]
    else:
      self.type.append(tiles.colours[self.buildings[i][0]][self.buildings[i][1]][0])
    screen.blit(Ui.Exit, (660, 110))
  
  def automation(self):
    for i in range(len(self.type)):
      if (self.type[i] == 'smelter' or self.type[i] == 'molder') and Buildings.machines_recipe[i] != 0:
        if self.rescources[i][1][1] in self.liquids[0]:
          self.rescources[i][1][0] = self.pipe_locs[2][self.pipe_locs[0].index(self.rescources[i][2])]
        elif self.rescources[i][0][0][1] in self.liquids[0]:
          self.rescources[i][0][0][0] = self.pipe_locs[2][self.pipe_locs[0].index(self.rescources[i][2])]
        if self.rescources[i][0][0][0] >= self.rescources[i][0][0][2] and self.time % self.rescources[i][0][0][3] == 0:
          self.rescources[i][0][0][0] -= self.rescources[i][0][0][2]
          self.rescources[i][1][0] += self.rescources[i][1][2]
        if self.rescources[i][1][1] in self.liquids[0]:
          self.pipe_locs[2][self.pipe_locs[0].index(self.rescources[i][2])] = self.rescources[i][1][0]
          self.pipe_locs[3][self.pipe_locs[0].index(self.rescources[i][2])] = self.rescources[i][1][1]
        elif self.rescources[i][0][0][1] in self.liquids[0]:
          self.pipe_locs[2][self.pipe_locs[0].index(self.rescources[i][2])] = self.rescources[i][0][0][0]
          self.pipe_locs[3][self.pipe_locs[0].index(self.rescources[i][2])] = self.rescources[i][0][0][1]
      if self.machines_recipe[i] == 0 and (self.rescources[i][1][0] != 0 or self.rescources[i][0][0][1] != 0):
        self.pipe_locs[2][self.pipe_locs[0].index(self.rescources[i][2])] = 0
        self.pipe_locs[3][self.pipe_locs[0].index(self.rescources[i][2])] = 'unusable'

screen = pygame.display.set_mode((800 , 800))

game_cam = camera()
tiles = map_tiles()
home_screen = loading_page()
inv = inventory()
Ui = ui()
Buildings = buildings()
turn = 0

while True:
  screen.fill('black')
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      pygame.quit()
    if event.type == pygame.KEYDOWN:
      if Buildings.input[4] != 4:
        if event.key == pygame.K_BACKSPACE:
          Buildings.input[5] = Buildings.input[5][:-1]
        elif event.key == pygame.K_RETURN:
          if Buildings.input[4] == 0 and int(Buildings.input[5]) < inv.items[Buildings.imp[0][0]] + 1:
            inv.items[Buildings.imp[0][0]] -= int(Buildings.input[5])
            Buildings.rescources[Buildings.i][0][0][0] += int(Buildings.input[5])
          elif Buildings.input[4] == 1 and int(Buildings.input[5]) < Buildings.rescources[Buildings.i][0][0][0] + 1:
            inv.items[Buildings.imp[0][0]] += int(Buildings.input[5])
            Buildings.rescources[Buildings.i][0][0][0] -= int(Buildings.input[5])
          elif Buildings.input[4] == 2 and int(Buildings.input[5]) < inv.items[Buildings.out[0]] + 1:
            inv.items[Buildings.out[0]] -= int(Buildings.input[5])
            Buildings.rescources[Buildings.i][1][0] += int(Buildings.input[5])
          elif Buildings.input[4] == 3 and int(Buildings.input[5]) < Buildings.rescources[Buildings.i][1][0] + 1:
            inv.items[Buildings.out[0]] += int(Buildings.input[5])
            Buildings.rescources[Buildings.i][1][0] -= int(Buildings.input[5])
          Buildings.input[4] = -1
        else: 
          if event.unicode in '1234567890' and len(Buildings.input[5]) < 3:
            Buildings.input[5] += event.unicode
      if event.key == pygame.K_UP:
        key_up = True
      if event.key == pygame.K_DOWN:
        key_down = True
      if event.key == pygame.K_LEFT:
        key_left = True
      if event.key == pygame.K_RIGHT:
        key_right = True
      if event.key == pygame.K_r:
        Ui.r_key = True
      if event.key == pygame.K_e:
        Ui.e_key = True
      if event.key == pygame.K_SPACE:
        Buildings.space1 = True
      if event.key == pygame.K_RETURN:
        Ui.space = True
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        key_up = False
      if event.key == pygame.K_DOWN:
        key_down = False
      if event.key == pygame.K_LEFT:
        key_left = False
      if event.key == pygame.K_RIGHT:
        key_right = False
      if event.key == pygame.K_r:
        Ui.r_key = False
      if event.key == pygame.K_e:
        Ui.e_key = False
      if event.key == pygame.K_SPACE:
        Buildings.space1 = False
      if event.key == pygame.K_RETURN:
        Ui.space = False
    if event.type == pygame.MOUSEBUTTONUP:
      Buildings.mouse_button = False
      x, y = pygame.mouse.get_pos()
      if Main_game == False and Home_page == True and home_screen.create_new_game.collidepoint(x, y) and Load == False:
          Main_game = True
          tiles.done_pt2 = False
      elif Main_game == False and Home_page == True and home_screen.quit.collidepoint(x, y) and Load == False and Save == False:
        pygame.quit()
      elif Main_game == False and Ui.Quit.collidepoint(x, y) and Load == False and Save == False:
        pygame.quit()
      elif Main_game == True and Ui.options_hitbox.collidepoint(x,y):
          Main_game = False
          Home_page = False
          Load = False
          Save = False
      elif Main_game == False and Home_page == False and Load == False and Save == False and Ui.Resume_game.collidepoint(x,y):
          Main_game = True
          tiles.done_pt2 = True
      elif Main_game == False and Home_page == False and Ui.Save_game.collidepoint(x,y) and Load == False and Save == False:
          Save = True
          time.sleep(0.5)
          Ui.selections = False
          Ui.Save = 4
      elif Main_game == False and Home_page == False and Ui.Load_game.collidepoint(x,y) and Load == False and Save == False:
          Load = True
          Ui.selection = False
          Ui.Save = 4
          time.sleep(0.5)
      elif Main_game == False and Home_page == False and Ui.Main_Menu.collidepoint(x,y) and Load == False and Save == False:
        Home_page = True
        turn = 0
        tiles.__init__()
        Buildings.__init__()
        inv.__init__()
        Ui.__init__()
      elif Main_game == False and Home_page == True and home_screen.load_game.collidepoint(x,y):
          Load = True
          Ui.selection = False
          Home_page = False
          Ui.Save = 4
          time.sleep(0.5)
      elif Ui.Save_1.collidepoint(x,y):
        Ui.Save = 0
        if Load == True:
          Ui.selection = True 
        else:
          Ui.selections = True
      elif Ui.Save_2.collidepoint(x,y) and Home_page == False and (Save == True or Load == True):
        Ui.Save = 1
        if Load == True:
          Ui.selection = True
        else:
          Ui.selections = True
      elif Ui.Save_3.collidepoint(x,y) and Home_page == False and (Save == True or Load == True):
        Ui.Save = 2
        if Load == True:
          Ui.selection = True
        else:
          Ui.selections = True
      elif Ui.Save_4.collidepoint(x,y):
        Ui.Save = 3
        if Load == True:
          Ui.selection = True
        else:
          Ui.selections = True
      if Ui.build_hitbox.collidepoint(x,y) and Main_game == True and Ui.build_hitbox_y == 720:
        Ui.build_menu = True 
        Ui.build_hitbox_y = 520
      elif Ui.build_hitbox.collidepoint(x,y) and Main_game == True and Ui.build_hitbox_y == 520:
        Ui.build_menu = False
        Ui.build_hitbox_y = 720
      elif Ui.close_hitbox.collidepoint(x,y) and Main_game == True and Buildings.i != -1:
        Buildings.i = -1
        Buildings.space = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      Buildings.mouse_button = True
    if pygame.MOUSEBUTTONDOWN != True:
      Buildings.reset = True

  if key_up == True:  
    game_cam.up()
  if key_down == True:  
    game_cam.down()
  if key_left == True:  
    game_cam.left()
  if key_right == True:  
    game_cam.right()
  
  if Main_game == True:
    if tiles.done_pt2 == False:
      turn += 1
      tiles.main_game()
      home_screen.loading(turn, tiles.done_pt2)
    else:
      if Buildings.space1 == False:
        Buildings.space2 = True
      if Buildings.space2 == True and Buildings.space1 == True:
        if Buildings.space1 == True and Buildings.space == False and Buildings.space2 == True:
          Buildings.space = True
          Buildings.space2 = False
        elif Buildings.space1 == True and Buildings.space == True and Buildings.space2 == True:
          Buildings.space = False
          Buildings.space2 = False
      tiles.click += 1
      Buildings.time += 1
      Ui.in_game_hitboxes()
      tiles.running(Tree)
      Ui.in_game_buttons(Options)
      inv.UI('Wood', 0)
      inv.UI('Iron Ore', 1)
      inv.UI('Copper Ore', 2)
      inv.UI('Coal', 3)
      inv.UI('Iron Ingot', 4)
      inv.UI('Iron Rod', 5)
      inv.UI('Iron Plate', 6)
      inv.UI('Copper Ingot', 7)
      inv.UI('Wire', 8)
      inv.UI('Copper Sheet', 9)
      inv.UI('Rotor', 10)
      inv.UI('Iron Crate', 11)
      inv.UI('Hammer', 12)
    if Ui.build_menu == True and Buildings.i == -1:
      Ui.new_turn = True
      # [number, [['amount 1', 'amount image 1'], ['amount 2', 'amount image 2']], 'name', [Ui.lower_case_name, Ui.upper_case_name], [1 time use (True/False), [[inv.items[?], amount, ?], [inv.items[?], amount, ?]]]]
      [inv.items[5], inv.items[6]] = Ui.Placement_system([0, [['10', 'images - Current Version\Iron Rod.png'], ['10', 'images - Current Version\Iron Plate.png']], 'molder', [Ui.molder, Ui.Molder], [False, [[inv.items[5], 10, 5], [inv.items[6], 1, 6]]]])
      [inv.items[0]] = Ui.Placement_system([1, [['5', 'images - Current Version\Wood.png']], 'construction bench', [Ui.construction, Ui.Construction_Bench], [False, [[inv.items[0], 5, 0]]]])
      [] = Ui.Placement_system([2, [], 'research center', [Ui.research_center, Ui.Research_Center], [True, []]])
      [inv.items[9], inv.items[5]] = Ui.Placement_system([3, [['10', 'images - Current Version\Copper Sheet.png'], ['6', 'images - Current Version\Iron Rod.png']], 'smelter', [Ui.smelter, Ui.Smelter], [False, [[inv.items[9], 10, 9], [inv.items[5], 6, 5]]]])
      [inv.items[9]] = Ui.Placement_system([4, [['5', 'images - Current Version\Copper Sheet.png']], 'pipe', [Ui.pipe, Ui.Pipe], [False, [[inv.items[9], 5, 9]]]])
    if Buildings.i != -1:
      inv.items[1], inv.items[4] = Buildings.Constuction_table(Buildings.i, [[['1','images - Current Version\Inv Iron Ore.png']], ['1','images - Current Version\Iron Ingot.png']],  [[inv.items[1], 1, 1]], [inv.items[4], 1, 4], True)
      if py72 == 'Hammer':
        inv.items[0], inv.items[5], inv.items[12] = Buildings.Constuction_table(Buildings.i, [[['1','images - Current Version\Inv Wood.png'], ['1','images - Current Version\Iron Rod.png']], ['1','images - Current Version\Hammer.png']],  [[inv.items[0], 1], [inv.items[5], 2]], [inv.items[12], 1], False)
      # inputs, output = (buildings.i, [[[amount 1, image 1], [amount 2, image 2]], [output amount, output image]], [[input: inv.items[?], amount], [input: inv.items[?], amount]], [output: inv.items[?], amount], False)
      inv.items[4], inv.items[5] = Buildings.Constuction_table(Buildings.i, [[['1','images - Current Version\Iron Ingot.png']], ['1', 'images - Current Version\Iron Rod.png']],  [[inv.items[4], 1]], [inv.items[5], 1], False)
      inv.items[4], inv.items[6] = Buildings.Constuction_table(Buildings.i, [[['1','images - Current Version\Iron Ingot.png']], ['1','images - Current Version\Iron Plate.png']], [[inv.items[4], 1]], [inv.items[6], 1], False)
      inv.items[2], inv.items[7] = Buildings.Constuction_table(Buildings.i, [[['1','images - Current Version\Inv Copper Ore.png']], ['1','images - Current Version\Copper Ingot.png']], [[inv.items[2], 1]], [inv.items[7], 1], False)
      inv.items[7], inv.items[8] = Buildings.Constuction_table(Buildings.i, [[['1','images - Current Version\Copper Ingot.png']], ['1','images - Current Version\Wire.png']],  [[inv.items[7], 1]], [inv.items[8], 1], False)
      inv.items[7], inv.items[9] = Buildings.Constuction_table(Buildings.i, [[['1','images - Current Version\Copper Ingot.png']], ['1','images - Current Version\Copper Sheet.png']],  [[inv.items[7], 1]], [inv.items[9], 1], False)
      inv.items[5], inv.items[6], inv.items[8], inv.items[10] = Buildings.Constuction_table(Buildings.i, [[['5','images - Current Version\Iron Rod.png'], ['5','images - Current Version\Iron Plate.png'], ['5','images - Current Version\Wire.png']], ['1', 'images - Current Version\Rotor.png']],  [[inv.items[5], 5], [inv.items[6], 5], [inv.items[8], 5]], [inv.items[10], 1], False)
      inv.items[5], inv.items[6], inv.items[11] = Buildings.Constuction_table(Buildings.i, [[['12','images - Current Version\Iron Rod.png'], ['6','images - Current Version\Iron Plate.png']], ['1','images - Current Version\Iron Crate.png']],  [[inv.items[5], 12], [inv.items[6], 6]], [inv.items[11], 1], False)
      # inputs, output = (buildings.i, 'name', [[inv.items[?], inv.items[?]], [amount, amount]], [[constuction bench new recipes], [new research names], [new research recipes], [new machine names]]
      [inv.items[4]] = Buildings.Research_center(Buildings.i, 'iron basics', [[inv.items[4]], [20]], [[[[['1','images - Current Version\Iron Ingot.png']], ['1','images - Current Version\Iron Rod.png']], [[['1','images - Current Version\Iron Ingot.png']], ['1','images - Current Version\Iron Plate.png']]], ['copper basics', 'molders'], [[['30','images - Current Version\Iron Rod.png'], ['30','images - Current Version\Iron Plate.png']], [['50','images - Current Version\Iron Rod.png'], ['50','images - Current Version\Iron Plate.png']]], []])
      inv.items[5], inv.items[6] = Buildings.Research_center(Buildings.i, 'copper basics', [[inv.items[5], inv.items[6]] , [30, 30]], [[[[['1','images - Current Version\Inv Copper Ore.png']], ['1','images - Current Version\Copper Ingot.png']], [[['1','images - Current Version\Copper Ingot.png']], ['1','images - Current Version\Wire.png']], [[['1','images - Current Version\Copper Ingot.png']], ['1','images - Current Version\Copper Sheet.png']]], ['manufacturing', 'smelters', 'pipes'], [[['30','images - Current Version\Iron Rod.png'], ['30','images - Current Version\Iron Plate.png'], ['30','images - Current Version\Wire.png'], ['30','images - Current Version\Copper Sheet.png']], [['30','images - Current Version\Iron Rod.png'], ['30','images - Current Version\Iron Plate.png'], ['30','images - Current Version\Copper Sheet.png']], [['50','images - Current Version\Copper Sheet.png']]], []])
      inv.items[5], inv.items[6] = Buildings.Research_center(Buildings.i, 'molders', [[inv.items[5], inv.items[6]] , [50, 50]], [[], [], [], ['molder']])
      inv.items[5], inv.items[6], inv.items[8], inv.items[9] = Buildings.Research_center(Buildings.i, 'manufacturing', [[inv.items[5], inv.items[6], inv.items[8], inv.items[9]] , [30, 30, 30, 30]], [[[[['5','images - Current Version\Iron Rod.png'], ['5','images - Current Version\Iron Plate.png'], ['5','images - Current Version\Wire.png']], ['1','images - Current Version\Rotor.png']], [[['12','images - Current Version\Iron Rod.png'], ['6','images - Current Version\Iron Plate.png']], ['1','images - Current Version\Iron Crate.png']]], [], [], []])
      inv.items[5], inv.items[6], inv.items[9] = Buildings.Research_center(Buildings.i, 'smelters', [[inv.items[5], inv.items[6], inv.items[9]] , [30, 30, 30]], [[], [], [], ['smelter']])
      [inv.items[9]] = Buildings.Research_center(Buildings.i, 'pipes', [[inv.items[9]] , [80]], [[], [], [], ['pipe']])
      #(buildings.i, machine, [[[input amount, input recipe, pickupable]], [output amount, output recipe, pickupable]], [[]])
      Buildings.automated_machines(Buildings.i, 'smelter', [[['1','images - Current Version\Inv Iron Ore.png', True]], ['1','images - Current Version\Iron Liquid.png', False]],  [[1, 1]], ['iron liquid', 1, 64], True)
      Buildings.automated_machines(Buildings.i, 'smelter', [[['1','images - Current Version\Inv Copper Ore.png', True]], ['1','images - Current Version\Copper Liquid.png', False]],  [[2, 1]], ['copper liquid', 1, 64], False)
      Buildings.automated_machines(Buildings.i, 'molder', [[['1', 'images - Current Version\Iron Liquid.png', False]], ['1',  'images - Current Version\Iron Ingot.png', True]],  [['iron liquid', 1]], [4, 1, 64], True)
      Buildings.automated_machines(Buildings.i, 'molder', [[['1', 'images - Current Version\Copper Liquid.png', False]], ['1',  'images - Current Version\Copper Ingot.png', True]],  [['copper liquid', 1]], [5, 1, 64], False)
      Buildings.pipe(Buildings.i)
    Buildings.automation()
  elif py72 == 'Tutorial':
    Ui.tutorial()
  else:
    if Home_page == True:
      Load == False
      home_screen.main_page()
    elif Load == True:
      if Ui.load_game(files) == True:
        Main_game = True
        tiles.done_pt2 = True
    else:
      if Save == True:
        values = tiles.colours
        if Ui.save_game(files) == True:
          Main_game = True
          tiles.done_pt2 = True
      elif Load == True:
        if Ui.load_game(files) == True:
          Main_game = True
          tiles.done_pt2 = True
          Save = False
      else:
        Ui.options_screen()
  if py72 == 'God':
    for z in range(len(inv.items)):
      inv.items[z] = 10000
  pygame.display.update()
  
  time.sleep(0.05)