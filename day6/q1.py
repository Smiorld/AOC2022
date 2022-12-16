import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

def duplica(queue):
    for i,x in enumerate(queue):
        if x in queue[i+1:]:
            return True
    return False


queue=[]
for line in file:
    line=line.replace("\n","")
    for i,x in enumerate(line):
        if i<3:
            queue.append(x)
        else:
            queue.append(x)
            if duplica(queue):
                queue.pop(0)
            else:
                print(i+1)
                print(queue)
                break
                
