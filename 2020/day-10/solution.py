#/usr/bin/python3
from collections import defaultdict

def preprocess(filename) -> list:
    return [int(line.strip()) for line in open(filename).readlines()]

def part1(array: list) -> int:
    array.sort()
    tb = defaultdict(int)
    last = 0
    for idx, item in enumerate(array):
        diff = item - last
        tb[diff] += 1
        last = item
        print(diff, end=" ")
        if idx % 10 == 0: print()
    tb[3] += 1
    return tb[1] * tb[3]

def part2(array: list) -> int:
    na = [0] + array
    diffs = [na[i] - na[i-1] for i in range(1, len(na))]
    tb = defaultdict(int)
    idx = 0
    while idx < len(diffs):
        if diffs[idx] != 1:
            idx += 1
            continue
        cnt = 0
        while idx < len(diffs) and diffs[idx] == 1:
            idx += 1
            cnt += 1
        tb[cnt] += 1
    tb.pop(1)
    factor = {4: 7, 3: 4, 2: 2}
    ans = 1
    for k, v in tb.items():
        ans *= factor[k] ** v
    return ans


if __name__ == "__main__":
    filename = "input.txt"
    data = preprocess(filename)
    ans1 = part1(data)
    ans2 = part2(data)
    print(f"ans 1 is {ans1}")
    print(f"ans 2 is {ans2}")
