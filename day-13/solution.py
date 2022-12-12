
def part1():
    filename = 'demo.txt'
    ipt = [line.rstrip() for line in open(filename).readlines()]
    invalid_bus_id = 'x'
    target_time, bus_id = ipt
    target_time = int(target_time)
    bus_id = [int(i) for i in bus_id.split(',') if i != invalid_bus_id]
    bus_id.sort()
    target_bus_id = 0
    min_wating_time = float('inf')
    for i in bus_id:
        times = target_time // i
        time_greater_than_target =  times * i + i
        diff = time_greater_than_target - target_time
        if min_wating_time > diff:
            target_bus_id = i
            min_wating_time = diff
    ans = target_bus_id * min_wating_time
    print(f'ans: {ans}')

def match_rule(ipt_advance: list, ipt):
    array = [-i for i in range(0, len(ipt_advance))]
    ipt_advance_copy = ipt_advance[:]
    for idx, bus_id in enumerate(ipt_advance):
        if bus_id == 'x':
            continue
        ipt_advance_copy[idx] += array[idx]
    same_val = ipt_advance_copy[0]
    for item in ipt_advance:
        if item == 'x':
            continue
        if item != same_val:
            return False
    print(ipt_advance_copy)
    input()
    # at this point, all bus's starting time match rule
    # except the import bus.
    for idx, tm in enumerate(ipt_advance):
        if tm == 'x':
            continue
        ipt_advance[idx] += ipt[idx]
        remain_tm = ipt_advance[:]
        remain_tm.remove(tm)
        for rtm in remain_tm:
            if rtm == tm:
                return True
        else:
            return False

def part2():
    filename = 'demo-2.txt'
    ipt = open(filename).readline().strip()
    placeholder_any = 'x'
    ipt = [int(i) if i != placeholder_any else i for i in ipt.split(',')]
    print(ipt)
    ipt_copy = ipt[:]
    while True:
        ipt_advance = [ updated_tm + tm if tm != placeholder_any else tm for updated_tm, tm in zip(ipt_copy, ipt)]
        ipt_copy = ipt_advance
        if ipt_copy[0] == 1068781:
            print(ipt_copy)
            input()
        if match_rule(ipt_advance, ipt):
            break
    ans = ipt[0]
    print(f'ans: {ans}')

def main():
    # part1()
    part2()

if __name__ == '__main__':
    main()