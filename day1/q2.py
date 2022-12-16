import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

top1=0
top2=0
top3=0
count=0
while 1:
    line = file.readline()
    if not line:
        break
    if bool(line.replace('\n','')):
        count+=int(line.replace('\n',''))
    else:
        if count>top1:
            top3=top2
            top2=top1
            top1=count
            count=0
            continue
        if count>top2:
            top3=top2
            top2=count
            count=0
            continue
        if count>top3:
            top3=count
            count=0
            continue
        count=0
if count!=0:
    if count>top1:
            top3=top2
            top2=top1
            top1=count
            count=0
    elif count>top2:
            top3=top2
            top2=count
            count=0
    elif count>top3:
            top3=count
print(top1+top2+top3)