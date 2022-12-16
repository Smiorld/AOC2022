import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

def decode(p):
    match p:
        case 'A':
            return 1
        case 'B':
            return 2
        case 'C':
            return 3
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3
    return 0


score=0
while 1:
    line = file.readline().replace('\n','')
    if not line:
        break
    tmp_line = line.split(' ')
    p1=decode(tmp_line[0])
    p2=decode(tmp_line[1])
    if p1==p2:
        score=score+3+p2
    elif (p1==1 and p2==3) or (p1==2 and p2==1) or (p1==3 and p2==2):
        score=score+0+p2
    else:
        score=score+6+p2
print(score)

    

