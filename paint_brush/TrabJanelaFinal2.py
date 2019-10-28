import sys,pygame,math,numpy
from pygame import gfxdraw

Formas =[]
Menu = []
#Start Valeu
Width = 900
Heigth = 900
WindowColor = (255,255,255)
Menux = 150
SetCOLOR = (0,0,0)
# start config
pygame.init()
screen = pygame.display.set_mode((Width,Heigth))
screen.fill(WindowColor)
pygame.display.flip()


#In window objects
'''
ID LIST:
0 = Circulo
1 = Linha
2 = Retangulo
3 = Quadrado
'''
Bottons = [] #(x1,y1,x2,y2)
GRID = []
#Colors
RED = (255,0,0)
BLUE = (0,0,255)
GREEN =(0,255,0)
BLACK = (0,0,0)
White = (255,255,255)
GRAY = (220,220,250)
ORANGE =(255,100,10)
YELLOW = (255,255,0)
BROWN = (100,40,0)
FGREEN =(0,50,0)
PINK =(255,100,100)
BLUEGREEN =(0,255,170)
LIME = (180,255,100)
NBLUE = (0,0,100)
SBLUE = (0,255,255)
PURPLE = (240,0,255)

def Colorfill(x1,x2,Cor):
	x = x1
	for x in range(x2):
		for y in range(Heigth):
			screen.set_at((x,y),Cor)
			y+=1
		x+=1

def ColorFULL(x1,y1,x2,y2,color):
	x = x1
	y = y1
	while y < y2:
		x = x1
		while x < x2:
			screen.set_at((x,y),color)
			x+=1
		y+=1
def COLORGRID(i,j):
	if i == 0:
		if j ==0:
			return RED
		if j ==1:
			return ORANGE
		if j == 2:
			return YELLOW
		if j == 3:
			return PINK
	elif i == 1:
		if j ==0:
			return BLUE
		if j ==1:
			return NBLUE
		if j == 2:
			return SBLUE
		if j == 3:
			return BLUEGREEN
	elif i == 2:
		if j ==0:
			return FGREEN
		if j ==1:
			return GREEN
		if j == 2:
			return LIME
		if j == 3:
			return BROWN
	elif i == 3:
		if j ==0:
			return BLACK
		if j ==1:
			return (180,180,180)
		if j == 2:
			return White
		if j == 3:
			return PURPLE

def PaintGRID():
	for i in range(4):
		for j in range(4):
			ColorFULL(GRID[0][j],GRID[1][i],GRID[0][j+1],GRID[1][i+1],COLORGRID(i,j))
def criaPainel():
	global Bottons
	x = Menux
	breseham(x,0,x,Heigth,BLACK)
	Menu.append((1,x,0,x,Heigth,BLACK))
	offset = round(Heigth/9)
	BottonH = 0
	GridH   = 2*offset
	Menu.append((1,0,BottonH,x,BottonH,BLACK))
	for i in range(7):
		Bottons.append((0,BottonH,x,BottonH+offset))
		BottonH = BottonH + offset
		Menu.append((1,0,BottonH,x,BottonH,BLACK))
		
		
	Grid(0,BottonH,x,BottonH + GridH,4)
	
def Grid(x1,y1,x2,y2,Num):
		W = round((x2-x1)/Num)
		H = round((y2-y1)/Num)
		newy = y1 + H
		newx = x1 + W
		while newy < y2 and newx< x2:
			Menu.append((1,x1,newy,x2,newy,BLACK))
			newy = newy + H
			Menu.append((1,newx,y1,newx,y2,BLACK))
			newx = newx + W
		
		GRID.append((x1,x1+W,x1+W+W,x1+W+W+W,x2))
		GRID.append((y1,y1+H,y1+H+H,y1+H+H+H,y2))
		Simbolos()

		
def Simbolos():
	global Bottons
	offset =  Bottons[0][3] - Bottons[0][1]
	offsetx = Bottons[0][2] - Bottons[0][0]
	Menu.append((1,10,(Bottons[0][1])+10,Bottons[0][2] - 10 ,(Bottons[0][3])-10,BLACK)) #desenha um linha no botao1
	
	cx = round(Bottons[1][2]/2)
	cy = round(Bottons[1][3] - Bottons[1][1]/2)
	r  = round((offset-10)/2)
	Menu.append((0,cx,cy,r,BLACK)) # desenha um circulo no botao2
	
	Menu.append((2,Bottons[2][0]+10,Bottons[2][1]+10,Bottons[2][2]-10,Bottons[2][3]-10,BLACK)) # desenha um retangulo no botao 3
	
	cx = round(Bottons[3][2]/2)
	cy = round(Bottons[3][3] - (offset/2))
	r  = round((offset - 10) /2)
	Menu.append((3,cx,cy,r,BLACK))
	
	# inicio da polilinha no botao 5
	midx=round(Bottons[4][0]/2)
	midy=Bottons[4][1]+round(offset/2)
	Menu.append((1,Bottons[4][0]+10,Bottons[4][3]-10,round(offsetx/3),Bottons[4][1]+10,BLACK)) 
	Menu.append((1,round(offsetx/3),Bottons[4][1]+10,round(offsetx/3)*2,Bottons[4][3]-10,BLACK))
	Menu.append((1,round(offsetx/3)*2,Bottons[4][3]-10,Bottons[4][2]-10,Bottons[4][1]+10,BLACK))
	#fim da polilinha
	
	#inicio da curva no Botão 6
	midx = round(Bottons[5][2]/2)
	Menu.append((6,(Bottons[5][0]+10,Bottons[5][1]+10),(midx,Bottons[5][1]-10),(Bottons[5][2]-10,Bottons[5][3]-10),BLACK))
	
	
	
	
	





def printFormas():
    global Formas
    for i in range(len(Formas)):
        if Formas[i][0] == 0:
            midpointCircle(Formas[i][1],Formas[i][2],Formas[i][3],Formas[i][4])
        elif Formas[i][0] == 1:
            breseham(Formas[i][1],Formas[i][2],Formas[i][3],Formas[i][4],Formas[i][5])		
        elif Formas[i][0] == 2:
            retangulo(Formas[i][1],Formas[i][2],Formas[i][3],Formas[i][4],Formas[i][5])
        elif Formas[i][0] == 3:
            midpointSquare(Formas[i][1],Formas[i][2],Formas[i][3],Formas[i][4])
        elif Formas[i][0]==5:
            floodfill(Formas[i][1],Formas[i][2],Formas[i][3])
        else:
            bezierQuadrada(Formas[i][1],Formas[i][2],Formas[i][3],Formas[i][4])
    printMenu()		
    pygame.display.update()

def printMenu():
	global Menu
	Colorfill(0,Menux,GRAY)
	PaintGRID()
	for i in range(len(Menu)):
		if Menu[i][0] == 0:
			midpointCircle(Menu[i][1],Menu[i][2],Menu[i][3],Menu[i][4])
		elif Menu[i][0] == 1:
			breseham(Menu[i][1],Menu[i][2],Menu[i][3],Menu[i][4],Menu[i][5])		
		elif Menu[i][0] == 2:
			retangulo(Menu[i][1],Menu[i][2],Menu[i][3],Menu[i][4],Menu[i][5])
		elif Menu[i][0] ==3:
			midpointSquare(Menu[i][1],Menu[i][2],Menu[i][3],Menu[i][4])
		else:
			bezierQuadrada(Menu[i][1],Menu[i][2],Menu[i][3],Menu[i][4])
	pygame.display.update()
# display 1/8 of circle
def Octeto(x,y,c1,c2,value):
	screen.set_at((x+c1,y+c2),value)
	screen.set_at((-x+c1,y+c2),value)
	screen.set_at((-y+c1,x+c2),value)
	screen.set_at((-y+c1,-x+c2),value)
	screen.set_at((-x+c1,-y+c2),value)
	screen.set_at((x+c1,-y+c2),value)
	screen.set_at((y+c1,-x+c2),value)
	screen.set_at((y+c1,x+c2),value)
	
	
	

def midpointCircle(c1,c2,radius,value):
	x = 0
	y = radius
	d = 1 -radius
	#offset = int(math.sqrt((c1)**2 + (c2)**2))
	screen.set_at((x+c1,y+c2),value)
	screen.set_at((y+c1,x+c2),value)
	screen.set_at((-y+c1,-x+c2),value)
	screen.set_at((-x+c1,-y+c2),value)
	while y > x :
		if d < 0 :
			d+= (2*x)+2
		else:
			d+= 2*(x-y)+5
			y-=1
		x+=1
		
		
		Octeto(x,y,c1,c2,value)


	
		

def breseham(x0, y0, x1, y1,value):

    dx = x1 - x0
    dy = y1 - y0

    if dy < 0:
        dy = -dy
        stepy = -1
    else:
        stepy = 1

    if dx < 0:
        dx = -dx
        stepx = -1
    else:
        stepx = 1

    dx <<= 2
    dy <<= 2

    screen.set_at((x0,y0),value)

    if dx > dy:
        fraction = dy - (dx >> 1)
        while x0 != x1:
            if fraction >= 0:
                y0 += stepy
                fraction -= dx
            x0 += stepx
            fraction += dy
            screen.set_at((x0,y0),value)
    else:
        fraction = dx - (dy >> 1)
        while y0 != y1:
            if fraction >= 0:
                x0 += stepx
                fraction -= dy
            y0 += stepy
            fraction += dx
            screen.set_at((x0,y0),value)

	


	
def Circle(value):
		BottonCliked = False
		global Formas
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
					return
				if event.type == pygame.MOUSEBUTTONUP:
					if not BottonCliked:
							
						cx = pygame.mouse.get_pos()[0]
						cy = pygame.mouse.get_pos()[1]
						BottonCliked = True
							
					else:
							
						endx = pygame.mouse.get_pos()[0]
						endy = pygame.mouse.get_pos()[1]
						rad = int(math.sqrt((endx - cx)**2 + (endy - cy)**2))
						Formas.append((0,cx,cy,rad,value))
						BottonCliked = False
						return;
							
				if event.type == pygame.MOUSEMOTION:
					if BottonCliked:
						auxx = pygame.mouse.get_pos()[0]
						auxy = pygame.mouse.get_pos()[1]
						screen.fill(WindowColor)
						#pygame.display.flip()
						rad = int(math.sqrt((auxx - cx)**2 + (auxy - cy)**2))
						midpointCircle(cx,cy,rad,value)
						printFormas()
						printMenu()
				if event.type == pygame.QUIT: 
					sys.exit()
def Line(value):
		BottonCliked = False
		global Formas
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
					return
				if event.type == pygame.MOUSEBUTTONUP:
					if not BottonCliked:
							
						inix = pygame.mouse.get_pos()[0]
						iniy = pygame.mouse.get_pos()[1]
						BottonCliked = True
					else:
							
						endx = pygame.mouse.get_pos()[0]
						endy = pygame.mouse.get_pos()[1]
						Formas.append((1,inix,iniy,endx,endy,value))
						BottonCliked = False
						return;
							
				if event.type == pygame.MOUSEMOTION:
					if BottonCliked:
						auxx = pygame.mouse.get_pos()[0]
						auxy = pygame.mouse.get_pos()[1]
						screen.fill(WindowColor)
						#pygame.display.update()
						breseham(inix,iniy,auxx,auxy,value)
						printFormas()
			
def Quarteto(x,y,c1,c2,value):
	screen.set_at((x+c1,y+c2),value)
	screen.set_at((-x+c1,y+c2),value)
	screen.set_at((-y+c1,x+c2),value)
	screen.set_at((-y+c1,-x+c2),value)
	screen.set_at((-x+c1,-y+c2),value)
	screen.set_at((x+c1,-y+c2),value)
	screen.set_at((y+c1,-x+c2),value)
	screen.set_at((y+c1,x+c2),value)
	
def midpointSquare(c1,c2,radius,value):
    x = 0
    y = radius
    d = 1 -radius
    offset = int(math.sqrt((c1)**2 + (c2)**2))

    
    screen.set_at((x+c1,y+c2),value)
    screen.set_at((y+c1,x+c2),value)
    screen.set_at((-y+c1,-x+c2),value)
    screen.set_at((-x+c1,-y+c2),value)
    
    while y > x :
        if d < 0 :
            d+= (2-x)+3
        else:
            d+= 2*(x-y)+5
            y-=1
        x+=1
		
        Quarteto(x,y,c1,c2,value)
 
		

def retangulo(x0, y0, x1, y1, value):
    breseham(x0, y0, x0, y1, value)
    breseham(x0, y0, x1, y0, value)
    breseham(x1, y0, x1, y1, value)
    breseham(x0, y1, x1, y1, value)
	
def Rectangle(value):
		BottonCliked = False
		global Formas
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
					return
				if event.type == pygame.MOUSEBUTTONUP:
					if not BottonCliked:
							
						inix = pygame.mouse.get_pos()[0]
						iniy = pygame.mouse.get_pos()[1]
						BottonCliked = True
							
					else:
							
						endx = pygame.mouse.get_pos()[0]
						endy = pygame.mouse.get_pos()[1]
						Formas.append((2,inix,iniy,endx,endy,value))
						BottonCliked = False
						return;
							
				if event.type == pygame.MOUSEMOTION:
					if BottonCliked:
						auxx = pygame.mouse.get_pos()[0]
						auxy = pygame.mouse.get_pos()[1]
						screen.fill((255,255,255))
						#pygame.display.flip()
						retangulo(inix,iniy,auxx,auxy,value)

						printFormas()
				
def Square(value):
		BottonCliked = False
		global Formas
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
					return
				if event.type == pygame.MOUSEBUTTONUP:
					if not BottonCliked:
						cx = pygame.mouse.get_pos()[0]
						cy = pygame.mouse.get_pos()[1]
						BottonCliked = True							
					else:                       
						endx = pygame.mouse.get_pos()[0]
						endy = pygame.mouse.get_pos()[1]
						rad = int(math.sqrt((endx - cx)**2 + (endy - cy)**2))
						Formas.append((3,cx,cy,rad,value))
						BottonCliked = False
						return;	
				if event.type == pygame.MOUSEMOTION:
					if BottonCliked:
						auxx = pygame.mouse.get_pos()[0]
						auxy = pygame.mouse.get_pos()[1]
						screen.fill((255,255,255))
						#pygame.display.flip()
						rad = int(math.sqrt((auxx - cx)**2 + (auxy - cy)**2))
						midpointSquare(cx,cy,rad,value)
						printFormas()
				

def floodfill(x, y,value):
    toFill = [(x, y)]
    oldColor = screen.get_at((x,y))[:3]
    #oldColor = WHITE
    while len(toFill) > 0:
        (x, y) = toFill.pop()        
  
        if screen.get_at((x,y))[:3] != oldColor: 
           continue
        
        screen.set_at((x,y),value)
        

        #pygame.display.flip()
        
        #toFill.append((x+1, y))
        #toFill.append((x-1, y))
        #toFill.append((x, y-1))
        #toFill.append((x, y+1))
        
        if x > 1:
            toFill.append((x-1, y))
        if x < Width-1:
            toFill.append((x+1, y))
        if y > 1:
            toFill.append((x, y-1))
        if y < Heigth-1:
            toFill.append((x, y+1))
        
        
def bezierQuadrada(p_ini,p_cont,p_fim,value):
        for t in numpy.arange(0,1,0.001):
                um_menos_t = 1-t
                um_menos_t_2 = um_menos_t*um_menos_t
                t2 = t*t
                x = um_menos_t_2 * p_ini[0] + (2*um_menos_t)*t*p_cont[0] + t2*p_fim[0]
                y = um_menos_t_2 * p_ini[1] + (2*um_menos_t)*t*p_cont[1] + t2*p_fim[1]
                x = int(numpy.floor(x))
                y = int(numpy.floor(y))
                screen.set_at((x,y), value)
                #pygame.display.flip()
       	
def Curve(value):
        count = 0
        global Formas
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                    return
                if event.type == pygame.MOUSEBUTTONUP:
                    if count == 0:
							
                        inix = pygame.mouse.get_pos()[0]
                        iniy = pygame.mouse.get_pos()[1]
                        count += 1
                    elif count == 1:
							
                        endx = pygame.mouse.get_pos()[0]
                        endy = pygame.mouse.get_pos()[1]
                        count += 1
                    else:
                        contx = pygame.mouse.get_pos()[0]
                        conty = pygame.mouse.get_pos()[1]
                        Formas.append((6,(inix,iniy),(contx,conty),(endx,endy),value))
                        count = 0
                        return
							
                if event.type == pygame.MOUSEMOTION:
                    if count == 1:
                        auxx = pygame.mouse.get_pos()[0]
                        auxy = pygame.mouse.get_pos()[1]
                        screen.fill(WindowColor)
                        #pygame.display.update()
                        breseham(inix,iniy,auxx,auxy,value)
                        printFormas()
                    elif count == 2:
                        auxx = pygame.mouse.get_pos()[0]
                        auxy = pygame.mouse.get_pos()[1]
                        screen.fill(WindowColor)
                        #pygame.display.update()
                        bezierQuadrada((inix,iniy),(auxx,auxy),(endx,endy),value)
                        printFormas()

		
def PoliLine(value):

        BottonCliked = False
        count = 0
        while 1:
            for event in pygame.event.get():
                
                if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                    pygame.display.update()
                    return
                
                if event.type == pygame.MOUSEBUTTONUP:
                    if not BottonCliked:
							
                        inix = pygame.mouse.get_pos()[0]
                        iniy = pygame.mouse.get_pos()[1]
                        finalx = inix
                        finaly = iniy
                        BottonCliked = True
							
                    else:
                        if count == 1:
                            endx = pygame.mouse.get_pos()[0]
                            endy = pygame.mouse.get_pos()[1]
                            Formas.append((1,finalx,finaly,endx,endy,value))
                            finalx = endx
                            finaly = endy
                            #pygame.display.update()
                        else:
                            endx = pygame.mouse.get_pos()[0]
                            endy = pygame.mouse.get_pos()[1]
                            finalx = endx
                            finaly = endy
                            Formas.append((1,inix,iniy,endx,endy,value))
                            count += 1
                            #pygame.display.update()
							
                if event.type == pygame.MOUSEMOTION:
                    if BottonCliked:
                        auxx = pygame.mouse.get_pos()[0]
                        auxy = pygame.mouse.get_pos()[1]
                        screen.fill((255,255,255))
                       # pygame.display.update()
                        breseham(finalx,finaly,auxx,auxy,value)
                        #pygame.display.update()

                        printFormas()		
def Fill(value):
        global Circulo	
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                     return 
                if event.type == pygame.MOUSEBUTTONUP:
                    inix = pygame.mouse.get_pos()[0]
                    iniy = pygame.mouse.get_pos()[1]
                    
                    
                    floodfill(inix,iniy,value)
                    Formas.append((5,inix,iniy,value))
                    screen.fill((255,255,255))
                    #pygame.display.update()
                    printFormas()
                    return						
def verificaBotao(): 
	x = pygame.mouse.get_pos()[0]
	y = pygame.mouse.get_pos()[1]
	for i in range(7):
		if x > Bottons[i][0] and x < Bottons[i][2] and y > Bottons[i][1] and y < Bottons[i][3]:
			return (i)
		i +=1
	
	for i in range(4):
		for j in range(4):
			if x > GRID[0][j] and x < GRID[0][j+1] and y > GRID[1][i] and y < GRID[1][i+1]:
				return (i,j)
		j +=1
	i+=1
	return None

criaPainel()
printMenu()
while 1:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONUP:
			b = verificaBotao()
			if b == (0):
				Line(SetCOLOR)
			elif b == (1):
				Circle(SetCOLOR)
			elif b == (2):
				Rectangle(SetCOLOR)
			elif b == (3):
				Square(SetCOLOR)
			elif b == (4):
				PoliLine(SetCOLOR)
			elif b == (5):
				Curve(SetCOLOR)
			elif b == (6):
				Fill(SetCOLOR)
			else:
				if b != None: 
					SetCOLOR = COLORGRID(b[0],b[1])
		if event.type == pygame.QUIT:
			sys.exit()



while 1:
	for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()