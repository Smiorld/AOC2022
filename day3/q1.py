import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

sum=0
while 1:
    line = str(file.readline().replace("\n",""))
    if not line:
        break
    first=line[0:int(len(line)/2)]
    second=line[int(len(line)/2):int(len(line))]
    for i in first:
        if i in second:
            if ord(i)>96:
                sum+=ord(i)-96
            else:
                sum+=ord(i)-64+26
            break
print(sum)