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
    result=decode(tmp_line[1])
    if result == 1: #lose
        if p1-1==0:
            score=score+0+3
        else:
            score=score+0+p1-1
    elif result == 2: #draw
        score=score+3+p1
    else: #win
        if p1+1==4:
            score=score+6+1
        else:
            score=score+6+p1+1
print(score)

