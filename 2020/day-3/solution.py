#!/usr/bin/python3

def preprocess(filename):
    return [list(line.rstrip()) for line in open(filename).readlines()]

def part1(maze: list, action: tuple = (0, 3, 1, 0)) -> int:
    """
    action: (up, right, down, left)
    default action
    coord: right 3, down 1 -> (row, row), (1, 3), (2, 6), (row, 3 * row)
    coord: in extend maze  -> (row, (3 * row) mod cols)
    """
    rows, cols = len(maze), len(maze[0])
    right, down = action[1:3]
    ans = 0
    for row_idx in range(down, rows, down):
        col_idx = (right * row_idx) % cols
        if maze[row_idx][col_idx] == '#':
            ans += 1
    return ans

def part2(maze: list) -> int:
    actions = ((0, 1, 1, 0),
               (0, 3, 1, 0),
               (0, 5, 1, 0),
               (0, 7, 1, 0),
               (0, 1, 2, 0))
    ans = 1
    for action in actions:
        ans *= part1(maze, action)
    return ans

if __name__ == "__main__":
    filename = "input.txt"
    data = preprocess(filename)
    ans1 = part1(data)
    ans2 = part2(data)
    print(f"part 1 ans is {ans1}")
    print(f"part 2 ans is {ans2}")
