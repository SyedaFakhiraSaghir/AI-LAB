from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def distance_callback(from_index, to_index):
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    return distances[from_index][to_index]

def main():
    manager = pywrapcp.RoutingIndexManager(4, 1, 0)
    routing = pywrapcp.RoutingModel(manager)
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    #setting first solution heuristic
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
