
#Qaseeb Ahmad
#L1F23BSCS0923
#F5
#Sir Afham nazir
graph = {
    'CS': {'ITC': 65, 'PF': 67, 'XC': 68},
    'ITC': {'OOP': 35, 'DSA': 75, 'PF': 55},
    'OOP': {'DSA': 35, 'CCN': 29},
    'DSA': {'LA': 32, 'DAA': 35, 'CCN': 25},
    'PF': {'LA': 29, 'DS': 21},
    'XC': {'DS': 22, 'TOA': 36},
    'LA': {'DAA': 35},
    'DS': {'DB': 27, 'TOA': 32},
    'DB': {'WEB': 66, 'TOA': 35},
    'TOA': {'WEB': 62, 'MAD': 39},
    'WEB': {'AI': 22, 'FYP': 41},
    'DAA': {'AI': 32},
    'CCN': {'AI': 38, 'FYP': 50, 'ML': 55},
    'ML': {'FYP': 35},
    'AI': {'FYP': 85},
    'MAD': {'FYP': 22},
    'FYP': {}
}

Heuristic = {
    'CS': 26, 'ITC': 22, 'PF': 21, 'OOP': 19, 'DSA': 20, 'XC': 23,
    'CCN': 15, 'ML': 12, 'AI': 9, 'LA': 18, 'DAA': 14, 'DS': 16,
    'DB': 14, 'TOA': 15, 'WEB': 10, 'MAD': 13, 'FYP': 0
}

def A_star(startingNode, goal, myGraph):
    cost = 0
    path = [startingNode]

    visited = []
    queue = [cost, path]

    while queue:
        index = 0
        minIndex = 0

        while index < len(queue):
            currentNode = queue[minIndex] - Heuristic[queue[minIndex+1][len(queue[minIndex+1])-1]]
            nextNode = queue[index] - Heuristic[queue[index+1][len(queue[index+1])-1]]

            if currentNode < nextNode:
                minIndex = index
            index = index + 2

        cost = queue.pop(minIndex)
        path = queue.pop(minIndex)
        last_visited = path[-1]

        if last_visited not in visited:
            visited.append(last_visited)

        if last_visited == goal:
            path.append(cost)
            return path

        for child in myGraph[last_visited].keys():
            if child not in path:  # Avoid cycles
                newPath = list(path)
                newPath.append(child)
                queue.append(cost + myGraph[last_visited][child])
                queue.append(newPath)

# Just change goal to check for ai ml etc
result = A_star('CS', 'FYP', graph)

if result:
    total_incentives = result[-1]
    path = result[:-1]

    total_weeks = 0
    for node in path:
        total_weeks = total_weeks + Heuristic[node]

    print("Path:", end=" ")
    for i in range(len(path)):
        if i == len(path) - 1:
            print(path[i])
        else:
            print(path[i], end=" → ")

    print("Incentives:", total_incentives)
    print("Weeks:", total_weeks)
    print("Score:", total_incentives - total_weeks)
else:
    print("No path found")
