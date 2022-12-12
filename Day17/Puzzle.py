def ParseFile(_File):
    with open(_File) as InputFile:
        return [int(Individual) for Individual in InputFile.read().strip().split("\n")]

def JugPermutations(_Jugs, _Target):
    PermutationCount = 0
    MinJugs = len(_Jugs)
    MinJugPermutations = 0
    Index = 0
    while Index in range(2**len(_Jugs)):
        JugCount = 0
        SubCount = 0
        for x in range(len(_Jugs)):
            if Index & (1 << x) == (1 << x):
                JugCount += 1
                SubCount += _Jugs[x]
        if not SubCount == _Target:
            Index += 1
            continue
        PermutationCount += 1
        if JugCount < MinJugs:
            MinJugs = JugCount
            MinJugPermutations = 1
        elif JugCount == MinJugs:
            MinJugPermutations += 1
        Index += 1

    return [PermutationCount, MinJugPermutations]


JugSizes = ParseFile("Day17\Input.txt")
JugSizes.sort(reverse=True)
TestSizes = [20, 15, 10, 5, 5]


JugData = JugPermutations(JugSizes, 150)
Part1 = JugData[0]
Part2 = JugData[1]

print(f'Puzzle 1: {Part1}')
print(f'Puzzle 2: {Part2}')