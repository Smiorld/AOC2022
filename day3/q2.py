import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

sum=0
while 1:
    line1 = str(file.readline().replace("\n",""))
    line2 = str(file.readline().replace("\n",""))
    line3 = str(file.readline().replace("\n",""))
    if not line1:
        break
    for i in line1:
        if i in line2 and i in line3:
            if ord(i)>96:
                sum+=ord(i)-96
            else:
                sum+=ord(i)-64+26
            break
print(sum)