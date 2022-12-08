from copy import deepcopy

filename = 'input.txt'
empty = 'L'
occpied = '#'
floor = '.'
padding = '*'


class StateMachine:

    def __init__(self, mp: list):
        self.state_map = mp
        self.rows = len(mp)
        self.cols = len(mp[0])

    def advance(self, occpied_changeable_limit):
        mp = deepcopy(self.state_map)
        for row, line in enumerate(self.state_map):
            for col, state in enumerate(line):
                if state == floor or state == padding:
                    continue
                elif state == empty:
                    if self.empty_changable(row, col):
                        mp[row][col] = occpied
                # occupied
                else:
                    if self.occpied_changeable(row, col, occpied_changeable_limit):
                        mp[row][col] = empty
        self.state_map = mp

    def empty_changable(self, row, col):
        ret = True
        funcs = [
            self.left, self.right, self.up, self.down, self.left_down,
            self.left_up, self.right_down, self.right_up
        ]
        for func in funcs:
            val = func(row, col)
            if val == empty or val == padding or val == floor:
                ret = ret and True
            else:
                ret = False
                break
        # print(f'ret: {ret}')
        # input()
        return ret

    def occpied_changeable(self, row, col, limit):
        cnt = 0
        funcs = [
            self.left, self.right, self.up, self.down, self.left_down,
            self.left_up, self.right_down, self.right_up
        ]
        for func in funcs:
            if func(row, col) == occpied:
                cnt += 1
        ret = True if cnt >= limit else False
        return ret

    def left(self, row, col):
        return self.state_map[row][col - 1]

    def right(self, row, col):
        return self.state_map[row][col + 1]

    def up(self, row, col):
        return self.state_map[row + 1][col]

    def down(self, row, col):
        return self.state_map[row - 1][col]

    def left_up(self, row, col):
        return self.state_map[row - 1][col - 1]

    def left_down(self, row, col):
        return self.state_map[row + 1][col - 1]

    def right_up(self, row, col):
        return self.state_map[row - 1][col + 1]

    def right_down(self, row, col):
        return self.state_map[row + 1][col + 1]

    def dump(self):
        return self.state_map

    def dump_str(self):
        for line in self.state_map:
            print(line)

    def count(self):
        cnt = 0
        for line in self.state_map:
            for state in line:
                if state == occpied:
                    cnt += 1
        return cnt


class StateMachine2(StateMachine):

    def find_first(self, idxs):
        ret = padding
        for x, y in idxs:
            state = self.state_map[x][y]
            if state == floor:
                continue
            else:
                ret = state
                break
        return ret

    def left(self, row, col):
        # None if all left seats are floor
        # else L or #
        idxs = [(row, i) for i in range(col - 1, 0, -1)]
        self.test(row, col, idxs, 'left')
        ret = self.find_first(idxs)
        return ret

    def right(self, row, col):
        idxs = [(row, i) for i in range(col + 1, self.cols)]
        self.test(row, col, idxs, 'right')
        ret = self.find_first(idxs)
        return ret

    def up(self, row, col):
        idxs = [(i, col) for i in range(row - 1, 0, -1)]
        self.test(row, col, idxs, 'up')
        ret = self.find_first(idxs)
        return ret

    def down(self, row, col):
        idxs = [ (i, col) for i in range(row + 1, self.cols) ]
        self.test(row, col, idxs, 'down')
        ret = self.find_first(idxs)
        return ret

    def left_up(self, row, col):
        # (row - 1, col - 1)
        limit = min(row, col)
        idxs = [(row - i, col - i) for i in range(1, limit)]
        self.test(row, col, idxs, 'left_up')
        ret = self.find_first(idxs)
        return ret

    def left_down(self, row, col):
        # (row + 1, col - 1)
        limit = min(self.rows - row, col)
        idxs = [(row + i, col - i) for i in range(1, limit)]
        self.test(row, col, idxs, 'left_down')
        ret = self.find_first(idxs)
        return ret

    def right_up(self, row, col):
        # (row - 1, col + 1)
        limit = min(row, self.cols - col)
        idxs = [(row - i, col + i) for i in range(1, limit)]
        self.test(row, col, idxs, 'right_up')
        ret = self.find_first(idxs)
        return ret

    def right_down(self, row, col):
        # (row + 1, col + 1)
        limit = min(self.rows - row, self.cols - col)
        idxs = [(row + i, col + i) for i in range(1, limit)]
        self.test(row, col, idxs, 'right_down')
        ret = self.find_first(idxs)
        return ret

    def test(self, row, col, idxs, name):
        return
        print(name)
        print(f'row: {row}, col: {col}')
        print(idxs)
        input()


def transfer(ipt: list):
    # add padding to grid
    # up down left right
    for line in ipt:
        line.insert(0, padding)
        line.append(padding)
    extra_line = [padding] * len(ipt[0])
    return [extra_line] + ipt + [extra_line]

def part1(grid):
    st = StateMachine(grid)
    rd = 0
    stp = st.dump()
    while True:
        st.advance(4)
        # st.dump_str()
        # input()
        if stp == st.dump():
            break
        stp = st.dump()
        rd += 1
        print(f'roud {rd}')
    print(st.count())

def part2(grid):
    st = StateMachine2(grid)
    rd = 0
    stp = st.dump()
    while True:
        st.advance(5)
        # st.dump_str()
        # input()
        if stp == st.dump():
            break
        stp = st.dump()
        rd += 1
        print(f'roud {rd}')
    print(st.count())

def main():
    ipt = [list(l.rstrip()) for l in open(filename).readlines()]
    ipt = transfer(ipt)
    # part1(ipt)
    part2(ipt)

if __name__ == '__main__':
    main()