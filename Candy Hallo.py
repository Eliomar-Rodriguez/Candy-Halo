
#Proyecto de Programación
#Tema: Copia de "Candy Crush"
#Estudiantes: Eliomar Rodríguez Arguedas   |   Steven Peraza Porras

#se importan las librerías de pygame y del sistema
import pygame,sys,os,random
from pygame.locals import *

#se declaran algunas variables claves y se inicializa el pygame
pygame.init()
nombre = ""
movs = 50
puntaje_total = 0
perder = pygame.mixer.Sound('smb_mariodie.wav')
gameover = pygame.mixer.Sound('smb_gameover.wav')
pantallazo = pygame.image.load("pantalla_de_game_over.png")
si1 = pygame.image.load("Boton Si.png")
si2 = pygame.image.load("Boton Si2.png")
no1 = pygame.image.load("Boton No.png")
no2 = pygame.image.load("Boton No2.png")


#Función que comienza el juego mediante el menú principal
def menu_juego():
    pygame.init()                   #se inicializa el pygame
    ventaname = pygame.display.set_mode((600,600))  #se crea la ventana y se agrega un fondo
    pygame.display.set_caption("Candy Hallo")
    fondom = pygame.image.load("fondo hal.png")
    ventaname.blit(fondom,(0,0))
    nuevo_juego1=pygame.image.load("Boton Nuevo Juego.png")
    nuevo_juego2=pygame.image.load("Boton Nuevo Juego2.png")
    highscore1=pygame.image.load("Boton Highscores.png")
    highscore2=pygame.image.load("Boton Highscores2.png")       #se cargan algunos botones y el cursor para su funcionamiento
    cursor1=Cursor()
    boton1 = Boton(nuevo_juego1,nuevo_juego2,200,200)
    boton2 = Boton2(highscore1,highscore2,200,300)
    reloj1 = pygame.time.Clock()
    pygame.mixer.music.load('Halloween_Instrumental_Music_-_Phantom_Manor.mp3')
    pygame.mixer.music.play()                               #se carga una música insturmental y se reproduce de fondo


    while True:                     #ciclo sin fin que refresca la ventana y verifica si existe algún evento de importancia
        for event in pygame.event.get():
            if event.type == QUIT:      #evento que cierra el programa si el jugador clickea la "x" de salir
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:                 #evento que reconoce si se clickeo alguna parte de la pantalla, si fue un botón, entonces ejecuta alguna acción
                if cursor1.colliderect(boton1.rect):
                    menu_nombre(nombre)
                    sys.exit(menu_juego)
                elif cursor1.colliderect(boton2.rect):
                    menu_high()
                    pygame.quit()
                    sys.exit(menu_juego)
        reloj1.tick(30)         #velocidad de refresco de la pantalla (30 fps)
        cursor1.update()
        boton1.update(ventaname,cursor1)
        boton2.update(ventaname,cursor1)        #comandos de refresco de botones y pantalla
        pygame.display.update()


def menu_nombre(nombre):
    pygame.init()               #se inicializa el pygame
    ventaname = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Candy Hallo")
    fondom = pygame.image.load("fondo hal_nom.png")
    comenzar1 = pygame.image.load("Boton Comenzar.png")          #se cargan algunos botones y el cursor para su funcionamiento
    comenzar2 = pygame.image.load("Boton Comenzar2.png")
    cursor1=Cursor()
    fuente = pygame.font.SysFont("Halloween Too", 50)
    reloj1 = pygame.time.Clock()
    pygame.mixer.music.load('Halloween_Music_-_Trick_or_Treat.mp3')  #se carga una música insturmental y se reproduce de fondo
    pygame.mixer.music.play()

    while True:                             #ciclo sin fin que refresca la ventana y verifica si existe algún evento de importancia
        for event in pygame.event.get():
            if event.type == QUIT:          #evento que cierra el programa si el jugador clickea la "x" de salir
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:             #evento que revisa si el jugador teclea una letra y la agrega al nombre del jugador
                if event.unicode.isalpha():
                    nombre += event.unicode
                elif event.key == K_BACKSPACE:      #evento que revisa si el jugador teclea retroceder y elimina una letra al nombre del jugador
                    nombre = nombre[:-1]
            elif event.type == MOUSEBUTTONDOWN:     #evento que reconoce si se clickeo alguna parte de la pantalla, si fue un botón, entonces ejecuta alguna acción
                if cursor1.colliderect(botoncom.rect):
                    juego_prin(nombre)
                    sys.exit(menu_juego)
        ventaname.blit(fondom,(0,0))
        if nombre != "":                                        #condicón de que si no existe un nombre de jugador no muestra el boton de jugar
            botoncom = Botoncom(comenzar1,comenzar2,185,425)
            cursor1.update()
            botoncom.update(ventaname,cursor1)
        reloj1.tick(30)
        block = fuente.render(nombre, True, (255, 0, 0))        #comandos de refresco de pantalla y botones
        rect = block.get_rect()
        rect.center = ventaname.get_rect().center
        ventaname.blit(block,rect)
        pygame.display.update()


#clase cursor para la activación del mouse en pantalla
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)      #atributos del cursor = posiciones en "x" y "y"
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()   #método para averiguar la posición del mouse.


#clase boton que sombrea el mismo cuando es tocado por el cursor.
class Boton(pygame.sprite.Sprite):
    def __init__(self,nuevo_juego1,nuevo_juego2,x,y):
        self.imagen_sin = nuevo_juego1
        self.imagen_con = nuevo_juego2              #atributos = carga de los botones anteriormente creados
        self.imagen_actual = self.imagen_sin
        self.rect = self.imagen_actual.get_rect()
        self.rect.left,self.rect.top = (x,y)
    def update(self,ventana,cursor1):
        if cursor1.colliderect(self.rect):
            self.imagen_actual = self.imagen_con    #método que comprueba si el rectangulo ocupado por el boton es tocado por el cursor, en ese caso, cambia la imagen del boton
        else:
            self.imagen_actual = self.imagen_sin
        ventana.blit(self.imagen_actual,self.rect)

#clase boton con la misma funcion que antes, excepto que funciona con otros atributos
class Boton2(pygame.sprite.Sprite):
    def __init__(self,highscore1,highscore2,w,z):
        self.imagen_sin2 = highscore1
        self.imagen_con2 = highscore2
        self.imagen_actual2 = self.imagen_sin2
        self.rect = self.imagen_actual2.get_rect()
        self.rect.left,self.rect.top = (w,z)
    def update(self,ventana,cursor1):
        if cursor1.colliderect(self.rect):
            self.imagen_actual2 = self.imagen_con2
        else:
            self.imagen_actual2 = self.imagen_sin2
        ventana.blit(self.imagen_actual2,self.rect)

#clase boton con la misma funcion que antes, excepto que funciona con otros atributos
class Botoncom(pygame.sprite.Sprite):
    def __init__(self,comenzar1,comenzar2,x,y):
        self.imagen_sin2 = comenzar1
        self.imagen_con2 = comenzar2
        self.imagen_actual2 = self.imagen_sin2
        self.rect = self.imagen_actual2.get_rect()
        self.rect.left,self.rect.top = (x,y)
    def update(self,ventana,cursor1):
        if cursor1.colliderect(self.rect):
            self.imagen_actual2 = self.imagen_con2
        else:
            self.imagen_actual2 = self.imagen_sin2
        ventana.blit(self.imagen_actual2,self.rect)

#Funcion que inicializa el juego en si
def juego_prin(nombre):
    global movs, puntaje_total
    pygame.init()           #se inicializa el pygame
    ventana = pygame.display.set_mode((1366,768),pygame.FULLSCREEN) #se crea una ventana nueva
    pygame.display.set_caption("Juego")
    color = (255,255,255)
    fondo = pygame.image.load("FCA.jpg")        #se carga un fondo y se le aplica a la ventana
    cargando = pygame.image.load("pantalla_de_cargando.png")
    reloj1 = pygame.time.Clock()
    datos_juego = pygame.image.load("Datos Juego.png")
    arana = pygame.image.load("Arana.png")
    calabaza = pygame.image.load("Calabaza.png")
    fantasma = pygame.image.load("fantasma.png")
    calavera = pygame.image.load("Calavera.png")    #se cargan las imagenes de los "dulces"
    batman = pygame.image.load("Murcielago.png")
    pygame.mixer.music.load('Creepy_Circus_Music_-_Old_Ticket_Booth.mp3')
    mover = pygame.mixer.Sound('smb_powerup.wav')
    triple = pygame.mixer.Sound('Triple_Combo.wav')
    cuatro = pygame.mixer.Sound('Super_Combo.wav')  #se cargan los efectos de sonido
    cinco = pygame.mixer.Sound('Combo_Breaker.wav')
    LARGO  = 50
    ALTO = 50                                       #se declaran algunas variables necesarias para el correcto funcionamiento del juego.
    MARGEN = 25
    matriz_logica = [[], [], [], [], [], [], [], [], []]
    tpa = ()
    bandera = False
    
    def crear_matriz():
        for x in range(9):
            for y in range(9):
                dulce = Dulces("normal",random.randint(1, 5))
                matriz_logica[x].append(dulce.get_num())  # llenar matriz con numeros aleatorios
        

    crear_matriz()
    
   
#Funcion: se encarga de verificar que existan elementos iguales dentro de la matriz para proceder a explotarlas y de esta manera sumar puntos
#Entradas: Coordenas de los numeros que son iguales dentro de la matriz
#Salidas:lista con las coordenadas de los numeros iguales para explotarlos en la funcion explotardulcecolumna y luego bajar los numeros e ingresar numeros random en la ultima fila
    def verificar_columnas():
        iguales=[]
        for x in range(9):  #x son las columnas
            for y in range(8):#y son las filas
                if matriz_logica[y][x] == matriz_logica[y+1][x]:
                    if iguales==[]:
                        iguales.append((y,x))
                        iguales.append((y+1,x))
                    else:
                        iguales.append((y+1,x))
                elif len(iguales)>=3:
                    explotardulcecolumna(iguales)
                    bajar_numeroscolumna(iguales)
                    return
                else:
                    iguales=[]
            if len(iguales)>= 3:
                explotardulcecolumna(iguales)
                bajar_numeroscolumna(iguales)
                return

    #Funcion: Se encarga de bajar los numeros a la hora de encontrar dulces iguales y explotarlos
    #Entradas: coordenadas en las que se encuentran los dulces iguales en la matriz
    #Salidas: genera random cuando ya esten ordenados como deben de ser y los ingresa en las posiciones que se encuentran en la lista de tuplas llamada iguales
    
    def bajar_numeroscolumna(iguales):
        veces=len(iguales)
        while iguales[-1][0]!=8:
            for tupla in iguales:
                x=tupla[0]
                y=tupla[1]
                for l in iguales:
                    fila=l[0]
                    if 8==fila:
                        for tupla in iguales:
                            x=tupla[0]
                            y=tupla[1]
                            num=random.randint(1,5)
                            matriz_logica[x][y]=num
                        return 0
                if x+veces<=8:
                    matriz_logica[x][y]=0
                    aux=matriz_logica[x+veces][y]
                    matriz_logica[x+veces][y]=0
                    matriz_logica[x][y]=aux
                    tuplanueva=(x+veces,y)
                    iguales[iguales.index(tupla)]=tuplanueva
        if iguales[-1][0]==8:
            for tupla in iguales:
                x=tupla[0]
                y=tupla[1]
                num=random.randint(1,5)
                matriz_logica[x][y]=num
        return 0

    #funcion: se encarga de sumar el puntaje de acuerdo a la cantidad de elementos iguales que se contraron
    #Entradas: coordenadas en las que se encuentran los dulces iguales en la matriz
    #Salidas: suma puntaje al puntaje total
    def explotardulcecolumna(iguales):
        global puntaje_total
        veces = len(iguales)
        for tupla in iguales:
            x = tupla[0]
            y = tupla[1]
            if x == 0:
                matriz_logica[x][y] = 0
                bajar_numeroscolumna(iguales)
            elif x == 8:
                num = random.randint(1, 5)
                matriz_logica[x][y] = num
            else:
                bajar_numeroscolumna(iguales)

        puntaje = veces * 50
        puntaje_total = puntaje_total + puntaje
        if veces == 3:
            pygame.time.delay(1000)
            triple.play()
        elif veces == 4:
            pygame.time.delay(1000)
            cuatro.play()
        elif veces <= 5:
            pygame.time.delay(1000)
            cinco.play()
        return

    #Funcion:   Se encarga de bajar los numeros que se encuentran en las filas y que son eliminados
    #Entradas:  coordenadas en las que se encuentran los dulces iguales en la matriz
    #Salidas:   ingresa numeros random en las posiciones que se encuentran en la lista de tuplas llamada coordenadas y luego de haberlos ordenado de la manera correcta
    def bajar_numeros(coordenadas):
        while coordenadas[0][0] != 8:
            for tupla in coordenadas:
                x = tupla[0]
                y = tupla[1]
                if x == 8:
                    for tupla in coordenadas:
                        x = tupla[0]
                        y = tupla[1]
                        num = random.randint(1, 5)
                        matriz_logica[x][y] = num
                else:
                    num = random.randint(1, 5)
                    matriz_logica[x][y] = num
                    aux = matriz_logica[x + 1][y]
                    matriz_logica[x][y] = aux
                    tuplanueva = (x + 1, y)
                    coordenadas[coordenadas.index(tupla)] = tuplanueva
        if coordenadas[0][0] == 8:
            for tupla in coordenadas:
                x = tupla[0]
                y = tupla[1]
                num = random.randint(1, 5)
                matriz_logica[x][y] = num
        return 0

    #Funcion: Se encarga de sumar puntaje al puntaje total y ya esta ordenado de una vez ingresa numeros random en las posiciones que contiene coordenadas
    #Entradas: lista de tuplas llamada coordenadas la cual contiene las ubicaciones de lo dulces iguales
    #Salidas: suma puntaje al puntaje total
    def explotardulfila(coordenadas):# explotar dulces de filas
        global puntaje_total
        veces = len(coordenadas)
        for tupla in coordenadas:
            x = tupla[0]
            y = tupla[1]
            if x == 0:
                matriz_logica[x][y] = 0
                bajar_numeros(coordenadas)
            elif x == 8:
                num = random.randint(1, 5)
                matriz_logica[x][y] = num
            else:
                bajar_numeros(coordenadas)

        puntaje = veces * 50
        puntaje_total = puntaje_total + puntaje
        print(puntaje_total)
        pygame.display.update()
        if veces == 3:
            pygame.time.delay(1000)
            triple.play()
        elif veces == 4:
            pygame.time.delay(1000)
            cuatro.play()
        elif veces <= 5:
            pygame.time.delay(1000)
            cinco.play()
        return

    #Funcion: funcion encargada de verificar que existan dulces iguales en las FILAS de la matriz para guardar sus coordenadas en la lista llamada coordenadas
    #Entradas: ---
    #Salidas: listas con las coordenadas de los dulces iguales y llama a funciones para explotar y sumar puntaje y proceder al siguiente moimiento
    def verificar_filas():
        count = 1
        coordenadas = []
        for listas in matriz_logica:
            for y in range(8):
                if listas[y] == listas[y + 1] and listas[y] != 0:
                    count += 1
                    posicion = matriz_logica.index(listas)
                    if coordenadas == []:
                        coordenadas.append((posicion, y))
                        coordenadas.append((posicion, y + 1))
                    else:
                        coordenadas.append((posicion, y + 1))
                elif len(coordenadas) >= 3:
                    explotardulfila(coordenadas)
                    bajar_numeros(coordenadas)
                    return

                else:
                    coordenadas = []
                    count = 1
            if count >= 3:
                explotardulfila(coordenadas)
                bajar_numeros(coordenadas)
                return

    #Funcion: funcion que como su nombre lo dice se encarga de pasar verificando que existan dulces iguales
    #en la matriz para proceder a eliminarlos y sumar puntos, hace este proceso mientras la cantidad
    # de movimientos sea mayor a 0
    #Entradas: cantidad de movimientos
    #Salidas: puntaje final luego de que movimientos llegara a 0
    def pasar_verificando(movs):
        while movs>0: #probar con !=0
            elementos=hay_mas()
            while elementos == True:
                elementos=hay_mas()
                verificar_filas()
                verificar_columnas()
            print("Cantidad de movimientos restantes: ",movs)
            return

    #Funcion: funcion que como su nombre lo dice se encarga de verificar si HAY MAS dulces iguales en la matriz
    #Entradas: ---
    #Salidas: valor booleano dependiendo si hay elementos iguales o no, sino hay retorna False
    def hay_mas():
        for matriz in matriz_logica:
            for y in range(7):
                x = matriz_logica.index(matriz)
                if matriz[y] == matriz[y + 1] and matriz[y] == matriz[y + 2]:
                    return True
                elif matriz_logica[y][x] == matriz_logica[y+1][x] and matriz_logica[y][x] == matriz_logica[y+2][x]:
                    return True
        return False

    
    def set_score(puntaje_total):
        puntuacion = pygame.font.SysFont("Halloween Too",65)
        score = puntuacion.render(str(puntaje_total),True, (255,255,255))     #función que permite ver la puntación en pantalla
        ventana.blit(score,[950,255])

    def movimientos():
        global movs
        cant_rest = pygame.font.SysFont("Halloween Too",65)         #función que permite ver los movimientos restantes en pantalla
        movimiento = cant_rest.render(str(movs),True,(255,255,255))
        ventana.blit(movimiento,[980,425])

    def cambiar(t1,t2):
        global movs
        n1,n2 = t1
        n3,n4 = t2
        n5 = matriz_logica [n3][n4]  #funcion que permite el cambio de "dulces" dentro de la matriz logica.
        matriz_logica [n3][n4] = matriz_logica[n1][n2]
        matriz_logica [n1][n2] = n5
        movs -= 1
        mover.play()
        
    ventana.blit(cargando,(0,0))
    pygame.mixer.music.play()
    triple.set_volume(0.0)
    cuatro.set_volume(0.0)                  #Pantalla de Cargando y efectos de sonido de la misma
    cinco.set_volume(0.0)
    verificar_filas()
    verificar_columnas()
    pasar_verificando(movs)
    puntaje_total = 0
    pygame.mixer.music.stop()
    pygame.time.delay(1500)
    triple.set_volume(1.0)
    cuatro.set_volume(1.0)
    cinco.set_volume(1.0)
    pygame.mixer.music.load('Mortal_Kombat_Theme_Song_Original.mp3')
    pygame.mixer.music.play(-1)                           #se cargan los sonidos del juego y la música de fondo.
    pygame.mixer.music.set_volume(0.1)
    while True:
        ventana.blit(fondo,(0,0))
        ventana.blit(datos_juego,(800,75))
            #Lineas verticales
        pygame.draw.line(ventana,color,(25,25),(25,700),3)
        pygame.draw.line(ventana,color,(100,25),(100,700),3)
        pygame.draw.line(ventana,color,(175,25),(175,700),3)
        pygame.draw.line(ventana,color,(250,25),(250,700),3)
        pygame.draw.line(ventana,color,(325,25),(325,700),3)
        pygame.draw.line(ventana,color,(400,25),(400,700),3)
        pygame.draw.line(ventana,color,(475,25),(475,700),3)
        pygame.draw.line(ventana,color,(550,25),(550,700),3)
        pygame.draw.line(ventana,color,(625,25),(625,700),3)
        pygame.draw.line(ventana,color,(700,25),(700,700),3)
            #Lineas Horizontales
        pygame.draw.line(ventana,color,(25,25),(700,25),3)
        pygame.draw.line(ventana,color,(25,100),(700,100),3)
        pygame.draw.line(ventana,color,(25,175),(700,175),3)
        pygame.draw.line(ventana,color,(25,250),(700,250),3)
        pygame.draw.line(ventana,color,(25,325),(700,325),3)
        pygame.draw.line(ventana,color,(25,400),(700,400),3)
        pygame.draw.line(ventana,color,(25,475),(700,475),3)
        pygame.draw.line(ventana,color,(25,550),(700,550),3)
        pygame.draw.line(ventana,color,(25,625),(700,625),3)
        pygame.draw.line(ventana,color,(25,700),(700,700),3)
        pygame.draw.line(ventana,color,(25,775),(700,775),3)
        
        #Proceso para cargar las imagenes de los "dulces" en pantalla dependiendo del numero dentro de la matriz logica
        
        for fila in range(9):  
            for columna in range(9):
                if matriz_logica[fila][columna] == 1:
                    ventana.blit(arana,[(MARGEN+LARGO) * columna + MARGEN,(MARGEN+ALTO) * fila + MARGEN,LARGO,ALTO])
                elif matriz_logica[fila][columna] == 2:
                    ventana.blit(calavera,[(MARGEN+LARGO) * columna + MARGEN,(MARGEN+ALTO) * fila + MARGEN,LARGO,ALTO])
                elif matriz_logica[fila][columna] == 3:
                    ventana.blit(calabaza,[(MARGEN+LARGO) * columna + MARGEN,(MARGEN+ALTO) * fila + MARGEN,LARGO,ALTO])
                elif matriz_logica[fila][columna] == 4:
                    ventana.blit(batman,[(MARGEN+LARGO) * columna + MARGEN,(MARGEN+ALTO) * fila + MARGEN,LARGO,ALTO])
                elif matriz_logica[fila][columna] == 5:
                    ventana.blit(fantasma,[(MARGEN+LARGO) * columna + MARGEN,(MARGEN+ALTO) * fila + MARGEN,LARGO,ALTO])
        for event in pygame.event.get():
            if event.type == KEYDOWN:             #evento que revisa si el jugador teclea una letra y la agrega al nombre del jugador
                if event.key == K_ESCAPE:      #evento que revisa si el jugador teclea escape para salir del juego
                    pygame.quit()
                    sys.exit()    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                columna = pos[0] // (LARGO + MARGEN)        #evento que revisa si el mouse fue clickeado, en ese caso, se obtiene la posicion del cursor, se utiliza una bandera y se llama la funcion de cambiar de lugar.
                fila = pos[1] // (ALTO + MARGEN)
                print(fila,columna)
                if event.type == pygame.MOUSEBUTTONUP:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    columna = pos[0] // (LARGO + MARGEN)
                    fila = pos[1] // (ALTO + MARGEN)
                    if bandera == False:
                        tpa = (fila, columna)
                        bandera = True
                        print("Inicial",(fila, columna))
                    else:
                        print("Comparado con :",(fila, columna))
                        if(((tpa[1]-1==columna and tpa[0]== fila) or  (tpa[1]+1==columna and tpa[0]== fila) or (tpa[0]-1==fila and tpa[1] == columna) or (tpa[0]+1==fila and tpa[1]==columna))):
                            bandera = False
                            cambiar(tpa, (fila, columna))

                        else:
                            print("Movimiento no valido")
                            tpa = ()
                            bandera = False
        verificar_filas()
        verificar_columnas()
        hay_mas()
        reloj1.tick(10)         #comandos para refrescar la pantalla
        set_score(puntaje_total)
        movimientos()
        pygame.display.update()
        if movs == 0:           #condición para ejecutar el gameover: si movimientos restantes es igual a "0"
            verificar_filas()
            verificar_columnas()
            movimientos()
            pygame.display.update()
            pygame.time.delay(1500)
            game_over(ventana,nombre,puntaje_total,pantallazo,si1,si2,no1,no2,fondo,reloj1)


#clase de dulces que contiene dos atributos:tipo y numero.
class Dulces:
    def __init__(self,tipo,num):
        self.tipo = tipo
        self.numero = num
    def get_num(self):
        return self.numero


#clase boton con la misma funcion que antes, excepto que funciona con otros atributos
class BotonY(pygame.sprite.Sprite):
    def __init__(self,si1,si2,x,y):
        self.imagen_sin = si1
        self.imagen_con = si2
        self.imagen_actual2 = self.imagen_sin
        self.rect = self.imagen_actual2.get_rect()
        self.rect.left,self.rect.top = (x,y)
    def update(self,ventana,cursor1):
        if cursor1.colliderect(self.rect):
            self.imagen_actual2 = self.imagen_con
        else:
            self.imagen_actual2 = self.imagen_sin
        ventana.blit(self.imagen_actual2,self.rect)

#clase boton con la misma funcion que antes, excepto que funciona con otros atributos
class BotonN(pygame.sprite.Sprite):
    def __init__(self,no1,no2,x,y):
        self.imagen_sin = no1
        self.imagen_con = no2
        self.imagen_actual2 = self.imagen_sin
        self.rect = self.imagen_actual2.get_rect()
        self.rect.left,self.rect.top = (x,y)
    def update(self,ventana,cursor1):
        if cursor1.colliderect(self.rect):
            self.imagen_actual2 = self.imagen_con
        else:
            self.imagen_actual2 = self.imagen_sin
        ventana.blit(self.imagen_actual2,self.rect)
        
#clase boton con la misma funcion que antes, excepto que funciona con otros atributos
class BotonV(pygame.sprite.Sprite):
    def __init__(self,vol1,vol2,x,y):
        self.imagen_sin = vol1
        self.imagen_con = vol2
        self.imagen_actual2 = self.imagen_sin
        self.rect = self.imagen_actual2.get_rect()
        self.rect.left,self.rect.top = (x,y)
    def update(self,ventana,cursor1):
        if cursor1.colliderect(self.rect):
            self.imagen_actual2 = self.imagen_con
        else:
            self.imagen_actual2 = self.imagen_sin
        ventana.blit(self.imagen_actual2,self.rect)

#función que acaba el juego, poniendo en pantalla el clasico "gameover" y dando una opcion de volver a juegar
def game_over(ventana,nombre,puntaje_total,pantallazo,si1,si2,no1,no2,fondo,reloj1):
        texto = "Fin de Juego"
        pygame.mixer.music.stop()
        looser = pygame.font.SysFont("Halloween Too",120)   #se carga e imprime en pantalla el mensaje de "fin de juego"
        badluck = looser.render(texto,True, (255,0,0))
        ventana.blit(pantallazo,(0,0))
        ventana.blit(badluck,(400,300))
        perder.play()                       #se reproduce el sonido de perder
        pygame.display.update()
        pygame.time.delay(3500)
        gameover.play()                     #se espera un tiempo, se imprime el "desea volver al menu", aparecen los botones de Y/N y suena otro sonido de perder.
        texto2 = "Desea volver al"
        texto3 = "menu principal"
        volver = pygame.font.SysFont("Halloween Spider",50)
        empezar = volver.render(texto2,True, (255,255,255))    #se carga e imprime en pantalla el mensaje de "volver al menu principal"
        empezar2 = volver.render(texto3,True, (255,255,255))
        crear_highscore(nombre,puntaje_total)
        cursor1 = Cursor()
        boton1 = BotonY(si1,si2,400,500)
        boton2 = BotonN(no1,no2,700,500)
        while True:
            ventana.blit(fondo,(0,0))
            ventana.blit(pantallazo,(0,0))          #ciclo sin fin que refresca la pantalla y espera a que el jugador accione un evento de los programados.
            ventana.blit(badluck,(400,300))
            ventana.blit(empezar,(450,400))
            ventana.blit(empezar2,(450,450))
            for event in pygame.event.get():
                if event.type == KEYDOWN:             #evento que revisa si el jugador teclea una letra y la agrega al nombre del jugador
                    if event.key == K_ESCAPE:      #evento que revisa si el jugador teclea escape para salir del juego
                        pygame.quit()
                        sys.exit()
                elif event.type == MOUSEBUTTONDOWN:     #evento que verifica si el mouse fue clickeado y si un boton fue accionado sale del sistema y vuelve a abrir el codigo desde el principio.
                    if cursor1.colliderect(boton1.rect):
                        pygame.quit()
                        os.popen('Candy Hallo.py')
                        sys.exit()
                    elif cursor1.colliderect(boton2.rect):
                        gracias = pygame.image.load("pantalla_de_gracias.png")
                        pygame.mixer.music.load('Msica_Tema_Crash_Bandicoot_1_Playstation_1.mp3')
                        ventana.blit(gracias,(0,0))
                        pygame.display.update()
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_volume(1.0)
                        pygame.time.delay(10000)
                        pygame.quit()
                        sys.exit()
            reloj1.tick(20)
            boton1.update(ventana,cursor1)
            boton2.update(ventana,cursor1)  #comandos de refresco de pantalla
            cursor1.update()
            pygame.display.update()


#Función que lanza la ventana de highsocres mediante el menú principal
def menu_high():
    pygame.init()                   #se inicializa el pygame
    ventaname = pygame.display.set_mode((600,600))  #se crea la ventana y se agrega un fondo
    pygame.display.set_caption("Candy Hallo")
    fondoh = pygame.image.load("FHS.jpg")
    ventaname.blit(fondoh,(0,0))      #se cargan algunos botones y el cursor para su funcionamiento
    cursor1=Cursor()
    vo11 = pygame.image.load("Boton Volver.png")
    vol2 = pygame.image.load("Boton Volver2.png")
    boton1 = BotonV(vo11,vol2,175,500)
    reloj1 = pygame.time.Clock()
    pygame.mixer.music.load('Spooky_Music_-_Halloween_Club.mp3')
    pygame.mixer.music.play()                               #se carga una música insturmental y se reproduce de fondo
    texto = "High Scores"
    fuente = pygame.font.SysFont("Halloween Spider",40)   #se carga e imprime en pantalla el titulo de "highscore"
    titulo = fuente.render(texto,True, (255,100,0))
    ventaname.blit(titulo,(150,15))
    texto = "Nombre"
    fuente = pygame.font.SysFont("Halloween Spider",35)   #se cargar e imprime en pantalla el mensaje de "nombres"
    titulo = fuente.render(texto,True, (255,100,0))
    ventaname.blit(titulo,(75,75))
    texto = "Puntaje"
    fuente = pygame.font.SysFont("Halloween Spider",35)   #se cargar e imprime en pantalla el mensaje de "puntaje"
    titulo = fuente.render(texto,True, (255,100,0))
    ventaname.blit(titulo,(350,75))
    

    while True:                     #ciclo sin fin que refresca la ventana y verifica si existe algún evento de importancia
        for event in pygame.event.get():
            if event.type == QUIT:      #evento que cierra el programa si el jugador clickea la "x" de salir
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:                 #evento que reconoce si se clickeo alguna parte de la pantalla, si fue un botón, entonces ejecuta alguna acción
                if cursor1.colliderect(boton1.rect):
                    menu_juego()
                    sys.exit(menu_high)

        reloj1.tick(30)         #velocidad de refresco de la pantalla (30 fps)
        mostrar_high_score(ventaname)
        cursor1.update()
        boton1.update(ventaname,cursor1)        #comandos de refresco de botones y pantalla
        pygame.display.update()

        
#función que imprime el nombre del jugador y su respectiva puntuación en el archivo "highscores.txt"
def crear_highscore(nombre,puntaje_total):
    archivo = open ("Highscores.txt","a")
    archivo.write (nombre+","+str(puntaje_total))       #se abre el archivo "highscores.txt" y se agrega el nombre y la puntuaciion del jugador.
    archivo.write ('\n')
    archivo.close()                                 #se cierra el archivo. 

#función que muestra los puntajes de todos los juegadores con sus nombres en consola.
def mostrar_high_score(ventaname):
    high_score = open ("Highscores.txt", "r")       #se abre el archivo "highscores.
    nombres = []
    pts = []
    primer = 0
    segundo = 0
    tercero = 0             #se declaran algunas variables para almacenar el nombre y la puntuacion de los 5 mejores puntajes.
    cuarto = 0
    quinto = 0
    primernom = ''
    segundonom = ''
    terceronom = ''
    cuartonom = ''
    quintonom = ''
    z = 0
    for linea in high_score:        #ciclo que elimina el enter del string y envia los nombres y los puntajes a dos listas apartes.
        nombre,puntaje = linea.rstrip("\\n").split(",") #quita el "\n"
        nombres.append(nombre)
        pts.append(int(puntaje))

    for mayores in pts:             #ciclo que conmpara los cinco mejores puntajes dentro de la lista indepediente de puntos.
        if mayores > primer:
            quinto = cuarto
            cuarto = tercero
            tercero = segundo
            segundo = primer
            primer = mayores
        elif mayores < primer and mayores > segundo:
            quinto = cuarto
            cuarto = tercero
            tercero = segundo
            segundo = mayores                        
        elif mayores < segundo and mayores > tercero:
            quinto = cuarto
            cuarto = tercero
            tercero = mayores       
        elif mayores < tercero and mayores > cuarto:
            quinto = cuarto
            cuarto = mayores
        elif mayores < cuarto and mayores > quinto:
            quinto = mayores
        else:
            pass

    for buscar in pts:              #ciclo que busca los puntajes mas altos y toma su posicion dentro de la lista de puntos
        if buscar == primer:        #para luego buscar esa misma posicion en la lista de nombres y guardarlo en la variable correspondiente.
            z = pts.index(buscar)
            primernom = nombres[z]
        elif buscar == segundo:
            z = pts.index(buscar)
            segundonom = nombres[z]
        elif buscar == tercero:
            z = pts.index(buscar)
            terceronom = nombres[z]
        elif buscar == cuarto:
            z = pts.index(buscar)
            cuartonom = nombres[z]
        elif buscar == quinto:
            z = pts.index(buscar)
            quintonom = nombres[z]
        else:
            pass

        #Codigo para imprimir los nombres y sus respectivos puntajes en pantalla.
    texto = primernom
    fuente = pygame.font.SysFont("Halloween Too",50)
    titulo = fuente.render(texto,True, (160,160,160))
    ventaname.blit(titulo,(50,150))
    texto2 = (str(primer))
    fuente = pygame.font.SysFont("Halloween Too",50)
    titulo = fuente.render(texto2,True, (160,160,160))
    ventaname.blit(titulo,(450,150))

    texto = segundonom
    fuente = pygame.font.SysFont("Halloween Too",50)
    titulo = fuente.render(texto,True, (160,160,160))
    ventaname.blit(titulo,(50,225))
    texto2 = (str(segundo))
    fuente = pygame.font.SysFont("Halloween Too",50)
    titulo = fuente.render(texto2,True, (160,160,160))
    ventaname.blit(titulo,(450,225))

    texto = terceronom
    fuente = pygame.font.SysFont("Halloween Too",50)
    titulo = fuente.render(texto,True, (160,160,160))
    ventaname.blit(titulo,(50,300))
    texto2 = (str(tercero))
    fuente = pygame.font.SysFont("Halloween Too",50)
    titulo = fuente.render(texto2,True, (160,160,160))
    ventaname.blit(titulo,(450,300))

    texto = cuartonom
    fuente = pygame.font.SysFont("Halloween Too",50)
    titulo = fuente.render(texto,True, (160,160,160))
    ventaname.blit(titulo,(50,375))
    texto2 = (str(cuarto))
    fuente = pygame.font.SysFont("Halloween Too",50)
    titulo = fuente.render(texto2,True, (160,160,160))
    ventaname.blit(titulo,(450,375))

    texto = quintonom
    fuente = pygame.font.SysFont("Halloween Too",50)
    titulo = fuente.render(texto,True, (160,160,160))
    ventaname.blit(titulo,(50,450))
    texto2 = (str(quinto))
    fuente = pygame.font.SysFont("Halloween Too",50)
    titulo = fuente.render(texto2,True, (160,160,160))
    ventaname.blit(titulo,(450,450))




#se llama la función de juego principal
menu_juego()


