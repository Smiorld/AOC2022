import os
import numpy as np
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

counter=0

grid = np.array([[int(digit) for digit in line.replace('\n','')] for line in file])
WEIGHT=len(grid[0])
HEIGHT=len(grid)

def check_up(i,j):
    global grid
    global counter
    tree_h=grid[i][j]
    if i>0: # if not edge
        for a in range(0,i):
            if grid[a][j]>=tree_h:
                return False
    counter+=1
    return True
        
def check_down(i,j):
    global grid
    global counter
    tree_h=grid[i][j]
    if i<HEIGHT-1: # if not edge
        for a in range(i+1,HEIGHT):
            if grid[a][j]>=tree_h:
                return False
    counter+=1
    return True

def check_left(i,j):
    global grid
    global counter
    tree_h=grid[i][j]
    if j>0: # if not edge
        for a in range(0,j):
            if grid[i][a]>=tree_h:
                return False
    counter+=1
    return True

def check_right(i,j):
    global grid
    global counter
    tree_h=grid[i][j]
    if j<WEIGHT-1: # if not edge
        for a in range(j+1,WEIGHT):
            if grid[i][a]>=tree_h:
                return False
    counter+=1
    return True

for i in range(0,HEIGHT):
    for j in range(0,WEIGHT):
        if check_up(i,j) or check_down(i,j) or check_left(i,j) or check_right(i,j):
            continue

print(counter)