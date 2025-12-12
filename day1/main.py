def parse_line(line):
    if line[0] == 'L':
        return int(line[1:])
    if line[0] == 'R':
        return -1 * int(line[1:])
    raise Exception("Error: line must start with 'L' or 'R'")

def easy_puzzle(dial_location, sequence):
    counter = 0
    for rotation_amount in sequence:
        dial_location += rotation_amount
        if dial_location % 100 == 0:
            counter += 1
    return counter

def hard_puzzle(dial_location, sequence):
    counter = 0
    def clicks(start, end):
        if start < end:
            return end // 100 - start // 100
        if start > end:
            return (start - 1) // 100 - (end - 1) // 100
        return 0
    for rotation_amount in sequence:
        start = dial_location
        end = dial_location + rotation_amount
        dial_location = end
        counter += clicks(start, end)
    return counter

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f]
    sequence = [parse_line(line) for line in lines]
    dial_location = 50
    print(f"Easy puzzle answer: {easy_puzzle(dial_location, sequence)}")
    print(f"Hard puzzle answer: {hard_puzzle(dial_location, sequence)}")
