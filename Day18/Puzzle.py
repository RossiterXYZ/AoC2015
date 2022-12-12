Faulty = False #Puzzle2

def ParseFile(_File):
    with open(_File) as InputFile:
        return [list(Individual) for Individual in InputFile.read().strip().split("\n")]

def PrintLightGrid(_Grid):
    print("\n".join(["".join(x) for x in _Grid]),'\n')

def ConwayCheck(_Grid, _x, _y):
    Directions = [
        {'x': -1, 'y': -1},
        {'x': -1, 'y': 0},
        {'x': -1, 'y': 1},
        {'x': 0, 'y': -1},
        {'x': 0, 'y': 1},
        {'x': 1, 'y': -1},
        {'x': 1, 'y': 0},
        {'x': 1, 'y': 1},
    ]
    Current = _Grid[_y][_x] == "#"
    LitNeighbours = 0 #42069 Fam
    for Dir in Directions:
        x = _x + Dir['x']
        y = _y + Dir['y']
        if not x in range(100) or not y in range(100):
            continue

        if _Grid[y][x] == '#':
            LitNeighbours += 1

    ReturnValue = LitNeighbours == 3 or (Current and LitNeighbours == 2)
    if ReturnValue:
        return '#'
    else:
        return '.'

def Conwayify(_Grid, _Faulty):
    NewGrid = [['#' for _ in range(100)] for _ in range(100)]
    for y in range(100):
        for x in range(100):
            if _Faulty and str(x)+'|'+str(y) in ['0|0', '0|99', '99|99', '99|0']:
                continue
            NewGrid[y][x] = ConwayCheck(_Grid, x, y)
    return NewGrid

def CountCells(_Grid):
    Count = 0
    for y in range(100):
        for x in range(100):
            if _Grid[y][x] == '#':
                Count += 1
    return Count

Grid = ParseFile("Day18\Input.txt")
if Faulty:
    Grid[0][0] = '#'
    Grid[0][99] = '#'
    Grid[99][99] = '#'
    Grid[99][0] = '#'
for _ in range(100):
    Grid = Conwayify(Grid, Faulty)

print(f'Puzzle {1+int(Faulty)}: {CountCells(Grid)}')