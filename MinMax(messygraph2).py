import math
def MinMax(total_depth,depth,terminal_values,Turn,index):
    if depth==total_depth:
        return terminal_values[index]
    
    if depth == 0:
        return max(MinMax(total_depth,depth+1,terminal_values,False,index*3),
        MinMax(total_depth,depth+1,terminal_values,False,index*3+1),
        MinMax(total_depth,depth+1,terminal_values,False,index*3+2))
    
    if depth == 1 and index == 1:
        return min(MinMax(total_depth,depth+1,terminal_values,True,index*2),
        MinMax(total_depth,depth+1,terminal_values,True,index*2+1),
        MinMax(total_depth,depth+1,terminal_values,True,index*2+2),
        100)
        
    if depth == 1 and index == 2:
        return min(MinMax(total_depth,depth+1,terminal_values,True,index*2 + 1),
        MinMax(total_depth,depth+1,terminal_values,True,index*2+2),
        MinMax(total_depth,depth+1,terminal_values,True,index*2+3))
        
    if depth == 2 and index == 0:
        return max(MinMax(total_depth,depth+1,terminal_values,False,index*2),
        MinMax(total_depth,depth+1,terminal_values,False,index*2+1),
        MinMax(total_depth,depth+1,terminal_values,False,index*2+2))
        
    if depth == 2 and index == 1:
        return MinMax(total_depth,depth+1,terminal_values,True,index * 2 + 1)
    
    if depth == 2 and index == 2:
         return MinMax(total_depth,depth+1,terminal_values,True,index * 2)
        
    if depth == 2 and index == 3:
        return max(MinMax(total_depth,depth+1,terminal_values,False,index*2),
        MinMax(total_depth,depth+1,terminal_values,False,index*2+1))
    
    if depth == 2 and index == 4:
        return max(MinMax(total_depth,depth+1,terminal_values,False,index  + 2 + 1),
        MinMax(total_depth,depth+1,terminal_values,False,index + 2+2),
        MinMax(total_depth,depth+1,terminal_values,False,index + 2+3),
        MinMax(total_depth,depth+1,terminal_values,False,index + 2+4))
    
    if depth == 2 and index == 5:
        return max(MinMax(total_depth,depth+1,terminal_values,False,index * 2 + 1),
        MinMax(total_depth,depth+1,terminal_values,False,index * 2+2))
        
    if depth == 2 and index == 6:
       return MinMax(total_depth,depth+1,terminal_values,True,index * 2 + 1)
        
    if depth == 2 and index == 7:
        return max(MinMax(total_depth,depth+1,terminal_values,False,index * 2),
        MinMax(total_depth,depth+1,terminal_values,False,index * 2+1))
        
    if Turn==True:
        return max(MinMax(total_depth,depth+1,terminal_values,False,index*2),
        MinMax(total_depth,depth+1,terminal_values,False,index*2+1))
    else:
        return min(MinMax(total_depth,depth+1,terminal_values,True,index*2),
        MinMax(total_depth,depth+1,terminal_values,True,index*2+1))


terminal_values = [23,28,21,-3,12,4,70,-4,-12,-70,-5,-100,-73,-14,-8,-24]
print(MinMax(3,0,terminal_values,True,0))
