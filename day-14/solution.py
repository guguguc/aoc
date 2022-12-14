from pprint import pprint
# filename = 'demo.txt'
filename = 'input.txt'
uneffected_bit = 'X'

def bitmask(mask: str, val: str) -> int:
    val = int(val)
    val = f'{val:08b}'
    val = f'{val:>036}'
    mask, val = list(mask), list(val)
    for idx, v in enumerate(val):
        if mask[idx] == uneffected_bit:
            continue
        val[idx] = mask[idx]
    val = ''.join(val)
    return int(val, 2)


def part1():
    sep = ' = '
    cmds = []
    ans = 0
    mp = dict()
    for line in open(filename).readlines():
        line = list(line.rstrip().partition(sep))
        line.remove(sep)
        if line[0] == 'mask':
            cmds.append([line])
        else:
            line[0] = line[0].removeprefix('mem[').removesuffix(']')
            cmds[len(cmds) - 1].append(line)
    for block in cmds:
        mask = block[0][1]
        mem_assign_op = block[1:]
        for op in mem_assign_op:
            addr, val = op
            mp[addr] = bitmask(mask, val)
    for v in mp.values():
        ans += v
    print(f'ans:{ans}')

def main():
    part1()

if __name__ == '__main__':
    main()