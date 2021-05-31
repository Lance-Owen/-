#含边界判定，有计数显示，可以暂停
import sys
import random
import pygame.freetype#文字增强
pygame.init()
size=width,height=700,400#窗口大小
black=0,0,0#黑色调出
screen=pygame.display.set_mode(size)#窗口大小
pygame.display.set_caption("贪吃蛇小游戏")#窗口名字
icon=pygame.image.load("snake.jpg")#加载图标
pygame.display.set_icon(icon)#设置图标
RED=pygame.Color("red")#调出颜色
BLACK=pygame.Color("black")
BLUE=pygame.Color("blue")
MOCCASIN=pygame.Color("moccasin")
screen.fill(MOCCASIN)#窗口填充
a=[[300,300],[300,310],[300,320]]#初始蛇身
fps=10#刷新速度
fclock=pygame.time.Clock()#创建一个Clock对象用于操作时间
f1 = pygame.freetype.Font('C:\Windows\Fonts\simkai.ttf', size=50)#导入字体
direct = 'up'#初始方向
def food():#产生食物坐标
    food_x=random.randint(0,width/10-2)*10
    food_y=random.randint(0,height/10-1)*10
    food_point=[food_x,food_y]
    return food_point
def eat(food_point,head_point,direction):#判断是否吃掉食物，并且移动
    if food_point[0]==head_point[0] and food_point[1]==head_point[1]:#如果吃掉食物，产生新的食物，移动
        food_point = food()
        a.insert(0, [head_point[0] + direction[0], head_point[1] + direction[1]])
    else:#没有吃掉食物，移动
        a.remove(a[-1])
        a.insert(0,[head_point[0]+direction[0],head_point[1]+direction[1]])
    return a,food_point
def gameover():#结束游戏
    print("GameOver!")
    sys.exit()  # 退出
food_point=food()
do_not=True#游戏状态切换中介
directs=['left','right','up','down']#方向列表
direct_step=[[-10,0],[10,0],[0,-10],[0,10]]#方向对应的坐标变化
while True:
    while do_not:#进行游戏
        for event in pygame.event.get():#事件发生
            if event.type == pygame.QUIT:  # 点击了退出
                sys.exit()  # 退出
            elif event.type == pygame.KEYDOWN:#按键按下事件
                if event.key == pygame.K_SPACE:#空格键
                    do_not = False
                if event.key == pygame.K_LEFT and direct != "right":#左键
                    direct = "left"
                elif event.key == pygame.K_RIGHT and direct != "left":#右键
                    direct = "right"
                elif event.key == pygame.K_UP and direct != "down":#上建
                    direct = "up"
                elif event.key == pygame.K_DOWN and direct != "up":#下键
                    direct = "down"
                elif event.key == pygame.K_ESCAPE:#Esc键
                    sys.exit()
        direct_index=directs.index(direct)#方向的地址索引
        screen.fill(MOCCASIN)
        x = eat(food_point, a[0], direct_step[direct_index])
        a, food_point = x[0], x[1]#更新数据
        for i in a:#绘画
            pygame.draw.rect(screen, RED, (i[0], i[1], 10, 10))
        pygame.draw.rect(screen, BLUE, (food_point[0], food_point[1], 10, 10))
        f1.render_to(screen,[630,170],str(len(a)),fgcolor=BLACK,bgcolor=None,size=50)#显示当前蛇长
        if a[0][0] > width or a[0][0] < 0:  # 判断是否超出边界
            gameover()
        elif a[0][1] > height or a[0][1] < 0:
            gameover()
        pygame.display.update()  # 对显示窗口进行更新，默认窗口全部重绘
        fclock.tick(fps)  # 窗口刷新速度，每秒300次
    while not do_not:#游戏暂停
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
