import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

marks=[[0,0]]
head=[0,0]
tail=[0,0]

def tail_move():
    global head, tail, marks
    if abs(head[0]-tail[0])<=1 and abs(head[1]-tail[1])<=1:
        pass
    else:
        if head[0]>tail[0]:
            tail=[tail[0]+1,tail[1]]
        elif head[0]<tail[0]:
            tail=(tail[0]-1,tail[1])
        if head[1]>tail[1]:
            tail=(tail[0],tail[1]+1)
        elif head[1]<tail[1]:
            tail=(tail[0],tail[1]-1)
    if [tail[0],tail[1]] not in marks:
        marks.append([tail[0],tail[1]])

def move_up():
    global head
    head=[head[0]-1,head[1]]
    tail_move()

def move_down():
    global head
    head=[head[0]+1,head[1]]
    tail_move()

def move_left():
    global head
    head=[head[0],head[1]-1]
    tail_move()

def move_right():
    global head
    head=[head[0],head[1]+1]
    tail_move()

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