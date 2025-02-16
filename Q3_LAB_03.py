# Implement Iterative deepening DFS on graph and tree.
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H','I'],
    'E': [],
    'F': ['I'],
    'G': ['I'],
    'H': ['F'],
    'I': ['A']
}
def dls(node, goal, depth, path,dictg):
    if depth == 0:
        return False
    if node == goal:
        path.append(node)
        return True
    if node not in dictg:
        return False
    for child in dictg[node]:
        if dls(child, goal, depth - 1, path,dictg):
            path.append(node)  
            return True
    return False

def iterative_deepening(start, goal, max_depth,dictg):
    for depth in range(max_depth + 1):
        print(f"Depth: {depth}")
        path = []
        if dls(start, goal, depth, path,dictg):
            print("\nPath to goal:", " → ".join(reversed(path))) 
            return
        print("Goal not found within depth limit.")

start_node = 'A'
goal_node = 'I'
max_search_depth = 5
iterative_deepening(start_node, goal_node, max_search_depth,graph)
iterative_deepening(start_node, goal_node, max_search_depth,tree)
