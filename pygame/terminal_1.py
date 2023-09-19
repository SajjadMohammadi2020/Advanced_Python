import pygame




inpu = []
con = True
while con : 
    vo = input()
    inpu.append(vo)
    if "end" in vo : 
        con = False 
pygame.init()
pen_size = 1
pen_col = (0,0,0)
screen = pygame.display.set_mode((300,300))
white = (255,255,255)
screen.fill(white)
for inp in inpu : 
    pygame.event.pump()
    if "end" in inp : 
        con = False
        pygame.image.save(screen, 'draw.png')
    if "change size" in inp : 
        new = int(inp.split(" ")[-1])
        pen_size = new
    if "change color" in inp : 
        R , G , B = map(int , inp.split(" ")[2:5])
        pen_col = (R,G,B)
    if "draw line" in inp : 
        a1_1,a1_2,a2_1,a2_2 = map(int,inp.split(" ")[2:6])
        a1 = (a1_1,a1_2)
        a2 = (a2_1,a2_2)
        pygame.draw.line(screen,pen_col,a1,a2,pen_size)
    if "draw circle" in inp : 
        c_1 , c_2 , r = map(int,inp.split(" ")[2:5])
        center = (c_1,c_2)
        pygame.draw.circle(screen,pen_col,center,r,pen_size)
    if "draw polygon" in inp : 
        v = []
        for i in map(int,inp.split(" ")[2:]) : 
            v.append(i)
        ras = []
        print(v)
        for i in range(0,len(v),2): 
            a = (v[i] , v[i+1])
            ras.append(a)
        pygame.draw.polygon(screen,pen_col,ras,pen_size)
    pygame.display.update()
pygame.event.pump()
