class Environment:
    def __init__(self, matrix, start, goal):
        self.matrix = matrix
        self.start = start
        self.goal = goal
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def get_percept(self):
        return self.matrix

class Agent:
    def __init__(self):
        self.visited = []
        self.queue = []
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    def bfs(self, env):
        percept = env.get_percept()
        start_pos = None
        goal_pos = None

        # find s and g
        for row in range(env.rows):
            for col in range(env.cols):
                if percept[row][col] == 'S':
                    start_pos = (row, col)
                elif percept[row][col] == 'G':
                    goal_pos = (row, col)

        if start_pos is None or goal_pos is None:
            print("start or goal not found")
            return

        self.queue.append((start_pos, [start_pos]))  
        self.visited.append(start_pos)

        while self.queue:
            (row, col), path = self.queue.pop(0)

            if (row, col) == goal_pos:
                print("Goal found! Shortest path:", path)
                return path

            for dr, dc in self.directions:
                nr, nc = row + dr, col + dc 

                if 0 <= nr < env.rows and 0 <= nc < env.cols and percept[nr][nc] != 1 and (nr, nc) not in self.visited:
                    self.queue.append(((nr, nc), path + [(nr, nc)]))
                    self.visited.append((nr, nc))

        print("path not found!\n")
        return

def run_agent(matrix, agent, env):
    print("Running BFS to reach goal\n")
    path = agent.bfs(env)

    if path:
        print("\noptimized path:\n")
        for r, c in path:
            if env.matrix[r][c] not in ('S', 'G'):
                env.matrix[r][c] = '*'
        for row in env.matrix:
            print(" ".join(str(cell) for cell in row))

# 0 = Open area, 1 = Obstacle, 'S' = Start, 'G' = Goal
matrix = [
    ['S', 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 'G']
]

start_node = 'S'
goal_node = 'G'

env = Environment(matrix, start_node, goal_node)
agent = Agent()
run_agent(matrix, agent, env)
