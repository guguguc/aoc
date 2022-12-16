from pprint import pprint
filename = 'demo2.txt'
filename = 'input.txt'
uneffected_bit = 'X'

def parse_input():
    # [[[mask, xxxx], [addr1, val1], [addr2, val2]]], []]
    sep = ' = '
    cmds = []
    for line in open(filename).readlines():
        line = list(line.rstrip().partition(sep))
        line.remove(sep)
        if line[0] == 'mask':
            cmds.append([line])
        else:
            line[0] = line[0].removeprefix('mem[').removesuffix(']')
            cmds[len(cmds) - 1].append(line)
    return cmds


def bitmask_v1(mask: str, mem_val: str) -> int:
    mem_val = int(mem_val)
    mem_val = f'{mem_val:08b}'
    mem_val = f'{mem_val:>036}'
    mask, mem_val = list(mask), list(mem_val)
    for idx, v in enumerate(mem_val):
        if mask[idx] == uneffected_bit:
            continue
        mem_val[idx] = mask[idx]
    mem_val = ''.join(mem_val)
    return int(mem_val, 2)

def bitmask_v2(mask: str, mem_addr: str) -> list:
    ret = []
    mem_addr = int(mem_addr)
    mem_addr = f'{mem_addr:08b}'
    mem_addr = f'{mem_addr:>036}'
    mask, mem_addr = list(mask), list(mem_addr)
    for idx, v in enumerate(mem_addr):
        if mask[idx] == uneffected_bit:
            mem_addr[idx] = uneffected_bit
        elif mask[idx] == '0':
            continue
        # 1
        else:
            mem_addr[idx] = '1'
    mem_addr = ''.join(mem_addr)
    generate_addr(mem_addr, ret)
    return ret

def generate_addr(addr: str, container: list):
    new_addr_0 = addr
    new_addr_1 = addr
    new_addr_0 = new_addr_0.replace('X', '1', 1)
    new_addr_1 = new_addr_1.replace('X', '0', 1)
    if new_addr_0.count('X') == 0:
        container.append(new_addr_0)
    else:
       generate_addr(new_addr_1, container)
    if new_addr_1.count('X') == 0:
        container.append(new_addr_1)
    else:
        generate_addr(new_addr_0, container)
    

def part1():
    ans = 0
    mp = dict()
    cmds = parse_input()
    for block in cmds:
        mask = block[0][1]
        mem_assign_op = block[1:]
        for op in mem_assign_op:
            addr, val = op
            mp[addr] = bitmask_v1(mask, val)
    for v in mp.values():
        ans += v
    print(f'ans:{ans}')

def part2():
    ans = 0
    mp = dict()
    cmds = parse_input()
    for block in cmds:
        mask = block[0][1]
        mem_assign_op = block[1:]
        for op in mem_assign_op:
            addr, val = op
            addrs = bitmask_v2(mask, addr)
            for addr in addrs:
                mp[addr] = int(val)
    for mem_val in mp.values():
        ans += mem_val
    print(f'ans: {ans}')

def main():
    # part1()
    part2()
    # test()

def test():
    addr = '000000000000000000000000000000X1101X'
    addrs = []
    generate_addr(addr, addrs)
    print(addrs)

if __name__ == '__main__':
    main()