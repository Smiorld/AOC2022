import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

max=0
count=0
while 1:
    line = file.readline()
    if not line:
        break
    if bool(line.replace('\n','')):
        count+=int(line.replace('\n',''))
    else:
        if count>max:
            max=count
        count=0
if count!=0:
    if count>max:
        max=count
print(max)