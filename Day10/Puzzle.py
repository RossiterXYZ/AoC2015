def LookAndSay(_Input):
    Count = 1
    Output = ''
    for Index in range(len(_Input)):
        Char = _Input[Index]
        if len(_Input) < Index + 2 or Char != _Input[Index + 1]:
            Output += str(Count) + Char
            Count = 1
        else:
            Count += 1
    return Output

Forty = 0
Fifty = 0
LookString = '1113122113'
for Index in range(50):
    LookString = LookAndSay(LookString)
    if Index == 39:
        Forty = len(LookString)
    if Index == 49:
        Fifty = len(LookString)

print(f'Puzzle 1: Forty = {Forty}')
print(f'Puzzle 2: Fifty = {Fifty}')