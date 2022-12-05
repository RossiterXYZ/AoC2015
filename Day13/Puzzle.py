Puzzle2 = False # Toggle for answer 1 or 2
PersonSet = set()
HappinessMap = {}
with open("Day13\Input.txt") as InputFile:
    for InputLine in InputFile:
        Person1, _, Positive, Value, _, _, _, _, _, _, Person2 = InputLine[:len(InputLine) - 2].split(' ')
        Value = int(Value)
        if Positive == "lose":
            Value = Value * -1
        if not Person1 in PersonSet:
            HappinessMap[Person1] = {}
            PersonSet.add(Person1)
        HappinessMap[Person1].update({Person2: Value})
if Puzzle2:
    print('Please be patient, this takes some time!')
    PersonSet.add('Me')
    HappinessMap['Me'] = {}
    for Person in PersonSet:
        HappinessMap['Me'].update({Person: 0})
        HappinessMap[Person].update({'Me': 0})

SeatingArrangements = [[]]
for _ in PersonSet:
    SeatingCopy = SeatingArrangements.copy()
    SeatingArrangements = []
    for SeatingList in SeatingCopy:
        for Person in PersonSet:
            if Person in SeatingList:
                continue
            TmpList = SeatingList.copy()
            TmpList.append(Person)
            SeatingArrangements.append(TmpList)
for Item in range(len(SeatingArrangements)):
    SeatingArrangements[Item].append(SeatingArrangements[Item][0])

Largest = 0
for Arrangement in SeatingArrangements:
    Sum = 0
    for Index in range(len(Arrangement) - 1):
        Sum += HappinessMap[Arrangement[Index]][Arrangement[Index+1]]
        Sum += HappinessMap[Arrangement[Index+1]][Arrangement[Index]]
    if Sum > Largest:
        Largest = Sum

if not Puzzle2:
    print(f'Puzzle 1: Everyone Else = {Largest}')
else:
    print(f'Puzzle 2: Including Me = {Largest}')