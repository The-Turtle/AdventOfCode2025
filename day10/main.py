def subsets(arr):
    result = [[]]
    for num in arr:
        new_subsets = []
        for subset in result:
            new_subsets.append(subset + [num])
        result.extend(new_subsets)
    return result

def add(vec1, vec2):
    return [a + b for a, b in zip(vec1, vec2)]

def f(lights, button_wirings):
    lights = [int(light) for light in lights]
    n = len(lights)
    vectors = []
    for wiring in button_wirings:
        vector = [0] * n
        for number in wiring:
            vector[number] += 1
        vectors.append(vector)
    answer = None
    for subset in subsets(vectors):
        sum = [0] * n
        for vector in subset:
            sum = add(sum, vector)
        if all((s % 2) == light for s, light in zip(sum, lights)):
            if answer is None or len(subset) < answer:
                answer = len(subset)
    return answer if answer is not None else -1

def g(joltages, button_wirings):
    n = len(joltages)
    vectors = []
    for wiring in button_wirings:
        vector = [0] * n
        for number in wiring:
            vector[number] += 1
        vectors.append(vector)
    memo = {}
    subset_sums_and_counts = []
    for subset in subsets(vectors):
        sum_vec = [0] * n
        for vector in subset:
            sum_vec = add(sum_vec, vector)
        subset_sums_and_counts.append((sum_vec, len(subset)))
    subset_sum_mod2_dict = {}
    for sum_vec, count in subset_sums_and_counts:
        key = tuple(s % 2 for s in sum_vec)
        if key not in subset_sum_mod2_dict:
            subset_sum_mod2_dict[key] = []
        subset_sum_mod2_dict[key].append((sum_vec, count))
    def answer(target):
        key = tuple(target)
        if any(t < 0 for t in target):
            return None
        if all(t == 0 for t in target):
            return 0
        if key in memo:
            return memo[key]
        min_result = None
        target_mod2 = tuple(t % 2 for t in target)
        if target_mod2 not in subset_sum_mod2_dict:
            return None
        for subset_sum, count in subset_sum_mod2_dict[target_mod2]:
            if all((s % 2) == (t % 2) for s, t in zip(subset_sum, target)):
                diff = [(t - s) // 2 for s, t in zip(subset_sum, target)]
                rec = answer(diff)
                if rec is not None:
                    total = 2 * rec + count
                    if min_result is None or total < min_result:
                        min_result = total
        memo[key] = min_result
        return min_result
    a = answer(joltages)
    return a


def easy_puzzle(configurations):
    answer = 0
    for lights, button_wirings, _ in configurations:
        answer += f(lights, button_wirings)
    return answer

def hard_puzzle(configurations):
    answer = 0
    for _, button_wirings, joltages in configurations:
        result = g(joltages, button_wirings)
        if result is None:
            raise ValueError("no solution")
        answer += result
    return answer

if __name__ == "__main__":
    with open("input.txt") as file_in:
        lines = file_in.readlines()

    configurations = []

    for line in lines:
        line = line.strip()
        start_sq = line.find('[')
        end_sq = line.find(']')
        sq_part = line[start_sq+1:end_sq]
        lights = [c == '#' for c in sq_part]

        start_curly = line.find('{')
        end_curly = line.find('}')
        curly_part = line[start_curly+1:end_curly]
        joltages = [int(x.strip()) for x in curly_part.split(',')]

        rest = line[end_sq+1:start_curly].strip()
        button_wirings = []
        for part in rest.split():
            if part.startswith('(') and part.endswith(')'):
                inner = part[1:-1]
                tuple_vals = tuple(int(x.strip()) for x in inner.split(','))
                button_wirings.append(tuple_vals)

        configuration = (lights, button_wirings, joltages)
        configurations.append(configuration)

    print(f"Easy puzzle answer: {easy_puzzle(configurations)}")
    print(f"Hard puzzle answer: {hard_puzzle(configurations)}")
