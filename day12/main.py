def area(present):
    return sum(sum(row) for row in present)

def packable(w, h, presents, counts):
    areas = [area(present) for present in presents]
    total_area = sum(a * c for a, c in zip(areas, counts))
    if total_area > w * h:
        return False
    max_present_height = max(len(present) for present in presents)
    max_present_width = max(len(row) for present in presents for row in present)
    lower_bound = (w // max_present_width) * (h // max_present_height)
    if sum(counts) <= lower_bound:
        return True
    print(sum(counts), lower_bound)
    raise RuntimeError("Unable to determine if the presents are packable with the given constraints.")


def puzzle(presents, puzzles):
    answer = 0
    for puzzle in puzzles:
        dimensions, counts = puzzle
        w, h = dimensions
        if packable(w, h, presents, counts):
            answer += 1
    return answer

with open('input.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]

    puzzles = []
    lines_to_remove = []
    for i, line in enumerate(lines):
        if 'x' in line:
            before_colon, after_colon = line.split(':', 1)
            x_str, y_str = before_colon.split('x')
            dimensions = (int(x_str.strip()), int(y_str.strip()))
            counts = [int(val) for val in after_colon.strip().split()]
            puzzles.append((dimensions, counts))
            lines_to_remove.append(i)

    for i in reversed(lines_to_remove):
        del lines[i]

    presents = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if ':' in line:
            # Start of a new grid
            grid_as_strings = []
            i += 1
            while i < len(lines) and ':' not in lines[i]:
                grid_as_strings.append(lines[i])
                i += 1
            # Convert grid_lines to boolean array
            grid_as_bool = []
            for row in grid_as_strings:
                if row:
                    grid_as_bool.append([c == '#' for c in row])
            presents.append(grid_as_bool)
        else:
            i += 1

    print(f"Puzzle answer: {puzzle(presents, puzzles)}")
