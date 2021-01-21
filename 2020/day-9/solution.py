#/usr/bin/python3

def preprocess(filename):
    return [int(line.strip()) for line in open(filename).readlines()]

def part1(array):
    l, r = 0, 24
    for item in array[r+1:]:
        window = array[l:r+1]
        st = set(window)
        for elem in window:
            target = item - elem
            if target != elem and target in st:
                break
        else:
            return item
        l += 1
        r += 1
    return -1

def part2(array, target):
    l, r = 0, 1
    while r < len(array):
        window = array[l:r+1]
        sm = sum(window)
        if sm < target:
            r += 1
        elif sm > target:
            l += 1
        else:
            if r-l+1 < 2: continue
            ans = max(window) + min(window)
            return ans
    return -1


if __name__ == "__main__":
    filename = "input.txt"
    data = preprocess(filename)
    ans1 = part1(data)
    ans2 = part2(data, ans1)
    print(f"ans 1 is {ans1}")
    print(f"ans 2 is {ans2}")
