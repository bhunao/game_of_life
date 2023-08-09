import pyxel
from itertools import product


SPEED = 5
PAUSE = True


width, height = 100, 50
xrange = range(width)
yrange = range(height)

table = [[0 for x in xrange] for y in yrange]
table[0][1] = 1
table[1][0] = 1
table[1][2] = 1
table[2][1] = 1

table[1][5] = 1
table[1][6] = 1
table[1][7] = 1

pyxel.init(width, height)
pyxel.mouse(True)


def neighbours(x, y):
    global table
    total_n = 0
    for _x in range(x-1, x+2):
        for _y in range(y-1, y+2):
            if (x, y) == (_x, _y) or _x < 0 or _x >= width or _y < 0 or _y >= height:
                continue
            if table[_y][_x] == 1:
                total_n += 1
    return total_n


neighbours(15, 1)


def draw():
    pyxel.cls(0)
    for y in yrange:
        for x in xrange:
            if table[y][x] == 1:
                pyxel.pset(x, y, 15)
            else:
                continue
                pyxel.pset(x, y, neighbours(x, y))


def update():
    global SPEED, PAUSE, table
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        print(pyxel.mouse_x, pyxel.mouse_y)
        table[pyxel.mouse_y][pyxel.mouse_x] = 1
    if pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT):
        print(neighbours(pyxel.mouse_x, pyxel.mouse_y))
    if pyxel.btnp(pyxel.KEY_SPACE):
        PAUSE = not PAUSE
    if pyxel.btnp(pyxel.KEY_R):
        table = [[0 for x in xrange] for y in yrange]

    if pyxel.frame_count % SPEED or PAUSE:
        return

    _table = table.copy()
    for x, y in product(xrange, yrange):
        alive = table[y][x] == 1
        n = neighbours(x, y)
        if (n == 2 or n == 3) and alive:
            _table[y][x] = 1
        elif n == 3 or n == 2:
            _table[y][x] = 1
        else:
            _table[y][x] = 0

    table = _table


pyxel.run(update, draw)
