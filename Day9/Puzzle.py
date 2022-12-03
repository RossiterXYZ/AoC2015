#TSP go brrr

TownSet = set()
Distances = {}

with open("Day9\Input.txt") as InputFile:
    for InputLine in InputFile:
        Town1, _, Town2, _, Distance = InputLine.split(' ')
        Distance = int(Distance)

        if not Town1 in TownSet:
            Distances[Town1] = {}
            TownSet.add(Town1)
        if not Town2 in TownSet:
            Distances[Town2] = {}
            TownSet.add(Town2)
        Distances[Town1][Town2] = Distance
        Distances[Town2][Town1] = Distance

TownVariations = [[]]
for _ in TownSet:
    TownCopy = TownVariations.copy()
    TownVariations = []
    for TownList in TownCopy:
        for Town in TownSet:
            if Town in TownList:
                continue
            TmpList = TownList.copy()
            TmpList.append(Town)
            TownVariations.append(TmpList)

Lowest = 99999
Highest = 0
for Variation in TownVariations:
    CurrentCost = 0
    for Index in range(1, len(Variation)):
        CurrentCost += Distances[Variation[Index-1]][Variation[Index]]
    if CurrentCost < Lowest:
        Lowest = CurrentCost
    if CurrentCost > Highest:
        Highest = CurrentCost

print(f'Puzzle 1: Lowest = {Lowest}')
print(f'Puzzle 2: Highest = {Highest}')