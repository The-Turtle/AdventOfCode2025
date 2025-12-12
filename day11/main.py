f_cache = {}

def f(s, wirings, avoid=[]):
    avoid_string = "".join(avoid)
    if avoid_string not in f_cache:
        f_cache[avoid_string] = {}
    cache = f_cache[avoid_string]
    if s == "out":
        return 1
    if s in avoid:
        return 0
    if s in cache:
        return cache[s]
    vals = wirings[s]
    total = 0
    for v in vals:
        total += f(v, wirings, avoid)
    cache[s] = total
    return total

def easy_puzzle(wirings):
    return f("you", wirings)

def hard_puzzle(wirings):
    total = f("svr", wirings, avoid=[])
    avoid_dac = f("svr", wirings, avoid=["dac"])
    avoid_fft = f("svr", wirings, avoid=["fft"])
    avoid_both = f("svr", wirings, avoid=["dac", "fft"])
    return total - avoid_dac - avoid_fft + avoid_both

if __name__ == "__main__":
    wirings = {}
    with open("input.txt") as file_in:
        for line in file_in:
            line = line.strip()
            if not line:
                continue
            key, values = line.split(":", 1)
            key = key.strip()
            values_list = [v for v in values.strip().split()]
            wirings[key] = values_list
    print(f"Easy puzzle answer: {easy_puzzle(wirings)}")
    print(f"Hard puzzle answer: {hard_puzzle(wirings)}")
