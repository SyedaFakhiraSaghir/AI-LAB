from ortools.sat.python import cp_model

def solve_sudoku():
    model = cp_model.CpModel()

    grid = [[model.NewIntVar(1, 9, f"cell_{i}_{j}") for j in range(9)] for i in range(9)]

    for i in range(9):
        model.AddAllDifferent([grid[i][j] for j in range(9)])
        model.AddAllDifferent([grid[j][i] for j in range(9)])
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            model.AddAllDifferent([grid[x][y] for x in range(i, i+3) for y in range(j, j+3)])

    diagonal1 = [grid[i][i] for i in range(9)]
    diagonal2 = [grid[i][8-i] for i in range(9)]
    model.Add(sum(diagonal1) % 3 == 0)
    model.Add(sum(diagonal2) % 3 == 0)

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(9):
        for j in range(9):
            if j < 8:
                model.AddBoolOr([grid[i][j] != 2, grid[i][j] != 3, grid[i][j] != 5, grid[i][j] != 7,
                                 grid[i][j+1] != 2, grid[i][j+1] != 3, grid[i][j+1] != 5, grid[i][j+1] != 7])
            if i < 8:
                model.AddBoolOr([grid[i][j] != 2, grid[i][j] != 3, grid[i][j] != 5, grid[i][j] != 7,
                                 grid[i+1][j] != 2, grid[i+1][j] != 3, grid[i+1][j] != 5, grid[i+1][j] != 7])

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:
        print("Solution found.")
        for row in grid:
            print([solver.Value(cell) for cell in row])
    else:
        print("No solution found.")

if __name__ == "__main__":
    solve_sudoku()
