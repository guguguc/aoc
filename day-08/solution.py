#/usr/bin/python3

def preprocess(filname) -> list:
    return [line.strip().split(" ") for line in open(filename).readlines()]

def decode(op, oprand, pc, rax):
    if op == "nop":
        pc += 1
    elif op == "jmp":
        pc += int(oprand)
    elif op == "acc":
        rax += int(oprand)
        pc += 1
    else:
        raise KeyError(f"invalid op {op} in line {pc}")
    return pc, rax

def part1(instructions: list, pc: int = 0) -> tuple[int, bool]:
    ans, cnt = 0, 0
    visited = set()
    while pc < len(instructions):
        op, oprand = instructions[pc]
        print(f"{cnt} op: {op}, oprand: {oprand}, line: {pc}")
        if pc not in visited:
            visited.add(pc)
        else:
            print(f"infinite loop in {pc+1}, op {op}, oprand {oprand}")
            return ans, False
        pc, ans = decode(op, oprand, pc, ans)
        cnt += 1
    return ans, True

def part2(instructions: list) -> int:
    ans, pc, cnt = 0, 0, 0
    replace = {"jmp": "nop", "nop": "jmp"}
    while pc < len(instructions):
        op, oprand = instructions[pc]
        if op in replace.keys():
            new_ins = instructions[:]
            new_ins[pc][0] = replace[op]
            remain_ans, isterm = part1(new_ins, pc)
            if isterm:
                print(f"change line {pc}, op {op} to op {replace[op]}")
                return ans + remain_ans
        pc, ans = decode(op, oprand, pc, ans)
    return ans


if __name__ == "__main__":
    filename = "input.txt"
    data = preprocess(filename)
    ans1, _ = part1(data)
    ans2 = part2(data)
    print(f"ans1 is {ans1}")
    print(f"ans2 is {ans2}")
