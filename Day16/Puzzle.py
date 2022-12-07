
def ParseFile(_File, _Function):
    ReturnList = []
    with open(_File) as InputFile:
        for InputLine in InputFile:
            ReturnList.append(_Function(InputLine))
    return ReturnList

def CreateSueList(_Input):
    ReturnValue = {}
    _Input = _Input.split(': ', 1)
    _Input = _Input[1].split(', ')

    for Entity in _Input:
        Entity = Entity.split(': ')
        ReturnValue[Entity[0]] = int(Entity[1])

    return ReturnValue

def CompareLists(_SueList, _ComparisonList, _DumbComparisons = False):
    ReturnIndexes = []

    for Index in range(len(_SueList)):
        Sue = _SueList[Index]
        SueInvalid = False
        for Item, Value in Sue.items():
            if Value <= _ComparisonList[Item] and Item in ['cats', 'trees'] and _DumbComparisons:
                SueInvalid = True
                break
            elif Value >= _ComparisonList[Item] and Item in ['pomeranians', 'goldfish'] and _DumbComparisons:
                SueInvalid = True
                break
            elif Value != _ComparisonList[Item] and not (Item in ['pomeranians', 'goldfish', 'cats', 'trees'] and _DumbComparisons):
                SueInvalid = True
                break

        if not SueInvalid:
            ReturnIndexes.append(Index)
    return ReturnIndexes

Comparison = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

SueList = ParseFile("Day16\Input.txt", CreateSueList)

print(f'Puzzle 1: Find Sue = {CompareLists(SueList, Comparison, False)[0]+1}')
print(f'Puzzle 2: Find REAL Sue = {CompareLists(SueList, Comparison, True)[0]+1}')