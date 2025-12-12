# returns the number of invalid IDs at most n whose chunks repeat r times
def running_count(n, r):
    digits = len(str(n))
    if digits % r == 0:
        first_chunk = int(str(n)[:digits // r])
        threshold = int(r * str(first_chunk))
        if threshold <= n:
           return first_chunk
        else:
           return first_chunk - 1
    else:
        return 10 ** (digits // r) - 1

# returns the sum of all invalid IDs at most n whose chunks repeat r times
def running_sum(n, r):
    c = running_count(n, r)
    d = len(str(c))
    output = 0
    for i in range(d):
        start = 10 ** i
        end = min(10 ** (i+1) - 1, c)
        sum_of_range = (start + end) * (end - start + 1) // 2
        scalar = sum(10 ** ((i+1)*j) for j in range(r))
        output += sum_of_range * scalar
    return output

# returns {1: mu(1), 2: mu(2), ..., n: mu(n)}
def get_mobius_values(n):
    mu = {i: 0 for i in range(1, n+1)}
    is_prime = {i: True for i in range(2, n+1)}
    primes = []

    mu[1] = 1

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            is_prime[i * p] = False
            if i % p == 0:
                mu[i * p] = 0
                break
            else:
                mu[i * p] = -mu[i]

    return mu

def easy_puzzle(intervals):
    answer = 0
    for interval in intervals:
        start, end = interval
        answer += running_sum(end, 2) - running_sum(start - 1, 2)
    return answer

def hard_puzzle(intervals):
    max_interval = max(end for _, end in intervals)
    max_digits = len(str(max_interval))
    mobius_values = get_mobius_values(max_digits)

    def g(n):
        output = 0
        for r in range(2, max_digits+1):
            output += running_sum(n, r) * -1 * mobius_values[r]
        return output

    answer = 0
    for interval in intervals:
        start, end = interval
        answer += g(end) - g(start - 1)
    return answer

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = f.read().split(',')
        intervals = [tuple(int(x) for x in item.split('-', 1)) for item in data]
    print(f"Easy puzzle answer: {easy_puzzle(intervals)}")
    print(f"Hard puzzle answer: {hard_puzzle(intervals)}")
