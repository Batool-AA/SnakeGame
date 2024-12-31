
import pygame      # importing libraries (1-3)
from pygame.locals import *
from pygame import mixer
import random
pygame.init()      #pygame initialization

#front screen design 
scr=pygame.display.set_mode((500,500))   #dimension
pygame.display.update()
pygame.display.set_caption('Snake game')    
img = pygame.image.load("snakebg2.jpg")   #bg img (9,10)
scr.blit(img,(0,0))
pygame.display.update()

#music
mixer.music.load('bgsong.wav') 
mixer.music.play(-1)    #to play it in a loop   

#screen text(13-22)
font = pygame.font.SysFont("Times New Roman",40)   
text = font.render("Snake Game",True,((5,5,5)))
scr.blit(text,[150,150])
font = pygame.font.SysFont("Times New Roman",20)
text_quit = font.render("Press Q to Quit",True,((5,5,5)))
scr.blit(text_quit,[170,250])
font = pygame.font.SysFont("Times New Roman",20)
text_c = font.render("Press S to Start",True,((5,5,5)))
scr.blit(text_c,[170,300])
pygame.display.update()

gamestart = True     #loop to keep the screen on until player presses "s" to start the game (23-32)

while gamestart:
      for event in pygame.event.get(): #pygame function to input keys
            if event.type== QUIT:    #input through mouse
                     pygame.quit()
            elif event.type== KEYDOWN:    #user gives input through keys (28-32)
               if event.key == K_q:
                     pygame.quit()
               if event.key == K_s:
                     gamestart = False
    
#function that summarizes everything happening in the game 

def game():

      snake_length = 20     #snake dimensions (35,36)
      snake_width = 20   

      snake_x = 250         #snake position (37,38)
      snake_y = 250

      x_change = 0          # initializing changing position of snake that is used below when the player presses left right up down keys (39,40)
      y_change = 0

      start= True           # initializing start so the loop works and game continues until the player hits walls or itself and game ends, start gets false and loop ends
      
      food_x = random.randint(50,450)   #initializing food position as random (42,43)
      food_y = random.randint(50,450) 

      score = 0             #initial score and speed
      speed = 10
      
      direction = "vertical"    #initializing a direction

      #starting game
      while start:
            for event in pygame.event.get(): #function to get input
                  if event.type== QUIT:    #exits through mouse
                        pygame.quit()

                  elif event.type== KEYDOWN:    #user gives input through keys 
                        if event.key== K_ESCAPE:   #escapes through keyboard (esc)
                              pygame.quit()

                        elif event.key== K_DOWN:    #down arrow adds 10 to the value of y and snake moves down
                              y_change = 10
                              x_change = 0
                              if (direction != "vertical" and snake_length != snake_width):
                                    snake_length, snake_width = snake_width, snake_length
                                    direction = "vertical"

                        elif event.key== K_UP:       #up arrow adds -10 to the value of y and snake moves up
                              y_change = -10
                              x_change = 0
                              if (direction != "vertical" and snake_length != snake_width):
                                    snake_length, snake_width = snake_width, snake_length
                                    direction = "vertical"

                        elif event.key== K_LEFT:      #left arrow adds -10 to the value of x and snake moves left
                              x_change = -10
                              y_change = 0
                              if (direction != "horizontal" and snake_length != snake_width):
                                    snake_length, snake_width = snake_width, snake_length
                                    direction = "horizontal"
                        
                        elif event.key==  K_RIGHT:      #right arrow adds 10 to the value of x and snake moves right
                              x_change = 10
                              y_change = 0
                              if (direction != "horizontal" and snake_length != snake_width):
                                    snake_length, snake_width = snake_width, snake_length
                                    direction = "horizontal"

            if snake_x >= 500 or snake_y >=500  or snake_x < 0 or snake_y < 0:   #if snake enters the border it dies
                  start = False

            snake_x += x_change    #changing snakes position 
            snake_y += y_change 
            scr.fill((140,199,14))     #screen fills itself when the snake leaves the spot  

            food = pygame.draw.rect(scr,((237,16,0)),[food_x,food_y,15,15])    #1: location x   2: location y   3,4: dimensions drawing food
            snake = pygame.draw.rect(scr,((0,0,255)),[snake_x,snake_y,snake_width,snake_length])   #1: location x   2: location y   3,4: dimensions drawing snake
            pygame.display.update()

            #score dimensions and properties 
            font_score = pygame.font.SysFont("Times New Roman",25)  
            text_score = font_score.render("Score: " + str(score),True,((5,5,5)))
            scr.blit(text_score,[10,10])
            pygame.display.update()

            #if snake collides with food
            if snake.colliderect(food):

                  food_x = random.randint(50,450)   #when snake collides food changes position
                  food_y = random.randint(50,450) 
                  pygame.draw.rect(scr,((237,16,0)),[food_x,food_y,15,15])
                  pygame.display.update()
                  
                  if direction == "vertical":  # if snake is moving up or down while colliding with the food, the length increases
                        snake_length += 10
                  elif direction == "horizontal":   #if the snake is moving left or right while colliding with the food, the width increases
                        snake_width += 10
                  pygame.draw.rect(scr,((0,0,255)),[snake_x,snake_y,snake_width,snake_length])

                  
                  score += 10     #score increases
                  font_score = pygame.font.SysFont("Times New Roman",25)
                  text_score = font_score.render("Score: " + str(score),True,((5,5,5)))
                  scr.blit(text_score,[10,10])
                  pygame.display.update()

                  # speed of snake increases
                  speed += 2 
                  
            clock = pygame.time.Clock()  
            clock.tick(speed)   #making the snake move at a given speed
            
      # gameover screen      
      img = pygame.image.load("snakebg2.jpg") #bg img
      scr.blit(img,(0,0))
      pygame.display.update() 

      #game over screen text
      font = pygame.font.SysFont("Times New Roman",40)
      text = font.render("Game Over",True,((5,5,5)))
      scr.blit(text,[150,150])
      font = pygame.font.SysFont("Times New Roman",20)
      text_quit = font.render("Press Q to Quit",True,((5,5,5)))
      scr.blit(text_quit,[170,250])
      font = pygame.font.SysFont("Times New Roman",20)
      text_c = font.render("Press S to Restart",True,((5,5,5)))
      scr.blit(text_c,[160,300])
      font_score = pygame.font.SysFont("Times New Roman",20)
      text_score = font_score.render("Score: " + str(score),True,((5,5,5)))
      scr.blit(text_score,[190,350])
      pygame.display.update()

      #making the screen appear
      gameover = True
      while gameover:
            for event in pygame.event.get(): #function to take input from user
                  if event.type== QUIT:    #quit through mouse
                        pygame.quit()
                  elif event.type== KEYDOWN:    #user gives input through keys
                        if event.key == K_ESCAPE:
                              pygame.quit()
                        if event.key == K_q:
                              pygame.quit()
                        if event.key == K_s:    #game restarts on pressing "s"
                              game()

game()     #calling the function to run the game
        
                     
               


               
