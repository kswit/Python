import pygame 
import numpy as np

def gauss_elimination(A,b):
    #b = np.array([400, 300])
    x=[0,0]
    if np.linalg.det(A) != 0:
        x = np.linalg.solve(A, b)
    #print(A)
    return x

def drawfunk():
    for ix in range(0,WIDTH,50):
        for iy in range(0,HEIGHT,50):
            animated_object.x=ix
            animated_object.y=iy
            A=[[ix-400,iy-300],[mousex-400,mousey-300]]
            b=[400,300]
            sx,sy=gauss_elimination(A,b)
            animated_object.drawline(400+sx,300+sy)

def gauss_elimination1(A, b):
    n = len(A)

    # Eliminacja do postaci schodkowej
    for i in range(n):
        # Wybierz element główny
        max_index = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_index][i]):
                max_index = j
        A[i], A[max_index] = A[max_index], A[i]
        b[i], b[max_index] = b[max_index], b[i]

        # Eliminacja wierszy poniżej i-tej
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    # Wyliczenie rozwiązania
    x1 = [0] * n
    if (A[i][i] == 0.0):return [1,1]
    for i in range(n - 1, -1, -1):
        x1[i] = b[i] / A[i][i]
        for j in range(i):
            b[j] -= A[j][i] * x1[i]

    return x1




pygame.init()
mouse = pygame.mouse.get_pos()
WIDTH, HEIGHT = 800, 600

class AnimatedObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = WIDTH
        self.height = HEIGHT
        self.velocity = 1
        self.m1=1
        self.m2=1

    def update(self):
        # Przesunięcie obiektu w prawo
        #self.x += self.velocity
        self.x+=self.m1*self.velocity
        self.y+=self.m2*self.velocity
        # Jeśli obiekt przesunął się poza ekran, zacznij od początku
        if self.x > WIDTH:
            self.x = 1
        if self.y > HEIGHT:
            self.y = 1
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0

    def draw(self):
        pygame.draw.circle(screen, "red", (self.x, self.y,),40)

    def drawline(self,lx,ly):
        pygame.draw.line(screen,"green",(self.x,self.y),(lx,ly),1)


    def mousemove(self,posx,posy):
        solution=[0,0]
        A=[[self.x,self.y],[posx,posy]]
        #print ("maciez",A)
        b = [100,100]
        if (mousex<800 and mousey <600 and mousex >0 and mousey >0):
            solution=gauss_elimination(A, b)
            newx,newy=solution
        #if (newx>0): 
        #if (newx>0): 
            self.m1=newx
            self.m2=newy
        

screen = pygame.display.set_mode((800, 600))
clock=pygame.time.Clock()
animated_object = AnimatedObject(WIDTH /2 , HEIGHT / 2)

#player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
running = True
speed=1

while running:
    mousex,mousey=0,0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
         
        elif event.type == pygame.MOUSEMOTION :
            pygame.Surface.fill(screen,"black")
            mousex,mousey=event.pos
            #print (mousex ,mousey  )
            if (mousex<800 and mousey <600 and mousex >0 and mousey >0):
                #animated_object.mousemove(mousex,mousey)
                drawfunk()
            #print (A)
    pygame.display.flip()
    #pygame.draw.line(screen,"blue",(mousex,mousey),(animated_object.x,animated_object.y), 1)
    #animated_object.update()
    #animated_object.draw()

    #if(mousex!=0):drawfunk()
    
    clock.tick(60)
    
pygame.quit()
