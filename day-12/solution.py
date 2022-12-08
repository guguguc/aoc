from pprint import pprint

class Direction:
    EAST = 'E'
    WEST = 'W'
    NORTH = 'N'
    SOUTH = 'S'
    LEFT = 'L'
    RIGHT = 'R'
    FORWARD = 'F'

filename = 'input.txt'

def rotate_left(start, degree):
    # 90, 180, 270
    mp = {Direction.EAST:{90:Direction.NORTH, 180:Direction.WEST, 270:Direction.SOUTH},
          Direction.WEST:{90:Direction.SOUTH, 180:Direction.EAST, 270:Direction.NORTH},
          Direction.NORTH:{90:Direction.WEST, 180:Direction.SOUTH, 270:Direction.EAST},
          Direction.SOUTH:{90:Direction.EAST, 180:Direction.NORTH, 270:Direction.WEST}}
    direction = mp[start][degree]
    return direction

def rotate_right(start, degree):
    mp = {Direction.EAST:{90:Direction.SOUTH, 180:Direction.WEST, 270:Direction.NORTH},
      Direction.WEST:{90:Direction.NORTH, 180:Direction.EAST, 270:Direction.SOUTH},
      Direction.NORTH:{90:Direction.EAST, 180:Direction.SOUTH, 270:Direction.WEST},
      Direction.SOUTH:{90:Direction.WEST, 180:Direction.NORTH, 270:Direction.EAST}}
    direction = mp[start][degree]
    return direction

def main():
    ipt = [l.rstrip() for l in open(filename).readlines()]
    ipt = [[instruction[0], int(instruction[1:])] for instruction in ipt]
    x, y = 0, 0
    start = Direction.EAST
    for ins in ipt:
        match ins:
            case [Direction.EAST, dis]:
                x += dis
            case [Direction.WEST, dis]:
                x -= dis
            case [Direction.NORTH, dis]:
                y += dis
            case [Direction.SOUTH, dis]:
                y -= dis
            case [Direction.LEFT, degree]:
                # degree (90, 180, 270)
                start = rotate_left(start, degree)
            case [Direction.RIGHT, degree]:
                start = rotate_right(start, degree)
            case [Direction.FORWARD, dis]:
                if start == Direction.EAST:
                    x += dis
                elif start == Direction.WEST:
                    x -= dis
                elif start == Direction.NORTH:
                    y += dis
                else:
                    y -= dis
            case _:
                raise ValueError()
        print(f'x:{x}, y:{y}')
    print(abs(x) + abs(y))


if __name__ == '__main__':
    main()
