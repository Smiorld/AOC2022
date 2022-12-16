import os
import re
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")
l=[
    [],
    ['F','C','J','P','H','T','W'],
    ['G','R','V','F','Z','J','B','H'],
    ['H','P','T','R'],
    ['Z','S','N','P','H','T'],
    ['N','V','F','Z','H','J','C','D'],
    ['P','M','G','F','W','D','Z'],
    ['M','V','Z','W','S','J','D','P'],
    ['N','D','S'],
    ['D','Z','S','F','M']
]

for i in range(10):
    file.readline()
for line in file:
    num=re.split('move|from|to',line.replace("\n",""))
    times=int(num[1])
    from_l=int(num[2])
    to_l=int(num[3])
    tmp=[]
    for i in range(times):
        tmp.append(l[from_l].pop())
    for i in range(times):
        l[to_l].append(tmp.pop())
output=''
for i in range(1,10):
    output+=str(l[i].pop())
print(output)