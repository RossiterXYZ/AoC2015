NiceStrings1 = 0
NiceStrings2 = 0

with open("Day5\Input.txt") as InputFile:
    for InputLine in InputFile:
        InputLine = InputLine.strip()
        LastChar = ''

        #Puzzle 1
        BadString = False
        VowelCount = 0
        FoundDouble = False
        for Char in InputLine:
            if not FoundDouble and LastChar == Char:
                FoundDouble = True
            if VowelCount < 3 and (Char == "a" or Char == "e" or Char == "i" or Char == "o" or Char == "u"):
                VowelCount += 1
            if (LastChar == "a" and Char == "b") or \
                (LastChar == "c" and Char == "d") or \
                (LastChar == "p" and Char == "q") or \
                (LastChar == "x" and Char == "y"):
                BadString = True
                break
            LastChar = Char
        if not BadString and VowelCount == 3 and FoundDouble:
            NiceStrings1 += 1

        #Puzzle 2
        Rule1 = False
        Rule2 = False
        for Index in range(16-2):
            String1 = InputLine[Index]
            String2 = InputLine[Index+2]
            if String1 == String2:
                Rule2 = True
                break
        if Rule2:
            for StartRange in range(16-3):
                for NextRange in range(StartRange+2,16-1):
                    String1 = InputLine[StartRange:StartRange+2]
                    String2 = InputLine[NextRange:NextRange+2]
                    if String1 == String2:
                        Rule1 = True
                        break
                if Rule1:
                    break
        if Rule1 and Rule2:
            NiceStrings2 += 1

print(f'Puzzle 1: First Ruleset = {NiceStrings1}')
print(f'Puzzle 2: Second Ruleset = {NiceStrings2}')