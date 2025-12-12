def area(pair1, pair2):
    x1, y1 = pair1
    x2, y2 = pair2
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)

def easy_puzzle(pairs):
    max_area = 0
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            a = area(pairs[i], pairs[j])
            if a > max_area:
                max_area = a
    return max_area

def sign(x):
    return int(x > 0) - int(x < 0)

def hard_puzzle(pairs):
    n = len(pairs)
    first_pair_index = pairs.index(min(pairs))
    pairs = pairs[first_pair_index:] + pairs[:first_pair_index]
    if not pairs[0][1] == pairs[1][1]:
        pairs = [pairs[0]] + list(reversed(pairs[1:]))
    expanded_pairs = []
    eps = 0.1
    for i in range(n):
        x, y = pairs[i]
        prev_x, prev_y = pairs[i-1]
        next_x, next_y = pairs[(i+1) % n]
        vec_in = (sign(x - prev_x), sign(y - prev_y))
        vec_out = (sign(next_x - x), sign(next_y - y))
        if vec_in == (1, 0) and vec_out == (0, 1):
            expanded_pairs.append((x + eps, y - eps))
        elif vec_in == (1, 0) and vec_out == (0, -1):
            expanded_pairs.append((x - eps, y - eps))
        elif vec_in == (-1, 0) and vec_out == (0, 1):
            expanded_pairs.append((x + eps, y + eps))
        elif vec_in == (-1, 0) and vec_out == (0, -1):
            expanded_pairs.append((x - eps, y + eps))
        elif vec_in == (0, 1) and vec_out == (1, 0):
            expanded_pairs.append((x + eps, y - eps))
        elif vec_in == (0, 1) and vec_out == (-1, 0):
            expanded_pairs.append((x + eps, y + eps))
        elif vec_in == (0, -1) and vec_out == (1, 0):
            expanded_pairs.append((x - eps, y - eps))
        elif vec_in == (0, -1) and vec_out == (-1, 0):
            expanded_pairs.append((x - eps, y + eps))
    vertical_edges = []
    horizontal_edges = []
    for i in range(n):
        x0, y0 = expanded_pairs[i]
        x1, y1 = expanded_pairs[(i+1) % n]
        if x0 == x1:
            y_start, y_end = sorted([y0, y1])
            vertical_edges.append((x0, y_start, y_end))
        elif y0 == y1:
            x_start, x_end = sorted([x0, x1])
            horizontal_edges.append((y0, x_start, x_end))
    vertical_edges.sort(key=lambda edge: edge[0])
    horizontal_edges.sort(key=lambda edge: edge[0])
    def horizontal_crossings(x_coord):
        y_coords = []
        for y, x_start, x_end in horizontal_edges:
            if x_start <= x_coord <= x_end:
                y_coords.append(y)
        return y_coords
    def vertical_crossings(y_coord):
        x_coords = []
        for x, y_start, y_end in vertical_edges:
            if y_start <= y_coord <= y_end:
                x_coords.append(x)
        return x_coords
    limb_dict = {}
    for pair in pairs:
        x, y = pair
        x_coords = vertical_crossings(y)
        x1 = max([xc for xc in x_coords if xc < x])
        x2 = min([xc for xc in x_coords if xc > x])
        y_coords = horizontal_crossings(x)
        y1 = max([yc for yc in y_coords if yc < y])
        y2 = min([yc for yc in y_coords if yc > y])
        limb_dict[pair] = (x2-x, y2-y, x-x1, y-y1)
    max_area = 0
    for i in range(n):
        for j in range(i+1, n):
            pair1 = pairs[i]
            pair2 = pairs[j]
            limbs1 = limb_dict[pair1]
            limbs2 = limb_dict[pair2]
            x1, y1 = pair1
            x2, y2 = pair2
            x_diff = abs(x1-x2)
            y_diff = abs(y1-y2)
            is_compatible = False
            if pair1[0] <= pair2[0] and pair1[1] <= pair2[1]:
                if limbs1[0] >= x_diff and limbs1[1] >= y_diff and limbs2[2] >= x_diff and limbs2[3] >= y_diff:
                    is_compatible = True
            if pair1[0] <= pair2[0] and pair1[1] >= pair2[1]:
                if limbs1[0] >= x_diff and limbs1[3] >= y_diff and limbs2[2] >= x_diff and limbs2[1] >= y_diff:
                    is_compatible = True
            if pair1[0] >= pair2[0] and pair1[1] <= pair2[1]:
                if limbs1[2] >= x_diff and limbs1[1] >= y_diff and limbs2[0] >= x_diff and limbs2[3] >= y_diff:
                    is_compatible = True
            if pair1[0] >= pair2[0] and pair1[1] >= pair2[1]:
                if limbs1[2] >= x_diff and limbs1[3] >= y_diff and limbs2[0] >= x_diff and limbs2[1] >= y_diff:
                    is_compatible = True
            if is_compatible:
                print(f"Compatible pair: {pair1}, {pair2}")
                max_area = max(max_area, area(pair1, pair2))
    return max_area

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        pairs = [tuple(map(int, line.strip().split(','))) for line in f if line.strip()]
    print(f"Easy puzzle answer: {easy_puzzle(pairs)}")
    print(f"Hard puzzle answer: {hard_puzzle(pairs)}")
