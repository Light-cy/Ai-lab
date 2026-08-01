import math
def MinMax(total_depth, depth, terminal_values, Turn, index):
    if depth == total_depth:
        return terminal_values[index]
    
    if depth == 0:
        return max(MinMax(total_depth, depth+1, terminal_values, False, index*3),
                   MinMax(total_depth, depth+1, terminal_values, False, index*3+1),
                   MinMax(total_depth, depth+1, terminal_values, False, index*3+2))
    
    if depth == 2 and index == 2:
        return MinMax(total_depth, depth+1, terminal_values, False, index * 2)
    
    if depth >= 2 and index >= 3:
        if Turn == True:
            return max(MinMax(total_depth, depth+1, terminal_values, False, index + 2),
                   MinMax(total_depth, depth+1, terminal_values, False, index + 2 +1))
        else:
            return min(MinMax(total_depth, depth+1, terminal_values, True, index + 2),
                   MinMax(total_depth, depth+1, terminal_values, True, index + 2 + 1))
    
    if Turn == True:
        return max(MinMax(total_depth, depth+1, terminal_values, False, index*2),
                   MinMax(total_depth, depth+1, terminal_values, False, index*2+1))
    else:
        return min(MinMax(total_depth, depth+1, terminal_values, True, index*2),
                   MinMax(total_depth, depth+1, terminal_values, True, index*2+1))

terminal_values = [2, 3, 5, 9, 0, 7, 4, 2, 1, 5, 6]

print(MinMax(3, 0, terminal_values, True, 0))