def product(arr):
    prod = 1
    for n in arr:
        prod *= n
    return prod

def easy_puzzle(char_array):
    num_2d_array = []
    for line in char_array[:-1]:
        line_str = ''.join(line)
        num_strs = line_str.split()
        nums = [int(s) for s in num_strs]
        num_2d_array.append(nums)
    operations = [c for c in char_array[-1] if c != ' ']
    answer = 0
    for i, op in enumerate(operations):
        col = [row[i] for row in num_2d_array]
        if op == '+':
            answer += sum(col)
        elif op == '*':
            answer += product(col)
    return answer

def hard_puzzle(char_array):
    col_strings = []
    for col in range(len(char_array[0])):
        col_str = ''.join(row[col] for row in char_array)
        col_str = col_str.replace(' ', '')
        col_strings.append(col_str)
    chunks = []
    current_chunk = []
    for col_str in col_strings:
        if col_str == '':
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = []
        else:
            current_chunk.append(col_str)
    if current_chunk:
        chunks.append(current_chunk)
    operations = []
    number_sets = []
    for chunk in chunks:
        op = ' '
        for i, s in enumerate(chunk):
            if '+' in s:
                op = '+'
                chunk[i] = s.replace('+', '')
                break
            elif '*' in s:
                op = '*'
                chunk[i] = s.replace('*', '')
                break
        operations.append(op)
        numbers = [int(s) for s in chunk]
        number_sets.append(numbers)
    sums_or_products = []
    for op, numbers in zip(operations, number_sets):
        if op == '+':
            sums_or_products.append(sum(numbers))
        elif op == '*':
            sums_or_products.append(product(numbers))
    answer = sum(sums_or_products)
    return answer

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()

    lines = [line.rstrip('\n') for line in lines]
    max_len = max(len(line) for line in lines)
    char_array = [list(line.ljust(max_len)) for line in lines]

    print(f"Easy puzzle answer: {easy_puzzle(char_array)}")
    print(f"Hard puzzle answer: {hard_puzzle(char_array)}")
