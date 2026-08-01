import math

def AlphaBeta(totaldepth, depth, terminalvalues, turn, index, A, B):
    # Base Case: Leaf node
    if depth == totaldepth:
        return terminalvalues[index]
    
    # Maximizer Logic
    if turn == True:
        Best = -1000 # Shuru mein -Infinity
        for i in range(2):
            # Recursion: Agli baari Minimizer (False) ki hogi
            # Humen A aur B agay pass karnay hain
            val = AlphaBeta(totaldepth, depth + 1, terminalvalues, False, index * 2 + i, A, B)
            
            Best = max(Best, val)
            A = max(A, Best) # Alpha update karo
            
            # Pruning Condition
            if A >= B:
                break
        return Best

    # Minimizer Logic
    else:
        Best = 1000 # Shuru mein +Infinity
        for i in range(2):
            # Recursion: Agli baari Maximizer (True) ki hogi
            val = AlphaBeta(totaldepth, depth + 1, terminalvalues, True, index * 2 + i, A, B)
            
            Best = min(Best, val)
            B = min(B, Best) # Beta update karo
            
            # Pruning Condition
            if A >= B:
                break
        return Best

# --- Main Execution ---
terminal_values = [-1, 4, 2, 6, -3, -5, 0, 7]

# Start with Alpha = -Infinity, Beta = +Infinity
print(AlphaBeta(3, 0, terminal_values, True, 0, -1000, 1000))