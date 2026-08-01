def Alpha_Beta(D, I, Turn, S, A, B):
    if D == 3:
        return S[I]

    # MAX player
    if Turn:
        Best = -1000
        for i in range(2):
            V = Alpha_Beta(D+1, I*2+i, not Turn, S, A, B)
            Best = max(Best, V)
            A = max(A, Best)
            if B <= A:
                break
        return Best

    # MIN player
    else:
        Best = 1000
        for i in range(2):
            V = Alpha_Beta(D+1, I*2+i, not Turn, S, A, B)
            Best = min(Best, V)
            B = min(B, Best)
            if B <= A:
                break
        return Best


Alpha = -1000
Beta = 1000
Score = [-3,-2,4,5,2,-6,9,7]

print("Optimal Value is:", Alpha_Beta(0,0,True,Score,Alpha,Beta))
