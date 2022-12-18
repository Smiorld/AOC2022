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
        
    

                
sum=0
index=0
while True:
    index+=1
    p1=file.readline().replace('\n','')
    p2=file.readline().replace('\n','')
    file.readline() # empty line
    if not p1:
        break
    p1=ast.literal_eval(p1) # convert list print output string back to list
    p2=ast.literal_eval(p2)
    result= compare(p1,p2)
    if result>=0:
        sum+=index
print(sum)
