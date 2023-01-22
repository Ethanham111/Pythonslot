import pygame
import numpy

#Identified symbols for Slot Machine, Probability of Getting them and How much Money you would win if you got 3 in a row
symbols = ["Apple", "Banana", "Kiwi", "Mango", "Strawberry"]
symbols_prob = [0.35, 0.25, 0.15, 0.15, 0.10]
symbols_winnings = {"Apple": 5, 
                    "Banana": 15, 
                    "Kiwi":35 , 
                    "Mango": 35, 
                    "Strawberry": 100
}
#Added the images to the slot machine to fit the black spaces
symbol_images = {"Apple": pygame.image.load('Assets/apple.png'), 
                "Banana": pygame.image.load('Assets/banana.png'), 
                "Kiwi": pygame.image.load('Assets/kiwi.png') , 
                "Mango": pygame.image.load('Assets/mango.png'), 
                "Strawberry": pygame.image.load('Assets/strawberry.png')
}
#Load image from Assets folder and sets its position 
class symbol_local(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, icon):
        super().__init__()
        self.image = pygame.image.load("Assets/"+icon+".png")
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def set_picture(self,image):
        self.image = image

#The game itself. We set the 3 symbools and if they draw 3 in a row, they get money! If not, they lose 15$ 
total = 500 #Total is given a value beforehand but I can improve in the future by getting user input?!
def run():
    global total
    rand_symbols = numpy.random.choice(symbols, 3, p= symbols_prob)

    box_left.set_picture(symbol_images[rand_symbols[0]])
    box_mid.set_picture(symbol_images[rand_symbols[1]])
    box_right.set_picture(symbol_images[rand_symbols[2]])

    if rand_symbols[0] == rand_symbols[1] == rand_symbols[2]:
        money = symbols_winnings[rand_symbols[0]]
        total += money
    else:
        total -= 15
        if total <= 0:
            pygame.quit()


#Initializing the GUI
pygame.init()
width = 800
height = 550
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Slot Machine created by Ethan Hamburg")
logo=pygame.image.load('Assets/slot-machine.png')
pygame.display.set_icon(logo)
white = [250, 250, 250]
screen.fill(white)


background = pygame.image.load('Assets/slot-machine.png')
view_total = pygame.font.SysFont("freesansbold.ttf", 50)
view_menu = pygame.font.SysFont("freesansbold.ttf", 25)

#COMPLETE GUESSING GAME FOR THE ALIGNMENT IT TOOK ME SO LONG ;-;
symbol_height = height / 2.75 
placeholder = pygame.sprite.Group()
box_left = symbol_local(40, symbol_height, "Apple")
box_mid = symbol_local(162, symbol_height, "Banana")
box_right = symbol_local(285, symbol_height,"Kiwi")

placeholder.add(box_left)
placeholder.add(box_mid)
placeholder.add(box_right)

#SAME THING HERE COMPLETE GUESSING GAME FOR THE ALIGNMENT
#Showcases the symbols on the side and their values
place_menu = pygame.sprite.Group()
place_1 = symbol_local(640, 100, "Apple")
place_2 = symbol_local(640, 175, "Banana")
place_3 = symbol_local(640, 250, "Kiwi")
place_4 = symbol_local(640, 325, "Mango")
place_5 = symbol_local(640, 400, "Strawberry")

#side menu for values
place_menu.add(place_1)
place_menu.add(place_2)
place_menu.add(place_3)
place_menu.add(place_4)
place_menu.add(place_5)

#The magic: Displays return next to Symbols (ANOTHER GUESSING GAME WITH ALIGNMENT) Use left click to spin!
text = view_total.render("Total amount: $" +str(total), True, (0,0,0))
game_run = True 
while game_run:
    screen.fill(white)
    screen.blit(background, (0, 0))
    placeholder.draw(screen)
    text = view_total.render("Total amount: $" +str(total), True, (0,0,0))
    screen.blit(text, (400, 25))
    menu1 = view_menu.render("3x = $5", True, (0, 0, 0))
    screen.blit(menu1, (550, 125))
    menu2 = view_menu.render("3x = $15", True, (0, 0, 0))
    screen.blit(menu2, (550, 200))
    menu3 = view_menu.render("3x = $35", True, (0, 0, 0))
    screen.blit(menu3, (550, 275))
    menu4 = view_menu.render("3x = $35", True, (0, 0, 0))
    screen.blit(menu4, (550, 350))
    menu5 = view_menu.render("3x = 100$", True, (0, 0, 0))
    screen.blit(menu5, (550, 425))
    place_menu.draw(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                run()





