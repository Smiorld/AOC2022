import os
import numpy as np
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

highest_score=0

grid = np.array([[int(digit) for digit in line.replace('\n','')] for line in file])
WEIGHT=len(grid[0])
HEIGHT=len(grid)

def check_up(i,j):
    global grid
    tree_h=grid[i][j]
    if i>0: # if not edge
        for a in range(i-1,-1,-1):
            if grid[a][j]>=tree_h:
                return i-a
        return i
    else:
        return 0
        
def check_down(i,j):
    global grid
    tree_h=grid[i][j]
    if i<HEIGHT-1: # if not edge
        for a in range(i+1,HEIGHT):
            if grid[a][j]>=tree_h:
                return a-i
        return HEIGHT-1-i
    else:
        return 0

def check_left(i,j):
    global grid
    tree_h=grid[i][j]
    if j>0: # if not edge
        for a in range(j-1,-1,-1):
            if grid[i][a]>=tree_h:
                return j-a
        return j
    else:
        return 0

def check_right(i,j):
    global grid
    tree_h=grid[i][j]
    if j<WEIGHT-1: # if not edge
        for a in range(j+1,WEIGHT):
            if grid[i][a]>=tree_h:
                return a-j
        return WEIGHT-1-j
    else:
        return 0

for i in range(0,HEIGHT):
    for j in range(0,WEIGHT):
        score = check_up(i,j) * check_down(i,j) * check_left(i,j) * check_right(i,j)
        if score>highest_score:
            highest_score=score

print(highest_score)