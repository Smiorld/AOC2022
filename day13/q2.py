import os
import ast
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

# typical recursive function
def compare(a,b):
    if isinstance(a, int) and isinstance(b, int):
        if a<b:
            return 1
        elif a==b:
            return 0
        else:
            return -1
    elif isinstance(a, list) and isinstance(b, list):
        for index,x in enumerate(a):
            if index>len(b)-1:
                return -1
            else:
                tmp_result= compare(x,b[index])
                if tmp_result!=0:
                    return tmp_result
                else:
                    continue
        if len(a)<len(b):
            return 1
        else:
            return 0
    else:
        # one is list, one is int
        if isinstance(a, list):
            return compare(a,[b])
        else:
            return compare([a],b)

p_list=[]
for line in file:
    line=line.replace('\n','')
    if line:
        p_list.append(ast.literal_eval(line))

p_list.append([[2]])
pos1=len(p_list)-1
p_list.append([[6]])
pos2=len(p_list)-1

# bubble sort
for i in range(len(p_list)):
    for j in range(len(p_list)-1-i):
        if compare(p_list[j],p_list[j+1])<0:
            tmp=p_list[j]
            p_list[j]=p_list[j+1]
            p_list[j+1]=tmp
            if j==pos1:
                pos1=j+1
            elif j+1==pos1:
                pos1=j
            if j==pos2:
                pos2=j+1
            elif j+1==pos2:
                pos2=j

# check the p_list
for i in range(len(p_list)-1):
    if compare(p_list[i],p_list[i+1])<0:
        print('error')
        break
print((pos1+1)*(pos2+1))
