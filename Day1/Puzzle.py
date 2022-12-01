#Puzzle 1
LeftCount = 0
RightCount = 0

#Puzzle 2
Floor = 0
Index = 0

with open("Day1\Input.txt") as InputFile:
    for InputLine in InputFile:
        #Puzzle 1
        LeftCount = InputLine.count('(')
        RightCount = InputLine.count(')')
        print(f'Puzzle 1: Ending Floor = {LeftCount - RightCount}')

        #Puzzle 2
        while Floor >= 0:
            if InputLine[Index] == "(":
                Floor += 1
            if InputLine[Index] == ")": #Coulda done else 🤷‍♀️
                Floor -= 1
            Index += 1
        print(f'Puzzle 2: First Basement Entry = {Index}')