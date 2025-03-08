from queue import PriorityQueue  
class Node:
    def __init__(self, pos, parent=None):
        self.pos = pos  
        self.parent = parent  
        self.g = 0  
        self.h = 0  
        self.f = 0  

    def __lt__(self, other):
        return self.f < other.f  

def heuristic(current_pos, end_pos):
    return abs(current_pos[0] - end_pos[0]) + abs(current_pos[1] - end_pos[1])

def best_first_search(maze, start, goals):
    r, c = len(maze), len(maze[0])  
    start_node = Node(start)  

    frontier = PriorityQueue()  #select value with least heuristic value
    frontier.put((0, start_node))  
    visited = set()  #keeps tracks of all visited positions

    while not frontier.empty():  # while there are nodes to explore
        _, current_node = frontier.get()  
        current_pos = current_node.pos  

        if current_pos in goals:  # if current position is a goal, construct path
            path = []
            while current_node:
                path.append(current_node.pos)
                current_node = current_node.parent
            return path[::-1]  #[start:end:step]
        print(f"current position: {current_pos}")
        visited.add(current_pos)  

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # loop through possible moves
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)
            
            #if all moves are invalid and lead to dead end backtrack
            if (0 <= new_pos[0] < r and 0 <= new_pos[1] < c and maze[new_pos[0]][new_pos[1]] == 0 and new_pos not in visited):  # check if move is valid
                new_node = Node(new_pos, current_node)  
                new_node.h = min(heuristic(new_pos, goal) for goal in goals)  
                frontier.put((new_node.h, new_node))  
                visited.add(new_pos)  
    return None  

def find_shortest_path_with_goals(maze, start, goals):
    goals_to_visit = set(goals)  
    final_path = []  
    c_pos = start  
    
    while goals_to_visit:  # while there are goals left to visit
        shortest_path = None  
        nearest_goal = None  
        for goal in goals_to_visit:  # loop through remaining goals
            path = best_first_search(maze, c_pos, [goal])  
            if path is not None and (shortest_path is None or len(path) < len(shortest_path)):  # check if path to goal is shortest
                shortest_path = path  
                nearest_goal = goal  
        if shortest_path is None:  # if no path found to any goal, return none
            return None  
        final_path.extend(shortest_path if not final_path else shortest_path[1:])  
        c_pos = nearest_goal  
        goals_to_visit.remove(nearest_goal)  
    return final_path  

maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)  
goals = [(4, 4), (2, 3)]  
path = find_shortest_path_with_goals(maze, start, goals)  
if path:  # check if a valid path is found
    print("Path covering all goals:", path)  
else:  # if no path found, print message
    print("No path found covering all goals")  
