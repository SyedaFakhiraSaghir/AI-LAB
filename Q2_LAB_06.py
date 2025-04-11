import numpy as np

def find_largest_landmass(grid):
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype='bool')
    max_area = 0
    max_perimeter = 0

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or visited[row, col] or grid[row, col] == 0:
            return 0, 0
        visited[row, col] = True
        area = 1
        perimeter = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr, nc] == 0:
                perimeter += 1
            elif not visited[nr, nc]:
                a, p = dfs(nr, nc)
                area += a
                perimeter += p
        return area, perimeter

    for row in range(rows):
        for col in range(cols):
            if grid[row, col] == 1 and not visited[row, col]:
                area, perimeter = dfs(row, col)
                if area > max_area:
                    max_area = area
                    max_perimeter = perimeter

    return max_perimeter

#grid
grid = np.array([
    [1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
])

print(find_largest_landmass(grid))
