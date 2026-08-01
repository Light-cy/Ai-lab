import math
def MinMax(total_depth,depth,terminal_values,Turn,index):
    if depth==total_depth:
        return terminal_values[index]
    if Turn==True:
        return max(MinMax(total_depth,depth+1,terminal_values,False,index*2),
        MinMax(total_depth,depth+1,terminal_values,False,index*2+1))
    else:
        return min(MinMax(total_depth,depth+1,terminal_values,True,index*2),
        MinMax(total_depth,depth+1,terminal_values,True,index*2+1))


terminal_values = [-1,4,2,6,-3,-5,0,7]

print(MinMax(3,0,terminal_values,True,0))
