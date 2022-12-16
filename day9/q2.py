import os
import numpy as np
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

marks=[[0,0]]
knots=np.array([[0,0]]*10)

def knot_move(head,tail):
    global knots, marks
    if abs(knots[head][0]-knots[tail][0])<=1 and abs(knots[head][1]-knots[tail][1])<=1:
        pass
    else:
        if knots[head][0]>knots[tail][0]:
            knots[tail][0]=knots[tail][0]+1
        elif knots[head][0]<knots[tail][0]:
            knots[tail][0]=knots[tail][0]-1
        if knots[head][1]>knots[tail][1]:
            knots[tail][1]=knots[tail][1]+1
        elif knots[head][1]<knots[tail][1]:
            knots[tail][1]=knots[tail][1]-1
    if tail==9 and [knots[tail][0],knots[tail][1]] not in marks:
        marks.append([knots[tail][0],knots[tail][1]])

def tails_move():
    global knots, marks
    for i in range(9):
        knot_move(i,i+1)
    

def move_up():
    global knots
    knots[0][0]=knots[0][0]-1
    tails_move()

def move_down():
    global knots
    knots[0][0]=knots[0][0]+1
    tails_move()

def move_left():
    global knots
    knots[0][1]=knots[0][1]-1
    tails_move()

def move_right():
    global knots
    knots[0][1]=knots[0][1]+1
    tails_move()

for line in file:
    line=line.replace('\n','').split(' ')
    if line[0]=='U':
        for i in range(int(line[1])):
            move_up()
    elif line[0]=='D':
        for i in range(int(line[1])):
            move_down()
    elif line[0]=='L':
        for i in range(int(line[1])):
            move_left()
    elif line[0]=='R':
        for i in range(int(line[1])):
            move_right()
print(len(marks))