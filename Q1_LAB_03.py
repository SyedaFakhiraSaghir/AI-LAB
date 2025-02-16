class Environment:
  def __init__(self, tree,st,goal,dl):
    self.graph=tree
    self.start=st
    self.goal=goal
    self.depth_limit=dl

  def get_percept(self):
    return self.graph

class Agent:
  def __init__(self):
    self.visited = set()
    self.queue=[]
    pass

  def act_ucs(self, env):
    frontier = [(env.start, 0)]
    cost_so_far = {env.start: 0}
    came_from = {env.start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, current_cost = frontier.pop(0)

        if current_node in self.visited:
            continue

        self.visited.add(current_node)

        if current_node == env.goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f'Goal found with ucs \nPath: {path}\ncost: {current_cost}')
            return path

        for neighbor, cost in env.graph[current_node].items():
            new_cost = current_cost + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                came_from[neighbor] = current_node
                frontier.append((neighbor, new_cost))

    print("Goal not found")
    return None

  def act_dls(self,env):
      visited = []
      stack = [(env.start, 0)]
      while stack:
          node, depth = stack.pop()
          if depth > depth_limit:
            print("\nGoal not found with dls!")
            return
          if node not in visited:
              visited.append(node)
              print(f"Visited: {node}")
              if node == env.goal:
                  print(f"\nGoal {env.goal} found with dls!")
                  return
              if node in graph:
                  for neighbour in reversed(graph[node]):
                      if neighbour not in visited:
                          stack.append((neighbour, depth + 1))

def run_agent(agent, env):
  print('************* running ucs:')
  agent.act_ucs(env)
  print('\n************* running dls:')
  agent.act_dls(env)

graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

start_node = 'A'
goal_node = 'G'
depth_limit=3
env=Environment(graph,start_node,goal_node,depth_limit)
agent=Agent()
run_agent(agent,env)
