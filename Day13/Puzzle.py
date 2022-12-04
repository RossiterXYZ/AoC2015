PersonSet = set()
HappinessMap = {}
with open("Day13\InputTest.txt") as InputFile:
    for InputLine in InputFile:
        Person1, _, Positive, Value, _, _, _, _, _, _, Person2 = InputLine[:len(InputLine) - 2].split(' ')
        Value = int(Value)
        if Positive == "lose":
            Value = Value * -1
        if not Person1 in PersonSet:
            HappinessMap[Person1] = {}
            PersonSet.add(Person1)
        HappinessMap[Person1].update({Person2: Value})

print(HappinessMap)
print(f'Puzzle 1: 1 = {1}')
print(f'Puzzle 2: 1 = {1}')