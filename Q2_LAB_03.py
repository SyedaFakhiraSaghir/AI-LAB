class Environment:
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start

    def get_percept(self):
        return self.graph

class Agent:
    def __init__(self):
        self.min_cost = float('inf')
        self.best_path = None

    def act_TSP(self, env):
        def tsp_backtrack(path, cost):
            if len(path) == len(env.graph):
              #if all nodes visited check if its the shortest path
                final_cost = cost + env.graph[path[-1]][env.start]
                if final_cost < self.min_cost:
                    self.min_cost = final_cost
                    self.best_path = path + [env.start]#store best path
                return

            current_node = path[-1]
            for neighbor in env.graph[current_node]:
              #explore unvisited neigbours
                if neighbor not in path:
                    tsp_backtrack(path + [neighbor], cost + env.graph[current_node][neighbor])
#backtrack from starting node
        tsp_backtrack([env.start], 0)
        print(f"\n {'-'.join(self.best_path)} \n cost: {self.min_cost}")

def run_agent(agent, env):
    print("Running TSP:")
    agent.act_TSP(env)

graph = {
    '1': {'2': 10, '3': 15, '4': 20},
    '2': {'1': 10, '3': 35, '4': 25},
    '3': {'1': 15, '2': 35, '4': 30},
    '4': {'1': 20, '2': 25, '3': 30}
}

start_node = '1'
env = Environment(graph, start_node)
agent = Agent()
run_agent(agent, env)
