import heapq
import random
import time
import threading

class Graph:
    def __init__(self, edges, h):
        self.g = edges  # adjacency list
        self.h = h  # heuristic values
        self.lock = threading.Lock()  # lock for thread safety

    def update_costs(self):
        while True:  # continuously update costs
            time.sleep(random.randint(2, 5))  # wait before updating
            with self.lock:  # ensure thread safety
                n = random.choice(list(self.g.keys()))  # pick a random node
                if self.g[n]:  # check if node has neighbors
                    nb = random.choice(list(self.g[n].keys()))  # pick a neighbor
                    new_cost = random.randint(1, 10)  # assign new cost
                    self.g[n][nb] = new_cost  # update cost
                    self.g[nb][n] = new_cost  # maintain bidirectional consistency
                    print(f"\nupdated: {n} → {nb} = {new_cost}")  # print update

    def get_neighbors(self, n):
        with self.lock:  # ensure thread safety
            return self.g[n].copy()  # return a copy to avoid modification issues

def a_star(graph, start, goal):
    q = [(0, start)]  # priority queue
    g_cost = {start: 0}  # cost from start to node
    parent = {start: None}  # track path

    while q:  # while there are nodes to explore
        _, node = heapq.heappop(q)  # get node with lowest cost

        if node == goal:  # if goal reached, construct path
            path = []  
            while node:
                path.append(node)  
                node = parent[node]  
            print("\npath found:", path[::-1])  
            return path[::-1]  

        for nb, cost in graph.get_neighbors(node).items():  # explore neighbors
            new_cost = g_cost[node] + cost  # calculate new cost
            f_cost = new_cost + graph.h[nb]  # total cost f(n) = g(n) + h(n)

            if nb not in g_cost or new_cost < g_cost[nb]:  # if better path found
                g_cost[nb] = new_cost  
                parent[nb] = node  
                heapq.heappush(q, (f_cost, nb))  

    print("\nno path found")  
    return None  

edges = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'D': 4, 'E': 1},
    'C': {'A': 5, 'F': 3},
    'D': {'B': 4, 'G': 2},
    'E': {'B': 1, 'G': 6},
    'F': {'C': 3, 'G': 2},
    'G': {'D': 2, 'E': 6, 'F': 2}
}

h = {  
    'A': 10, 'B': 8, 'C': 7, 'D': 5, 'E': 3, 'F': 6, 'G': 0  
}

graph = Graph(edges, h)  
threading.Thread(target=graph.update_costs, daemon=True).start()  

print("\nstarting a* search:")  
a_star(graph, 'A', 'G')  
