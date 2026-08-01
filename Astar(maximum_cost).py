graph={
    'S':{'A':3,'C':2,'D':2},
    'A':{},
    'C':{'F':1},
    'D':{'B':3,'G':8},
    'B':{'E':2},
    'E':{'G':2},
    'F':{'E':0,'G':4},
    'G':{}
}
H={
    'S':20,
    'A':18,
    'C':16,
    'D':14,
    'B':10,
    'E':9,
    'F':10,
    'G':0
}
def Astar(start,goal):
    cost=0
    path=[start]
    visited=[]
    queue=[cost,path]
    while queue:
        index=0
        minIndex=0
        
        while index<len(queue):

        #MAXIMUM COST MINIMUM HEURISTIC
            current = H[queue[minIndex+1][len(queue[minIndex+1])-1]]-queue[minIndex]
            next= H[queue[index+1][len(queue[index+1])-1]]-queue[index]
            if current>next:
                minIndex=index
            index=index+2
           
        cost=queue.pop(minIndex)
        path=queue.pop(minIndex)
        last=path[-1]
        
        if last not in visited:
            visited.append(last)
        if last==goal:
            path.append(str(cost))
            return path
        
        for child in graph[last].keys():
            newPath=list(path)
            newPath.append(child)
            queue.append(cost+graph[last][child])
            queue.append(newPath)

print(Astar('S','G'))