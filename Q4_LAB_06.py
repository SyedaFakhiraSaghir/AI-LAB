# Q4
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def main():
    manager = pywrapcp.RoutingIndexManager(10, 5, 0)  # 10 packages, 5 robots
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        distances = [
            [0, 10, 15, 20, 25, 30, 35, 40, 45, 50],
            [10, 0, 35, 25, 30, 20, 15, 10, 5, 0],
            [15, 35, 0, 30, 25, 20, 15, 10, 5, 0],
            [20, 25, 30, 0, 15, 10, 5, 0, 5, 10],
            [25, 30, 25, 15, 0, 10, 5, 0, 5, 10],
            [30, 20, 20, 10, 10, 0, 5, 10, 15, 20],
            [35, 15, 15, 5, 5, 5, 0, 10, 15, 20],
            [40, 10, 10, 0, 0, 10, 10, 0, 10, 15],
            [45, 5, 5, 5, 5, 15, 15, 10, 0, 10],
            [50, 0, 0, 10, 10, 20, 20, 15, 10, 0]
        ]
        return distances[from_index][to_index]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    solution = routing.SolveWithParameters(search_parameters)

    if solution:
        print("Solution found.")
        index = routing.Start(0)
        route = []
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route.append(node_index)
            index = solution.Value(routing.NextVar(index))
        print(route)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
