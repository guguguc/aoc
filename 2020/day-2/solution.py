#!/usr/bin/python3

def preprocess(filename) -> int:
    lines = [line.rstrip() for line in open(file).readlines()]
    data = [] 
    for line in lines:
        policy, target, passwd = line.split(sep=' ')
        policy = tuple(map(int, policy.split('-')))
        target = target.rstrip(':')
        data.append((policy, target, passwd))
    return data

def part1(info) -> int:
    ans = 0
    for policy, target, passwd in info:
        min_cnt, max_cnt = policy
        cnt = passwd.count(target)
        cond = cnt in range(min_cnt, max_cnt+1)
        if (cond): ans += 1
    return ans

def part2(info) -> int:
    ans = 0
    for policy, target, passwd in info:
        pos1, pos2 = policy
        pos1 -= 1; pos2 -= 1
        cond0 = pos1 < len(passwd) and pos2 < len(passwd)
        cond1 = (passwd[pos1] == target) ^ (passwd[pos2] == target)
        if (cond0 and cond1): ans += 1
    return ans

if __name__ == "__main__":
    filename = "input.txt"
    data = preprocess(filename)
    print(f"part 1 ans is {part1(data)}")
    print(f"part 2 ans is {part2(data)}")
