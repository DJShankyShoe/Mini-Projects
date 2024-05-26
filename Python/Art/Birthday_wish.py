import turtle
import math
import random
import itertools

one = turtle.Turtle()
two = turtle.Turtle()

def background(colour, speed):

    one.color(colour,colour)
    one.up()
    one.begin_fill()
    one.speed(speed)
    one.forward(650)
    one.left(90)
    one.forward(340)
    one.left(90)
    one.forward(1300)
    one.left(90)
    one.forward(680)
    one.left(90)
    one.forward(1300)
    one.left(90)
    one.forward(340)
    one.end_fill()
    one.goto(0,0)
    one.down()


def hearts(color):
    
    #hearts
    d = 110
    h = 40
    s = 30 
    e = 38    
    
    x = 10
    
    two.up()
    two.begin_fill()
    two.color(color)
    two.speed(11)
    
    two.left(45)
    two.forward(d/x)
    two.right(45)
    two.forward(h/x)
    two.right(45)
    two.forward(s/x)
    two.right(45)
    two.forward(s/x)
    two.right(45)
    two.forward(e/x)
    
    two.left(90)
    two.forward(e/x)
    two.right(45)
    two.forward(s/x)
    two.right(45)
    two.forward(s/x)
    two.right(45)
    two.forward(h/x)
    two.right(45)
    two.forward(d/x)
    
    two.end_fill()
    
    
def heart_sizes():
    
    
    #hearts
    d = 110
    h = 40
    s = 30 
    e = 38
    
    
    for i in range(0, 2):
        for run in range(1, 10):
            x = run * 0.1
            x += i

            #hearts
            one.up()
            one.begin_fill()
            one.color("Deep Pink","Deep Pink")
            one.speed(11)
            
            one.left(45)
            one.forward(d*x)
            one.right(45)
            one.forward(h*x)
            one.right(45)
            one.forward(s*x)
            one.right(45)
            one.forward(s*x)
            one.right(45)
            one.forward(e*x)
            
            one.left(90)
            one.forward(e*x)
            one.right(45)
            one.forward(s*x)
            one.right(45)
            one.forward(s*x)
            one.right(45)
            one.forward(h*x)
            one.right(45)
            one.forward(d*x)
            one.right(135)
            
            one.end_fill()   
            yield
    

def random_hearts():
    for run in range(17):
        for run in range(3):
            two.up()
            two.goto(random.randrange(-600, 600),random.randrange(-300, 300))
            hearts("Deep Pink")
        yield
        
        
        




def oren():
    one.right(180)
    two.right(180)
    one.up()
    two.up()    

def h(color, num, thick):
    one.pensize(thick)
    one.color(color)
    one.forward(num)
    yield
    one.backward(num/2)
    yield
    one.right(90)
    yield
    one.forward(num/2)
    yield
    one.left(90)
    yield
    one.forward(num/2)
    yield
    one.left(180)
    yield
    one.forward(num)
    yield

def a(color, num, thick):
    two.pensize(thick)
    two.color(color)
    two.forward(num)
    yield
    two.right(90)
    yield
    two.forward(num/2)
    yield
    two.right(90)
    yield
    two.forward(num)
    yield
    two.right(180)
    yield
    two.forward(num/2)
    yield
    two.left(90)
    yield
    two.forward(num/2)
    yield
    two.left(180)
    yield
    two.forward(num/2)
    yield
    two.right(90)
    yield
    two.forward(num/2)
    yield

def A(color, num, thick):
    two.pensize(thick)
    two.color(color)
    two.forward(num)
    yield
    two.right(90)
    yield
    two.forward(num/2)
    yield
    two.right(90)
    yield
    two.forward(num)
    yield
    two.right(180)
    yield
    two.forward(num/2)
    yield
    two.left(90)
    yield
    two.forward(num/2)
    yield
    two.left(180)
    yield
    two.forward(num/2)
    yield
    two.right(90)
    yield
    two.forward(num/2)
    yield
    
def p(color, num, thick):
    one.pensize(thick)
    one.color(color)
    one.forward(num)
    yield
    one.right(90)
    yield
    one.forward(num/2)
    yield
    one.right(90)
    yield
    one.forward(num/2)
    yield
    one.right(90)
    yield
    one.forward(num/2)
    yield
    one.up()
    yield
    one.left(90)
    yield
    one.forward(num/2)
    yield
    one.left(90)
    yield
    one.forward(num/2)
    yield
    one.right(90)
    yield
    one.down()
    yield

def y(color, num, thick):
    two.pensize(thick)
    two.color(color)
    two.forward(num/2)
    yield
    two.right(90)
    yield
    two.forward(num/4)
    yield
    two.left(90)
    yield
    two.forward(num/2)
    yield
    two.left(90)
    yield
    two.up()
    yield
    two.forward(num/2)
    yield
    two.down()
    yield
    two.left(90)
    yield
    two.forward(num/2)
    yield
    two.left(90)
    yield
    two.forward(num/4)
    yield
    two.right(90)
    yield
    two.forward(num/2)
    yield

def B(color, num, thick):
    one.pensize(thick)
    one.color(color)
    one.forward(num)
    one.right(90)
    one.forward((num/8)*3)
    one.right(45)
    one.forward(num/6)
    one.right(45)
    one.forward(num/4)
    one.right(45)
    one.forward(num/6)  
    one.right(45)
    one.forward((num/8)*3)
    one.right(180)
    one.forward(num/2)
    one.right(45)
    one.forward(num/6)
    one.right(45)
    one.forward(num/4)
    one.right(45)
    one.forward(num/6) 
    one.right(45)
    one.forward(num/2) 
    one.left(90)

def i(color, num, thick):
    two.pensize(thick)
    two.color(color)
    two.up()
    yield
    two.forward(num)
    yield
    two.down()
    yield
    two.right(90)
    yield
    two.forward(num/2)
    yield
    two.right(180)
    yield
    two.forward(num/4)
    yield
    two.left(90)
    yield
    two.forward(num)
    yield
    two.right(90)
    yield
    two.forward(num/4)
    yield
    two.right(180)
    yield
    two.forward(num/2)
    yield
    two.right(90)
    yield


def r(color, num, thick):
    one.pensize(thick)
    one.color(color)
    one.forward(num)
    yield
    one.right(90)
    yield
    one.forward(num/2)
    yield
    one.right(90)
    yield
    one.forward(num/2)
    yield
    one.right(90)
    yield
    one.forward(num/2)
    yield
    one.left(135)
    yield
    one.forward(math.sqrt((2*num**2)/4))
    yield
    one.right(45)
    yield


def t(color, num, thick):
    two.pensize(thick)
    two.color(color)
    two.up()
    yield
    two.forward(num)
    yield
    two.down()
    yield
    two.right(90)
    yield
    two.forward((num/4)*3)
    yield
    two.right(180)
    yield
    two.forward((num/8)*3)
    yield
    two.left(90)
    yield
    two.forward(num)
    yield


def d(color, num, thick):
    one.pensize(thick)
    one.color(color)
    one.forward(num)
    yield
    one.right(90)
    yield
    one.forward(num/4)
    yield
    one.right(45)
    yield
    one.forward(math.sqrt((2*num**2)/16))
    yield
    one.right(45)
    yield
    one.forward(num/2)
    yield
    one.right(45)
    yield
    one.forward(math.sqrt((2*num**2)/16))   
    yield
    one.right(45)
    yield
    one.forward(num/4)
    yield
    one.left(90)
    yield




background("Bisque", 7)
for a, b in itertools.zip_longest(random_hearts(), heart_sizes()):
    pass
one.right(90)


background("Light Pink", 11)

one.speed(4)
two.speed(4)


two.right(135)

num = 180
thick = 5
color = "Deep Pink"

#h
one.goto(-600 + (3*num)/2 + (num/4)*3 + 200, -200)
#a
two.goto(-350 + num/2 + 50, 100)
two.right(180)
two.down()

for a, b in itertools.zip_longest(A(color, num, thick), h(color, num, thick)):
    pass

oren()
#r
one.goto(-600 + num + 100, -200)
#y
two.goto(-350 + 2*num + 200 + num/4 , 100)
one.down()
two.down()

for a, b in itertools.zip_longest(r(color, num, thick), y(color, num, thick)):
    pass

oren()
#p
one.goto(-350 + 3*num/2 + 150, 100)
#y
two.goto(-600 + 6*num/2 + 350 + (num/4)*3 + num/4, -200)
one.down()
two.down()

for a, b in itertools.zip_longest(p(color, num, thick), y(color, num, thick)):
    pass

oren()
#D
one.goto(-600 + 2*num + (num/4)*3 + 250, -200)
#I
two.goto(-600 + num/2 + 50, -200)
one.down()
two.down()

for a, b in itertools.zip_longest(d(color, num, thick), i(color, num, thick)):
    pass

oren()
#P
one.goto(-350 + num + 100, 100)
#T
two.goto(-600 + 3*num/2 + 150, -200)
one.down()
two.down()

for a, b in itertools.zip_longest(p(color, num, thick), t(color, num, thick)):
    pass

oren()
#h
one.goto(-350, 100)
#A
two.goto(-600 + 5*num/2 + (num/4)*3 + 300, -200)
one.down()
two.down()

for a, b in itertools.zip_longest(A(color, num, thick), h(color, num, thick)):
    pass

oren()
#B
one.goto(-600,-200)
one.down()
two.down()

B(color, num, thick)


for run in range(20):
    two.up()
    two.goto(random.randrange(-600, 600),random.randrange(-300, 300))
    hearts("Bisque")



for run in range(4):
    background("purple", 11)
one.right(180)
one.speed(11)

def m(color, num, thick):
    one.pensize(thick)
    one.color(color)
    one.right(25)
    one.forward(num*0.6)
    one.right(155)
    one.forward(num)
    one.up()
    one.right(90)
    one.forward(num*0.2536)
    one.right(90)
    one.forward(num*0.4562)
    one.left(25)
    one.down()
    one.forward(num*0.6)
    one.left(155)
    one.forward(num)

def o(color, num, thick):
    one.pensize(thick)
    one.color(color)
    one.right(90)
    one.up()
    one.forward(3*num/16)
    one.down()
    one.left(90)
    one.forward(num/2)
    one.left(90)
    one.forward(3*num/8)
    one.left(90)
    one.forward(num)
    one.left(90)    
    one.forward(3*num/8)
    one.left(90)
    one.forward(num/2)    
    


for run in range(25, 250, 25):
    m("Bisque", run, 5)
    background("purple", 11)
    one.left(90)

for run in range(25, 250, 25):
    o("Bisque", run, 5)
    background("purple", 11)
    one.left(90)
    
one.left(180)

for run in range(25, 250, 25):
    m("Bisque", run, 5)
    background("purple", 11)
    one.left(90)


color = "Bisque"
num = 150
thick = 5
one.goto(-100,0)

m(color, num, thick)
one.up()
one.goto(0,0)
one.down()
o(color, num, thick)
one.up()
one.goto(100,0)
one.down()
one.right(180)
m(color, num, thick)

    
    
turtle.done()