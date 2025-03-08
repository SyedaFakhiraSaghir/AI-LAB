import heapq
class map:
    def __init__(self, roads, h, time_windows):
        self.r = roads 
        self.h = h  # heuristic value
        self.t = time_window  # delivery time window

    def greedy_bfs(self, start, deliveries):
        q = []  # priority queue
        heapq.heappush(q, (self.h[start], start, [start], 0))  # (heuristic, node, path, time)
        while q:  # while there are deliveries left
            _, loc, path, time = heapq.heappop(q)  # get next location
            if set(path) >= set(deliveries):  # if all deliveries done
                print(f"Optimized route:{path} \nTotal time: {time}")
                return path, time  
            for nb, travel_time in self.r.get(loc, {}).items():  # explore neighbors
                new_time = time + travel_time  # update travel time           
                if nb in deliveries and not (self.t[nb][0] <= new_time <= self.t[nb][1]):  
                    continue  # skip if time window is missed     
                heapq.heappush(q, (self.h[nb], nb, path + [nb], new_time))  
        print("route NOT found")  
        return None, float('inf')  

roads = {
    'A': {'B': 3, 'C': 8},
    'B': {'A': 3, 'D': 5, 'E': 2},
    'C': {'A': 8, 'F': 4},
    'D': {'B': 5, 'G': 3},
    'E': {'B': 2, 'G': 7},
    'F': {'C': 4, 'G': 3},
    'G': {'D': 3, 'E': 7, 'F': 3}
}
h = {
    'A': 10, 'B': 8, 'C': 7, 'D': 5, 'E': 3, 'F': 6, 'G': 0  
}
time_window = {
    'D': (5, 15),
    'E': (2, 12),
    'F': (6, 18),
    'G': (10, 20)
}
city = map(roads, h, time_window)
city.greedy_bfs('A', ['D', 'E', 'F', 'G'])  
