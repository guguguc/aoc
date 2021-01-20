#/usr/bin/python3
def preprocess(filename) -> list[str]:
    return [line.strip() for line in open(filename).readlines()]

def decode_seq(seq: str) -> int:
    l, r = 0, 2 ** len(seq) - 1
    for c in seq:
        mid = (l + r) >> 1
        if c == '0':
            l = mid + 1
        elif c == '1':
            r = mid
    assert l == r
    return l

def get_id(row: int, col: int) -> int:
    return row * 8 + col

def part1(seqs: list[str]) -> tuple[int, list]:
    ans = 0
    plane = []
    for seq in seqs:
        seq = seq.translate(str.maketrans("FBLR", "1010"))
        row = decode_seq(seq[:7])
        col = decode_seq(seq[7:])
        plane.append((row, col))
        ans = max(ans, get_id(row, col))
    return ans, plane

def part2(plane: list[tuple]) -> int:
    plane.sort(key=lambda coord: (coord[0], coord[1]))
    plane = [get_id(*coord) for coord in plane]
    last = plane[0]
    for sid in plane[1:]:
        if sid != last+1:
            return sid
        last = sid
    return -1

if __name__ == "__main__":
    from matplotlib import pyplot
    from pprint import pprint

    filename = "input.txt"
    data = preprocess(filename)
    ans1, plane = part1(data)
    ans2 = part2(plane)
    print(f"ans 1 is {ans1}")
    print(f"ans 2 is {ans2}")
