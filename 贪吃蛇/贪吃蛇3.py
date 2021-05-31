#含边界判定，有计数显示，可以暂停
import sys
import random
import pygame.freetype
pygame.init()#初始化init()及设置
size=width,height=700,400
black=0,0,0
screen=pygame.display.set_mode(size)#窗口大小
pygame.display.set_caption("贪吃蛇小游戏")#窗口名字
icon=pygame.image.load("snake.jpg")
pygame.display.set_icon(icon)
RED=pygame.Color("red")
BLACK=pygame.Color("black")
BLUE=pygame.Color("blue")
MOCCASIN=pygame.Color("moccasin")
screen.fill(MOCCASIN)
a=[[300,300],[300,310],[300,320]]
fps=10
fclock=pygame.time.Clock()#创建一个Clock对象用于操作时间
f1 = pygame.freetype.Font('C:\Windows\Fonts\simkai.ttf', size=50)
direct = 'up'#初始方向
def food():
    food_x=random.randint(0,width/10-2)*10
    food_y=random.randint(0,height/10-1)*10
    food_point=[food_x,food_y]
    return food_point
def eat(food_point,head_point,direction):
    if food_point[0]==head_point[0] and food_point[1]==head_point[1]:
        food_point = food()
        a.insert(0, [head_point[0] + direction[0], head_point[1] + direction[1]])
    else:
        a.remove(a[-1])
        a.insert(0,[head_point[0]+direction[0],head_point[1]+direction[1]])
    return a,food_point
def gameover():
    print("GameOver!")
    sys.exit()  # 退出
food_point=food()
do_not=True
directs=['left','right','up','down']
direct_step=[[-10,0],[10,0],[0,-10],[0,10]]
while True:
    while do_not:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 点击了退出
                sys.exit()  # 退出
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    do_not = False
                if event.key == pygame.K_LEFT and direct != "right":
                    direct = "left"
                elif event.key == pygame.K_RIGHT and direct != "left":
                    direct = "right"
                elif event.key == pygame.K_UP and direct != "down":
                    direct = "up"
                elif event.key == pygame.K_DOWN and direct != "up":
                    direct = "down"
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
        direct_index=directs.index(direct)
        screen.fill(MOCCASIN)
        x = eat(food_point, a[0], direct_step[direct_index])
        a, food_point = x[0], x[1]
        for i in a:
            pygame.draw.rect(screen, RED, (i[0], i[1], 10, 10))
        pygame.draw.rect(screen, BLUE, (food_point[0], food_point[1], 10, 10))
        f1.render_to(screen,[630,170],str(len(a)),fgcolor=BLACK,bgcolor=None,size=50)
        if a[0][0] > width or a[0][0] < 0:  # 判断是否超出边界
            gameover()
        elif a[0][1] > height or a[0][1] < 0:
            gameover()
        pygame.display.update()  # 对显示窗口进行更新，默认窗口全部重绘
        fclock.tick(fps)  # 窗口刷新速度，每秒300次
    while not do_not:
        screen.fill(MOCCASIN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 点击了退出
                sys.exit()  # 退出
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    do_not = True
        f1.render_to(screen,[250,150],"游戏暂停",fgcolor=BLACK,bgcolor=None,size=50)
        pygame.display.update()  # 对显示窗口进行更新，默认窗口全部重绘
        fclock.tick(fps)  # 窗口刷新速度，每秒300次
