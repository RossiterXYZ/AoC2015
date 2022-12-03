WholeFile = 0
ParseFile = 0
EncodeFile = 0

with open("Day8\Input.txt") as InputFile:
    for InputLine in InputFile:
        WholeFile += len(InputLine) - 1
        ParseFile += len(InputLine) - 3
        EncodeFile += len(InputLine) + 3

        Iterate = 1
        while Iterate in range(1, len(InputLine) - 2):
            Char = InputLine[Iterate]
            if Char == '\\':
                if InputLine[Iterate+1] == 'x':
                    ParseFile -= 3
                    Iterate += 3
                else:
                    ParseFile -= 1
                    Iterate += 1
                    EncodeFile += 1
                EncodeFile += 1
            Iterate += 1

print(f'Puzzle 1: Decode = {WholeFile - ParseFile}')
print(f'Puzzle 2: Encode = {EncodeFile - WholeFile}')