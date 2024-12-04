graph={
    'P':['Q','R','S'],
    'Q':['P','R'],
    'R':['P','Q','T'],
    'T':['R'],
    'S':['P']
}

visited = []
queue = []

def bfs(node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m)
        for n in graph[m]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
print('following is the breadth first search')
bfs('P')