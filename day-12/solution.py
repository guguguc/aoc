from pprint import pprint

# filename = 'demo.txt'
filename = 'input.txt'

class Direction:
    EAST = 'E'
    WEST = 'W'
    NORTH = 'N'
    SOUTH = 'S'
    LEFT = 'L'
    RIGHT = 'R'
    FORWARD = 'F'

class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vec2D):
            raise TypeError(f'error: {other} is not Coord type!')
        ret = Vec2D(self.x + other.x, self.y + other.y)
        return ret

    def __sub__(self, other):
        if not isinstance(other, Vec2D):
            raise TypeError(f'error: {other} is not Coord type!')
        ret = Vec2D(self.x - other.x, self.y - other.y)
        return ret

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError(f'error: {scalar} is not a scalar!')
        return Vec2D(self.x * scalar, self.y * scalar)

    def rotate(self, derection: Direction, degree):
        # derection
        # degree 90 180 270
        if degree == 180:
            self.x, self.y = -self.x, -self.y
        elif degree == 90:
            if derection == Direction.LEFT:
                self.x, self.y = -self.y, self.x
            elif derection == Direction.RIGHT:
                self.x, self.y = self.y, -self.x
            else:
                pass
        elif degree == 270:
            if derection == Direction.LEFT:
                self.x, self.y = self.y, -self.x
            elif derection == Direction.RIGHT:
                self.x, self.y = -self.y, self.x
            else:
                pass
        else:
            pass

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def mahattaan_distance(self):
        return abs(self.x) + abs(self.y)

    def __str__(self):
        return f'({self.x}, {self.y})'
        


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

def part1(ipt):
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
    print(f'ans: {abs(x) + abs(y)}')

def part2(ipt):
    # only action F changes ship's position
    # other action acts on waypoint
    waypoint = Vec2D(10, 1)
    start = Vec2D(0, 0)
    for ins in ipt:
        match ins:
            case [Direction.EAST, dis]:
                waypoint.x += dis
            case [Direction.WEST, dis]:
                waypoint.x -= dis
            case [Direction.NORTH, dis]:
                waypoint.y += dis
            case [Direction.SOUTH, dis]:
                waypoint.y -= dis
            case [(Direction.LEFT | Direction.RIGHT) as derction, degree]:
                # degree (90, 180, 270)
                waypoint_relate_of_ship = waypoint - start
                waypoint_relate_of_ship.rotate(derction, degree)
                waypoint = start + waypoint_relate_of_ship
            case [Direction.FORWARD, dis]:
                diff = waypoint - start
                start = start + dis * diff
                waypoint = waypoint + dis * diff
            case e:
                print(e)
                raise ValueError()
        print(f'waypoint: {waypoint}, start: {start}')
    print(f'ans: {start.mahattaan_distance()}')

def main():
    ipt = [l.rstrip() for l in open(filename).readlines()]
    ipt = [[instruction[0], int(instruction[1:])] for instruction in ipt]
    # part1(ipt)
    part2(ipt)
    

if __name__ == '__main__':
    main()
