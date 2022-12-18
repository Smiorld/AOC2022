import os
import operator
import numpy as np
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__,'input.txt'), 'r',encoding="utf-8")

# the input is complecated and I plan to initialize the values manually

opt={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv,'**':operator.pow}

monkey_items =[
    [57],
    [58,93,88,81,72,73,65],
    [65,95],
    [58,80,81,83],
    [58,89,90,96,55],
    [66,73,87,58,62,67],
    [85,55,89],
    [73,80,54,94,90,52,69,58]
]

monkey_inspect = [
    ['*',13],
    ['+',2],
    ['+',6],
    ['**',2],
    ['+',3],
    ['*',7],
    ['+',4],
    ['+',7]
]

monkey_test = np.array([11,7,13,5,3,17,2,19])

monkey_throw=np.array([[3,2],[6,7],[3,5],[4,5],[1,7],[4,1],[2,0],[6,0]])

# logic starts

inspect_counter=[0]*8

def one_round():
    global monkey_items,monkey_inspect,monkey_test,monkey_throw,inspect_counter
    # evey monkey operates in turn
    for i in range(8):
        for item in monkey_items[i]:
            # inspect each item
            inspect_counter[i]+=1
            # item worry value changes
            item=int(opt[monkey_inspect[i][0]](item,monkey_inspect[i][1])/3)
            #test and throw it to next monkey
            if item%monkey_test[i]==0:
                monkey_items[monkey_throw[i][0]].append(item)
            else:
                monkey_items[monkey_throw[i][1]].append(item)
        monkey_items[i]=[]

# run 20 rounds
for i in range(20):
    one_round()

# find the two monkeys inspected most items
max1=max(enumerate(inspect_counter),key=operator.itemgetter(1))
inspect_counter.pop(max1[0])
max2=max(enumerate(inspect_counter),key=operator.itemgetter(1))
print(max1[1]*max2[1])



