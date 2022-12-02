LogicList = {}
Puzzle2 = True

with open("Day7\Input.txt") as InputFile:
    for InputLine in InputFile:
        InputLine = InputLine.strip().split(' -> ')
        LogicList[InputLine[1]] = InputLine[0]

if Puzzle2:
    LogicList["b"] = 46065

while LogicList['a'] == "lx":
    for Variable, Condition in LogicList.items():
        if type(Condition) is int:
            continue
        if Condition.find("AND") != -1:
            Var1, _, Var2 = Condition.split(' ')
            if not(Var1.isnumeric() or type(LogicList[Var1]) is int):
                continue
            if not(Var2.isnumeric() or type(LogicList[Var2]) is int):
                continue

            if Var1.isnumeric():
                Var1 = int(Var1)
            else:
                Var1 = LogicList[Var1]
            if Var2.isnumeric():
                Var2 = int(Var2)
            else:
                Var2 = LogicList[Var2]

            LogicList[Variable] = Var1 & Var2
        #\AND
        elif Condition.find("OR") != -1:
            Var1, _, Var2 = Condition.split(' ')

            if not(Var1.isnumeric() or type(LogicList[Var1]) is int):
                continue
            if not(Var2.isnumeric() or type(LogicList[Var2]) is int):
                continue

            if Var1.isnumeric():
                Var1 = int(Var1)
            else:
                Var1 = LogicList[Var1]
            if Var2.isnumeric():
                Var2 = int(Var2)
            else:
                Var2 = LogicList[Var2]

            LogicList[Variable] = Var1 | Var2
        #\OR
        elif Condition.find("NOT") != -1:
            _, Var1 = Condition.split(' ')
            if not(Var1.isnumeric() or type(LogicList[Var1]) is int):
                continue

            if Var1.isnumeric():
                Var1 = int(Var1)
            else:
                Var1 = LogicList[Var1]

            LogicList[Variable] = ~Var1 & 0xffff
        #\NOT
        elif Condition.find("RSHIFT") != -1:
            Var1, _, Value = Condition.split(' ')
            if not(Var1.isnumeric() or type(LogicList[Var1]) is int):
                continue

            if Var1.isnumeric():
                Var1 = int(Var1)
            else:
                Var1 = LogicList[Var1]

            LogicList[Variable] = Var1 >> int(Value) & 0xffff
            print(f'Output: {LogicList[Variable]} [RSHIFT]\n{Var1:016b} {Var1}\n{Value}\n{LogicList[Variable]:>016b} {LogicList[Variable]}\n')
        #\RSHIFT
        elif Condition.find("LSHIFT") != -1:
            Var1, _, Value = Condition.split(' ')
            if not(Var1.isnumeric() or type(LogicList[Var1]) is int):
                continue

            if Var1.isnumeric():
                Var1 = int(Var1)
            else:
                Var1 = LogicList[Var1]

            LogicList[Variable] = Var1 << int(Value) & 0xffff
        #\LSHIFT
        elif not Condition.isnumeric():
            if type(LogicList[Condition]) is int:
                LogicList[Variable] = LogicList[Condition]
        else:
            LogicList[Variable] = int(Condition)

if not Puzzle2:
    print(f'Puzzle 1: Logic Trace = {LogicList["a"]}')
else:
    print(f'Puzzle 2: Logic Override = {LogicList["a"]}')