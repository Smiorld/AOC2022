import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

counter=0
while 1:
    line = str(file.readline().replace("\n",""))
    if not line:
        break
    line=line.split(",")
    e1=line[0].split("-")
    e2=line[1].split("-")

    if int(e1[0])>int(e2[1]) or int(e1[1])<int(e2[0]) :
        pass
    else:
        counter+=1
print(counter)