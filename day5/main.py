class Interval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def size(self):
        return self.upper - self.lower + 1


def easy_puzzle(interval_list, number_list):
    count = 0
    for number in number_list:
        for interval in interval_list:
            if interval.lower <= number and number <= interval.upper:
                count += 1
                break
    return count

def hard_puzzle(intervals):
    intervals.sort(key=lambda x: x.lower)
    condensed_intervals = []
    for interval in intervals:
        if len(condensed_intervals) == 0 or interval.lower > condensed_intervals[-1].upper:
            condensed_intervals.append(interval)
        else:
            condensed_intervals[-1].upper = max(condensed_intervals[-1].upper, interval.upper)
    answer = 0
    for interval in condensed_intervals:
        answer += interval.size()
    return answer

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = [line.strip() for line in f if line.strip()]

    intervals = []
    numbers = []

    for line in lines:
        if '-' in line:
            parts = line.split('-')
            intervals.append(Interval(int(parts[0]), int(parts[1])))
        elif line.isdigit():
            numbers.append(int(line))

    print(f"Easy puzzle answer: {easy_puzzle(intervals, numbers)}")
    print(f"Hard puzzle answer: {hard_puzzle(intervals)}")
