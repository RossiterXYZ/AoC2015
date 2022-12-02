print('Warning: Takes a few seconds to run!')

Lights1 = [[0 for i in range(1000)] for j in range(1000)]
LightCount1 = 0
Lights2 = [[0 for i in range(1000)] for j in range(1000)]
LightCount2 = 0

with open("Day6\Input.txt") as InputFile:
    for InputLine in InputFile:
        InputLine = InputLine.strip()
        InputLine = InputLine[5:].split(' ')

        Method = InputLine[0]
        x1, y1 = InputLine[1].split(',')
        x2, y2 = InputLine[3].split(',')

        for i in range(int(x1), int(x2)+1):
            for j in range(int(y1), int(y2)+1):
                if Method == "e":
                    Lights1[i][j] = (Lights1[i][j] + 1) % 2
                    Lights2[i][j] += 2
                elif Method == "off":
                    Lights1[i][j] = 0
                    Lights2[i][j] = max(0, Lights2[i][j] - 1)
                elif Method == "on":
                    Lights1[i][j] = 1
                    Lights2[i][j] += 1

for i in range(1000):
    for j in range(1000):
        if Lights1[i][j] > 0:
            LightCount1 += 1
        LightCount2 += Lights2[i][j]

print(f'Puzzle 1: State = {LightCount1}')
print(f'Puzzle 2: Brightness = {LightCount2}')