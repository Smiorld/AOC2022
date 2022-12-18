import os
import numpy as np
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

# read paths
paths=[[tuple([int(x) for x in n.strip().split(',')]) for n in line.replace('\n','').split('->')] for line in file.readlines()]

# find boundaries
max_rock_y=0
max_rock_x=0
for path in paths:
    for rock in path:
        if rock[0]>max_rock_x:
            max_rock_x=rock[0]
        if rock[1]>max_rock_y:
            max_rock_y=rock[1]

# create rock map
# 0: empty, 1: rock, 2: sand
rock_map=np.zeros((max_rock_y+1+2,max_rock_x+1+max_rock_y),dtype=int)
for i in range(max_rock_x+1+max_rock_y):
    rock_map[max_rock_y+2,i]=1

 
# draw paths
for path in paths:
    for i in range(len(path)-1):
        if path[i][0]==path[i+1][0]:
            # x direction line
            if path[i][1]<path[i+1][1]:
                for y in range(path[i][1],path[i+1][1]+1):
                    rock_map[y,path[i][0]]=1
            else:
                for y in range(path[i+1][1],path[i][1]+1):
                    rock_map[y,path[i][0]]=1
        else:
            # y direction line
            if path[i][0]<path[i+1][0]:
                for x in range(path[i][0],path[i+1][0]+1):
                    rock_map[path[i][1],x]=1
            else:
                for x in range(path[i+1][0],path[i][0]+1):
                    rock_map[path[i][1],x]=1

# drop 1 unit of sand

def drop_sand():
    global rock_map, max_rock_x, max_rock_y
    rest_pos= sand_go_down((0,500))
    if rest_pos:
        rock_map[rest_pos]=2
        return True
    else:
        return False

def sand_go_down(pos):
    global rock_map, max_rock_x, max_rock_y
    if pos[0]+1 < len(rock_map) and rock_map[pos[0]+1,pos[1]]==0:
        return sand_go_down((pos[0]+1,pos[1]))
    else:
        if pos[0]+1 >= len(rock_map):
            return False
        else:
            # sand drop on a rock or a rest sand. need split way to left down or right down
            if rock_map[pos[0]+1,pos[1]-1]==0:
                return sand_go_down((pos[0]+1,pos[1]-1))
            elif rock_map[pos[0]+1,pos[1]+1]==0:
                return sand_go_down((pos[0]+1,pos[1]+1))
            else:
                if pos==(0,500):
                    return False
                return pos

counter=0
while True:
    if not drop_sand():
        break
    counter+=1
print(counter+1)# add 1 for the last sand that block the entrance

