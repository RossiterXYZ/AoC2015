FileLength = 0

Loop = 0
with open("Day8\Input.txt") as InputFile:
    for InputLine in InputFile:
        ParsedLine = len(InputLine)-3
        print(f'Line:   {InputLine}\nChange: {ParsedLine}\n')
        if Loop > 5:
            break
        Loop += 1

