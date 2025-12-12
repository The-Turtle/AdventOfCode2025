def largest_n_digit_subsequence(data, n):
    if len(data) < n:
        raise ValueError("Data length is less than n")
    if n == 0:
        return []
    digit = max(data[:len(data)-(n-1)])
    index = data.index(digit)
    return [digit] + largest_n_digit_subsequence(data[index+1:], n-1)

def arr_to_int(arr):
    return int(''.join(map(str, arr)))

def easy_puzzle(data):
    answer = 0
    for line in data:
        print(arr_to_int(largest_n_digit_subsequence(line, 2)))
        answer += arr_to_int(largest_n_digit_subsequence(line, 2))
    return answer

def hard_puzzle(data):
    answer = 0
    for line in data:
        answer += arr_to_int(largest_n_digit_subsequence(line, 12))
    return answer

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = [list(map(int, line.strip())) for line in f]
    print(f"Easy puzzle answer: {easy_puzzle(data)}")
    print(f"Hard puzzle answer: {hard_puzzle(data)}")
