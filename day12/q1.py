import os
import numpy as np
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

# not much to say, A* algorithm implementation

# first organize the input data to a 2D numpy array as a map
map=[]
Start=(0,0)
End=(0,0)
for index1,line in enumerate(file):
    line=line.replace('\n','')
    tmp_l=[]
    for index2,i in enumerate(line):
        if i=='S':
            Start=(index1,index2)
            tmp_l.append(1)
        elif i=='E':
            End=(index1,index2)
            tmp_l.append(26)
        else:
            tmp_l.append(ord(i)-ord('a')+1)
    map.append(tmp_l)
map=np.array(map)

# now we have a map, and the start and end point
# A* algorithm impementation

class Node:
    def __init__(self,pos,g,h):
        self.pos=pos
        self.g=g
        self.h=h
        self.f=g+h
    def __eq__(self,other):
        return self.pos==other.pos

def cal_h(pos1,pos2=End):
    return pow(pos1[0]-pos2[0],2)+pow(pos1[1]-pos2[1],2)

def min_g_node(open):
    return min(open,key=lambda x:x.g)

def get_node_by_pos(open:list[Node],pos) ->Node:   
    for i in open:
        if i.pos==pos:
            return i
    return open[0] # this won't execute but to make the type checker happy

def accessable(pos1,pos2):
    global map
    # pos1 and pos2 are neighbors
    if map[pos1[0],pos1[1]]+1>=map[pos2[0],pos2[1]]:
        return True
    else:
        return False


def check_neighbor(node:Node,open,closed):
    # neighbor up
    if node.pos[0]-1>=0:
        up_pos=(node.pos[0]-1,node.pos[1])
        if accessable(node.pos,up_pos):
            if closed[up_pos[0],up_pos[1]]==0:
                # append to open
                # check if it is in open, if so, keep the one with smaller g
                if Node(up_pos,node.g+1,cal_h(up_pos)) in open:
                    if get_node_by_pos(open,up_pos).g>node.g+1:
                        open.remove(get_node_by_pos(open,up_pos))
                        open.append(Node(up_pos,node.g+1,cal_h(up_pos)))
                else:
                    #if not in open, append it
                    open.append(Node(up_pos,node.g+1,cal_h(up_pos)))

    # neighbor down
    if node.pos[0]+1<map.shape[0]:
        down_pos=(node.pos[0]+1,node.pos[1])
        if accessable(node.pos,down_pos):
            if closed[down_pos[0],down_pos[1]]==0:
                # append to open
                # check if it is in open, if so, keep the one with smaller g
                if Node(down_pos,node.g+1,cal_h(down_pos)) in open:
                    if get_node_by_pos(open,down_pos).g>node.g+1:
                        open.remove(get_node_by_pos(open,down_pos))
                        open.append(Node(down_pos,node.g+1,cal_h(down_pos)))
                else:
                    #if not in open, append it
                    open.append(Node(down_pos,node.g+1,cal_h(down_pos)))
    
    # neighbor left
    if node.pos[1]-1>=0:
        left_pos=(node.pos[0],node.pos[1]-1)
        if accessable(node.pos,left_pos):
            if closed[left_pos[0],left_pos[1]]==0:
                # append to open
                # check if it is in open, if so, keep the one with smaller g
                if Node(left_pos,node.g+1,cal_h(left_pos)) in open:
                    if get_node_by_pos(open,left_pos).g>node.g+1:
                        open.remove(get_node_by_pos(open,left_pos))
                        open.append(Node(left_pos,node.g+1,cal_h(left_pos)))
                else:
                    #if not in open, append it
                    open.append(Node(left_pos,node.g+1,cal_h(left_pos)))

    # neighbor right
    if node.pos[1]+1<map.shape[1]:
        right_pos=(node.pos[0],node.pos[1]+1)
        if accessable(node.pos,right_pos):
            if closed[right_pos[0],right_pos[1]]==0:
                # append to open
                # check if it is in open, if so, keep the one with smaller g
                if Node(right_pos,node.g+1,cal_h(right_pos)) in open:
                    if get_node_by_pos(open,right_pos).g>node.g+1:
                        open.remove(get_node_by_pos(open,right_pos))
                        open.append(Node(right_pos,node.g+1,cal_h(right_pos)))
                else:
                    #if not in open, append it
                    open.append(Node(right_pos,node.g+1,cal_h(right_pos)))
    
    # after checking neighbors, append the node to closed and remove it from open
    closed[node.pos[0],node.pos[1]]=1
    open.remove(node)
    

def check_end(End,close):  
    if close[End[0],End[1]]==1:
        return True
    else:
        return False

open=[Node(Start,0,cal_h(Start))]
closed=np.zeros(map.shape)


while open:
    # check if min_g_node is the End node
    # if so, break
    # if not run check_neighbor
    if min_g_node(open).pos==End:
        print(min_g_node(open).f)
        break
    check_neighbor(min_g_node(open),open,closed)
