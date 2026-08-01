def Alpha_Beta(D,I,Turn,S,A,B):
    if D==3:
        return S[I]
    if Turn:
        Best=Beta
        print(Best)
        for i in range(0,2):
            V=Alpha_Beta(D+1,I*2+i,False,S,A,B)
            Best=max(Best,V)
            A=max(A,Best)
            if B<=A:
                break
        return Best

    else:
        Best=Alpha
        for i in range(0,2):
            V=Alpha_Beta(D+1,I*2+i,True,S,A,B)
            Best=min(Best,V)
            A=min(A,Best)
            if B<=A:
                break
        return Best

Alpha=1000
Beta=-1000
Score=[-3,-2,4,5,2,-6,9,7]
print("Optimal Vale is : ", Alpha_Beta(0,0,True,Score,Beta,Alpha))