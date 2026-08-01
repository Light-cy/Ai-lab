graph ={

    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}
visited =[]
queue =[]

def BFS(startingNode,visited):
    visited.append(startingNode)
    queue.append(startingNode)
    
    while queue:
        node = queue.pop(0)
        print(node, end="  ")
        for child in graph[node]:
            if child not in visited:
                visited.append(child)
                queue.append(child)
            
BFS('A', visited)