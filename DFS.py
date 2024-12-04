# #ADJACENCY LIST
# graph = {
# 'A' : ['B','C'],
# 'B' : ['D', 'E'],
# 'C' : ['F'],
# 'D' : [],
# 'E':['F'],
# 'F' : [],
# }
graph={
    'P':['Q','R','S'],
    'Q':['P','R'],
    'R':['P','Q','T'],
    'T':['R'],
    'S':['P']
}

visited = set()

def dfs(node):
    if node not in visited:
        print(node)
        visited.add(node)
        for n in graph[node]:
            dfs(n)

print("Following is the Depth-First Search")
dfs('P')