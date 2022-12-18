#!/usr/bin/python3
from check import check_fields, is_valid

def preprocess(filename: str) -> list[dict]:
    items = []
    chunk = ""
    for line in open(filename):
        chunk += line
        if not line.strip():
            item = chunk.replace("\n", " ").strip().split(" ")
            item = dict([pair.split(":") for pair in item])
            items.append(item)
            chunk = ""
    return items

def part1(items: list[dict]) -> int:
    ans = 0
    for item in items:
        if check_fields(item.keys()): ans += 1
    return ans

def part2(items: list[dict]) -> int:
    ans = 0
    for item in items:
        if is_valid(item): ans += 1
    return ans

if __name__ == "__main__":
    filename = "input.txt"
    items = preprocess(filename)
    ans1 = part1(items)
    ans2 = part2(items)
    print(f"ans 1 is {ans1}")
    print(f"ans 2 is {ans2}")
