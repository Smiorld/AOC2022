import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

# this one is relatively difficult.
# I plan to create a dictionary as the base dir. 
# Every sub dir will be a key:dictionary pair.
# Every sub file will be a key:value pair. The value represents the file size.

base={} # base dir, also known as "/"
currentpath=[]
total_sizes=0

def add_file(size,file):
    global currentpath,base
    tmp=base
    for i in currentpath:
        tmp=tmp[i]
    tmp.update({str(file):int(size)})


def add_dir(dir):
    global currentpath,base
    tmp=base
    for i in currentpath:
        tmp=tmp[i]
    tmp.update({str(dir):{}})

def count_size(a): # a is a dictionary
    size=0
    for i in a:
        if isinstance(a[i],dict):
            size+=count_size(a[i])
        else:
            size+=int(a[i])
    return size

def total_size(size):
    global total_sizes
    total_sizes+=size
    return total_sizes

# read from input.txt
for line in file:
    if line[0]=='$': # user command
        line=line.replace('$','').replace('\n','').strip().split(' ')
        if line[0]=='cd': # cd
            if line[1]=='..': # cd ..
                currentpath.pop()
            elif line[1]=='/': # cd /
                currentpath=[]
            else: # cd dir
                currentpath.append(line[1])
        else: # ls
            pass
    else: # system print
        line=line.replace('\n','').strip().split(' ')
        if line[0]=='dir': # dir xxx
            add_dir(line[1])
        else: # file
            add_file(line[0],line[1])
        
# count each dir
def go_through(a): # a is a dictionary
    count=count_size(a)
    if count<100000:
        total_size(count)
    for i in a:
        if isinstance(a[i],dict): # if it is a dir
            go_through(a[i])
        else: # if it is a file
            pass

go_through(base)
print(total_sizes)




    