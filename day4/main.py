def neighbors(grid, x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]):
                if grid[nx][ny]:
                    count += 1
    return count

def count(grid):
    return sum(row.count(True) for row in grid)

def prune(grid):
    to_flip = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] and neighbors(grid, x, y) <= 3:
                to_flip.append((x, y))
    for x, y in to_flip:
        grid[x][y] = False

def easy_puzzle(grid):
    grid = [row[:] for row in grid]
    start_count = count(grid)
    prune(grid)
    end_count = count(grid)
    return start_count - end_count

def hard_puzzle(grid):
    grid = [row[:] for row in grid]
    start_count = count(grid)
    current_count = start_count
    while True:
        prune(grid)
        new_count = count(grid)
        if new_count == current_count:
            break
        else:
            current_count = new_count
    end_count = current_count
    for row in grid:
        print(''.join('@' if cell else '.' for cell in row))
    return start_count - end_count

if __name__ == "__main__":
    with open("input.txt") as f:
        grid = []
        for line in f:
            row = []
            for char in line.strip():
                if char == '@':
                    row.append(True)
                elif char == '.':
                    row.append(False)
                else:
                    raise ValueError(f"Unexpected character: {char}")
            grid.append(row)
    print(f"Easy puzzle answer: {easy_puzzle(grid)}")
    print(f"Hard puzzle answer: {hard_puzzle(grid)}")
