#!/usr/bin/python3
from functools import reduce

def preprocess(filename):
    data = []
    fp = open(filename)
    chunk = ""
    for line in fp.readlines():
        chunk += line
        if not line.strip():
            data.append(chunk.strip().split("\n"))
            chunk = ""
    data.append(chunk.strip().split("\n"))
    return data

    fp.close()

def part1(groups):
    ans = 0
    for group in data:
        questions = "".join(group)
        ans += len(set(questions))
    return ans

def part2(groups):
    ans = 0
    for group in groups:
        group = map(set, group)
        inter = reduce(lambda st1, st2: st1.intersection(st2), group)
        ans += len(inter)
    return ans


if __name__ == "__main__":
    filename = "input.txt"
    data = preprocess(filename)
    ans1 = part1(data)
    ans2 = part2(data)
    print(f"ans 1 is {ans1}")
    print(f"ans 2 is {ans2}")
