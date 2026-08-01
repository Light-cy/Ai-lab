
MyGraph = {
    'A' : ['B','C'],
    'B' : ['A','C','D'],
    'C' : ['A','B','E'],
    'D' : ['B','E','F'],
    'E' : ['C','D','F'],
    'F' : ['D','E'],
}
HeuristicVales={
    'A' : 25,
    'B' : 8,
    'C' : 20,
    'D' : 6,
    'E' : 12,
    'F' : 0,
}

def HCS_simple(start,goal):
    Node=start
    while True:
        print(Node)
        if Node==goal:
            print('Goal Node Found...')
            break
        minH=Node
        for child in MyGraph[Node]:
            if HeuristicVales[minH] > HeuristicVales[child]:
                minH=child
        if minH==Node:
            print('Max Point.....')
            break
        Node=minH
        
HCS_simple('A','F')
            