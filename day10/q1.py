import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

value=1
next_value=0
cycle=0
stop_executing_at=0
counter=0
sum=0

def clock_go():
    global value, next_value, cycle, stop_executing_at,sum,counter
    # at the start of the cycle
    if stop_executing_at==cycle:
        line=file.readline().replace('\n','').split(' ')
        if line[0]=='noop':
            stop_executing_at+=1
            next_value=0
        elif line[0]=='addx':
            next_value=int(line[1])
            stop_executing_at+=2
    # during the cycle
    cycle+=1
    if (cycle-20) % 40==0:
        sum+=value*cycle
        counter+=1
    # at the end of the cycle
    if cycle==stop_executing_at:
        value+=next_value

while True:
    clock_go()
    if counter==6:
        break
print(sum)