def easy_puzzle(s_col, grid):
    col_count = len(grid[0])
    beams = [False] * col_count
    beams[s_col] = True
    counter = 0
    for row in grid:
        for i in range(0, col_count):
            if row[i] == "^" and beams[i]:
                beams[i-1] = True
                beams[i+1] = True
                beams[i] = False
                counter += 1
    return counter

def hard_puzzle(s_col, grid):
    col_count = len(grid[0])
    beam_counts = [0] * col_count
    beam_counts[s_col] = 1
    for row in grid:
        for i in range(0, col_count):
            if row[i] == "^":
                beam_counts[i-1] += beam_counts[i]
                beam_counts[i+1] += beam_counts[i]
                beam_counts[i] = 0
    return sum(beam_counts)

if __name__ == "__main__":
    with open("input.txt") as f:
        grid = [list(line.strip()) for line in f if line.strip()]
    s_col = None
    for idx, val in enumerate(grid[0]):
        if val == 'S':
            s_col = idx
            break
    print(f"Easy puzzle answer: {easy_puzzle(s_col, grid)}")
    print(f"Hard puzzle answer: {hard_puzzle(s_col, grid)}")
