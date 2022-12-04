import json

def ReturnSum(_Input, _ToggleRed = False):
    Sum = 0

    if type(_Input) is dict:
        for _, Entry in _Input.items():
            if type(Entry) is dict or type(Entry) is list:
                Sum += ReturnSum(Entry, _ToggleRed)
            elif type(Entry) is int:
                Sum += Entry
            elif (_ToggleRed) and (type(Entry) is str) and (Entry == 'red'):
                return 0
    elif type(_Input) is list:
        for Entry in _Input:
            if type(Entry) is dict or type(Entry) is list:
                Sum += ReturnSum(Entry, _ToggleRed)
            elif type(Entry) is int:
                Sum += Entry
    elif type(_Input) is int:
        Sum += _Input

    return Sum

with open("Day12\Input.txt") as InputFile:
    for InputLine in InputFile:
        JSONData = json.loads(InputLine)

print(f'Puzzle 1: FileCount = {ReturnSum(JSONData)}')
print(f'Puzzle 2: !Red = {ReturnSum(JSONData, True)}')