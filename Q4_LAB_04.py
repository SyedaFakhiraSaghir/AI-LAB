import heapq
import random
import time
import threading

class map:
    def __init__(self, roads, h):
        self.r = roads  # adjacency list (road network)
        self.h = h  # heuristic values (estimated distance to goal)
        self.lock = threading.Lock()  # lock for thread safety

    def update_traffic(self):
        while True:  # continuously update traffic conditions
            time.sleep(random.randint(2, 5))  # simulate random traffic updates
            with self.lock:  # ensure thread safety
                u = random.choice(list(self.r.keys()))  # pick a random location
                if self.r[u]:  # check if location has roads
                    v = random.choice(list(self.r[u].keys()))  # pick a random road
                    new_time = random.randint(1, 15)  # simulate new traffic delay
                    self.r[u][v] = new_time  # update travel time
                    self.r[v][u] = new_time  # maintain bidirectional consistency
                    print(f"Traffic update: {u} → {v} = {new_time} minutes")  # print update

    def get_neighbors(self, u):
        with self.lock:  # ensure thread safety
            return self.r[u].copy()  # return a copy to avoid modification issues

def a_star(city, start, goal):
    q = [(0, start)]  # priority queue (f(n), location)
    g_time = {start: 0}  # travel time from start
    parent = {start: None}  # track path

    while q:  # while there are locations to explore
        _, loc = heapq.heappop(q)  # get location with lowest f(n)
        if loc == goal:  # if goal reached, construct path
            path = []
            while loc:
                path.append(loc)
                loc = parent[loc]
            print(f"\nfastest route:{path[::-1]}")  
            return path[::-1]  
        for nb, travel_time in city.get_neighbors(loc).items():  # explore neighbors
            new_time = g_time[loc] + travel_time  # calculate new travel time
            f_time = new_time + city.h[nb]  # total time f(n) = g(n) + h(n)
            if nb not in g_time or new_time < g_time[nb]:  # if better route found
                g_time[nb] = new_time  
                parent[nb] = loc  
                heapq.heappush(q, (f_time, nb))  
    print("route not found")  
    return None  

roads = {
    'A': {'B': 30, 'C': 129},
    'B': {'A': 32, 'D': 5, 'E': 2},
    'C': {'A': 84, 'F': 4},
    'D': {'B': 5, 'G': 30},
    'E': {'B': 2, 'G': 71},
    'F': {'C': 41, 'G': 32},
    'G': {'D': 32, 'E': 70, 'F': 3},
    'H': {'A': 12, 'F': 99, 'B': 8}
}
h = {
    'A': 12, 'B': 9, 'C': 8, 'D': 5, 'E': 4, 'F': 6, 'G': 0  ,'H':10
}
city = map(roads, h)  
threading.Thread(target=city.update_traffic, daemon=True).start()  
print("\nstarting navigation:")  
a_star(city, 'A', 'G')  
