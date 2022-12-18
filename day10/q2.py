import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

value=1
next_value=0
cycle=0
crt_pos_offset=1
stop_executing_at=0
crt_output=""
def clock_go():
    global value, next_value, cycle, stop_executing_at,crt_output,crt_pos_offset
    # at the start of the cycle
    if stop_executing_at==cycle:
        line=file.readline().replace('\n','').split(' ')
        if not line:
            return False
        if line[0]=='noop':
            stop_executing_at+=1
            next_value=0
        elif line[0]=='addx':
            next_value=int(line[1])
            stop_executing_at+=2
    # during the cycle
    cycle+=1
    crt_pos=cycle-crt_pos_offset
    if abs(value-crt_pos)<=1:
        crt_output+="#"
    else:
        crt_output+="."
    if cycle%40==0:
        print(crt_output)
        crt_output=""
        crt_pos_offset+=40
    # at the end of the cycle
    if cycle==stop_executing_at:
        value+=next_value
    
    return True

while True:
    clock_go()
    if cycle>=240:
        break
