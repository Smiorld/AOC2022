import os
import numpy as np
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

# Nah my code is not worth referring to. It ran for several minutes to get the answer.

class diamond_area():
    def __init__(self,S,B):

        manhattan_d=abs(S[0]-B[0])+abs(S[1]-B[1])
        self.s=S
        self.b=B
        self.p_up=(S[0],S[1]+manhattan_d)
        self.p_left=(S[0]-manhattan_d,S[1])
        self.p_right=(S[0]+manhattan_d,S[1])
        self.p_down=(S[0],S[1]-manhattan_d)
        
    def is_point_above_line(self,test_point,p1,p2):
        # y=kx+b. k=(y2-y1)/(x2-x1)
        k=(p2[1]-p1[1])/(p2[0]-p1[0])
        # b=y1-kx1 or b=y2-kx2
        b=p1[1]-k*p1[0]
        if test_point[1]>=k*test_point[0]+b:
            return True
        else:
            return False
    
    def is_point_below_line(self,test_point,p1,p2):
        # y=kx+b. k=(y2-y1)/(x2-x1)
        k=(p2[1]-p1[1])/(p2[0]-p1[0])
        # b=y1-kx1 or b=y2-kx2
        b=p1[1]-k*p1[0]
        if test_point[1]<=k*test_point[0]+b:
            return True
        else:
            return False

    def is_point_in_area(self,point):
        if self.is_point_below_line(point,self.p_up,self.p_left) and self.is_point_below_line(point,self.p_up,self.p_right) and self.is_point_above_line(point,self.p_left,self.p_down) and self.is_point_above_line(point,self.p_right,self.p_down):
            return True
        else:
            return False
    
    def get_intersection(self,y,p1,p2):
        # y=kx+b. k=(y2-y1)/(x2-x1)
        k=(p2[1]-p1[1])/(p2[0]-p1[0])
        # b=y1-kx1 or b=y2-kx2
        b=p1[1]-k*p1[0]
        x=(y-b)/k
        return int(x)

    # this is a special function for the next fucntion to use
    def check_intersection(self,y,p1,p2):
        x=self.get_intersection(y,p1,p2)
        return self.is_point_in_area([x,y])

    def mark_horizental_line_in_area(self,y_value):
        if self.check_intersection(y_value,self.p_up,self.p_left):
            x_left=self.get_intersection(y_value,self.p_up,self.p_left)
            x_right=self.get_intersection(y_value,self.p_up,self.p_right)
            return (int(x_left),int(x_right))
        elif self.check_intersection(y_value,self.p_left,self.p_down):
            x_left=self.get_intersection(y_value,self.p_left,self.p_down)
            x_right=self.get_intersection(y_value,self.p_right,self.p_down)
            return (int(x_left),int(x_right))
        else:
            return None
    
diamonds=[]
for line in file:
    line=line.replace('\n','').replace('Sensor at x=','').replace(' y=','').replace(': closest beacon is at x=',' ').split(' ')
    s=[ int(x) for x in line[0].split(',')  ]
    b=[ int(x) for x in line[1].split(',')  ]
    diamonds.append(diamond_area(s,b))

def range_union(a):
        b = []
        for begin,end in sorted(a):
            if b and b[-1][1] >= begin - 1:
                b[-1][1] = max(b[-1][1], end)
            else:
                b.append([begin, end])
        return b
for y in range(0,4000001):
    ranges=[]
    for i in diamonds:
        range = i.mark_horizental_line_in_area(y)
        if range:
            ranges.append(range)

    result_ranges=range_union(ranges)
    sum=0
    for i in result_ranges:
        min1=max(0,i[0])
        max1=min(4000000,i[1])
        if min1<=max1:
            sum+=(max1-min1+1)
    if sum!=4000001:
        print(y)
        print(result_ranges)
        break


    
