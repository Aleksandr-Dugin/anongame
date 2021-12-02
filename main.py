import pygame 
from consts import * 
import time 
import random

SIZE = 150
clock = pygame.time.Clock()

class Snake:

    def __init__(self, screen, length):
    
        self.length = length
        self.count = 0
        self.x = [SIZE] * self.length 
        self.y = [SIZE] * self.length
        self.heigth =  SURF_HEIGTH 
        self.width = SURF_WIDTH 
        self.screen = screen 
        self.anon = pygame.image.load("images/snake.png").convert() 
        self.anon = pygame.transform.scale(self.anon, (self.width, self.heigth))
        self.direction = "down"     


    def move_left(self): 
        #self.direction = "left"
        
        self.direction = "left" 

    def move_rigth(self): 
        #self.x = "rigth" 
        self.direction = "rigth" 
    def move_up(self):
        #self.direction = "up" 
        self.direction = "up" 
    def move_down(self): 
        #self.direction = "down"
        self.direction = "down"

    def draw(self): 
        
        for i in range(self.length): 
            
            self.screen.blit(self.anon, (self.x[i], self.y[i]))        

    

#        pygame.display.flip()


    def border_check(self):  

        if self.x[0] < -50: 
            self.x[0] = 850
        if self.x[0] > 950: 
            self.x[0] =0
        if self.x[0]< -50: 
            self.x[0] = 850
        
        if self.x[0] > 850: 
            self.x[0]= 0
        if self.y[0] < -100: 
            self.y[0] = 700
        elif  self.y[0] > 800: 
            self.y[0] = 0
        if self.y[0] < -100: 
            self.y[0] = 700
        elif self.y[0] > 800: 
            self.y[0] = 0

    def increase_length(self): 
        self.length+=1
        self.x.append(-1) 
        self.y.append(-1)




    def walk(self): 
        for i in range(self.length - 1, 0, -1): 
            self.x[i] = self.x[i -1]
            self.y[i] = self.y[i - 1]  


        if self.direction == "rigth": 
            self.x[0] += 50 
        if self.direction == "down": 
            self.y[0] += 50
        if self.direction == "left": 
            self.x[0] -= 50
        if self.direction == "up": 
            self.y[0] -=50

        self.draw()


    '''def walk: 
        if self.direction == "down": 
            self.y -= 5
        if self.direction == "up": 
            self.y += 5
        if self.direction == "left": 
            self.x -= 5
        if self.direction == "rigth": 
            self.x += 5 

        self.draw()         
'''


class Game: 
    def __init__(self): 
        pygame.init() 
        
        self.screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGTH_SCREEN)) 

        self.apple = Apple(self.screen) 
        self.snake = Snake(self.screen, 1)     
        self.snake.draw() 
        self.apple.draw()

   
    def is_collision(self, x1, y1, x2, y2):
        #if x1 >= x2 and x1 < x2 + SIZE: 
            #if y1 >= y2 and y1 < y2 + SIZE: 
         
        if (abs(x1 - x2) < 50 and abs(y1- y2) < 100): 

             return True 
        return False 


    def render_background(self): 
        bg = pygame.image.load("images/138853-haker-haker_bezopasnosti-golovnoj_ubor-shlyapa-anonimnye_narkomany-1920x1080.jpg") 	
        self.screen.blit(bg, (0,0))
    
    def play(self): 

        self.render_background() 
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
        
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.apple.move()
            self.snake.increase_length()
        for i in range(3, self.snake.length): 
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game over" 

    def show_game_over(self): 
        self.render_background() 
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Hack is over! Youre killed capitalist are: {self.snake.length - 1}", True, (255, 255, 255))
        self.screen.blit(line1, (100,500))
        line2 = font.render("To hack again press Enter. To leave press Escape!", True, (255, 255, 255))
        self.screen.blit(line2, (100,400))
        pygame.display.flip()


    def reset(self):
        self.apple = Apple(self.screen) 
        self.snake = Snake(self.screen, 1)     



       
    def run(self): 
       
        run = True 
        pause = False
        while run: 
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    run = False 
        
            keys = pygame.key.get_pressed() 
            
            self.snake.border_check()   
            if keys[pygame.K_RETURN]: 
                pause = False 
    
            if not pause: 

                if keys[pygame.K_RIGHT]: 
                    self.snake.move_rigth() 

                if keys[pygame.K_LEFT]: 

                    self.snake.move_left()

                if keys[pygame.K_UP]: 
                    self.snake.move_up()
                     
                if keys[pygame.K_DOWN]: 

                    self.snake.move_down()
            try:
                if not pause: 
                    self.play()
            except Exception as e: 
                self.show_game_over()
                pause = True 
                self.reset()

            time.sleep(0.18)
            clock.tick(200) 

    def display_score(self): 
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))        
        self.screen.blit(score, (750,30))
        self.snake.count+=1







class Apple: 
    def __init__(self, screen): 
        self.screen = screen 
        self.x = ENEMY_X 
        self.y = ENEMY_Y
        self.width = SURF_WIDTH + 10
        self.heigth = SURF_HEIGTH + 10
        
        self.image = [
                    pygame.image.load("images/tim_cook.png"),
                    pygame.image.load("images/mark_zuck.png"),
                    pygame.image.load("images/bill_gates.png")
                ]
        self.image = [
                    pygame.transform.scale(self.image[0], (self.width, self.heigth)),
                    pygame.transform.scale(self.image[1], (self.width, self.heigth)), 
                    pygame.transform.scale(self.image[2], (self.width, self.heigth)),
            ]

        self.rand_img = random.choice(self.image)
    def move(self): 

        self.rand_img = random.choice(self.image)
        self.x = randint(0, 850)
        self.y = randint(0, 700)




    def draw(self):
        self.screen.blit(self.rand_img, (self.x, self.y)) 
        #pygame.display.flip() 
    

if __name__ == "__main__": 
    game = Game() 
    game.run()





